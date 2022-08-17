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

The user will select one or multiple columns to start with the column extraction process. All columns can be extracted, except for primary key columns. Once selected, the inspector panel will list 'Extract Columns to Table' as an action. Selecting this option will open the 'Extract Columns to Table' dialog.

![image](/assets/design/specs/column-extraction/185139636-9a8a048c-9f87-4e26-aa2c-88f4e8d1648d.png)

## Extract Columns Dialog

The dialog will list the columns that will be extracted and the table that will be created. The user can change the name of the new table. The dialog will also list the foreign key that will be created between the new table and the original table. The user can change the name of the foreign key.

![image](/assets/design/specs/column-extraction/185140900-ea1514c3-2423-42ad-ab98-a4f87848f463.png)

### Impact of the Extract Columns Operation

Since the split operation will affect the original table, the user should be made aware of the operation's impact. The dialog will make the following information clear:

- The original table will be updated to remove the extracted columns
- A new table will be created with the extracted columns
- A foreign key will be created between the new table and the original table

### Link Column Name Convention

To help users understand the role of the link column, the name of the link column will follow a convention that will be applied when users name the new table. The convention will be:

`table_name` `+` `Id`

![image](/assets/design/specs/column-extraction/185142290-db3d6fc7-86b6-4a2d-8c23-7ed48104c8cc.png)

### Allowing the user to modify the original column selection

Under the `Columns to Extract` section, the user can extend the original column selection by selecting additional columns. The user can also remove columns from the selection.

This component could be reused for all actions involving column subsets.

Additionally, the user can rename the columns that will be extracted in cases where the column name is not descriptive enough.

## Finalizing the Extract Column Operation

Once the user is happy with the changes, they can click on the `Extract Columns` button. The inspector panel will be toggled and the new link column will be selected in the original table. Under the `Columns` section, the user will see the new table listed as a link.

![image](/assets/design/specs/column-extraction/185143860-f2995fc4-c767-4cce-aaa6-319ef27630ff.png)
