---
title: Email Data Type
description: 
published: true
date: 2021-08-11T09:05:46.024Z
tags: 
editor: markdown
dateCreated: 2021-08-10T16:15:43.563Z
---

# Context
Email data types are custom Mathesar data types used to store email addresses. 

# Prototype 
[Email Data Type Prototype](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?page-id=3750%3A28603&node-id=3757%3A31323&viewport=-337%2C513%2C0.9479455947875977&scaling=contain&starting-point-node-id=3757%3A31323)

# User Experience
## Scenarios
### User sets a column to 'Email' data type
The user can set the column data type to 'Email' by accessing the 'Data Type Options' in the columns header menu.
Depending on whether there are existing values or not, and if they are valid email values, the outcomes will vary:
If there are valid email values, the system will convert them to email types. A valid email will have a username and domain name joined by a '@' symbol.
If there are no valid email values, the system will discard the existing values and default to an empty cell.

### User enters a new 'Email' data type value
The user might enter a new email value with a valid format. If the value is not a valid email, an error should be displayed, preventing the row from being saved.

### User filters an 'Email' data type column
Users can filter 'email' data type columns by regular 'Text' type filters as well as 'Email' specific filters such as domain name.

### User groups an 'Email' data type column
Users can group 'email' data types columns by first letter or domain.


## Additional Changes
### New record row placement
The new record row, originally designed to sit at the bottom of the table, will now be on top. Change is due to confusing placement within groups and compensating for the pagination change impact on the usability of adding new records. 