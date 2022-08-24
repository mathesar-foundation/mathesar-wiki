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

In data modeling, it's usual practice to split data up into related tables. In the context of Mathesar, one way of doing this is by extracting columns from a table into a new table. This process is known as column extraction.

This spec describes the steps a user would take to create a new table from a subset of columns from an existing table.

## Design Goals

- Allow users to split a table into multiple new tables by selecting columns
- Help users understand the impact of splitting a table
- Help users understand how the tables are linked after the split operation

## Splitting a Table by Extracting Columns

### Selecting columns as a starting point

The user will select one or multiple columns to start with the column extraction process. All columns can be extracted, except for primary key columns. Once selected, the inspector panel will list 'New linked table from columns' as an action. Selecting this option will open the 'New linked table from columns' dialog.

![image](/assets/design/specs/column-extraction/8p3u9NbBGBr6gqPx7VW9RZ.png)

## Extract Columns Dialog

The dialog will list the columns that will be extracted and the table that will be created. The user can change the name of the new table. The dialog will also list the links that will be created between the new table and the original table. The user can change the name of the link column.

![image](https://share.balsamiq.com/c/7prBiuRUXhPYi6wZxwRcyV.png)

### Impact of the Extract Columns Operation

Since the split operation will affect the original table, the user should be made aware of the operation's outcome. The dialog should incorporate information regarding the changes that will be done to both the original table and the new table. This includes:

- The original table will lose the selected columns
- The original table will gain a new link column
- The new linked table will gain the selected columns

### Link Column Naming Convention

The link column's name will be based on the table name. So if the user enters Author as a table name, then the link column would also be called Author. If the name is already taken, then the link column will be called Author 1, Author 2, etc.

### Allowing the user to modify the original column selection

Under the `Columns to Extract` section, the user can extend the original column selection by selecting additional columns. The user can also remove columns from the selection.

This component could be reused for all actions involving column subsets.

## Finalizing the Extract Column Operation

Once the user is happy with the changes, they can click on the `Extract Columns` button. The inspector panel will be toggled and the new link column will be selected in the original table. Under the `Columns` section, the user will see the new table listed as a link.

![image](https://share.balsamiq.com/c/99zmoTssPdnh2AYS5tDeWJ.png)

This spec does not include the implementation of 'Link Properties' which should be handled in a separate spec.
