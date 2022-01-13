---
title: Product Specs
description: Views: UI Requirements for Views
published: true
date: 2022-01-13T19:49:54Z
tags: 
editor: markdown
dateCreated: 2022-01-13T19:49:54Z
---

Based on the models defined for [views](/product/specs/2022-01-views/02-modeling-views.md) and their [columns](/product/specs/2022-01-views/03-modeling-view-columns.md), the first version of Views should support the following features.

I've marked the features we should support as "for alpha release", but I've also listed a few potential future features so that we can think about them while designing code architecture and UI/UX.

## Query
- **For alpha release**: Users should be able to see the query associated with a View after it has been loaded.
- **Potential future features**:
	- Users can edit the query associated with a View.
	- Users can create a new View using a query.

## Columns
- **For alpha release**: Users should be able to see all columns associated with a view. Each column should show:
	- Data Type (non-editable)
	- Data Sources (editable if there's no Formula)
	- Data Formula (editable in simple cases)
- **Potential future features**:
	- Show virtual columns involved in view creation (via CTEs, subqueries, etc.)
	- Allow editing data formula using SQL

## Rows
- **For alpha release**: 
	- Users should be able to see the rows associated with a view.
	- If a cell is a direct representation of a record, users should be able to edit that record via that cell.
	- If a column is a direct representation of a record, users should be able to add a new record via that cell.
- **Potential future features**:
	- Users can edit the query associated with a View.
	- Users can create a new View using a query.

## Filters
- **For alpha release**:
	- Users should be able to see what filters are applied to their View.
	- Users should be able to edit and delete filters applied to their view, including basic use cases for columns that are not visible in the View.
- **Potential future features**:
	- Improvements to what columns can be used for filters to support more complex use cases.

## Sorting
- **For alpha release**:
	- Users should be able to see what sorts are applied to their View.
	- Users should be able to edit and delete sorts applied to their view, including basic use cases for columns that are not visible in the View.
- **Potential future features**:
	- Improvements to what columns can be used for sorts to support more complex use cases.

## Aggregations
- **For alpha release**:
	- Users should be able to see what aggregations are applied to their View.
	- Users should be able to edit and delete basic aggregations applied to their view (such as `DISTINCT` and `GROUP BY`)
- **Potential future features**:
	- Improvements to editing and deleting aggregations that support more complex use cases (such as `GROUPING SETS`) 

## Row Limit
- **For alpha release**:
	- Users should be able to see if a row limit is applied.
	- Users should be able to edit or delete a row limit if one is applied.
- **Potential future features**:
	- Users should be able to add a row limit if none is applied.

## Row Offset
- **For alpha release**:
	- Users should be able to see if a row offset is applied.
	- Users should be able to edit or delete a row offset if one is applied.
- **Potential future features**:
	- Users should be able to add a row offset if none is applied.

## Groups
- **For alpha release**:
	- Views should support the same groupings as tables based on column data types.
- **Potential future features**:
	- Additional grouping features based on data sources or data formula.