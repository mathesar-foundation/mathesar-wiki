---
title: Product Specs
description: Views: UI Requirements for Views
published: true
date: 2022-01-13T19:49:54Z
tags: 
editor: markdown
dateCreated: 2022-01-13T19:49:54Z
---

The first version of Views should support the following features.

I've marked the features we should support as "for alpha release", but I've also listed a few potential future features so that we can think about them while designing code architecture and UI/UX.

# View Setup
The View Setup functionality should be invoked when creating Views or adding or removing columns to an existing View. What we are doing here is either creating or editing the underlying [Query](/product/specs/2022-01-views/03-modeling-view-query) that defines a View.

View Setup should only be enabled for an existing View if the Query is editable.

View Setup should allow users to:
- Add or remove [Columns](/product/specs/2022-01-views/04-modeling-view-columns) to the View
	- If adding, the user should be able to set their Source and Formula
	- When the column added involves a JOIN, the user should be able to change the type of JOIN used.
- Add or remove [Query attributes](/product/specs/2022-01-views/03-modeling-view-query)

Here are some *very* rough wireframes to illustrate the idea.
![View Query Setup](/assets/product/specs/2022-01-views/05-ui-requirements-for-views/Query Setup.png Setup.png)
![View Add Column](/assets/product/specs/2022-01-views/05-ui-requirements-for-views/View Setup_ Add Column.png Setup_ Add Column.png)

# Interacting with View Data
This covers functionality for Views that have already been created.

## Query
- **For alpha release**: 
	- Users should be able to see the query associated with a View after it has been loaded.
	- If the Query is editable, the user could see the broken down attributes.
- **Potential future features**:
	- SQL editor for queries
	- View creation using SQL.

## Columns
- **For alpha release**: Users should be able to see all columns associated with a view. Each column should show all the [Column attributes](/product/specs/2022-01-views/04-modeling-view-columns), which are non-editable.
- **Potential future features**:
	- Show virtual columns involved in view creation (via CTEs, subqueries, etc.)
	- Allow editing formula through UI
	- Allow using SQL to edit formula

*Very* rough wireframe to illustrate the idea.
![Views Column Detail](assets/product/specs/2022-01-views/View Column Menu.png)

## Rows
- **For alpha release**: 
	- Users should be able to see the rows associated with a view.
	- If a cell is a direct representation of a record, users should be able to edit that record via that cell. The entire record should be edited through a form, not just the single item.
		- "Direct representation" means that the record has only one data source, no formula, and is not a Link.
	- If a column is a direct representation of a record, users should be able to add a new record of the same type via the View UI.
- **Potential future features**:
	- "Smarter" editing of Views

## Filters
- **For alpha release**:
	- Users should be able to see what filters are applied to their View.
	- Users should be able to apply new filters to the View.
	- Users should be able to save filters applied to the View in the UI to the View Query.
		- Under the hood, this will create a new View with an updated query and delete the old View. In the UI, this will appear as if the View has been updated.
- **Potential future features**:
	- Improvements to what columns can be used for filters to support more complex use cases.

## Sorting
- **For alpha release**:
	- Users should be able to see what sorts are applied to their View.
	- Users should be able to apply new sorts to the View.
	- Users should be able to save sorts applied to the View in the UI to the View Query..
		- Under the hood, this will create a new View with an updated query and delete the old View. In the UI, this will appear as if the View has been updated.
- **Potential future features**:
	- Improvements to what columns can be used for sorts to support more complex use cases.

## Groups
- **For alpha release**:
	- Views should support the same groupings as tables based on column data types.
	- Groups cannot be saved to the database.
- **Potential future features**:
	- The ability to save groups as part of a view. This will only work within the Mathesar UI, not at the DB level.
	- Additional grouping features based on data sources or data formula.
