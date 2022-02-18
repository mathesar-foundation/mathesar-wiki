---
title: 03. The Query Builder
description: 
published: true
date: 2022-02-18T20:01:45.855Z
tags: 
editor: markdown
dateCreated: 2022-02-05T23:04:47.283Z
---

> Under construction.
{.is-warning}


This page describes how the query builder should work.

# Product Requirements

## Navigating to the Query Builder
- The query builder should be accessible from anywhere in a schema. It should not be tied to a specific table or view.
- The query builder should be able to be pre-populated with a query and linked to.
	- For example, if a user tries to set a unique constraint for a column that has non-unique values, we may want to open up the query builder with a pre-populated query that shows all duplicate rows.

## Reference Table
All queries will start from a single "reference table". This table will determine which columns are available to be added to the output of the View. The user should be able to set the reference table at the start of building their query. They might either explicitly set it or we could infer it from the first column they select.

We might also want to show the reference table in the query builder UI somehow.

## Selecting Output Columns
Users should be able to add columns to see in the query's output.

- Users can add columns in two ways: from a table or from a formula.

### From a Table
- The user will see a list of [available columns](#available-columns).
- Once the user has added a column, we make a best guess for the following attributes:
    - **Source Relationship**: This is the relationship of the column's table to the reference table. 
        - If there's only one way that the tables are related, there is no need to make a guess.
        - If there are multiple relationships between the table, we will pick one.
    - **Aggregation**: This sets how the column is aggregated (list, count, average, min, max, etc.). 
        - This is only applicable to tables which have multiple related records to the reference table. 
        - By default, we will aggregate columns as a list.
- The user will see the source relationship and aggregations used and can alter them if desired. 
- The user can also alter the column in the following ways:
  - Adding a **Formula**: This alters the column to use a formula where one of the variables is the column.
  - Adding a **Filter**: This filters the column's results to a subset.
- Once added, the user can also edit formulas and filters.
- The user can delete the column if they choose.

### From a Formula
- The user will see a list of available formulas organized by type of formula.
- The user can select a formula. They will then be prompted for the variables to use in that formula.
    - The number of variables and the types of data they accept depend on the formula chosen.
- Once they select the variables for the formula, the column is then added.
- The user can edit the formula if they choose.
- The user can also apply a filter to the column and edit a filter once applied.
- The user can delete the column if they choose.

## Query Refinement
In addition to adding columns, the user should be able to perform the following actions:
- Add filters to the query (based on the columns added)
- Add sorting to the query (based on the columns added)
- Aggregate the query (based on the columns added)
- Limit the number of rows returned
- Apply an offset to the rows returned

## Preview and Actions
- We should show users a live preview of their data as they build their query.
- We should allow users to see a temporary view of their query (this won't be saved as a View but they won't see the "query building" part of the screen)
- We should allow users to save their query as a permanent View.

# Implementation Details

## Available Columns
> Information about calculating available columns will go here.
{.is-info}

## Formulas
> Information about calculating available columns will go here.
{.is-info}
