---
title: Views: Modeling View Columns
description: 
published: true
date: 2022-01-13T19:49:54Z
tags: 
editor: markdown
dateCreated: 2022-01-13T19:49:54Z
---

Here's how I think we should model view columns in our API and UI. Each heading represents an attribute of a View Column.

### Data Type
- **Definition**: This is the final data type of the content of the column after any computations etc. are applied.
- **Allowed values**: same as Table data types.
- **Required**. Data type should always be set, at the very least, we can treat unknown data types as text.

### Data Sources
 - **Definition**: This is the set of source columns that are used to generate the data in the current View column.
- **Allowed values**: references to other Table or View columns, including other columns in the same View.
- **Optional**: This could be empty for purely calculated columns (e.g. using the Postgres `random()` function and putting the output in a column)

### Data Formula
- **Definition**: This is the formula used to generate data in for this column.
- **Allowed values**: SQL function + operators
- **Optional**: Columns that are direct copies of other columns from tables or views won't have a formula.

We should allow users to either use a pre-set set of formulas or (in the future) enter a custom formula using whatever functions are installed on their Postgres database.