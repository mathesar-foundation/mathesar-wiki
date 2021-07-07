---
title: Working with Schemas
description: 
published: true
date: 2021-07-07T15:04:13.254Z
tags: 
editor: markdown
dateCreated: 2021-07-07T10:57:41.105Z
---

# Context
Users within Mathesar will have multiple data tables that they want to organize and manage. Schemas can be a helpful mechanism to segregate their data for different purposes. Users with more experience with databases will want to incorporate these for reasons that might go beyond just organizing their database objects. However, this organizational aspect will be a primary feature of the design solution.

# Prototype
[Working with Schemas Figma Prototype](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?page-id=2144%3A12391&node-id=2146%3A12394&viewport=2334%2C1300%2C2.543393611907959&scaling=contain)

# User Experience

## User creates their first schema
A Mathesar user that has no schemas created will have to specify one to start creating tables. A default schema is created when users choose to start with a Mathesar managed database.

## User chooses how they want to start adding tables to their schema
Once the schema is created, the User will have to create tables. If the schema is empty, they will have the option to choose from the list of table creation methods. In the future, this could accommodate multiple tables import, but for now, we'll assume it's a single table being created.

## User edits the schema details
For various reasons, a user might, at some point, edit the given name of a schema. They might also want to delete the schema altogether but must do so in a context where they can be informed about the consequences.

## User navigates back to list of all schemas
When working on a particular schema, a user might navigate back to a list of all schemas.


# Interactions
## Editing inline vs. edit modal
There are cases where, for example, we might want to edit details, such as a table name inline (by clicking on the name label) rather than using a separate modal to provide a form with details.
In schemas, we might add additional settings that we want to make accessible to users, such as managing access privileges and permissions, etc. This could also be solved by having a schema details dedicated view that is not contained within a modal. 
Additionally, a schema might not allow editing of its name, in which case, inline editing might make it harder to inform the user about these limitations. 

## Preventing Deletion of Schema
Deleting a schema could lead to problems when any of its tables had relations with tables from another schema. Users need to be aware of this when they proceed to delete the schema. However, preventing them from doing so might be harder to verify, and the User could find it difficult to break all schema references before proceeding. If we do allow deletion, we'll need to either turn the schema references in other tables to a different type or represent the error once the User opens an affected table.

# User Interface
## Top navigation bar
Included on this spec is an initial draft of what our top navigation bar might look like. There are still details to be resolved in how we might incorporate searching or jumping across different databases and schemas (similar to what Github does). 



