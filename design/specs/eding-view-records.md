---
title: Editing Records Within a View
description: 
published: true
date: 2021-09-13T07:15:57.956Z
tags: 
editor: markdown
dateCreated: 2021-09-09T08:03:57.235Z
---

# Context
Users working within views may want to add new records to one or more source tables without dealing with multiple objects, following the spreadsheet-like experience that Mathesar aims to offer. This design problem presents some challenges in avoiding conflicts between objects, especially if there are dependencies. A proposed solution for this is described in this spec, taking into account two potential scenarios for views that can and cannot be updated.

# Prototype
[Prototype for Editing Records within a View](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?page-id=4928%3A47261&node-id=5072%3A57556&viewport=324%2C48%2C0.93&scaling=contain&starting-point-node-id=5072%3A57556&show-proto-sidebar=1)

# User Experience

## Scenario 1: If the view allows editing (updatable view)
### User adds a record
Users will be able to add records directly from views. However, they might need to add multiple records across more than one table, depending on how the view is structured. For that reason, some of the constraints applied to the referenced tables might influence the interactions. 

For convenience, users can add values to the fields of a new record directly in the table. However, a record form will also be available, allowing users to edit the complete record, as it exists in the referenced table.

#### The record table allows empty values for all fields
If the table allows for empty values, the user can leave it blank or enter a value. Doing so will not prevent the new record from being saved.

#### The record table does not allow an empty value for some of the fields
If the table has fields that aren't in the view but can't be empty, the user will have to fill those out. Otherwise, the system cannot save the new record. For such cases, the record form will show and indicate to the user which fields cannot be empty.

### User removes a record
A user will be able to remove a record from a view. This action might affect the underlying tables and their relations, for example, if the deleted record is referenced via a foreign key in other tables.
Warnings are needed for such cases to inform the user about the potential conflicts that removing records might cause.

#### The record was linked as a foreign key
If the deleted record was linked to other tables or views, the user could still delete it, but the system must display a warning with a list of those affected objects.

#### The record was not linked as a foreign key
If the deleted record was not linked to other tables or views, the user should delete it without warnings.

### User edits a record
Users will be able to edit records by changing the values directly from the table. The input control will depend on the data type of the referenced column. 

#### User edits the selected field from the record
A user can edit a single field from the table by selecting it and changing its contents. This action will change the record, but all other fields will be left the same.

#### User edits the entire record
A user can edit all fields from a record by opening the record form, which can be accessed by clicking on the 'Edit Record' button from the view's toolbar.
[Prototype for Edit Record Form](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?page-id=4928%3A47261&node-id=5118%3A61344&viewport=324%2C48%2C0.93&scaling=contain&starting-point-node-id=5118%3A61344&show-proto-sidebar=1)

## Scenario 2: If the view doesn't allow edit (non-updatable view)
### User adds, removes, or edits records that are part of a view
If the view doesn't allow editing, the user will navigate to the source table and make changes there. The user can select a record's field and click on the edit button from the view toolbar, and this action will trigger a dialog where the user can choose to navigate and open the source table.

[Prototype for Non-Updatable View](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?page-id=4928%3A47261&node-id=5118%3A63068&viewport=324%2C48%2C0.93&scaling=contain&starting-point-node-id=5118%3A63068&show-proto-sidebar=1)

# Other Interactions
## User reorders columns in a view
A user might want to change the order in which columns are laid out in a view and can do so by dragging and dropping the columns into place. Note that this will require saving the view. Otherwise, the system will revert the order. The system should display a warning for a user that tries to close a view with unsaved changes.

When being dragged, the column will indicate its new placement visually, as represented in the following example:
[Visual indicator of new column placement](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?page-id=5182%3A54399&node-id=5182%3A54896&viewport=273%2C48%2C0.68&scaling=min-zoom)


# Global Updates
Some items from previous reviews for the 'Working with Views' milestone have been included in this prototype and can be accessed in the steps defined for view creation.
[Prototype for Creating a View](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?page-id=4928%3A47261&node-id=5118%3A66661&viewport=324%2C48%2C0.93&scaling=contain&starting-point-node-id=5118%3A66661&show-proto-sidebar=1)

- Add a column to view the menu
- Column options for a linked column
- Set Up Lookup Column
- Relationships in View List (previously referenced tables)