---
title: 02. Feature Requirements
description: 
published: true
date: 2023-05-11T14:36:25.059Z
tags: 
editor: markdown
dateCreated: 2022-01-24T23:01:08.734Z
---

To work with **Queries** and **Views** in Mathesar, we'll need to support the following functionality:

## Query Builder
Mathesar should support a visual query builder to allow users to construct **Queries**. The query builder should be accessible from anywhere in Mathesar and should not be tied to a single table or view.

The query builder should allow users to:
- Construct a query by selecting:
    - columns to use
    - filters to apply to columns used or their tables
    - formulas to use
    - aggregations to apply
    - summaries (group by) to apply
    - sorting to apply
    - a limit/offset for the rows returned
- Select columns to see in the output query
- Preview the query results live
- Save a query as a **View**

## Creating Views
Mathesar should also support creating **Views**, which are essentially saved **Queries**. View creation should start by using the query builder.

## Interacting with Views
Views should be a separate category of objects in Mathesar, just like Tables. Users should be able to:
- See all views in a given schema
- Find the view they want
- Open a view
- See data relevant to views, including the underlying query, column data provenance, etc.
- Apply filters, sorting, and grouping to views (similar to tables)
- Edit data in views where possible

## Query Builder Hooks
We should hook into the query builder from Tables and Views wherever the context makes sense to introduce the user to it. This involves updating the designs for tables and views to pre-create queries and link to the query builder.

Some examples:
- Creating a new view from scratch
- Editing the structure of a view
- Saving the currently applied filters, sorts, and groups of a table.
- Finding duplicate rows in a table if they can't apply a unique constraint to a column due to non-unique rows being present.
- Creating an editable view while creating a new mapping table through the "Link Table" feature.