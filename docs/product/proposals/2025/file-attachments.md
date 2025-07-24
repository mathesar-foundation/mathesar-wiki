# File Attachments

!!! info "This proposal is based on [these requirements](../../requirements/2025/file-attachments.md)."


## Solution

Mathesar will implement support for file attachments on records by introducing a new "Files" column type that allows users to upload, remove, and view files.

### User-facing terminology

Airtable and NocoDB use the term "Attachment" for this feature, whereas Baserow uses the term "File".

Mathesar will employ the following terms for users:

- **"Files"** — the name of the UI type for the column
- **"File"** — a single file attachment within a cell

Additionally, we'll use the following terms internally:

- **"File cell"** — one cell within a Files column (Note this is not "Files Cell", just for the sake of simplicity)

### Multiple files per cell

Each cell in a Files column may contain zero, one, or multiple files. Cells can not be restricted to contain a certain number of files.

### File immutability

Uploaded files are considered immutable. Mathesar will not offer any functionality to modify a file after it has been uploaded. Changing a file will require that the user removes the file and re-uploads the modified version as a new file.

### MIME sniffing

When a user uploads a file, the service layer will employ a MIME sniffing library to determine the MIME type of the uploaded file.

### File storage

File contents will be persisted to the local filesystem within the `mathesar_service` Docker container.

The "file attachments directory" will:

- contain all user-uploaded file attachments
- be mounted to a Docker volume

### File paths

Within the file attachments directory, each file will be stored according to a content-addressable path that the service layer derives.

An example path:

```
image/png/5a/5ac8a32af423f6bff83c9a270a3aa7abbafe6a90e3bd62744a1c5d7715cb0c93
```

The path derivation algorithm works as follows:

1. The sniffed MIME value is split into it's "type" and "subtype". In the example above, those values are "image" and "png". (Every MIME value always has exactly one type and exactly one subtype.)

    - The **MIME "type"** is used as the first directory.
    - The **MIME "subtype"** is used as the second directory.
    
    Note that the subtype may contain dots and plus signs. This should be okay. It will never contain spaces or forward slashes.

1. The service layer computes a SHA-256 hash of the file and serializes it to lowercase hexadecimal.

    - The **first two hex characters of the hash** are used for the third directory.
    - The **full hash** is used as the file name

Rationale:

- The service layer needs to know the MIME type in order to appropriately set the `Content-Type` HTTP header when serving the file. Encoding it in the URL is a simple way to memoize the MIME sniffing done at upload time so that we don't need to re-sniff it at serve time.

- Hash-based file storage keeps file paths tied to file content. A file uploaded twice will only be stored once — even if uploaded with different names or file extensions.

- One layer of hash-based sharding is used to address filesystem performance degradation with large directories. If a Mathesar installation has roughly 100k uploaded files, the largest directory would contain roughly 400 files. For comparison, if an installation had 1M uploaded files, then it might be more performant to use an additional layer of sharding — but we don't anticipate file attachments on that scale.

### Thumbnail images

- Mathesar will generate thumbnail images for some file types.

    We will prioritize implementing thumbnail images for **image file types**. If we end up utilizing a library which supports thumbnail images for other files types (e.g. PDF, video, docx, etc) then we will enable that support too — so long as it does not require additional implementation time on our part.
    
- Thumbnails images will be stored in the **same file attachments directory** as user uploads, using the same content-addressable file path system.

- Thumbnail images will **maintain the aspect ratio** of their corresponding source files. No cropping!

- Thumbnail image dimensions will be calculated such that the **max dimension is 100px**.

