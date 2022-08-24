---
title: Column Extraction
description: 
published: true
date: 2022-07-22T11:12:59.313Z
tags: 
editor: markdown
dateCreated: 2022-07-22T11:12:59.313Z
---

## Context

In data modeling, it's usual practice to split data up into related tables. In the context of Mathesar, one way of doing this is by extracting columns from a table into a new table.

Data is often split up into related tables for the following reasons:

- To use one table per type of object
- To avoid data duplication

This spec describes the steps a user would take to create a new table from a subset of columns from an existing table. It also describes the steps a user would take to move one or more columns from one table to another linked table.

## Design Goals

- Allow users to split a table into multiple new tables by selecting columns
- Help users understand the impact of splitting a table
- Allow users to move columns from a table to another link table

## Splitting a Table by Extracting Columns

### Selecting columns as a starting point

The user will select one or multiple columns to start with the column move process. All columns can be moved, except for primary key columns, unorderable columns like JSON-type columns and referent columns (Columns referenced by other columns).

Once selected, the inspector panel will list 'New linked table from columns' as an action. Selecting this option will open the 'New linked table from columns' dialog.

When a user selects a column that cannot be moved, the move action will be disabled and a tooltip will be available explaining why the column cannot be moved.

![image](/assets/design/specs/column-extraction/8p3u9NbBGBr6gqPx7VW9RZ.png)

## Extract Columns Dialog

The dialog will list the columns that will be moved and the table that will be created. The user can change the name of the new table. The dialog will also list the links that will be created between the new table and the original table. The user can change the name of the link column.

![image](/assets/design/specs/column-extraction/7prBiuRUXhPYi6wZxwRcyV.png)

### Impact of the Extract Columns Operation

Since the split operation will affect the original table, the user should be made aware of the operation's outcome. The dialog should incorporate information regarding the changes that will be done to both the original table and the new table. This includes:

- The original table will lose the selected columns
- The original table will gain a new link column
- The new linked table will gain the selected columns

## Moving Columns to a Linked Table

In some cases, a user may want to move columns from one table to another table. This can be done by selecting the columns and using the 'Move to existing linked table' action in the inspector panel.

### Selecting a the link column

A table might be linked to through more than one column. The user will be able to select the link column to use for the move operation under the 'Link Column' section. If only one link column exists, it will be selected by default.

No link column is created when moving columns to an existing linked table.

![image](/assets/design/specs/column-extraction/gzGpUGi1srtxQ2kwd2TruB.png)

### Link Column Naming Convention

The link column's name will be based on the table name. So if the user enters Author as a table name, then the link column would also be called Author. If the name is already taken, then the link column will be called Author 1, Author 2, etc.

The discussion related to the naming convention can be found in the following [email thread](https://groups.google.com/a/mathesar.org/g/mathesar-developers/c/yu1dOjV7EC8).

### Allowing the user to modify the original column selection

Under the `Columns to Extract` section, the user can extend the original column selection by selecting additional columns. The user can also remove columns from the selection.

Only columns that can be moved will be available for selection. A message inside the dropdown menu will inform users that the columns listed are the only ones that can be moved.

"Only columns that can be moved are listed. Primary key columns, unorderable columns like JSON-type columns and referent columns (columns referenced by other columns) cannot be moved."

## Finalizing the Extract Column Operation

Once the user is happy with the changes, they can click on the `Extract Columns` button. The inspector panel will be toggled and the new link column will be selected in the original table. Under the `Columns` section, the user will see the new table listed as a link.

![image](/assets/design/specs/column-extraction/99zmoTssPdnh2AYS5tDeWJ.png)

This spec does not include the implementation of 'Link Properties' which should be handled in a separate spec.
