---
title: NULL Value Specs
description: 
published: true
date: 2021-11-25T09:00:00.201Z
tags: 
editor: markdown
dateCreated: 2021-11-25T09:00:00.201Z
---

## Context

A `NULL` value indicates that a value does not exist in a database. It is important to clarify that `NULL` is not the same as blank or zero. Ideally, we want users to think of `NULL` values as placeholders for unknown or missing values applicable otherwise.

## Prototype

### Link

[Prototype](https://mathesar-prototype.netlify.app/?activeTable=2)

### Videos

- Scenario 1  [Video](https://www.loom.com/share/b12f7634961e4cf29e258d2e46f2a7be)
- Scenario 2: [Video](https://www.loom.com/share/bd127b3214794cd5bf22a146a1ea7ae8)
- Scenario 3: [Video](https://www.loom.com/share/c998551736104417ac671b5d556f3365)

## User Experience

### Considerations for handling `NULL` Values

When presented in tables, `NULL` values should be visually distinct so that the user understands that they are not the same as other string types. The style should attempt to communicate the absence of a value, similar to how placeholders are used in text input fields.
As for the process of transforming values to and from `NULL`, it will be important to have a consistent way of doing this across different data types.

## Scenarios

### Scenario 1: User identifies a `NULL` Value

#### Scenario 1a: The user identifies a `NULL` value in a table

##### Steps for 1a

1. The user opens a table that contains `NULL` values.
2. The user identifies a cell that contains a `NULL` value.
    - The cell contains the word `NULL` in all uppercase letters
    - The cell has a different styling
        - A lighter background-color
        - A muted text color
        - A different font style (italic)

#### Scenario 1b: The user identifies a `NULL` value in a record preview

##### Steps for 1b

1. The user edits a value in a column that links to records from another table.
2. The user sees the list of records displayed in the record selection dropdown.
3. The user identifies a record that contains a `NULL` value.
    - The field contains the word `NULL` in all uppercase letters
    - The text has a muted text color
    - The text has a different font style (italic)

#### Scenario 1c: The user identifies a `NULL` value in a boolean type column in checkbox display mode

##### Steps for 1c

1. The user opens a table that contains `NULL` values.
2. The user identifies a cell that contains an indeterminate state checkbox.
3. The user hovers over the indeterminate checkbox, and a tooltip with the legend `NULL` is displayed.

### Scenario 2: User edits a `NULL` Value

#### Scenario 2a: Replacing `NULL` with a new value

##### Steps for 2a

1. The user edits a `NULL` value in a column.
2. The enters `edit mode`.
3. The user enters a new value and leaves `edit mode` by pressing the `enter` key or clicking outside the active cell.
4. The new value replaces the `NULL` value.

#### Scenario 2b: Replacing `NULL` with an empty string

##### Steps for 2b

1. The user edits a `NULL` value in a column.
2. The user enters `edit mode`.
3. A text input box is displayed in `edit mode` with a placeholder set to `NULL`.
4. The new typed-in value replaces the placeholder text.
5. The user clears the new value by pressing the `backspace` key until the value is completely cleared.
6. The user leaves `edit mode`.
7. An empty string replaces the `NULL` value. The cell appears blank.

#### Scenario 2c: The data type is boolean with checkbox display mode enabled

##### Steps for 2c

1. The user edits a `NULL` value in a column set to boolean type with the checkbox display mode enabled.
    - The field contains a checkbox in an indeterminate state, meaning the value is `NULL`.
2. The user clicks on the checkbox, going from indeterminate `NULL` to checked `TRUE`.
3. The user can click on the checkbox again to mark it as `FALSE`.
4. To return the value to `NULL`, the user can select the cell and press the `delete` key or use the contextual menu and select the `Set as NULL` option.

#### Scenario 2d: The data type is number

##### Steps for 2d

1. The user edits a `NULL` value in a column set to `number` type.
2. The user double-clicks the cell to enter `edit mode`.
3. The user leaves `edit mode` without making any changes.
4. The `NULL` value remains unchanged.

### Scenario 3: User sets a value to `NULL`

#### Scenario 3a: The column accepts `NULL` values

##### Steps for 3a

1. The user selects a cell in a column that contains a value.
2. The user clears the content of the selected cell.
    - By pressing the `delete` key.
    - By opening the contextual menu and selecting the `Set as NULL` option.
3. The selected cell now has a `NULL` value.

#### Scenario 3b: The column does not accept `NULL` values

##### Steps for 3b

1. The user selects a cell in a column that contains a value.
2. The user attempts to clear the content of the selected cell.
    - By pressing the `delete` key.
        - The system prevents the insertion of a `NULL` value.
        - An error message indicates that a NOT `NULL` constraint is applied to the column, and the system cannot insert `NULL` values.
    - By opening the contextual menu and selecting the `Set as NULL` option.
        - The 'Set as `NULL`' option is disabled, and the user cannot select it.

## Interactions

### Select vs. Edit Mode Behaviors

When in `Edit Mode`, a cell provides additional functionality and interactions to users. `Edit Mode` is toggled by double-clicking on a cell. However, certain data types could have different interactions. Once specific behaviors and components for each data types are introduced, these interactions will needs to be further defined to ensure compatibility.

#### Text or Numeric Types

For the implementation of this spec, we should consider the following notes regarding the editing of text and numeric types as summarized in the following table:

| current mode | DOM `key` | result |
| -- | -- | -- |
| select | any text character | switch to edit mode, place cursor at end, append character to end of cell contents |
| select | `Backspace` | switch to edit mode, place cursor at end, delete last character |
| select | `Delete` | nothing |
| select | `Shift+Backspace` | set cell value to NULL |
| select | `Shift+Delete` | set cell value to NULL |
| edit | `Backspace` | delete character to the left of cursor |
| edit | `Delete` | delete character to the right of cursor |

#### Boolean Type

In the case of boolean types, consider the following:

- Consider that the `checkbox` is smaller than the cell, so clicking outside the `checkbox` would select the cell, and pressing `delete` would make the cell `NULL.`
- Clicking inside the `checkbox` would toggle the value of the checkbox, similar to spreadsheets.

#### With Dropdown Enabled

Certain column configurations will display a dropdown when editing the contents of a cell. For example, a column with a single-column foreign key constraint will show a record selector dropdown when in edit mode.

In the case of cells with dropdown enabled, consider the following:

- If no record is selected the cell content should be `NULL`
- To set content of the cell as `NULL` the user can press the `delete` key while the cell is in `select mode`.
- To set content of the cell as `NULL` the user can deselect a selected record from the record selector, by clicking on a selected item and then closing the dropdown.

## Related Discussions

- [UX for NULL Values](https://github.com/centerofci/mathesar/discussions/832)
