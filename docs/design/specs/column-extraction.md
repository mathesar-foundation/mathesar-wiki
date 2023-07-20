---
title: Column Extraction
description: 
published: true
date: 2023-05-11T14:41:32.692Z
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

## Scenario 1: New Linked Table from Columns

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

## Scenario 2: Moving Columns to a Linked Table

In some cases, a user may want to move columns from one table to another table. This can be done by selecting the columns and using the 'Move to existing linked table' action in the inspector panel.

### Selecting a the link column

A table might be linked to through more than one column. The user will be able to select the link column to use for the move operation under the 'Link Column' section. If only one link column exists, it will be selected by default.

![image](/assets/design/specs/column-extraction/gzGpUGi1srtxQ2kwd2TruB.png)

### Impact of the Move Columns Operation

- The original table will lose the selected columns
- The original table will not gain any new link column
- The linked table will gain the selected columns

## Finalizing the Move Column Operation

Once the user is happy with the changes, they can click on the `Move Columns` button. The user will be taken back to the original table and the selected columns will be moved to the linked table.

## Pending Design Problems

### Moving columns in two directions

Some edge cases remain to be explored and addressed in regards to moving columns between tables.

Given the following scenarios:

- Move columns from referrer table(table with foreign key column) to referent table
- Move columns from referent table to referrer Table

Should we allow moving columns in both directions?

### Moving Column Limitations

Also, there are a few edge cases in addition to the limitations(some columns are not allowed) we have with moving columns to a new Table.

### Other Edge Cases

- Multiple Tables referencing the Linked Table(Table to which the column is moved) -
- Given there is a Table(let's call it an external Table) other than the original Table that happens to reference the Linked Table.
- And the Linked table has a normalised record.
- When a column is moved into the Reference Table.
- The normalised record might be split into multiple records.
- This leads to the question of which foreign key value the external Table record should point to.

A real-life example

Before moving

| Author Id | First name |
|-----------|------------|
| 1         | Jason      |

| Publication | Title       | Author | Last Name |
|-------------|-------------|--------|-----------|
| 1           | Steady Slow | 1      | Smith     |
| 2           | Think Fast  | 1      | Stone     |

| Award | Title | Author |
|-------|-------|--------|
| 1     | Nobel | 1      |

Jason won the Nobel prize
After moving

| Author Id | First Name | Last Name |
|-----------|------------|-----------|
| 1         | Jason      | Smith     |
| 2         | Jason      | Stone     |

| Publication | Title       | Author |
|-------------|-------------|--------|
| 1           | Steady Slow | 1      |
| 2           | Think Fast  | 2      |

| Award | Title | Author |
|-------|-------|--------|
| 1     | Nobel | ?      |
