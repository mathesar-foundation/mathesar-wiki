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

![image](https://share.balsamiq.com/c/8p3u9NbBGBr6gqPx7VW9RZ.png)

## Extract Columns Dialog

The dialog will list the columns that will be extracted and the table that will be created. The user can change the name of the new table. The dialog will also list the links that will be created between the new table and the original table. The user can change the name of the link column.

![image](https://share.balsamiq.com/c/7prBiuRUXhPYi6wZxwRcyV.png)

### Impact of the Extract Columns Operation

Since the split operation will affect the original table, the user should be made aware of the operation's impact. The dialog should communicate the following:

- The original table will be updated to remove the extracted columns
- A new table will be created with the extracted columns
- A link will be created between the new table and the original table

### Link Column Naming Convention

It was decided that the link column naming convention should be as follows:

>In the application, where singularization is not straightforward, we don’t suggest column names. Instead we require the user to manually name the FK column.

In this case, since we cannot infer the new table name from the selected columns, then the user must manually enter both, new table name and link column name.

#### Using Rules to Generate Column Names

In the future we might use a pre-defined list of rules to infer the singular form of the table name, but for now we will require the user to enter both names.

Applying these rules would require us to choose a specific column from which to generate the final name. If we select the first column, we'll end up with a table called "First Names" and a link column called "First Name."

### Allowing the user to modify the original column selection

Under the `Columns to Extract` section, the user can extend the original column selection by selecting additional columns. The user can also remove columns from the selection.

This component could be reused for all actions involving column subsets.

Additionally, the user can rename the columns that will be extracted in cases where the column name is not descriptive enough.

## Finalizing the Extract Column Operation

Once the user is happy with the changes, they can click on the `Extract Columns` button. The inspector panel will be toggled and the new link column will be selected in the original table. Under the `Columns` section, the user will see the new table listed as a link.

![image](/assets/design/specs/column-extraction/185143860-f2995fc4-c767-4cce-aaa6-319ef27630ff.png)

Additional details regarding 'Link Properties' will be added in a future spec.
