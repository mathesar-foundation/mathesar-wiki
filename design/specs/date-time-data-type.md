---
title: Date and Time Data Type
description: 
published: true
date: 2021-08-13T09:26:20.048Z
tags: 
editor: markdown
dateCreated: 2021-08-06T16:29:46.474Z
---

> The content of this spec is under review and might change.
{.is-warning}


# Context
Date and Time data types are used to represent temporal values. Each temporal value can be displayed in different formats depending on the data or user needs (e.g., 6 Aug 2021, 06/08/2021).

# Prototype
[Date/Time Data Type Figma Prototype](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?page-id=3559%3A26639&node-id=3559%3A26640&viewport=-379%2C563%2C0.21144694089889526&scaling=contain&starting-point-node-id=3559%3A26640)

# User Experience

## The user sets a column to 'Date and Time' type
The user can set the column type by accessing the column header menu's  'data type options.'
### If the column is empty
The 'Date and Time' data type is set, and the user can now input data with a date picker or manually. The system will restrict the allowed values based on the set format. 
### If the column contains values
If the system can't parse the values, the system will not set the 'Date and Time' data type. The user will receive a warning, and if they choose to proceed, the system will empty the column values.

## The user enters a new value for a  'Date and Time' data type column
When entering values in a column set to the 'Date and Time' type, the users will be able to do so from a date or time picker for easier input.

## The user filters a 'Date and Time' data type column
Values in a 'Date and Time' data type column can be filtered by various parameters such as specific date, a range of dates, dates after or before a certain date, and also by using natural language phrases like "now," "today," "next week," "next month."

## The user groups a 'Date and Time' data type column
Values in a 'Date and Time' data type column can be grouped by different date and time units. Depending on the user's chosen display type (date and time, date only, or time only), the options might include the date and time-specific units or not. 
