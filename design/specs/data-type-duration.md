---
title: Duration Data Type Specs
description: 
published: true
date: 2021-08-10T09:42:44.190Z
tags: 
editor: markdown
dateCreated: 2021-08-10T09:42:44.190Z
---

> The content of this spec is under review and might change.
{.is-warning}

# Context
Duration data types represent a period of time measured in hours, minutes, and/or seconds.

# Prototype 
[Duration Data Type Prototype](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?page-id=3652%3A28432&node-id=3652%3A28433&viewport=1951%2C518%2C0.7335814833641052&scaling=min-zoom&starting-point-node-id=3652%3A28433)

# User ExperienceT
## Scenarios
### User sets a column to 'Duration' data type
The user can set the column data type to 'Duration' by accessing the 'Data Type Options' in the columns header menu.
Depending on whether there are existing values or not, and if they are valid duration values, the outcomes will vary:
If there are valid duration values, the system will convert them to duration types. For example, '120' might become '2:00' if interpreted as total minutes.
If there are no valid duration values, the system will discard the existing values and default to an empty cell.

### User enters a new 'Duration' data type value
Depending on the duration format configuration, an empty cell will provide a placeholder format indicator such as 'h:mm' when the cell is in an active state. Depending on the format, the user might input a value using the exact format or in the unit values of minutes or seconds. For example, '240' will be formatted as '4:00.'

### User filters a 'Duration' data type column
Users can filter 'duration' data type columns with the same options as 'Number' data type, and it also allows natural language expressions to be used, such as 'greater than 2 hours.

### User groups a 'Duration' data type column
Users can group 'duration' data types columns by different duration units such as hours, minutes, or seconds. Users can apply filters to limit the number of examples or capture specific ranges.
