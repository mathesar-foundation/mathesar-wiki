---
title: Email Data Type
description: 
published: true
date: 2021-08-10T16:15:43.563Z
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
- If there are valid email values, the system will convert them to email types. A valid email will have a username and domain name joined by a '@' symbol.
- If there are no valid email values, the system will discard the existing values and default to an empty cell.

