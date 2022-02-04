---
title: 05. UI Requirements
description: 
published: true
date: 2022-02-04T03:37:53.322Z
tags: 
editor: markdown
dateCreated: 2022-01-24T23:01:08.734Z
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

![view_builder_1.png](/assets/product/specs/2022-01-views/05-ui-requirements-for-views/view_builder_1.png)
![view_builder_2.png](/assets/product/specs/2022-01-views/05-ui-requirements-for-views/view_builder_2.png)
![view_builder_3.png](/assets/product/specs/2022-01-views/05-ui-requirements-for-views/view_builder_3.png)
![view_builder_4.png](/assets/product/specs/2022-01-views/05-ui-requirements-for-views/view_builder_4.png)
![view_builder_5.png](/assets/product/specs/2022-01-views/05-ui-requirements-for-views/view_builder_5.png)

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

![view_column_menu.png](/assets/product/specs/2022-01-views/05-ui-requirements-for-views/view_column_menu.png)

## Rows
- **For alpha release**: 
	- Users should be able to see the rows associated with a view.
	- Cells may be editable, depending on the [Formula](/en/product/specs/2022-01-views/07-formulas) involved.
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