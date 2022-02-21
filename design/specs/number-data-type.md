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

## Prototype

> This prototype might be outdated due to global component updates. Please refer to the link under 'Setting Options' for an updated version of the shared components.
{.is-warning}

[Number Data Type Figma Prototype](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?page-id=3043%3A25937&node-id=3118%3A23009&viewport=-201%2C-496%2C0.35054445266723633&scaling=contain&starting-point-node-id=3118%3A23009)

# User Experience

## Scenarios

### User sets number data type options

A user can access the data type configuration of a table field via the column menu. Depending on which data type is selected, the content of the configuration panel will change.

#### Setting Options

The following is an interactive representation of the various options that users can set for this type:
[Number Type Options](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?page-id=4260%3A37440&node-id=4270%3A39634&viewport=324%2C48%2C0.21&scaling=contain&starting-point-node-id=4270%3A39634&show-proto-sidebar=1)

### User sets different data type formats

When setting a number type, a user can pick from different formats, including decimals, floats, and integers.

### User filters the values of a number data type column

A user can filter the values of a number data type column. The filtering options will vary depending on the type selected. 

### User groups records according to numeric values of a column

A user can create groups based on the numeric values of a column. The User can choose to group by unique values or automatic ranges. Range options can be set so that groups are created by size or number of groups.

#### User defines range manually

A user can set a min and max value for a range and the increment size.

#### User defines ranges automatically
A user can set the number of groups or the size for each group. If the number of groups is set to 2, the range will be divided into two equal groups. If the group size parameter is set to 5, the values will be divided into ranges with an equal number of unique values. In this case, 5, not all groups will have the same number of equal values, as the total might not be divided into equal parts.

[Examples of Grouping by Range Options](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?page-id=3458%3A26001&node-id=3469%3A27264&viewport=69%2C76%2C0.7793133854866028&scaling=min-zoom)

## Review Notes

### 'Friendly' and 'Database' type display

We want to make sure users of all levels can understand and use the appropriate data types. Because the distinction between database types is sometimes not evident to beginner levels, we want to map them to more familiar categorizations. The design ensures that information will be available but prioritizes the user-friendly types in terms of visibility.

### Number type alignment

The interface should align number types to the right for easier reading of numbers with decimals.

## Update 21 Feb 2022

### Currency Format for Number Types

Users can now format the number type to represent currency values when set to decimal. For this, users can add a currency symbol to the number and set options like showing a thousand separators or changing the position of the currency symbol.

Additionally, the interface must inform the user that this is a display option and lacks specialized functionality provided by the `Money` data type.

Changes to the `Money` data type are also required as part of this update. Refer to [Money Data Type Specs](/design/specs/money-data-type) for more information.

#### Updated Prototype

[Figma Prototype - Updated Number Type Display Options](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?page-id=7552%3A83433&node-id=7552%3A83433&viewport=241%2C48%2C0.46&scaling=contain)

#### Scenario: A user sets the number type to be displayed in currency format

- The user sets a column type to `number.`
- The user opens the data type menu and opens the `Display` section.
- The user sets the `Format` option to `Currency` and [additional options](#currency_format_options) are displayed.
- The user can change or leave the default options.
- The user saves the data type changes.

#### Currency Format Options

- Select Symbol: Users can select the symbol that will be displayed along with the number. The currency symbol is set to $ (US Dollar) by default.
- Symbol position: Users can select the position for the currency symbol. The options are start or end.
- Digit Grouping: Options are '123456789','123,456,789','123456,789' or '12,34,56,789'
- Digit Grouping Symbol: Options are 'none','thin space','.' or ','
- Decimal Symbol: Options are '.' or ','
