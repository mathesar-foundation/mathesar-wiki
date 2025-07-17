# File Attachments

[Requirements](../requirements/2025/file-attachments.md)

## Solution

Mathesar will implement support for file attachments on records by introducing a new "Files" column type that allows users to upload, remove, and view files. The files column can contain one or multiple files. Files will be persisted to the local filesystem and the actual database will store files in a JSON structure which references the paths to files alongside any other necessary metadata.

The user will be able to filter and sort in Mathesar's UI based on the file column. Filtering on files can be done by:

- "Files" column is or isn't NULL (are attachments present or not?)
- "Files" column filenames contains value (Simple text search of aggregated file names)
- "Files" column contains file type (Hardcoded list of file types based on MIME type, inferred at upload)

## Tradeoffs

### Local-only backend

Initially, file support will use a local filesystem backend, with support for Docker-based deployments to mount the files directory to a volume. As follow-up work to this project we will add support for S3 protocol-compatible remote backends, potentially using a library like [django-storages](https://django-storages.readthedocs.io/en/latest/backends/s3_compatible/index.html).

### Limited in-app file previews

Initially, file previews will be constrained to images _only_. All other file types will require the user to open them in a new tab, leveraging built-in browser file previewing, or to download the file to view it.

Other projects in the ecosystem tend to show previews for many more file types, like PDFs. This functionally technically depends on generating thumbnails, which we also do not plan to support initially.

### No thumbnail generation

To improve load times and data usage for tables with many attachments, most applications generate thumbnails of attached images. For this MVP, will we exclude this functionality. We will prioritize adding it in later if we see users encountering performance issues.

### Single-file uploading

Our new file upload modal will only support one file at a time initially. This will allow us to leverage the existing file import component for data sources in the table import flow while minimizing the amount of changes necessary to the component.

### Paste and import support

To keep this simple initially:

- The user _can_ paste the value of one file column cell into another file column cell
- The user _can't_ paste a file into a Mathesar cell to upload it and attach it to a record
- The user _can_ import files into Mathesar through the standard import flow. This only supports columns of public urls to files.

This will mean initially that there is a gap in functionality where users will not be able to "bulk" import files into existing tables.

### Editing file metadata

Initially, we will not allow users to edit filenames or any other metadata.

## High-Level Implementation Plan

### Frontend work

- New "File" column type
- "File" column type cell display:
 - Present a row of square attachments. Show a file icon for all non-images. Display images constrained to a square aspect ratio.
 - At the end of attachments have a "+" button which triggers the file upload modal.
- New "File Upload" Modal
  - Rework the existing file upload component (used for table importing) to support an expanded set of file types and to display in a modal.
- "Lightbox view" for file cells
  - Clicking a focused "File" cell will trigger a simple lightbox that displays:
    - Left/right buttons to cycle through the files in the cell
    - Thumbnails of the files in the cell (similarly to the in-cell representation)
    - And for the active file, displays:
      - The file name
      - A button to remove the current file from the record
      - An large, centered image, for images, otherwise the same simple icon from the cell view
      - A "download" button for the current file
      - If simple, we should also show the filesize and MIME type, but this is optional

### Backend work

- Configuration for the file backend
- Documentation for users on how to configure the files directory to work with Docker volumes
- RPC methods for:
  - Uploading files
  - Storing files in the DB
  - Deleting files
- Wiring to download files from URLs during the import flow

## Research

To define the scope of this work I looked into the file attachment implementations of Airtable, Baserow, and NocoDB. All of these softwares can be easily evaluated for free to explore their file functionality and how they each handle some of the specific functionality here.

## Community Engagement

Multiple users have expressed interest or a critical dependency on this functionality in order to fully adopt Mathesar. Their feedback should be carefully considered during development with the goal of making this feature sufficient for their use cases.
