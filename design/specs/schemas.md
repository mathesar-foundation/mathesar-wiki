---
title: Working with Schemas
description: 
published: true
date: 2021-07-14T10:01:02.349Z
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
A Mathesar user that has no schemas created will have to specify one to start creating tables. A default schema is created when users choose to begin with a Mathesar managed database.

## User chooses how they want to start adding tables to their schema
Once the schema is created, the user will have to create tables. If the schema is empty, they will have the option to choose from the list of table creation methods. In the future, this could accommodate multiple tables import, but for now, we'll assume it's a single table being created.

## User edits the schema details
For various reasons, a user might, at some point, edit the given name of a schema. They might also want to delete the schema altogether but must do so in a context where the system can inform them about the consequences.

## User navigates back to list of all schemas
When working on a particular schema, a user might navigate back to a list of all schemas.

## User jumps to another schema from the top navigation
A user can click on the top search bar to reveal a list of their recently opened schemas and databases. Typing the name of any existing schema or database should display a list of all matching items. 

## User tries to delete a non-empty schema
Before a user can delete a schema containing other objects such as tables or views, they must be aware of this information and the content that the system will delete along with the schema. 

## User deletes an empty schema
An empty schema can be deleted by a user with the appropriate permissions and no additional steps. 

# Interactions
## Editing inline vs. edit modal
There are cases where, for example, we might want to edit details, such as a table name inline (by clicking on the name label) rather than using a separate modal to provide a form with more information.
In schemas, we might add additional settings that we want to make accessible to users, such as managing access privileges and permissions, etc. The requirement could also be solved by having a schema details dedicated view that is not contained within a modal. 
Additionally, a schema might not allow editing of its name, in which case, inline editing might make it harder to inform the user about these limitations. 

## Preventing Deletion of Schema
Deleting a schema could lead to problems when any of its tables had relations with tables from another schema. Users need to be aware of this when they proceed to delete the schema. However, preventing them from doing so might be harder to verify, and the user could find it difficult to break all schema references before proceeding. If we allow deletion, we'll need to either turn the schema references in other tables to a different type or represent the error once the user opens an affected table.

# User Interface
## Top navigation bar
Included in this spec is an initial draft of what our top navigation bar might look like when implemented. There are still details to resolve, like how we might incorporate searching or jump across different databases and schemas (similar to what Github does). 

## Search bar navigation
The top search bar allows users to search through high-level objects such as schemas and databases that Mathesar manages.

# Review Notes

## Search and Jump To Navigation
With the introduction of the top navigation, we identified the opportunity to have a global control for navigation across databases and schemas that do not rely on the sidebar being visible at all times. This change would simplify other aspects of the user experience, allowing users to navigate away from a schema while keeping track of global notifications and other async operations.

When activated, the search and jump to navigation should display a list of recently navigated objects (schemas and databases).

## Public Schemas
Public schemas within Mathesar will be considered to be a special type. The system will add Contraints to prevent deletion or edits that might disrupt the database functionality.

The public schemas will also have a distinct visual icon to identify them.

## List of Databases
Changes introduced on this spec have invalidated the previously proposed solutions for database navigation. We will revisit the issues on this functionality in a later milestone.