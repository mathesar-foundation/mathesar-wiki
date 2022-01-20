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

# Interacting with Views
This covers functionality for Views that have already been created.

## Query
- **For alpha release**: Users should be able to see the query associated with a View after it has been loaded.
- **Potential future features**:
	- Users can edit the query associated with a View.
	- Users can create a new View using a query.

## Columns
- **For alpha release**: Users should be able to see all columns associated with a view. Each column should show:
	- Data Type (non-editable)
	- Sources (non-editable, set when adding a new column to a View)
	- Formula (non-editable, set when adding a new column to a View)
	- Link (non-editable, set when adding a new column to a View)
- **Potential future features**:
	- Show virtual columns involved in view creation (via CTEs, subqueries, etc.)
	- Allow editing formula through UI
	- Allow using SQL to edit formula

## Rows
- **For alpha release**: 
	- Users should be able to see the rows associated with a view.
	- If a cell is a direct representation of a record, users should be able to edit that record via that cell. The entire record should be edited through a form, not just the single item.
		- "Direct representation" means that the record has only one data source and no formula.
	- If a column is a direct representation of a record, users should be able to add a new record of the same type via the View UI.
- **Potential future features**:
	- Users can edit the query associated with a View.
	- Users can create a new View using a query.

## Filters
- **For alpha release**:
	- Users should be able to see what filters are applied to their View.
	- Users should be able to edit and delete filters applied to their view in the UI, including basic use cases for columns that are not visible in the View.
		- By default, these filters are not saved to the database.
	- Users should be able to save filters applied to the View in the UI.
		- Under the hood, this will create a new View with an updated query and delete the old View. In the UI, this will appear as if the View has been updated.
- **Potential future features**:
	- Improvements to what columns can be used for filters to support more complex use cases.

## Sorting
- **For alpha release**:
	- Users should be able to see what sorts are applied to their View.
	- Users should be able to edit and delete sorts applied to their view, including basic use cases for columns that are not visible in the View.
		- By default, these sorts are not saved to the database.
	- Users should be able to save sorts applied to the View in the UI.
		- Under the hood, this will create a new View with an updated query and delete the old View. In the UI, this will appear as if the View has been updated.
- **Potential future features**:
	- Improvements to what columns can be used for sorts to support more complex use cases.

## Aggregations
- **For alpha release**:
	- Users should be able to see what aggregations are applied to their View.
	- Users should be able to edit and delete basic aggregations applied to their view (such as `DISTINCT` and `GROUP BY`)
		- By default, these aggregations are not saved to the database.
	- Users should be able to save aggregations applied to the View in the UI.
		- Under the hood, this will create a new View with an updated query and delete the old View. In the UI, this will appear as if the View has been updated.
- **Potential future features**:
	- Improvements to editing and deleting aggregations that support more complex use cases (such as `GROUPING SETS`) 

## Row Limit
- **For alpha release**:
	- Users should be able to see if a row limit is applied.
	- Users should be able to edit or delete a row limit if one is applied. This should save directly to the database.
- **Potential future features**:
	- Users should be able to add a row limit if none is applied.

## Row Offset
- **For alpha release**:
	- Users should be able to see if a row offset is applied.
	- Users should be able to edit or delete a row offset if one is applied. This should save directly to the database.
- **Potential future features**:
	- Users should be able to add a row offset if none is applied.

## Groups
- **For alpha release**:
	- Views should support the same groupings as tables based on column data types.
	- Groups cannot be saved to the database.
- **Potential future features**:
	- The ability to save groups as part of a view. This will only work within the Mathesar UI, not at the DB level.
	- Additional grouping features based on data sources or data formula.

# View Setup
This covers functionality for creating Views or adding new columns to an existing View.

`TODO`
