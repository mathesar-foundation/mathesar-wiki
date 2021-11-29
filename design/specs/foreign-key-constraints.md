---
title: Usage of Foreign Key Constraints
description: 
published: true
date: 2021-11-09T16:59:23.145Z
tags: 
editor: markdown
dateCreated: 2021-10-19T09:20:55.088Z
---
## Context

This spec describes the design solution for [Usage of Foreign Key constraints](https://github.com/centerofci/mathesar/issues/243).

## Prototype Link and Video Walkthrough

### Prototype

[Prototype Link](https://mathesar-prototype.netlify.app/)

### Videos

- All Scenarios (LATEST): <https://www.loom.com/share/725945b7cc074b7ebc42f62bdd5f325e>

----

- Scenario 1: <https://www.loom.com/share/def72e9ff7754b9e833c18dbdf9958c7>
- Scenario 2: <https://www.loom.com/share/6aeeb12f776f4307beca97057ff60c48>
- Scenario 3: <https://www.loom.com/share/d2cf81ac75ce47e8941669720ecc28e9>
- Scenario 4: <https://www.loom.com/share/be12a128b41d443281babab0ccbcd112>
- Scenario 5: <https://www.loom.com/share/9b5ab511981e4850acd7453fc907c81b>

## Scenarios

### Scenario 1: User Adds a Foreign Key Constraint

A user wants to link records from another table into their current table. Both tables belong to the same schema. For this purpose, foreign key constraints can be applied to change the relationship between one table and another based on the values of columns of the linked tables.

### Scenario 1a: Automatically adding foreign key constraints from the 'Link Table' dialog

#### Assumptions for 1a

- The user is not familiar with the concept of foreign keys.
- The user has created tables within Mathesar, where the ID column is automatically generated and set as primary key.

#### Steps for 1a

- The user starts the 'Link Table' process by clicking on the 'Link Table' button in the table toolbar area.
- The user reads the instructions presented within the [link table](#link-table) component and understands that the tables will be linked by setting up a foreign key constraint. They also understand that manual configuration is available.
- The user selects the table they wish to link to from the [table selector](#table-selector).
- A list of questions is displayed. The user can answer 'yes' or 'no' depending on the relationship they want to create.
- The user answers all the questions listed. The answers will determine the location of the foreign key or whether a new table needs to be created.
  - Answering 'yes' to both questions will set up a mapping table with foreign key columns for both tables, creating a many-to-many relationship.
  - Answering 'yes' to any of the questions and 'no' to the other will set up a foreign key column in the appropriate table, creating a one-to-many relationship. The column is added to the table on the 'many' side of the relationship.
  - Answering 'no' to both questions will set a unique constraint on a new column so that each record can only be linked to another unique record from the other table, creating a one-to-one relationship.
- Once questions are answered,  a summary of the system's changes is displayed in a section titled 'Under the Hood.' At the same time, a diagram illustrating the structure of the new relationship is displayed next to the questions.
- Before creating the link, the user will have the chance to rename the new columns or tables. Invalid column or table names should display an inline warning and prevent saving.

### Scenario 1b: Manually from the 'Table Constraints' settings

#### Assumptions for 1b

- The user is somewhat if not entirely familiar with the concept of foreign keys.

#### Steps for 1b

- A user wants to set up a foreign key constraint to single or multiple columns to a currently active table.
- The user opens the table options by clicking on the table name label in the toolbar area. From the menu, the user selects the option 'Table Constraints'
- This opens a dialog from which the user can set all supported constraint types.
- The user sees a layout with two panels. On one side, all the existing constraints are listed. On the other side, a form with the constraints configuration is displayed. The form corresponds to the currently active list item.
- The list panel contains actions at the bottom of the panel. From there, the user can choose to add or delete an item from the list. The user clicks on 'Add' to create a new constraint.
- The user is presented with a form. From there, they select the type of constraint to be added. The user selects the 'Foreign Key' constraint option from the list.
- The user selects single or multiple columns they wish to apply the constraint to.
- The user selects a table to be referenced by these columns.
- The user selects a column in the reference table from which the column will match values. By default, this is set to the 'Primary Key' column in the referenced table. When changing this field, the user can select only columns with a UNIQUE or PRIMARY KEY constraint.

## Scenario 2: User Edits an Existing Foreign Key Constraint

### Scenario 2a: From table constraint settings

#### Assumptions for 2a

- This scenario assumes that foreign keys will be updated, rather than dropped and replaced. This implementation detail is still pending discussion.

#### Steps for 2a

- A user wants to edit an existing foreign key constraint to change the selected columns or select another referenced table.
- The user can open a specific foreign key constraint form by clicking on the foreign key link in the column header.
- If the modified FK constraint causes existing column values to become invalid, the user will receive a warning and be aware of the potential implications of this change, like loss of data or broken views.

## Scenario 3: User Identifies a Column With a Foreign Key Constraint Applied

### Scenario 3a: The foreign key constraint is set to a single column

#### Steps for 3a

- The user opens a table that contains columns with a foreign key constraint applied.
- The user identifies the columns in two ways:
  - The user looks at the column header and sees the foreign key indicator. This indicator shows a key icon and the referenced table and column next to it.
    - The user can click the indicator to display the foreign key settings for the specific column.
    - The indicator can be hovered over to display a tooltip with information about the foreign key constraints.
  - The user looks at the column fields and sees that values are added with different styling, a tag-like element with a colored background.

### Scenario 3b: The foreign key constraint is set to multiple columns

#### Steps for 3b

- The user opens a table that contains columns with a multi-column foreign key constraint applied.
  - The indicator, in this case, looks similar to the single-column one. However, the user will understand that the foreign key constraints are referencing the same table.
    - The user can tell that a referenced table is the same because they share the same color. The system could use other UI elements instead of color. Still, the idea is to create a visual distinction that can be easily scanned.
  - The indicator can be hovered over to see additional information. From here, the user will understand that the constraint references more than one column.

## Scenario 4: User Sees a Preview of the Linked Record in a Column With a Foreign Key Constraint Applied

In most cases, the values displayed within a foreign key column won't serve to identify the associated record. A preview of the linked record in columns with a foreign key constraint can help the user identify it.

By default, the preview will include columns based on certain criteria, such as constraints applied or data type. However, users will be able to change these by updating the reference table preferences.

### Scenario 4a: The option for record preview is enabled

#### Steps for 4a

- The user opens a table that contains columns with a foreign key constraint applied.
  - The column contains the referenced values for each cell. Five fields are displayed.
    - The displayed fields from the reference table are prioritized applying the following criteria:
      - They have unique values, meaning that either a primary key, foreign key or unique constraint are applied to the column.
      - They have a text data type.
    - If the user wants to show specific fields, these can be selected in the referenced table options under the 'Table Preferences' option. 

- The displayed fields are presented as concatenated values. Visual contrast is created between the field name and its corresponding value so that it is easier to read.
- When clicked, the field displays the [record selector](#record-selector) component containing a pre-filtered list. A single matching item is displayed.

### Scenario 4b: The option for record preview is disabled

#### Steps for 4b

- The user opens a table that has columns with a foreign key constraint applied.
  - The column contains the primary key value for the referenced column only.
  - When clicked, the field displays the [record selector](#record-selector) component containing a pre-filtered list. A single matching item is displayed.

## Scenario 5: User Edits the Values of a Column With a Foreign Key Constraint Applied

Linked records can be changed or removed according to the user's preference. Since values are references to records in other tables, users must understand that changes to references don't affect the original records. However, changes to the values of records in the referenced table do.

### Scenario 5a: The field has an existing value

#### Steps for 5a

- The user opens a table that has columns with a foreign key constraint applied.
  - The column contains the referenced values for each cell.
  - When clicked, a pre-filtered list is displayed inside the [record selector](#record-selector) component. The dropdown includes a search input, that if modified, will show other matching records. Clicking on any of those records will close the dropdown and replace the existing one.
  - Note that in the case of multi-column foreign key constraints, the system could modify additional fields.

### Scenario 5b: The field is empty

#### Steps for 5b

- The user opens a table that has columns with a foreign key constraint applied.
  - The column contains no values.
  - When clicked, a list of records is displayed inside the [record selector](#record-selector) component. The list shows the first 50 records.
  - An text input field is available within the dropdown to filter the records based on partial or complete value matches. As the user types in a value, the list narrows down the records. The system can search only the first five fields. Search across all types is supported.
  - If there's a single match for the entered value, it should become highlighted, allowing the user to confirm the selection.
  - If the table contains no records, the user sees an option to add a record.
  - If there aren't any matches, the user sees an option to add a record for the new entered value or to try changing the 'Search Columns' table preference.

## Components

### Record Selector

The record selector component is used to retrieve records from other tables and add them as values to cells according to the referenced column.

### Table Selector

The table selector allows users to select tables from a schema. This spec doesn't go into details on how this selector would work. It also doesn't consider the scenario for selecting both tables and views.

### Record Preview

The record preview allows users to identify records linked in other tables. It shows the first five field names and values. A specific limit for the value length needs to be defined so that space usage is optimal.

## Other Considerations

### Search Columns

- Some primary key columns would be useful, some very not useful (e.g., the one we create). Text helps with this, but there may also be other considerations.
- Multi-column unique constraints are potentially useful, but only if all columns are included.
- Non-unique columns are never useful unless a unique column is included (that gives info for the user to choose between rows with duplicate entries in non-unique columns).

### Linked Records for Multi-Column Foreign Key Constraints

- The current UI does not take into account multi-column foreign key constraints and how those would be retrieved and selected.

### Usage of Color

- A suggestion to use color as a means to differentiate table references has been included in this spec. However, there are implementation details which need to be discussed before a decision can be made.

## Related Discussions

- [Editing values for columns with a foreign key constraint applied](https://github.com/centerofci/mathesar/discussions/796)
- [Handling duplicate foreign key columns from the 'Link Table' dialog](https://github.com/centerofci/mathesar/discussions/791)
- [Help users link tables via question-based forms](https://github.com/centerofci/mathesar/discussions/790)
- [Handling Composite Primary Keys and Junction Tables](https://github.com/centerofci/mathesar/discussions/804)