- Thumbnail images will be saved in the **AVIF** file format. (This format is very compact and now [widely supported](https://caniuse.com/avif)!)

- The AVIF compression settings will be as follows:
    - 8 bits per channel
    - Quality = 50/100
    - Do _not_ embed a color profile (to keep size down)

### Data in Postgres

Data in the Postgres user database will work as follows:

- We'll add a custom PostgreSQL composite type called `mathesar_types.local_thumbnail` with the following properties:
    - `path`: text (the file path, relative to the file uploads directory)
    - `width`: int (the width of the thumbnail image, in pixels)
    - `height`: int (the height of the thumbnail image, in pixels)

- We'll add a custom PostgreSQL composite type called `mathesar_types.local_file` which will reference _one_ locally-stored file. It will have the following properties:
    - `name`: text — e.g. "cat.jpg"
    - `path`: text (the file path, relative to the file uploads directory)
    - `size`: integer (the file size in bytes)
    - `mime_type`: text — e.g. "image/jpeg"
    - `metadata`: jsonb (additional file-type-specific metadata)
    - `thumbnail`: mathesar_types.local_thumbnail (will be NULL for file types that don't support thumbnails)

- The Postgres type for a "Files" column will be an array of `mathesar_types.local_file`.

### File name on download

When a user downloads a file, the name of the saved file will be taken from the file name as stored in Postgres.

### File name editing

Users will be able to _edit_ the file name for each file. These edits will only affect the data in Postgres. They will not touch the files stored in the file attachments directory.

Null and empty-sting file names will be _allowed_.

### File Cell Viewer

The front end will have a "File cell viewer" which allows the user to work with all the files associated with a single cell. 

Capabilities

- Upload a new file to the cell
- View thumbnails for all files in the cell, with the ability to scroll the thumbnails as necessary.
- View a single file within the browser (for supported file types, e.g. images)
- View the next/previous file within the array of files
- Remove a single file from the cell
- Rename a single file
- Download a single file

Behavior:

- The File Cell Viewer simultaneously displays a large view of one file (the "active" file) while also displaying thumbnail views for all files in the cell.
- Exactly one file is active at all times. This means that if no files are present in the cell, the file cell viewer cannot be opened.
- The file name and size are shown for the active file.
- Viewing the full file within the File Cell Viewer will only be supported for image file types (at least initially).
- Left-clicking the download link will trigger the browser's native download dialog.
- Opening the download link in a new tab will allow the user to view the file in the browser for file types supported by the browser (e.g. PDF, video, etc.)

Further UX details, design, and layout decisions are TBD.

### Empty file cells

When using Postgres arrays, an empty array is a distinct from a NULL value. This difference opens the door to potential problems for users.

The behavior of "empty" file cells needs to be consistent, from the user's perspective, For example we want to avoid a situation where users can end up with two seemingly identical "empty" file cells that actually behave differently when the "is empty" filter function is used.

Some ways we might choose to approach this problem:

- Enforce that Files columns are NOT NULL, with an empty array as a default. This gets a little tricky if the user manually removes the constraint and then sets a cell to NULL.

- Prevent empty arrays by establishing a trigger to convert an empty array to be NULL instead.

- Allow a mix of different representations of "empty"; use application logic to handle both cases.

We'll need to consider behavior for: filter, sort, group, copy, paste, "set to null", and potentially other user-facing functionality.

The best solution is TBD, pending further brainstorming and analysis of various tradeoffs.

### Loading behavior when adding a file

When the user uploads a single file, the loading experience will be very basic.

1. The user will see a loading spinner somewhere. (No progress bar.)
1. After the file is uploaded and all the server-side logic is completed (including the thumbnail generation), the spinner will resolve.

### File deletion UX

Currently, Mathesar allows the contents of a single cell to be set to NULL via the context menu. No confirmation dialog appears.

However, deleting files is (arguably) a more destructive operation, so we would like to use confirmation dialogs.

- When removing a single file from a cell, Mathesar will present a confirmation dialog.

- The "Set to NULL" cell context menu option will need to operate different on Files cells.

    - The option will be labeled:
    
        > Remove all files
    
    - It will have a confirmation dialog

### File content deletion strategy

There are many ways that file _associations_ can be removed from Postgres:

- One entry deleted from the files cell array
- The entire cell set to NULL (or empty array)
- The record deleted
- The column deleted (or even just cast to TEXT)
- The table/schema/database dropped

These operations can happen outside Mathesar too!

When a file association is removed from Postgres, what happens to the _file_?

For this MVP, Mathesar will **leave the file in place**.

Rationale:

- Because file associations can be removed outside of Mathesar, a robust file removal strategy inherently needs to be periodic instead of immediate. Otherwise orphaned files would always be possible.

- Thus, a script-based tool to remove orphaned files would seem to be a sound approach. Mathesar administrators could run such a tool on an ad-hoc basis, or configure it to run periodically via cron. The tool could also be designed to report _missing_ files too, allowing for a bidirectional reconciliation of file references.

- We don't necessarily need the file removal tool right away. So taking this approach also allows us to punt some work into the future.

### Copying and exporting file cells

When a Files cell is copied to the clipboard or exported to a CSV file, Mathesar will
serialize the content of the Postgres data to a string. None of the _file content_ will be included. The exact serialization format is not important.

### Pasting data into file cells

We'll allow Mathesar users to paste into file cells **only when copying from file cells in Mathesar**. In such cases, the data will be written directly to Postgres with no attempt at validating or modifying the files in the file attachments directory.

For the MVP, we will _not_ support:

- Copy-pasting _files_ into file cells
- Copy-pasting serialized file reference data stored in CSV format (e.g. as exported from Mathesar).

### Table page behavior

On the table page, a single file cell will:

- Display file thumbnail images, if present.
- If a file does not have a thumbnail, a generic icon will display in its place. The same icon will be used for all file types, regardless of MIME.
- Click a button to upload a file into the cell. This will open a modal into which the user can drag a file.
- Click a single file to open the file cell viewer, with the clicked file activated.

When the user does not have permission to modify the column in Postgres, the cell will be disabled. In this case, UI to upload/remove/rename will be hidden. Users will still be able to view/download files though.

### Record page behavior

On the record page, the UI for a Files field will be very similar to the UI on the table page.

Additionally (but only if it's very easy) we'd like to make the UI slightly taller (e.g. 80px tall). This way the thumbnails are clearer.

### Data explorer behavior

Behavior in the data explorer should match that of the table page (with a disabled cell). Users will be able to view and download files from the data explorer.

### Forms behavior

Initially, file attachments will not be compatible with forms. The mechanism to enforce this incompatibility (and the exact user behavior when attempting to use files in forms) will be determined during implementation.

### Filtering behavior

If it's easy, we'd like to allow users to filter on a Files column being empty (or not empty).

Aside from that, we'll not attempt to implement any files-specific filtering initially.

### Behavior of other Files-specific input elements

Throughout the Mathesar UI, there are various places that offer type-dependent inputs. In these UI locations, Mathesar will offer a simple text box for Files columns:

- A column's default value
- The record selector search field
- The value in an equality filtering condition

The text boxes in these places will be essentially useless. They won't allow users to upload files. In theory, a user could copy the Postgres cell serialization from a sheet and paste it into the default value. Perhaps that would work. But it's not important. The point is that we need to show _something_ in these UI locations and we don't have a good mechanism to hide them. So we'll show a text box, essentially as a simplified fallback, akin to our handling of unknown types.

### Record selector behavior

File thumbnails (or icons) will display in the record selector, but the user will not be able to click anything in the cell. There will be no way to open the file cell viewer.

### Import behavior

Importing from CSV will function as with an unknown type — if the value provided can be cast to the Postgres type, then Mathesar will accept it. But users will have no way of importing files into a Files column.

### Permissions behavior

Permissions for working with files follow the permissions for working with the particular Files cell, as determined in Postgres. At the Postgres level, the operations of adding, removing, and renaming files are all the same DB-level operation — it's all just an update. This means that Mathesar admin users will not have the ability to (for example) grant a user access to add files while restricting their ability to remove files. It also means that (in theory) an UPDATE could fail for more complex permissions reasons of which the front end is unable to foresee (e.g. RLS).

### Upload failure behavior

When uploading a file: two things need to happen:

- The file is written to disk
- The DB cell is updated

The service layer will ensure that **both** happen — or that **neither** happen.

### File access control

**Uploaded files will be viewable by anyone with the URL, including anonymous users.**

This is for the sake of simplicity and ease of implementation.

If we need tighter security controls in the future, we could consider implementing some sort of self-signed URLs similar to S3.

### Security

We'll ensure that uploaded SVG files and HTML files are safe to work with in Mathesar, even if they contain malicious script tags with XSS. We'll need to consider display of such files in the full viewer, as thumbnails, and when opened in a new tab.

## Tradeoffs

### Local-only backend

Our user research has shown that Mathesar administrators are likely to want support for an S3-compatible file storage backend. However to keep scope tight, the file attachments MVP will only support locally-stored files. After this project, we are likely to prioritize implementing a system for pluggable remote file storage backends, potentially using a library like [django-storages](https://django-storages.readthedocs.io/en/latest/backends/s3_compatible/index.html).

### No ability to restrict a cell to zero or _one_ file

In the future we could consider implementing a (simpler) "File" column type which has a _scalar_ file type at the Postgres level (instead of an array). This would allow users to work with files relationally — and more elegantly handle cases where one and only one file is _required_ for a record.

None of the competing products we've evaluated seem to offer such functionality, which is why we are not pursuing it at this time.

### No reordering files within a cell

Airtable allows users to drag to re-order files within a cell. We will not support this initially.

### No special filtering

Airtable allows users to perform complex filtering such as searching within all the file names of files cells. We won't implement any special filtering initially.

### No ability to drop an upload into a cell

Airtable allows users to upload files by dragging them directly into table cells. To keep scope tight, we won't support this initially.

### No upload from other sources

Airtable allows users to upload from many other sources, such as URL, Dropbox, etc. To keep scope tight, we won't support this initially.

### No file size limits

Mathesar administrators could conceivably wish to restrict file uploads to a certain size threshold. We can implement this if someone asks.

### Limited in-app file previews

Initially, file previews will be constrained to images _only_. All other file types will require the user to open them in a new tab, leveraging built-in browser file previewing, or to download the file to view it.

Other projects in the ecosystem tend to show previews for many more file types, like PDFs. This functionally technically depends on generating thumbnails, which we also do not plan to support initially.

### Single-file uploading

Our new file upload modal will only support one file at a time initially. This will allow us to leverage the existing file import component for data sources in the table import flow while minimizing the amount of changes necessary to the component.

## High-Level Implementation Plan

### DB-layer work

- New types

### New APIs

- File upload API
    - Uploads one file into one cell.
    - Probably cannot be RPC-based
    - Should accept parameters similar to `records.patch`
    - Should return a value identical to `records.patch`
    - Functionality
        - MIME sniffing
        - Hashing
        - Thumbnail generation
        - File writing
        - DB updating
        - Failover
        - Atomicity checks to guard against inconsistent state, in the event of an error

- File download API

    - Plain HTTP-based (not RPC).

    - Should be accessible anonymously
    
    - Should accept a file path string like:

        ```
        image/png/5a/5ac8a32af423f6bff83c9a270a3aa7abbafe6a90e3bd62744a1c5d7715cb0c93
        ```

        This can be a query parameter, or just part of the endpoint path itself.

    - Should also accept an optional `file_name` parameter, as a query parameter.

    - Should respond with a `Content-Type` as derived from the first two path segments.

    - Should respond with `Cache-Control` that recommends clients use aggressive caching. E.g.:

        ```
        Cache-Control: public, max-age=31536000, immutable
        ```

        This is especially important when serving thumbnails.

    - Should set
    
        ```
        Content-Disposition: inline
        ```

    - When a `file_name` parameter is supplied, should set:

        ```
        Content-Disposition: inline; filename="example.pdf"
        ```
        
        This is useful in the case where the user opens a PDF in a new tab and then decides to save it afterwards.

    - Set a strict CSP

        ```
        Content-Security-Policy: default-src 'none'; style-src 'none'; img-src 'none';
        ```

        This is an important security measure so that uploaded HTML/SVG files can't be used as XSS attack vectors.

### Frontend work

- New "File" column type

- "File" column type cell display:
    - Present a row of square attachments. Show a file icon for all non-images. Display images constrained to a square aspect ratio.
    - At the end of attachments have a "+" button which triggers the file upload modal.

- New "File Upload" Modal
    - Rework the existing file upload component (used for table importing) to support an expanded set of file types and to display in a modal.

- File Cell Viewer

    - Download button will implemented as a hyperlink:

        ```html
        <a href={downloadUrl} download={fileName}>Download</a>
        ```

### User-facing documentation work

We'll release this feature with accompanying user documentation. Specifically, it will address:

- Files being accessible anonymously via URL
- Files not being deleted when removed from the cell
- The limited in-app file previews
- No limits on file upload size
- Wow to configure the files directory to work with Docker volumes

## Research

To define the scope of this work I looked into the file attachment implementations of Airtable, Baserow, and NocoDB. All of these softwares can be easily evaluated for free to explore their file functionality and how they each handle some of the specific functionality here.

## Community Engagement

Multiple users have expressed interest or a critical dependency on this functionality in order to fully adopt Mathesar. Their feedback should be carefully considered during development with the goal of making this feature sufficient for their use cases.
