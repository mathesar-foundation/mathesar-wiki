---
title: Viewing a View
description: 
published: true
date: 2023-05-11T14:33:51.508Z
tags: 
editor: markdown
dateCreated: 2021-09-03T09:04:39.016Z
---

> This spec is outdated and should not be followed.
{.is-danger}

# Context
Views can help users make sense of the data they have in tables and the references between them. However, when coming from the context of spreadsheet-like interfaces, a user might experience some difficulties incorporating views into their process.
An optimal design solution would make table associations in the context of views easy to understand and modify if needed. 

# Prototype
[Prototype for Viewing Views](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?page-id=4816%3A56910&node-id=4816%3A57282&viewport=324%2C48%2C0.2&scaling=scale-down-width&starting-point-node-id=4816%3A57282)

# User Experience
## Scenarios
### A user understands that columns in a view are referenced
Because views look exactly like tables, users who are new to views might have difficulty understanding why they can't edit something or why some fields might be missing from the referenced table or present from other tables.

> Note that at this point, users can only select other columns and add them to the view without performing aggregations or data transformations. The design, as it is currently described, does not contemplate those scenarios.  
{.is-warning}


#### Using Color
The icons at the column header label could show the different referenced fields present in a given view by identifying them by colors. These interface elements could help users understand how many tables are referenced and which fields belong to the same table.

#### Displaying reference in a view column's menu
The menu for columns in views has slight differences compared to that of tables. For example, it doesn't allow changing database settings such as data types. Users can, however, view the referenced column details, navigate to the parent table or change the referenced field. 

#### Viewing a list of all referenced entities
A user might want to see a complete list of all referenced entities rather than opening details for every column in a view. In that case, they can click on the 'Referenced Entities' option located in the 'View Options' menu.

### A user filters, sorts, or groups data in a view
Users can apply filters, sorts, or groups as they'd do in tables when working from a view. The only difference is that users can save the resulting query into the current view or a new one. A table cannot have saved filters. The only way to keep them is to create a view from a filtered table.

### A user views the query that created a view
Users can access the system's query to generate a view from the 'View Options' menu in the view toolbar area.