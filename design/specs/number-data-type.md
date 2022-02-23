---
title: Number Data Type
description: 
published: true
date: 2021-08-23T09:53:24.773Z
tags: 
editor: markdown
dateCreated: 2021-07-23T20:02:57.303Z
---

# Context
Number data types allow users to add numeric values in different formats. 

# Prototype
> This prototype might be outdated due to global component updates. Please refer to the link under 'Setting Options' for an updated version of the shared components.
{.is-warning}

[Number Data Type Figma Prototype](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?page-id=3043%3A25937&node-id=3118%3A23009&viewport=-201%2C-496%2C0.35054445266723633&scaling=contain&starting-point-node-id=3118%3A23009)

# User Experience

## Scenarios
### User sets number data type options
A user can access the data type configuration of a field through the column menu. Depending on which data type is selected, the content of the configuration panel will change.

#### Setting Options
The following is an interactive representation of the various options that users can set for this type:
[Number Type Options](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?page-id=4260%3A37440&node-id=4270%3A39634&viewport=324%2C48%2C0.21&scaling=contain&starting-point-node-id=4270%3A39634&show-proto-sidebar=1)

### User sets different data type formats
When setting a number type, a user can pick from different formats, including decimals, floats, integers.

### User filters the values of a number data type column
A user can filter the values of a number data type column. The filtering options will vary depending on the type selected. 

### User groups records according to numeric values of a column
A user can create groups based on the numeric values of a column. The User can choose to group by unique values or automatic ranges. Range options can be set so that groups are created by size or number of groups.

#### User defines range manually
A user can set a min and max value for a range and the increment size
#### User defines ranges automatically
A user can set the number of groups or the size for each group. If the parameter for the number of groups is set to 2, the range will be divided into two equal groups. If the group size parameter is set to 5, the values will be divided into ranges with an equal number of unique values. In this case, 5, not all groups will have the same number of equal values, as the total might not be divided into equal parts.

[Examples of Grouping by Range Options](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?page-id=3458%3A26001&node-id=3469%3A27264&viewport=69%2C76%2C0.7793133854866028&scaling=min-zoom)

## Review Notes
### 'Friendly' and 'Database' type display
We want to make sure users of all levels can understand and use the appropriate data types. Because the distinction between database types is sometimes not evident to beginner levels, we want to map them to more familiar categorizations. The design ensures that information will be available but prioritizes the user-friendly types in terms of visibility.

### Number type alignment
Number types should be aligned to the right for easier reading of numbers with decimals.