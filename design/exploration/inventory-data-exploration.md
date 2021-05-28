---
title: Inventory: Data Exploration
description: 
published: true
date: 2021-05-04T18:48:21.549Z
tags: 
editor: markdown
dateCreated: 2021-05-04T18:37:21.882Z
---

> Refer to [Inventory Use Case](/design/exploration/use-cases/inventory-use-case) for additional context.
{.is-info}

# Context
The user has created a new table in Mathesar via file import. The table is used to organize their music album collection.

![upload_24f01dd5f890ed625316f0f42e2e6c95.gif](/assets/design/exploration/inventory-data-exploration/upload_24f01dd5f890ed625316f0f42e2e6c95.gif)

The user's goal is to create a top-level **releases** table and break **artists** into another table.

# Goals
- Create separate tables for related information
- Move data that will repeat often into a reference table
- Connect reference tables with foreign keys

## User creates a new table inside an existing schema
Once the user has created their initial table, they need to add an additional one to include the data they want to link. The user can enter the data manually or they can create a new table by import, the difference is that this time they add it to an existing schema.

![upload_314ee62b7fb18439e4860713da71af57.gif](/assets/design/exploration/inventory-data-exploration/upload_314ee62b7fb18439e4860713da71af57.gif)

![upload_0a739701669a8d3913b365ef516a7055.gif](/assets/design/exploration/inventory-data-exploration/upload_0a739701669a8d3913b365ef516a7055.gif)

### Notes
- ID field is visible 
- If ID is detected during import the user can accept it
- Assumption is that ID = primary key
- Import from file can detect attributes and propose an append rather than replacing

### Questions
- When creating a new table, do we show a sample field? Or no fields at all?
- Can an existing table be replaced by file import?

## User opens a table
From a sidebar panel, the user can see a list of all tables inside a schema. To open a table, all they have to do is click on the corresponding item link. The table will open as a tab in the content area and be closed from the tab.

There are two alternatives to solve this step, and each has its pros and cons.

### Open tables as tabs that can be closed

![9i3tkus.gif](/assets/design/exploration/inventory-data-exploration/9i3tkus.gif)

#### Pros
- Can open tables from different schemas
- Can access multiple schemas from sidebar

#### Cons
- Sidebar takes horizontal space


### List all tables as tabs that can be selected

![ibeojth.gif](/assets/design/exploration/inventory-data-exploration/ibeojth.gif)

#### Pros
- Save up space by removing sidebar

#### Cons
- Can't fit too many tables in the same view

## User creates a relationship between two tables

![upload_c3499aaef0865fe3837e3308a6adadef.gif](/assets/design/exploration/inventory-data-exploration/upload_c3499aaef0865fe3837e3308a6adadef.gif)

# Questions & Notes

### Questions
- How does the user know changes have been saved?
    - Interface needs to show auto-save status
    - Consider activity log
- Can users undo changes?
    - Yes
- Can users undo table deletion?
    - Yes. Users should be able to retrieve a table from an archive.

### Notes
- Add views to sidebar
- User breaks column into a new table (look at dabble DB example)
- New view is created to show combined data, user redirected to that new table
- If user wants to add a computed field a view is added
