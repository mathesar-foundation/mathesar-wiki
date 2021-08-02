---
title: Number Data Type
description: 
published: true
date: 2021-08-02T09:24:18.842Z
tags: 
editor: markdown
dateCreated: 2021-07-23T20:02:57.303Z
---

> This spec is in the review process, and its contents are subject to change. 
{.is-warning}

# Context
Number data types allow users to add numeric values in different formats. 

# Prototype
[Number Data Type Figma Prototype](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?page-id=3043%3A25937&node-id=3118%3A23009&viewport=-201%2C-496%2C0.35054445266723633&scaling=contain&starting-point-node-id=3118%3A23009)

# User Experience

## Scenarios
### User sets number data type options
A user can access the data type configuration of a field through the column menu. Depending on which data type is selected, the content of the configuration panel will change.

### User sets different data type formats
When setting a number type, a user can pick from different formats, including decimals, floats, integers, and percentages.
[Examples of options available for each type](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?page-id=3172%3A22488&node-id=3172%3A22489&viewport=682%2C424%2C0.9095099568367004&scaling=min-zoom)

### User filters the values of a number data type column
A user can filter the values of a number data type column. The filtering options will vary depending on the type selected. 

### User groups records according to numeric values of a column
A user can create groups based on the numeric values of a column. The User can choose to group by unique values or automatic ranges. Range options can be set so that groups are created by size or number of groups.

## Review Notes
### 'Friendly' and 'Database' type display
We want to make sure users of all levels can understand and use the appropriate data types. Because the distinction between database types is sometimes not evident to beginner levels, we want to map them to more familiar categorizations. The design ensures that information will be available but prioritizes the user-friendly types in terms of visibility.