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

## Prototype Link and Video Walkthrough

## Scenarios

### Scenario 1 : User Adds a Foreign Key Constraint

A user wants to link records from another table into their current table. Both tables belong to the same schema.

### Scenario 1a: Automatically from the 'Link Table' dialog

#### Steps for Scenario 1a

- The user starts the 'Link Table' process by clicking on the 'Link Table' button in the table toolbar area.
- The user reads the instructions in the 'Link Table' dialog and understands that the tables will be linked by setting up a foreign key constraint. They also understand that manual configuration is available.
- The user selects the table they wish to link to from the [table selector](#table-selector).
- A list of questions is displayed, the user can answer 'yes' or 'no' depending on the type of relationship they want to create.
- The user answers all the questions listed. The answers will determine the location of the foreign key or whether a new table needs to be created.
  - Answering 'yes' to both questions will set up a mapping table with foreign key columns for both tables, creating a many-to-many relationship.
  - Answering 'yes' to any of the questions and 'no' to the other will set up a foreign key column in the appropriate table, creating a one-to-many relationship. The column is added to the table on the 'many' side of the relationship.
- Once questions are answered,  a summary of the system's changes is displayed in a section titled 'Under the Hood.'
- Before creating the link, the user will have the chance to rename the new columns or tables. Invalid column or table names should display an inline warning and prevent saving.

### Scenario 1b: Manually from the 'Table Constraints' settings

#### Steps for Scenario 1b

- A user wants to set up a foreign key constraint to single or multiple columns to a currently active table.
- The user opens the table options by clicking on the table name label in the toolbar area. From the menu, the user selects the option 'Table Constraints'
- The user sees a layout with two panels. On one side, all the existing constraints are listed. On the other side, a form with the constraints configuration is displayed. The form corresponds to the currently active list item.
- The list panel contains actions at the bottom of the panel. From there, the user can choose to add or delete an item from the list. The user clicks on 'Add' to create a new constraint.
- The user is presented with a form. From there, they select the type of constraint to be added. The user selects the 'Foreign Key' constraint option from the list.
- The user selects single or multiple columns they wish to apply the constraint to.
- The user selects a table to be referenced by these columns.
- The user selects a column in the reference table from which the column will match values. By default, this is set to the 'Primary Key' column in the referenced table. When changing this field, the user understands that a column with unique values is preferred for setting up a foreign key column.

## Scenario 2: User Edits an Existing Foreign Key Constraint

### Scenario 2a: From the column header menu

#### Steps for Scenario 2a

- The user hovers over the foreign key reference link below the column name.
- Information about the constraints applied to the column are displayed in a tooltip.
- The user clicks on the foreign key reference link below the column name.
- Constraint settings open for the column.

### Scenario 2b: From table constraint settings

#### Steps for Scenario 2b

- A user wants to edit an existing foreign key constraint to change the selected columns or select another referenced table.
- The user can open a specific foreign key constraint form by clicking on the foreign key link in the column header.
- If the modified FK constraint causes existing column values to become invalid, the user will receive a warning and be aware of the potential implications of this change, like loss of data or broken views.

## User Identifies a Column With a Foreign Key Constraint Applied

### The foreign key constraint is set to a single column

- The user opens a table that contains columns with a foreign key constraint applied.
- The user identifies the columns in two ways:
  - The user looks at the column header and sees the foreign key indicator. This indicator shows a key icon and the referenced table and column next to it.
    - The indicator can be clicked to display the foreign key settings for the specific column.
    - The indicator can be hovered over to display a tooltip with information about the foreign key constraints.
  - The user looks at the column fields and sees that values are added with different styling, a tag-like element with a colored background.

### The foreign key constraint is set to multiple columns

- The user opens a table that contains columns with a multi-column foreign key constraint applied.
  - The indicator in this case looks similar to the single-column one, however the user will understand that the foreign key constraints are referencing the same table.
    - The user can tell that a referenced table is the same because they share the same color. Other UI elements could be used instead of color, however the idea is to create a visual distinction that can be easily scanned.
  - The indicator can be hovered over to see additional information, from here the user will understand that the constraint references more than one column.

## User Sees a Preview of the Linked Record in a Column With a Foreign Key Constraint Applied

## User Edits the Values of a Column With a Foreign Key Constraint Applied

### The field is empty

### The field contains a value

## Components

### Table Selector
