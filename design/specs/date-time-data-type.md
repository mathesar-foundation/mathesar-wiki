---
title: Date, Time, and DateTime Data Types
description: 
published: true
date: 2021-08-20T09:56:05.001Z
tags: 
editor: markdown
dateCreated: 2021-08-06T16:29:46.474Z
---

## Context

Date, Time, and DateTime Data Types represent temporal values. The system can display each temporal value in different formats depending on the data or user needs (e.g., 6 Aug 2021, 06/08/2021).

For this purpose, three different data types will be available for storing date and time data:

### Date

Used for values with a date part only. Keeps track of days in the format `YYYY-MM-DD`.

### Time

Used for values representing a time of day in hours, minutes, seconds, and optional fractions of seconds in the format `hh:mm:ss`.

### DateTime

Used for values that contain both date and time parts in the format `YYYY-MM-DD hh:mm:ss`.

## Prototype

[Date, Time and DateTime Data Type Options](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?page-id=7250%3A80778&node-id=7251%3A82246&viewport=300%2C48%2C0.41&scaling=min-zoom)

## User Experience

Date, Time, and DateTime Data Types should allow users to set display options to present the data in formats different from how the values are stored.

## Scenarios

### Scenario 1: The user sets a column to a Date, Time or DateTime type

#### Scenario 1a: The column is set as to Time data type

1. The user opens the column type menu and selects the option listed as 'Time'.
2. The database and display options for Time are displayed in the menu.

#### Scenario 1b: The column is set as Date data type

1. The user opens the column type menu and selects the option listed as 'Date'.
2. The database and display options for Date are displayed in the menu.

#### Scenario 1c: The column is set as DateTime data type

1. The user opens the column type menu and selects the option listed as 'Date & Time'
2. The database and display options for DateTime are displayed in the menu.

### Scenario 2: If the column is empty

A Date, Time, or DateTime data type is set and the user can now input values with a date or time picker or manually. The system will restrict the allowed values based on the set format.

### Scenario 3: If the column contains values

If the system can't parse the values, the system will not set a Date, Time, or DateTime data type. The user will receive a warning, and if they choose to proceed, the system will empty the column values.

### Scenario 4: The user enters a new value for a Date, Time, or DateTime data type

When entering values in a column set to a Date, Time, or DateTime data type, the users will be able to do so from a date or time picker for easier input.

### Scenario 5: The user filters a Date, Time, or DateTime data type column

Values in a 'Date and Time' data type column can be filtered by various parameters such as specific date, a range of dates, dates after or before a certain date, and also by using natural language phrases like "now," "today," "next week," "next month."

### Scenario 6: The user groups a Date, Time, or DateTime data type column

Values in a Date, Time, or DateTime data type column can be grouped by different date and time units. Depending on the user's chosen data type, the options might include the date and time-specific units or not.
