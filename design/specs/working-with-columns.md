---
title: Working with Columns
description: 
published: true
date: 2021-07-19T17:34:31.394Z
tags: 
editor: markdown
dateCreated: 2021-07-19T17:34:31.394Z
---

# Context
Working with columns is a central part of a users' database structuring experience, especially in scenarios where tables aren't imported, instead created within Mathesar. It is then on the user to add them, set the data types and other properties according to their needs.
This spec describes the steps and components users would have to interact with to structure a table from scratch and populate it with data.

# Prototype
[Working with Columns Figma Prototype](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?page-id=2750%3A17660&node-id=2816%3A18654&viewport=2205%2C368%2C0.5616371035575867&scaling=contain&starting-point-node-id=2816%3A18654)

# User Experience
The user experience for adding columns looks to favor default settings so that a user can structure a table without worrying too much about explicitly defining columns properties at every step. 

## User adds a new column
Users can add new columns by using the add column button next to the last column or by toggling the menu on any column header to insert a new column at the location.

## User deletes a column
Users can delete a column by toggling the column header menu and choosing the option to 'Delete Column.' In case the column deletion affects other tables or views, the user should receive a warning.

## User renames a column
Users can change a column name at any time without affecting other tables and views referencing it. To rename a column, the user can click on its name label or choose the 'Rename Column' option from the column's header menu.

## User edits a column type
Users can choose the column data type by choosing from the data types dropdown menu.

### Implementation Notes
Ideally, users should only change the column data type if it matches their data. Still, when there are inconsistencies, the user will have to resolve them or cancel the data type re-assignment. We will deal with these types of errors when working with specific data types.


## User changes column settings to disallow null values
Users can change the column settings to allow or disallow null values. If changed, and if the column contains null values, a warning will be indicated by the affected cells. The errors will prevent saving the column settings change until resolved.

## User changes column settings to disallow duplicate values
Users can also change column settings to prevent duplicate entries. If set from the column options, the unique constraint will only affect the values on that specific field.

## User changes table unique constraint settings
Users can set table-level constraints by accessing the table properties menu found on the table toolbar area. Changing these settings will impact the entire table. 

## User sets the default value for a column
A user might want to set a default value so that every new record contains the appropiate value. In this case, the user can choose from no value, a zero value for numerical types or a default value. The options will vary depending on the set data type.

## User replaces NULL values across the entire table
Users can use the replace values functionality in order to resolve errors with non nullable columns. 

## User removes duplicate values across the entire table
Users can use the remove duplicates functionality in order to resolve problems caused by duplicate values. The can choose to select one or more columns and the affected records will be removed.