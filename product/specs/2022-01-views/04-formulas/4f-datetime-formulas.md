---
title: (f) Date, Time, and Duration Formulas
description: 
published: true
date: 2022-03-01T00:16:57.505Z
tags: 
editor: markdown
dateCreated: 2022-02-26T00:25:24.180Z
---

> Under construction
{.is-warning}

These formulas operate on date & time types. They are based on PostgreSQL [date/time functions and operators](https://www.postgresql.org/docs/9.1/functions-datetime.html).

# Add Duration to Date
Adds a duration to a date or datetime.

- **Date Type**: Datetime or Time (depends on input) 
- **Variables Accepted**:
    - **Date or Time**:
        - **Type**: Single Record Date or Time-Like
        - **Description**: Date or time to add the duration to
    - **Duration**:
        - **Type**: Single Record Duration-Like
        - **Description**: Duration to add
- **Editable?**: No
- **PostgreSQL Mapping**: `+` operator 

# Subtract Duration from Date
Subtracts a duration from a date or datetime.

- **Date Type**: Datetime or Time (depends on input)
- **Variables Accepted**:
    - **Date or Time**:
        - **Type**: Single Record Date or Time-Like
        - **Description**: Date or time to subtract the duration from
    - **Duration**:
        - **Type**: Single Record Duration-Like
        - **Description**: Duration to subtract
- **Editable?**: No
- **PostgreSQL Mapping**: `-` operator 

# Date Difference (Age)
Subtracts a datetime type from a datetime type and returns the resulting duration

- **Date Type**: Duration 
- **Variables Accepted**:
    - **Date or Time 1**:
        - **Type**: Single Record Date or Time-Like
        - **Description**: First date(time)
    - **Date or Time 2**:
        - **Type**: Single Record Date or Time-Like
        - **Description**: Second date(time)
- **Editable?**: No
- **PostgreSQL Mapping**: `-` operator 

# Current Date
Always shows current date.

- **Date Type**: Date 
- **Variables Accepted**: *None*
- **Editable?**: No
- **PostgreSQL Mapping**: `current_date` function

# Current Time
Always shows current time.

- **Date Type**: Time 
- **Variables Accepted**: *None*
- **Editable?**: No
- **PostgreSQL Mapping**: `current_time` function

# Current Date & Time
Always shows current date and time.

- **Date Type**: Datetime 
- **Variables Accepted**: *None*
- **Editable?**: No
- **PostgreSQL Mapping**: `current_timestamp` function

# Truncate
Truncates date to specified precision.

- **Date Type**: Datetime 
- **Variables Accepted**:
    - **Date or Time**:
        - **Type**: Single Record Datetime-Like
        - **Description**: Datetime to truncate
    - **Precision**:
        - **Type**: Choice. Options:
            - microseconds
            - milliseconds
            - second
            - minute
            - hour
            - day
            - week
            - month
            - quarter
            - year
            - decade
            - century
            - millennium
        - **Description**: Precision to truncate to.
- **Editable?**: No
- **PostgreSQL Mapping**: `date_trunc` function 

# Extract
Extracts a specific part of a date from a datetime.

- **Date Type**: Text 
- **Variables Accepted**:
    - **Date or Time**:
        - **Type**: Single Record Datetime-Like
        - **Description**: Datetime to extract the part from
    - **Precision**:
        - **Type**: Choice. Options:
            - microseconds
            - milliseconds
            - second
            - minute
            - hour
            - day
            - week
            - month
            - quarter
            - year
            - decade
            - century
            - millennium
            - day of week
            - day of year
            - epoch
            - day of week (ISO)
            - year (ISO)
            - timezone
            - timezone hour
            - timezone minute
        - **Description**: Precision to truncate to.
- **Editable?**: No
- **PostgreSQL Mapping**: `extract` function. This then needs to be processed if needed into a friendly representation based on the display options of the column (e.g. `1` for month might become `January`)

# Convert Timezone
Converts a datetime into a specified timezone.

- **Date Type**: Datetime 
- **Variables Accepted**:
    - **Date or Time*:
        - **Type**: Single Record Datetime-Like
        - **Description**: Timestamp to convert
    - **Timezone**:
        - **Type**: Choice. Options are a list of valid timezones.
        - **Description**: Timezone to convert to
- **Editable?**: No
- **PostgreSQL Mapping**: `timezone(zone, timestamp)` function 
