---
title: Basic Table Operations Spec
description: 
published: true
date: 2021-08-18T13:45:22.782Z
tags: 
editor: markdown
dateCreated: 2021-07-13T12:08:32.516Z
---

# Context

Tables are database objects that contain all the data in a database. To manage, update and structure their database, users need to perform basic table operations such as adding new tables, editing their properties, and deleting them if needed. This spec describes the various steps and interfaces a user would have to interact with to perform these tasks.

# Prototype
[Table Operations Figma Prototype](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?page-id=2365%3A14712&node-id=2563%3A15775&viewport=-582%2C536%2C0.7798178791999817&scaling=contain)

# User Experience

## User adds a new table
A user can add a new table by clicking on the 'Add Table' button located in the schema navigation sidebar. Clicking on the 'Add Table' button will automatically insert a new table to the top of the list. The newly inserted table will have a placeholder name such as 'Unnamed Table' or 'Table 1' to allow users to refer to the table later if no user-defined name is provided during the table creation process.

## User edits a new table name
Users can update a table name during the table creation process, even before the table is saved, by replacing the table's placeholder name in the text input control located at the top of the tab content panel.

## User edits an existing table name
If the table has been saved, the user can always access the table name input by clicking on the table name heading on the top of the tab content panel.

## User adds an empty table
During the table creation process, a user might choose to add an empty table. Once they select this option, there are no other steps required, and the user can start modifying the table's content from scratch. Only a protected mathesar ID field is created, which gets populated once the user saves new data. To enter user-defined data, a user must create a new column field. 

## User adds a table from imported data via clipboard content
A user might choose to create a new table from imported data. In which case, they have multiple options, such as uploading a file, pasting content from the clipboard, or downloading the file from a URL. In the case of clipboard content, the user can paste the contents of a CSV file or copy and paste from spreadsheet apps, such as Google Sheets or Excel. Mathesar will recognize the format and generate a table accordingly.

## User adds a new table from imported data via URL
A user might also have a link that points to a valid file that they want to import. In this case, the user can point to the file by entering a web address.

## User deletes a table
The option to delete a table is available in the context menu located in the table's toolbar at the top of the tab panel. If the table is not empty, the user will have to confirm the deletion. 

# Interactions

## Sequential Table Names
A user might add multiple tables without user-defined names, in which case the system can assign a numerical appendix to the placeholder name. 

## Input Errors
Inputs that contain validation errors should provide users with a clear reason for what is causing the error and how to fix it. These messages should become visible when the user interacts with the field, either hovering or focusing on it.

## Bulk Table Operations
Performing operations on a single table at a time can quickly become an issue if the user has many tables. Bulk operations will be considered in a future iteration.

# Review Notes

## Placeholder Names
Naming tables should be optional at the moment of creation. The user should get a naming suggestion every time they create a new table. Mathesar should have the ability to auto-generate such names with incremental numbers. The decision to do so in the front-end or back-end will be decided later.

## Table Options Menu
A menu that contains table-related options can be accessed from the top toolbar. This menu should have additional functionality in the future, such as 'Duplicate Table,' which is only included now for reference.

## Showing Related Tables and Views in the Delete Dialog
When a user decides to delete a table, they will have to review a list of all related tables and views before confirming their choice.