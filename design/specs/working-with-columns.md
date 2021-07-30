---
title: Working with Columns
description: 
published: true
date: 2021-07-30T18:30:12.471Z
tags: 
editor: markdown
dateCreated: 2021-07-19T17:34:31.394Z
---

> This spec is in the review process, and its contents are subject to change. 
{.is-warning}

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

## User changes column settings to disallow empty values
Users can alter the column settings to allow or disallow empty (null or empty string) values. If changed, and if the column contains empty values, a warning message will appear, and the system will not save the change. The user can then choose to show a filtered view of the table showing the values that the user must change to alter the column constraint.

## User changes column settings to disallow duplicate values
Users can also change column settings to prevent duplicate entries. If set from the column options, the unique constraint will only affect the values on that specific column.

## User changes table unique constraint settings
Users can set table-level constraints by accessing the table properties menu found on the table toolbar area. Changing these settings will impact the entire table. 

## User sets the default value for a column
A user might want to set a default value so that every new record contains the appropriate value. In this case, the user can choose from no value, a zero value for numerical types, or a default value. The options will vary depending on the set data type.


# Review Notes
## Labeling of  Menus
Menus that list options for different objects, such as tables, columns, and records, should be easily discovered by users. We have simplified the column-related options to a single menu that users can access in context from the column header. As for table-related actions, we have updated the label to 'Table Actions' for increased clarity. Once all controls and options for the MVP are in place, we will revisit all labels to ensure we are applying the same consistent patterns across the entire app.

## NULL, Empty, Blank Fields
To simplify the way we handle the filtering of columns based on the content of a field, we have nested the NULL condition under the 'Empty' definition, which also includes empty strings. 

## Providing options to solve problems when presenting warnings (Help me fix this problem)
Whenever possible, we want to guide users towards resolving problems that hinder their goals within Mathesar. We are introducing a pattern for specific warnings to present suggested actions based on the context. In this case, for example, we allow users to navigate to pre-filtered views in order solve issues that prevent them from changing column settings.

## Column vs. Table Constraints
There were some concerns over having both table-level and column-level constraints. We are introducing a help/more info icon next to some options so that users can learn more about them. Once we have the design for the complete set of functionality for the MVP, we can look at the different ways we can educate users within Mathesar.
