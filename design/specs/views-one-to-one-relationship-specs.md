---
title: One-to-one Relationship Specs
description: 
published: true
date: 2021-09-02T07:32:21.700Z
tags: 
editor: markdown
dateCreated: 2021-08-24T09:02:15.127Z
---

# Context
Users within Mathesar will want to create relationships between tables for different purposes. For example, they might have an 'artist_id' column in an artist's table, and they want to relate that with the artist's releases on another table. For that, each 'releases' table record is linked to an artist on the 'artist' table with the same 'artist_id.'

## Primary and Foreign Keys
Primary and foreign keys are the basis of a relational database. They allow tables to be referenced from other tables. Allowing not only to connect the data from the tables in meaningful ways but also to maintain data integrity.
In the context of Mathesar, we attempt to help users incorporate these concepts in their database design while simplifying the experience so that users can create table relations without fully understanding how primary and foreign keys work.
Ideally, users will want to relate a table to another, and throughout the process, discover the role that key constraints have in performing these actions. This will happen at first by understanding the purpose for the automatically generated primary key that Mathesar adds to every record and later when referencing this key from another table.
Because Mathesar seeks to maintain access and visibility of all the tables in the database, there might be some friction in how users familiarize themselves with the concept of related tables at first. They will have to use views to reference other table's data to be more compatible with the spreadsheet standard.

# Prototype
[One-to-one Relationship Prototype](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?page-id=4218%3A36833&node-id=4218%3A37265&viewport=324%2C48%2C0.44&scaling=contain&starting-point-node-id=4218%3A37265)

# User Experience
## Scenarios
### A user changes a column's settings to link to another table
A user can set a column to reference another table's data by selecting the option 'Link to Another Table' from the column's header menu. This action should open a modal where the user can choose a referenced table and set additional options.

### A user selects a referenced table for the new linked column
A user can reference any table where a primary key is set as long as they are in the same schema. The table selector displays not only the table name but also the primary key column for reference.

### A user enters data into a linked column. 
Once the linked column has been successfully set up, the user can begin to enter data. The values of the related fields must match exactly any of the values specified in the referenced table's lookup field.

### A user deletes a linked record in the reference table.
Records from a referenced table that have been linked in other tables can be deleted as long as the user unchecks the 'Allow Orphan Records' option while setting up the table relation. While there are reasons why a user might choose to do this, the default should remain to restrict the record's deletion. A warning would display, indicating that the user must first remove the record's key reference from the other table.

### A user transforms a linked column into a regular one.
If users decide that they no longer want to reference a table from a column, they can unlink it. This action will not affect the content of the column's fields; however, the system will remove the foreign key constraints and set the data type to that of the referenced table's primary key type. Users can unlink a column by clicking on the 'Unlink Column' option in the column's header menu.

### A user sees a list of table constraints
Table constraints need to reflect all applied constraints accurately. For that reason, every time a column is linked to another table, the system will add the foreign key constraint to the list. These constraints will be read-only.

### A user changes the default lookup field for a table
For every table created within Mathesar, a lookup field is assigned by default. The default value will be assigned based on the column's position, with the first column after the ID column set as default. A user, for any reason, might want to change this, in which case they can select another lookup field by accessing the 'Set Lookup Field' menu item from the 'Table Actions' menu.