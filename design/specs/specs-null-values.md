---
title: Null Value Specs
description: 
published: true
date: 2021-11-25T09:00:00.201Z
tags: 
editor: markdown
dateCreated: 2021-11-25T09:00:00.201Z
---

## Context

NULL values are used to indicate that a value does not exist in a database. It is important to make it clear to users that NULL is not the same as blank or zero. Ideally, we want users to think of NULL values as placeholders for unknown or missing values that are applicable.

## Prototype

### Link

[Prototype](https://mathesar-prototype.netlify.app/?activeTable=2)

### Videos

- Scenario 1: [Video](https://www.loom.com/share/527224982d534a2db082359360147ad4)
- Scenario 2: [Video](https://www.loom.com/share/7de3c90af3d74ac195397c643f318867)
- Scenario 3: [Video](https://www.loom.com/share/7ea4ca9fe3e14acdbffac5ea8e77e760)

## User Experience

### Considerations for handling NULL Values

When presented in the form of tabular data, NULL values should be visually distinct so that the user understands that they are not the same as other string types. The style should attempt to communicate the absence of a value, similar to how placeholders are used in text input fields.
As for the process of transforming values to and from NULL, it will be important to have a consistent way of doing this across different data types.

## Scenarios

### Scenario 1: User identifies a NULL Value

#### Scenario 1a: The user identifies a NULL value in a table

#### Steps for 1a

1. The user opens a table that contains NULL values
2. The user identifies a cell that contains a NULL value
    - The cell contains the word NULL in all uppercase letters
    - The cell has a lighter background-color
    - The cell has a muted text color
    - The cell has a different font style (italic)

#### Scenario 1b: The user identifies a NULL value in a record preview

#### Steps for 1b

1. The user edits a value in a column that links to records from another table
2. The user sees the list of records displayed in the record selection dropdown
3. The user identifies a record that contains a NULL value
    - The field contains the word NULL in all uppercase letters
    - The text has a muted text color
    - The text has a different font style (italic)

### Scenario 2: User edits a NULL Value

#### Scenario 2a: The data type is text

#### Steps for 2a

1. The user edits a NULL value in a column that is set to text data type
2. The user double-clicks the value cell and enters edit mode
3. The user enters a value and leaves edit mode by hitting enter or clicking outside of the active cell
4. The NULL value is replaced by the new value

#### Scenario 2b: The data type is text, and the value is empty

#### Steps for 2b

1. The user edits a NULL value in a column that is set to text data type
2. The user double-clicks the value cell and enters edit mode
3. The user doesn't enter a value and leaves edit mode by hitting enter or clicking outside of the active cell
4. The NULL value is replaced by an empty string

#### Scenario 2c: The data type is boolean with checkbox display enabled

#### Steps for 2c

1. The user edits a NULL value in a column that is set to boolean type with the checkbox display property enabled
    - The field contains a checkbox in an indeterminate state
2. The user clicks on the checkbox, going from indeterminate (NULL) to checked (TRUE).
3. The user can click on the checkbox again to mark it as false. However, it does not go back to NULL.

#### Scenario 2d: The data type is number

#### Steps for 2d

1. The user edits a NULL value in a column that is set to number type
2. The user double-clicks the cell to enter edit mode
3. The user exists in edit mode without making any changes
4. The NULL value remains

### Scenario 3: User sets a value to NULL

#### Scenario 3a: The column accepts NULL values

#### Steps for 3a

1. The user selects a cell in a column that contains a value
2. The user clears the content of the selected cell
    - By pressing the delete key
    - By opening the contextual menu and selecting the 'Set as NULL' option
3. The selected cell now has a NULL value

#### Scenario 3b: The column does not accept NULL values

#### Steps for 3b

1. The user selects a cell in a column that contains a value
2. The user attempts to clear the content of the selected cell
    - By pressing the delete key
        - The system prevents the insertion of a NULL value
        - An error message indicates to the user that a NOT NULL constraint is applied to the column, and the system cannot insert NULL values
    - By opening the contextual menu and selecting the 'Set as NULL' option
        - The 'Set as NULL' option is disabled, and the user cannot select it

## Related Discussions

- [UX for NULL Values](https://github.com/centerofci/mathesar/discussions/832)
