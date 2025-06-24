# Usage of Foreign Key Constraints

## Context

This spec describes the design solution for [Usage of Foreign Key constraints](https://github.com/mathesar-foundation/mathesar/issues/243).

## Prototype Link and Video Walkthrough

### Prototype

[Prototype Link](https://mathesar-prototype.netlify.app/)

### Videos

----

- Scenario 1: <https://www.loom.com/share/01fb12b24f0e4270822da212622a8844>
- Scenario 2: <https://www.loom.com/share/87fce49545c744d1b475693b7d43c2bf>
- Scenario 3: <https://www.loom.com/share/e43763b172e449fa9fddff25b311123f>
- Scenario 4: <https://www.loom.com/share/6deed11141f34c4ba495c4adb7117982>
- Scenario 5: <https://www.loom.com/share/b90ee712055a4a9cb24a499f943c0bbe>

----

## Scenarios

### Scenario 1: User Adds a Foreign Key Constraint

A user wants to link records from another table into their current table. Both tables belong to the same schema. For this purpose, foreign key constraints can change the relationship between one table and another based on the values of columns belonging to the linked tables.

### Scenario 1a: Automatically adding foreign key constraints from the 'Link Table' dialog

#### Assumptions for 1a

- The user is not familiar with the concept of foreign keys.
- The user has at least one table with a (non-composite) primary key constraint set.

#### Steps for 1a

- The user starts the link Table process by clicking on the `Link Table` button in the table toolbar area.
- The user reads the instructions presented within the link table component and understands that the tables will be linked by setting up a foreign key constraint. They also understand that manual configuration is available.
- The user selects the table they wish to link to from the [table selector](#table-selector).
  - Only tables that have a primary key constraint will allow selection. Tables without a primary key constraint will still be listed but shown with a warning.
- A list of questions is displayed once a table is selected. The user can answer 'yes' or 'no' depending on the relationship they want to create.
- The user answers all the questions listed. The answers will determine the location of the foreign key or whether a new table needs to be created.
  - Answering 'yes' to both questions will set up a mapping table with foreign key columns for both tables, creating a many-to-many relationship.
  - Answering 'yes' to any of the questions and 'no' to the other will set up a foreign key column in the appropriate table, creating a one-to-many relationship. The system will add the column to the table on the 'many' side of the relationship.
  - Answering 'no' to both questions will set a unique constraint on a new column so that each record can only be linked to another unique record from the other table, creating a one-to-one relationship.
- Once questions are answered, the dialog will display a summary of the system's changes in a section titled 'Under the Hood.' At the same time, a diagram illustrating the structure of the new relationship is displayed next to the questions.
- Before creating the link, the user will have the chance to rename the new columns or tables. Invalid column or table names should prevent saving.

### Scenario 1b: Manually from the 'Table Constraints' settings

#### Assumptions for 1b

- The user is not familiar with the concept of foreign keys.

#### Steps for 1b

- A user wants to set up a foreign key constraint to single or multiple columns to a currently active table.
- The user opens the table options by clicking on the table name label in the toolbar area. From the menu, the user selects the option 'Table Constraints.'
- This opens a dialog from which the user can set all supported constraint types.
- The user sees a layout with two panels. On one side, all the existing constraints are listed. On the other side, a form with the constraints configuration is displayed. The form corresponds to the currently active list item.
- The list panel contains actions at the bottom of the panel. The user can choose to add or delete an item from the list. The user clicks on 'Add' to create a new constraint.
- The user is presented with a form. From there, they select the type of constraint to be added. The user selects the 'Foreign Key' constraint option from the list.
The user selects single or multiple columns to which they wish to apply the constraint.

- The user selects a table to be referenced by these columns.
- The user selects a column in the reference table from which the column will match values. This is set to the 'Primary Key' column in the referenced table by default. When changing this field, the user can select only columns with a `UNIQUE` or `PRIMARY KEY` constraint.

## Scenario 2: User Deletes an Existing Foreign Key Constraint

### Scenario 2a: From table constraint settings

#### Assumptions for 2a

- This scenario assumes that the system will not allow users to update foreign keys. The process to edit a foreign key will be to drop it and replace it.

#### Steps for 2a

- A user wants to edit an existing foreign key constraint to change the referring column or select another referenced table.
- The user can view the details for an existing foreign key constraint by clicking on the 'Table Constraints' option in the table menu.
- From the list of constraints, the user selects the constraint for which they want to see details.
- The user Deletes the selected constraint.

## Scenario 3: User Identifies a Column With a Foreign Key Constraint Applied

### Scenario 3a: The foreign key constraint is set to a single column

#### Steps for 3a

- The user opens a table containing at least one column with a foreign key constraint applied.
- The user can identify the columns in two ways:
  - The user looks at the column header and sees a foreign key indicator. The indicator shows a key icon and the referenced table and column names.
  - The cell content is styled as a tag-like element with a colored background. The cell also contains a toggle to open the `record selector` dropdown.

### Scenario 3b: The foreign key constraint is set to multiple columns

#### Steps for 3b

- The user opens a table containing columns with a multi-column foreign key constraint applied.
  - The indicator, in this case, looks similar to the single-column one. However, the user will understand that the foreign key constraints reference the same table.
    - The user can tell that a referenced table is the same because they share the same color. The system could use other UI elements instead of color. Still, the idea is to create a visual distinction that users can scan easily.

## Scenario 4: User Sees a Preview of the Linked Record in a Column With a Foreign Key Constraint Applied

In most cases, the values displayed within a foreign key column won't identify the associated record. A preview of the linked record in columns with a foreign key constraint can help the user identify it.

By default, the preview will include columns based on specific criteria, such as constraints applied or data type. However, users can change these by updating the referenced table preferences.

### Scenario 4a: The option for record preview is enabled

#### Steps for 4a

- The user opens a table containing columns with a foreign key constraint applied.
  - The column contains the referenced values for each cell. Five fields are displayed.
    - The displayed fields from the reference table are prioritized applying the following criteria:
      - They have unique values, meaning that either a primary key, foreign key, or unique constraint are applied to the column.
      - They have a text data type.
    - If the user wants to show specific fields, these can be selected in the referenced table options under the 'Table Preferences' option.

- The displayed fields are presented as concatenated values. The visual contrast between the field name and its corresponding value increases readability.
- When clicked, the field displays the [record selector](#record-selector) component containing a pre-filtered list. A single matching item is displayed.
- The user can disable the record preview by opening the 'Table Link' preferences from the column header menu and unchecking the 'Show Record Preview' option.

### Scenario 4b: The option for record preview is disabled

#### Steps for 4b

- The user opens a table containing columns with a foreign key constraint applied.
  - The column contains the primary key value for the referenced column only.
  - When clicked, the field displays the [record selector](#record-selector) component containing a pre-filtered list. A single matching item is displayed.
- The user can enable the record preview by opening the 'Table Link' preferences from the column header menu and checking the 'Show Record Preview' option.

## Scenario 5: User Edits the Values of a Column With a Foreign Key Constraint Applied

Linked records can be changed or deleted according to the user's preference. Since values are references to records in other tables, users must understand that changes to references don't affect the original records. However, changes to the values of records in the referenced table do.

### Scenario 5a: The field has an existing value

#### Steps for 5a

- The user opens a table containing columns with a foreign key constraint applied.
  - The column contains the referenced values for each cell.
  - When clicked, a pre-filtered list is displayed inside the [record selector](#record-selector) component. The dropdown includes a search input that will show other matching records if modified. Clicking on any of those records will close the dropdown and replace the existing one.
  - Note that in the case of multi-column foreign key constraints, there will be no dropdown displayed, and the user can edit the field like a regular text field.
  
### Scenario 5b: The field is empty

#### Steps for 5b

- The user opens a table containing columns with a foreign key constraint applied.
  - The column contains no values.
  - When clicked, a list of records is displayed inside the [record selector](#record-selector) component. The list shows the first 50 records.
  - An text input field is available within the dropdown to filter the records based on partial or complete value matches. The list narrows down the records as the user types in a value. The system can search only the first five fields. Search across all types is supported.
  - If there's a single match for the entered value, it should become highlighted, allowing the user to confirm the selection.
  - If there aren't any matches, a suggestion to change the 'Search Columns' table preference is displayed.

## Components

### Record Selector

The record selector component retrieves records from other tables and adds them as values to cells. The list of records is shown according to the referenced table set in a foreign key constraint column.

### Table Selector

The table selector allows users to select tables from a schema. This spec doesn't go into details on how this selector would work. It also doesn't consider the scenario for selecting both tables and views.

### Record Preview

The record preview allows users to identify records linked in other tables. It shows the first five field names and values. A specific limit for the value length needs to be defined so that space usage is optimal.

### Table Constraints

The table constraints settings list and provide details for all table-level constraints. Its most basic implementation will allow users to know which constraints exist and see the columns they apply. Users will also add or delete constraints but not edit them.

### Table Preferences

Table preferences will contain a group of options that users can set up to change specific properties of tables relevant only in the context of Mathesar, meaning they don't alter any database table properties. An example of this could be setting up a table's default search columns.

## Other Considerations

### Linked Records for Multi-Column Foreign Key Constraints

- The current UI does not consider multi-column foreign key constraints and how those would be retrieved and selected. Record search and selection via the dropdown component will not be supported. Instead, the cells will be limited to input and edit text values. The text values will have to match the primary keys of the referenced records and be unique.

### Usage of Color

- A suggestion to use color as a means to differentiate table references has been included in this spec. However, implementation details need to be discussed before deciding if the user interface will use color elements to create a visual connection between elements.

## Related Discussions

- [Add 'Table Link Preferences' Option to Column Menu](https://github.com/mathesar-foundation/mathesar/discussions/854)
- [Editing values for columns with a foreign key constraint applied](https://github.com/mathesar-foundation/mathesar/discussions/796)
- [Handling duplicate foreign key columns from the 'Link Table' dialog](https://github.com/mathesar-foundation/mathesar/discussions/791)
- [Help users link tables via question-based forms](https://github.com/mathesar-foundation/mathesar/discussions/790)
- [Handling Composite Primary Keys and Junction Tables](https://github.com/mathesar-foundation/mathesar/discussions/804)