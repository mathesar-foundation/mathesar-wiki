---
title: Global Data Type Components
description: 
published: true
date: 2023-07-19T23:21:03.653Z
tags: 
editor: markdown
dateCreated: 2021-08-31T08:38:10.315Z
---

## Context

Data types are data attributes that help to interpret their values and define the operations that the users can do and the values that can be stored. In the context of Mathesar, functionality and options will vary according to selected data types.

### Design Consistency Across All Data Types

It is part of Mathesar's future strategy to offer data modeling recommendations based on data types. This goal will be dependent on the user's adoption and understanding of data type functionality. For this reason, users must have a consistent experience when manipulating different data types within Mathesar. This document goes over the design elements and components common across data types to ensure cohesive design implementation.

## Components

### Data Type Options Menu

The data type options menu contains all of the configurations for a data type. These settings include database and display options. Most options are exclusive to each data type, except for setting a default value.

## Prototype

[Data Type Options Menu Prototype](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?page-id=4260%3A37440&node-id=4270%3A39549&viewport=324%2C48%2C0.29&scaling=contain&starting-point-node-id=4270%3A39549&show-proto-sidebar=1)

[Filter, group and sort prototype](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?page-id=4612%3A39411&node-id=4612%3A39412&viewport=324%2C48%2C0.23&scaling=contain&starting-point-node-id=4612%3A39412&show-proto-sidebar=1)

### Jan 2022 Update for Date, Time and DateTime Types

[Date, Time and DateTime Data Type Options](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?page-id=7250%3A80778&node-id=7251%3A82246&viewport=300%2C48%2C0.41&scaling=min-zoom)

### Database Options

Database options are those that define how the data is stored in the database. Users cannot always undo changes made to database options once they have applied them. Warnings need to be displayed to users to prevent data from being lost.

### Display Options

Display options change how the data is presented in the columns and can be changed without affecting the underlying data.

### Set default value

The Set Default Value field in all database options should allow data input using the same specialized input components available for the table interface.

### Data Type Filters, Groups, and Sorts

Filtering, grouping, and sorting operators and fields will be different according to each data type. Some options, like grouping by range, will only be available for number-based types, such as Number, Money, and Duration.

### Range by Time Unit Selector for Duration Types

Group by range in duration types will allow users to select a unit measure to create ranges with increments such as '5 years,'15 minutes', etc.

### Natural Language (date literals) Support for Date/Time Filters

Filter operators for Date/Time will allow natural language values such as 'Today,' 'Yesterday,' 'Last Month.'

## Specialized Components

When a data type is set for a column, additional functionality might be present at the field level to facilitate data input in the correct format.

### Date, Time or DateTime Picker

For Date, Time or DateTime input, a specialized component will be available so that users can enter dates using a calendar-like interface and unit-specific inputs with increment controls for time.

### Boolean Dropdown and Checkbox

For boolean values input, a specialized component will be available according to the display options set by the user. In the case of dropdown, clicking on the cell will display a menu with options for TRUE, FALSE, or NULL. Users will be able to copy and paste the values from the dropdown as true or false, but not the custom labels if enabled.

### Currency Formatting

For currency values input, the formatting will be automatically added after a value has been entered. For example, if the user enters 10000 and the currency locale settings are set to US dollars, the displayed value will be $10,000.00.

### Percentage Formatting

For number values input, the percentage formatting will be automatically added after a value has been entered. For example, if the user enters 0.20 and the number format settings are set to a percentage, the displayed value will be 20%.

### Long Text Detection and cell size adjustment

The cell input control will be automatically resized when active if a value exceeds a specific length for text values input. This adjustment will allow users to view the contents of a cell that has multi-line text. When inactive, the overflowing content should be indicated by adding an ellipsis icon in the cell.

### Alignment for Number Types

Contents of number type cells (number, duration, money) should be right-aligned for easier reading and data comparison.

### Font Variant for Number Types

Number types should be displayed using a font variant that supports tabular figures (numbers are all of the same size), allowing them to be easily aligned.

### Decimal Precision Settings for Money vs. Number

In number types, decimal precision is a database setting and in money type it is set as a display option.
