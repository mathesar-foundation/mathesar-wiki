---
title: Clipboard Interaction specs
description: 
published: true
date: 2022-03-27T00:00:00.000Z
tags: 
editor: markdown
dateCreated: 2022-03-27T00:00:00.000Z
---

## Design goals

- Allow users to copy/paste one (and sometimes multiple) cell values within Mathesar -- and also between Mathesar and another applications.

## Additional Context

- [GitHub Issue](https://github.com/centerofci/mathesar/issues/2377)
- [Usability Improvements project](https://wiki.mathesar.org/en/projects/2023-04-usability-improvements.md) which contains this work

## Terminology and abbreviations in this document

- ⏩ represents a tab character within strings
- MIME refers to a [MIME type](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types)
- TSV refers to "Tab Separated Value"
- Similar products
    - **Calc** means LibreOffice Calc
    - **Sheets** means Google Sheets
    - **Airtable** means Airtable
    - **GT** means Google Tables

## Research

### How clipboards work

- When you copy data into your system clipboard, that data is stored along with an associated MIME type. In the simplest scenario of copying plain text, the text you copy is stored along with the MIME type `text/plain`.
- The clipboard can also hold multiple representations of the same data simultaneously with each representation being associated with a different MIME type. This allows applications to do things like write `text/html` data to the clipboard for rich text while also writing `text/plain` for a plain text representation of the same data.
- When you paste, it's up to the receiving application to read the different MIME types and decide which representation to receive, potentially incorporating some user input into that decision process.
- Some applications even write other vendor-specific metadata into the clipboard, associating it with non-standard MIME types. For example, when copying cells in Google Sheets, the application writes some JSON data to the clipboard and associates it with the MIME type:

    ```
    application/x-vnd.google-docs-embedded-grid_range_clip+wrapped
    ```

- You can inspect your clipboard contents and their MIME types by pasting into this [clipboard inspector app](https://evercoder.github.io/clipboard-inspector/).

### How web clipboard APIs work

- All browsers have a [_synchronous_ clipboard API](https://developer.mozilla.org/en-US/docs/Web/API/ClipboardEvent)
    - It's based on the DOM events `copy`, `paste`, and `cut` which bubble up from the focused element any time the user triggers the corresponding keyboard shortcut.
    - It allows reading/writing data from/to the clipboard with arbitrary MIME types.
    - It's widely supported.
    - It is constrained by its reliance on user-initiated clipboard events via keyboard shortcuts. So it can't, for example, respond to copy/paste via a custom context menu.
    - It's synchronous nature has the unfortunate consequence of locking the main thread while processing the clipboard data.

- Most browsers also implement the newer [_asynchronous_ clipboard API](https://developer.mozilla.org/en-US/docs/Web/API/Clipboard)

    - It provides imperative, asynchronous methods to read and write clipboard data without responding to user events.
    - It can process large clipboard data without locking the main thread.
    - Copying plain text (i.e. MIME type `text/plain`) to the clipboard is widely supported and does not require any special permissions.
    - Copying data with any other MIME type unfortunately [lacks support](https://caniuse.com/mdn-api_clipboard_write) in Firefox.
    - Pasting text from the clipboard has even worse support, and also (by design) requires a special browser permission (for security reasons).

### How other products work

#### Copying

- MIME types
    - **Calc** writes `text/plain`, `text/html`, and a few others that we don't care about
    - **Sheets** writes `text/plain`, `text/html`, and a vendor specific representation in JSON
    - **Airtable** and **GT** only write `text/plain`

- When generating TSV text from a cell containing a newline or tab (delimiter) character
    - **Calc** and **GT** Corrupt the data, converting the delimiter to space
    - **Sheets** quotes the cell with double quotes
    - **Airtable** quotes the cell when it contains a newline but not when it contains a tab. This seems like a bug.

- When quoting a cell value that contains a double quote character
    - **Calc**, **Sheets**, and **Airtable** escape the double quote by preceding it with a double quote

- User feedback
    - **Calc** puts a dashed blue border around the copied cells
    - **Sheets** puts a then dashed black border around the cells that moves
    - **Airtable** and **GT** show a toast message

- Non-rectangular cell grids
    - **Calc** does not allow cells to be copied from multiple selections
    - **Sheets** copies the cells from the most recent selection, leaving other selections un-copied
    - **Airtable** does not allow multiple selections

#### Pasting

- MIME types
    - **Calc** and **Sheets** read `text/html` if available, with `text/plain` as a fallback
    - **Airtable** and **GT** only read `text/plain`

- When receiving pasted TSV text containing quoted cells
    - **Calc**, **Sheets**, and **Airtable** remove quotes from cells. This makes it possible to copy-paste cells that contain delimiters but also makes it impossible to copy-paste a cell containing text surrounded with double quotes. Because these products prefer reading `text/html`, this limitation may not present itself often when copying/pasting between these products.
    - **GT** had bugs that prevented me from trying this out

- User feedback
    - **Calc** removes the border around the copied cells
    - **Sheets** keeps the border around the copied cells
    - **Airtable** shows a toast message with a progress indicator
    - **GT** requires a confirmation when pasting more than one cell at a time

- When pasting into an FK column
    - **Airtable** uses the pasted value to lookup an existing record (using its "Primary field") or create a new one if needed. This is very slick.
    - **GT** works okay if the value is copied from cells within that same column, but it shows a toast error otherwise. They seem to be using some sort of internal clipboard to handle this.

- When pasting into a column of a different type
    - **Airtable** Spends time to save, but then the value is empty afterwards. Sometimes see error toast "Can't paste into this field. The destination field is computed." Overall, weird behavior. Feels buggy.
    - **GT** shows a toast error

- Non-rectangular cell grids
    - **Calc** handles each line of source data on its own, pasting over existing cells until the line terminates. Existing cells after the line ends will be left untouched.
    - **Sheets** paste into a rectangle large enough to contain all cells in the source data. Blank values are used to fill in the missing cells.
    - **Airtable** pastes all text into one cell.

- Other notes
    -  **Airtable** appears to use some sort of internal clipboard in addition to the system clipboard. I noticed this when experimenting with cells containing tab characters.

        The (three) cells `one` `two` `three` produce the TSV `one⏩two⏩three` when copied, but the (two) cells `one⏩two` `three` also produce that same TSV text. I can copy-paste the two-cell variant within the same browser tab successfully, but when I try copy-pasting that two-cell across browsers, then the two-cell variant becomes the three-cell variant. This seems to be poorly implemented to me.

## Mathesar's clipboard design

### Copying cells from Mathesar

- Copying cells is triggered by the user's platform-specific keyboard shortcut. There is no context menu entry to trigger a copy.

- When the browser's focus is on a cell element, the `copy` event copies the content of all the selected cells in the sheet which contains the focused cell.

    - When a non-cell element has focus, cells cannot be copied, even if they are selected. This behavior is somewhat important, given that we have pages like the Record Page which can contain multiple sheets (and thus distinct cell selections simultaneously).

    - Mathesar do not currently provide a visual indication when the cell has focus, but we have an [issue](https://github.com/centerofci/mathesar/issues/2380) discussing problems with this approach and ways to fix it. Those improvements can be implemented separately from the clipboard interaction implementation.

- When copying, Mathesar writes the following data to the clipboard:

    - `text/plain`
    
        This is a TSV representation of the cell data, as described in more detail below.

    - `application/x-vnd.mathesar-sheet-clipboard`

        This is a Mathesar-specific representation of the cell data, as described in more detail below.

- After copying, a toast message displays the number of cells copied. (Similar to **Airtable**)

    > Copied 3 cells.

- After copying, the cell selection border style remains as before (unlike **Sheets** and **Calc** which add a dashed border).

- Some products (e.g. **Sheets**, **Calc**) support "multiple selections" wherein the user can hold `Ctrl` to formulate a non-rectangular selection of cells. Mathesar does not currently support this feature, but it's worth considering how the clipboard feature might interact with such a feature. As noted in the "How other products work" section, no other product that I tested actually allowed the user to copy non-rectangular cell selections. So I think it's safe to say that if Mathesar implements multiple cell selections in the future, we would want to ensure that the copied cell data is always rectangular. We could enforce this constraint by disallowing the copy action when multiple selections are present (like **Calc**) or by only copying the most recently made selection (like **Sheets**).

- This spec does not implement any "cut" operation.

### TSV data representation

- Serialization
    - If a cell contains one or more tab or newline characters, then the cell value should be enclosed in double quotes
    - When enclosing a cell in double quotes, the double quote character should be escaped by preceding it with a double quote.

- Deserialization
    - _This is to be improvised during implementation taking a best effort at reversing the above serialization logic._ 😬

- Notes
    - The serialization logic seems to be pretty straightforward and consistent across **Calc** and **Sheets**, so I think it makes sense to stick with it.
    - It seems hard (impossible?) to create a deserializer which accurately reverses that logic for all cases. Sometimes cells are quoted. Sometimes they're not. It's chaos! I have also noticed inconsistencies between **Calc** and **Sheets** here. For example, **Calc** deserializes `""one""⏩two` to `"one"⏩two` whereas **Sheets** deserializes it to `one""` `two`. Both seem wrong to me, so I'm not sure what logic they're using in their deserializers.
    - It might be worth looking for a third-party CSV/TSV library to handle the serialization/deserialization.

### Mathesar-specific data representation

- It's JSON that looks like this:

    ```json
    {
      "columns": [
        { "type": "timestamp without time zone", "fk": false },
        { "type": "integer", "fk": true },
        { "type": "boolean", "fk": false },
        { "type": "text", "fk": false },
        { "type": "mathesar_types.email", "fk": false }

      ],
      "cells": [
        [
          { "raw": "1893-11-22T15:05:11.0 AD", "text": "11/22/1893 15:05" },
          { "raw": 1287, "text": "This is a record summary" },
          { "raw": false, "text": "No" },
          { "raw": null },
          { "raw": "foo@example.org" }
        ]
      ]
    }
    ```

    or, in TypeScript:

    ```ts
    interface ClipboardCells {
      columns: { type: string, fk: boolean }[];
      cells: { raw: unknown, text?: string }[][];
    }
    ```

- Each cell is stored as an object.
    - The object always has a `raw` property which holds the cell value, as transmitted via the API.
    - If the cell is formatted differently from the raw value for display, then the cell object also has a `text` property holding a string representation of the displayed value.


### Pasting cells to Mathesar

- If the clipboard has data with a MIME type matching our Mathesar-specific representation, we use that data. Otherwise, we use the `text/plain` data.

- When using plain text paste data, Mathesar displays a modal which allows the user to configure the parsing of the paste data. This feature has some overlap with the [UI for Importing data into existing tables](https://wiki.mathesar.org/en/community/mentoring/project-ideas/ui-import-data-existing-table) GSoC project, so it is not yet fully specified.

- After pasting, all pasted cells are selected.

- Non-rectangular data is handled in the same manner as **Calc** (described above).

- Pasting across multiple records is handled via a new, yet-to-be designed API. It might look something like this

    `POST`

    ```json
    [
      {
        "table": 1287,
        "data": [
          { "1": 17, "3": "foo", "18": null },
          { "1": 18, "3": "bar", "18": "baz" },
          { "1": 19, "3": null, "18": "bat" },
        ]
      }
    ]
    ```

    The API would handles updating existing records as well as creating new records.

    This API is subject to further discussion and design. It could be that we don't even need it.

- If the paste data extends beyond the column limits, Mathesar shows an error and no data is modified

    > **Unable to Paste**
    > 
    > The table does not have enough columns to hold the copied data.

- If the paste data extends beyond the rows displayed in the table, then new rows are added as needed. This means that it's possible to paste into the placeholder row at the bottom of the table.

    The sheet has separate sections for displays "saved records" and "new records" with "new records" extending past the pagination page size. This presents a challenge for pasting new records because there could be hundreds of new records and we don't necessarily want to hold all that data in memory as the user continues to use the application.

    If, after pasting, the number of new records will be 50 or fewer, then the sheet displays them as new records, as if the user had manually added them.

    If, after pasting, the number of new records will be more than 50, then the sheet fully refreshes, wiping out any new records that were displayed on the sheet prior to pasting.

- When the paste data has an empty string for a cell value, `null` is used if possible, with an empty string as a fallback for non-nullable text columns.

- When multiple cells are selected during paste:

    - The paste data is repeated as needed to completely fill the selection. (Same as **Calc**.)
    - If the paste data extends beyond the selection, then the selection is increased to fit the paste data. (Same as **Sheets**.)

#### Pasting cells into columns of different types

1. Column metadata from the source data is matched to columns in the target table. For each pairing, the following logic takes place:
    - Some pairings of column types cannot be pasted. For example an `email` column cannot be pasted into a `number` column. These pairings result in an error.
    - If the target column is a text column and the source column has formatted values, then Mathesar asks the user what to do. Examples of this include copying FK data into a text column, or copying dates into a text column.

1. If any pairing results in an error, Mathesar aborts the paste and displays a toast error to the user such as:

    > **Unable to Paste**
    >
    > Email data cannot be pasted into a Number column.

1. If any pairing results in a "ask" outcome, then Mathesar prompts the user via a dialog like the following:

    > **Paste**
    >
    > The data you are pasting can be represented in multiple ways. Paste the raw values to use the text
    >
    > `Paste Raw Values` &nbsp; &nbsp; &nbsp; `Paste Formatted Values`

    "Paste Formatted Values" is selected by default.

    When "Paste Formatted Values" is chosen, formatted values will be used for the paste when possible. Otherwise, raw values will be used.


## Design imperfections and future considerations

- In my [initial "copy" implementation](https://github.com/centerofci/mathesar/pull/2773), I notice that copying a lot of cells takes some time and **locks the main thread.** This is not great, but it's because we're using the sync API. It's hard to get around this though since the async API isn't fully implemented in Firefox yet. We could potentially use the async API if it's available, while falling back to the sync API for Firefox. If we want to do that, I'd rather do it later when/if users ask for improved performance here.

- It would be nice to add **context menu entries for copy/paste**, but there are some challenges here.

    - When copying: If we use the synchronous clipboard API it seems[^1] that we can't trigger copy events programmatically. Somehow Google Sheets is doing it, but I haven't dug deeper to figure out how. With the async clipboard API Firefox lacks support for MIME types other than `text/plain`.

    - When pasting: The synchronous clipboard API doesn't allow programmatic pasting at all. The async clipboard API doesn't work allow pasting in Firefox and requires a special permission in other browsers.

    We could consider showing context menus in some browsers. We could also consider showing a "How to Paste" modal on paste which only serves to add discoverability to the clipboard feature. **Sheets** actually does this when you choose the "Paste" option whin the context menu.

    Overall, this doesn't seem worth the additional complexity currently.


- It would be nice to copy an **HTML representation** (i.e. `text/html`) of the cell data too.

    - This would allow users to copy data from Mathesar and paste into word-processing applications as an HTML table.
    - This behavior would be consistent with **Calc** and **Sheets**.
    - It would allow better copy/paste of text containing tabs, newlines, and quotes
    - It would take some extra processing time to generate the data though, and I'd kind of like to avoid that until Firefox has implemented the async clipboard API.
    - We could consider taking this up later.

[^1]: MDN [says](https://developer.mozilla.org/en-US/docs/Web/API/Element/copy_event)

    > It's possible to construct and dispatch a synthetic copy event, but this will not affect the system clipboard.



