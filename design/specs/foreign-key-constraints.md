---
title: Usage of Foreign Key Constraints
description: 
published: true
date: 2021-11-09T09:01:04.462Z
tags: 
editor: markdown
dateCreated: 2021-10-19T09:20:55.088Z
---

# Context

# Scenarios
## User Adds a Foreign Key Constraint
### Automatically from the 'Link Table' dialog

#### Steps

- The user wants to link values from a table to another table belonging to the same schema.
- The user starts the 'Link Table' process by clicking on the 'Link Table' button in the table toolbar area.
- The user reads the instructions in the 'Link Table' dialog and understands that the tables will be linked by setting up a foreign key constraint. They also understand that manual configuration is available. 
- The user selects the table they wish to link to.
- The user answers 'yes' or 'no' to the questions presented. The answers will determine the location of the foreign key or whether a new table needs to be created
	- Answering 'yes' to both questions will set up a mapping table with foreign key columns for both tables creating a many-to-many relationship
  - Answering 'yes' to any of the questions and 'no' to the other will set up a foreign key column in the appropiate table creating a one-to-many relationship. The column is added to the table on the 'many' side of the relationship.
- Once the questions are answered, the user will read a summary of the changes that will be made by the system, in a section titled 'Under the Hood'.
- Before creating the link, the user will have the chance to rename the new columns or tables.

### Manually from the 'Table Constraints' settings

## User Edits a Foreign Key Constraint
### Manually from the 'Table Constraints' settings

## User Identifies a Column With a Foreign Key Constraint Applied
### The foreign key constraint is set to a single column
### The foreign key constraint is set to multiple columns

## User Sees a Preview of the Linked Table in a Column With a Foreign Key Constraint Applied

## User Edits the Values of a Column With a Foreign Key Constraint Applied
### The field is empty
### The field contains a value
### The new field value is invalid


> This spec is outdated and should not be followed.
{.is-danger}

# Context
This design spec describes the proposed solution for the problem defined in the issue [Design for using Foreign Key constraints](https://github.com/centerofci/mathesar/issues/243). 
In summary, this issue addresses how users set up relationships between data in two different tables.

## Prototype Walkthrough
[Video: Setting Up a Relationship](https://www.loom.com/share/146b0aa3adbb41009ce1a49caeb936ab)
[Video: Lookup Fields](https://www.loom.com/share/757f7ace02a84296912c6df45410e5e7)
[Prototype Link](https://mathesar-prototype.netlify.app/)

## Concepts
### Table relationship
Two tables can be linked together using a "foreign key constraint" to identify this relationship. Relating tables prevents issues like data conflicts and duplication and supports data consistency and integrity.
For users, this knowledge of "linked tables" is critical for the system's overall usability.

### Primary Key
Primary keys are unique identifiers used to identify records in a table. In Mathesar, primary keys are set by default to the id column, and their values are generated automatically. 

### Foreign Key
The foreign key is a relationship between two tables that identifies which column in the other table references the first one.

### Lookup Column
They are used to show information from linked records in another table. The lookup column setting determines which column values are visible when displaying the record.

## Scenarios
### A user wants to create a one-to-many table relationship between two existing tables
A user has a table named 'artist' that contains records for artists in a music album collection. The user wants to link each artist to records in another table named 'track.' If successful, the user should link all tracks associated with an artist to records in the 'artist' table.


### Steps

#### 1. The user opens the 'track' table and adds a new column to link records from the 'artist' table
- From the sidebar navigation list of tables, click on a table named 'track.'
- Click on 'Add new Column,' and a new column is added with text type by default
#### The user opens the new column menu and selects the 'Link to Another Table' option
- Click on the column header to show the menu and select the 'Link to Another Table' option

**Note: This step does not cover the scenario where a user has a unique table, in which case they need to create an additional table to add a relationship.**

#### 2. The user selects a table from the list of available tables
- The user selects the table on the 'one side of the 'one-to-many' relationship.

#### 3. The user selects a column belonging to the selected table to create the link
- The primary key column is pre-selected by default
#### The user sets the new column as a foreign key for a column in the 'artist' table
- If the column had values, this action would clear those unless they exactly matched contents from the linked column
#### The user retrieves records from the linked table and adds them to the new column
- Autocomplete should allow users to complete this action without additional clicks
- When no results are available, we should show an option to add a new record
#### 4. The user removes the foreign key constraint from the column
- The system will assign the column the type of the column that was linked (if the linked column was a duration type, then it should be assigned as such)

---

### A user wants to update the lookup field for a table
A user has a table named 'track' with a lookup field set to 'ISRC' (an alphanumeric code used to identify songs in the music industry). However, the field 'track name' is easier to retrieve and recall, and the user wants to display it when linking records from this table. 

### Steps
#### 1. The user opens the table options menu
- The table options menu can be accessed from the table toolbar by clicking on the table name.
#### 2. The user selects the 'Set Lookup Column' option
This action will open a dialog with a column selector from which the user can select a column and assign it as a 'lookup column.'
#### 3. The user sets another column as a 'Lookup Column.'
This action automatically changes the displayed value in all linked records from this table. The user understands that the display value is not the same as the foreign key value used to create the relationship.