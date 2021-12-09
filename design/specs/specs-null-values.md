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

`NULL` values indicate that a value does not exist in a database. It is important to clarify that `NULL` is not the same as blank or zero. Ideally, we want users to think of `NULL` values as placeholders for unknown or missing values that are applicable.

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
    - The cell has a lighter background-color
    - The cell has a muted text color
    - The cell has a different font style (italic)

#### Scenario 1b: The user identifies a `NULL` value in a record preview

##### Steps for 1b

1. The user edits a value in a column that links to records from another table.
2. The user sees the list of records displayed in the record selection dropdown.
3. The user identifies a record that contains a `NULL` value.
    - The field contains the word `NULL` in all uppercase letters
    - The text has a muted text color
    - The text has a different font style (italic)

### Scenario 2: User edits a `NULL` Value

#### Scenario 2a: The data type is text

##### Steps for 2a

1. The user edits a `NULL` value in a column that is set to text data type.
2. The user double-clicks the value cell to enter edit mode.
3. The user enters a value and leaves edit mode by pressing the enter key or clicking outside of the active cell.
4. The `NULL` value is replaced by the new value.

#### Scenario 2b: The data type is text, and the value is cleared

#### Steps for 2b

1. The user edits a `NULL` value in a column that is set to text data type.
2. The user double-clicks the value cell to enter edit mode.
3. In edit mode, a text input box is displayed with a placeholder set to `NULL`.
4. The user types in a value, and the placeholder text is replaced by the new typed-in value.
5. The user clears the new value by hitting the backspace key until the value is completely cleared.
6. The user exits edit mode.
7. The `NULL` value is replaced by an empty string, and the cell is blank.

#### Scenario 2c: The data type is boolean with checkbox display enabled

##### Steps for 2c

1. The user edits a `NULL` value in a column that is set to boolean type with the checkbox display property enabled.
    - The field contains a checkbox in an indeterminate state.
    - Hovering over the `NULL` checkbox will display a tooltip with the '`NULL`' legend.
2. The user clicks on the checkbox, going from indeterminate (`NULL`) to checked (TRUE).
3. The user can click on the checkbox again to mark it as false and go back to `NULL`.

#### Scenario 2d: The data type is number

##### Steps for 2d

1. The user edits a `NULL` value in a column set to number type.
2. The user double-clicks the cell to enter edit mode.
3. The user exists in edit mode without making any changes.
4. The `NULL` value remains.

### Scenario 3: User sets a value to `NULL`

#### Scenario 3a: The column accepts `NULL` values

##### Steps for 3a

1. The user selects a cell in a column that contains a value.
2. The user clears the content of the selected cell.
    - By pressing the `delete` key.
    - By opening the contextual menu and selecting the 'Set as `NULL`' option.
3. The selected cell now has a `NULL` value.

#### Scenario 3b: The column does not accept `NULL` values

##### Steps for 3b

1. The user selects a cell in a column that contains a value.
2. The user attempts to clear the content of the selected cell.
    - By pressing the `delete` key.
        - The system prevents the insertion of a `NULL` value.
        - An error message indicates that a NOT `NULL` constraint is applied to the column, and the system cannot insert `NULL` values.
    - By opening the contextual menu and selecting the 'Set as `NULL`' option.
        - The 'Set as `NULL`' option is disabled, and the user cannot select it.

## Interactions

### edit mode Behavior

The 'edit mode' state of a cell changes some interactions or provides additional functionality to users while editing data in a table. How users enter and exit 'edit mode' must be defined in better detail as more data types and cell-level functionality are introduced.

For the implementation of this spec, we should consider the following notes:

1. User highlights the cell with a single click. Pressing the `delete` or `backspace` key will delete the cell state and convert it to a `NULL` value.
2. The user presses any key other than `delete` or `backspace` the cell enters edit mode.  Pressing `delete` or `backspace` will delete the text inside the cell.

The same can be applied for boolean types too. The `checkbox` should be smaller than the cell.

1. Clicking outside the `checkbox` would select the cell, and pressing `delete` would make the cell `NULL`
2. Clicking inside the `checkbox` would toggle the value of the checkbox, similar to spreadsheets.

## Related Discussions

- [UX for NULL Values](https://github.com/centerofci/mathesar/discussions/832)
