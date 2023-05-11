---
title: 05. View Structure
description: 
published: true
date: 2023-05-11T14:36:16.949Z
tags: 
editor: markdown
dateCreated: 2022-01-24T22:54:40.594Z
---

Once a query is built using the [Query Builder](/en/product/specs/2022-01-views/03-the-query-builder), it can be saved as a View. Users should be able to see and use Views in Mathesar just like [Tables](/en/product/concepts/tables).

This page describes how Views should work.

# Navigating to Views
Users should be able to:
- See all views in a given schema
- Find the view they want
- Open a view

# Interacting with a Single View
Once the user has opened a view, it should support the following features.

## View Data
- The user should be able to see the View's columns and rows.
- Users should be able to apply filters, sorts, and groups to the view data, similar to tables.

## Editing View Data
- The user should be able to edit data in rows if the column is editable.
    - Columns that use [Formulas](/en/product/specs/2022-01-views/04-formulas) have different editing behavior depending on the formula.
    - Columns that are direct representations of data from an underlying table should be editable.
- The user should be able to open up a form to edit the record of any cell with a single record as a source.

## Column Information
The user should be able to see all column information for each view column. Please see [06. View Columns](/en/product/specs/2022-01-views/06-view-columns) for details.

## Query
Users should be able to see the underlying SQL query that powers the view. This is read-only, but can be copied and pasted.

We could also potentially show a read-only breakdown of the query into [Query Builder](/en/product/specs/2022-01-views/03-the-query-builder) features, but I'm not sure if this is feasible or would be a good idea.

## View Structural Updates
Users should be able to perform the following actions:
- Save filters and sorts applied in the UI to the View query (permanently applying those sorts/filters)
- Save filters and sorts applied in the UI to a new View
- Create a new "summarized" view of any groupings applied
- Open the current view in the query builder to edit its structure