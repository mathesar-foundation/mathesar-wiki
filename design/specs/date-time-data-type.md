---
title: Date and Time Data Type
description: 
published: true
date: 2021-08-06T16:45:20.534Z
tags: 
editor: markdown
dateCreated: 2021-08-06T16:29:46.474Z
---

# Context
Date and Time data types are used to represent temporal values. Each temporal value can be displayed in different formats depending on the data or user needs (e.g., 6 Aug 2021, 06/08/2021).

# Prototype
[Date/Time Data Type Figma Prototype](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?page-id=3559%3A26639&node-id=3576%3A27555&viewport=2021%2C524%2C0.5210340619087219&scaling=contain&starting-point-node-id=3576%3A27555)

# User Experience

## The user sets a column to 'Date and Time' type
The user can set the column type by accessing the column header menu's  'data type options.'
### If the column is empty
The 'Date and Time' data type is set, and the user can now input data with a date picker or manually. The system will restrict the allowed values based on the set format. 
### If the column contains values
If the values can't be parsed, the system will not set the 'Date and Time' data type. The user will receive a warning, and if they choose to proceed, the system will empty the column values.

## The user enters a new value for a  'Date and Time' data type column
When entering values in a column set to the 'Date and Time' type, the users will be able to do so from a date or time picker for easier input.

## The user filters a 'Date and Time' data type column
Values in a 'Date and Time' data type column can be filtered by various parameters such as specific date, a range of dates, dates after or before a certain date, and also by using natural language phrases like "now," "today," "next week," "next month."

[Date/Time Data Type Filter Options Figma Prototype](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?page-id=3577%3A29502&node-id=3577%3A29694&viewport=223%2C320%2C0.4651184380054474&scaling=min-zoom)

## The user groups a 'Date and Time' data type column
Values in a 'Date and Time' data type column can be grouped by range. Where maximum and minimum dates can be provided as well as the desired interval for each group.

[Date/Time Data Type Group Options Figma Prototype](https://www.figma.com/file/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?node-id=3596%3A31421)
