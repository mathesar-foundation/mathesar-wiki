---
title: Boolean Data Type
description: 
published: true
date: 2021-08-20T12:40:49.664Z
tags: 
editor: markdown
dateCreated: 2021-08-12T09:27:03.181Z
---

# Context
Boolean data types are used to store TRUE or FALSE values. 

# Prototype
> This prototype might be outdated due to global component updates. Please refer to the link under 'Setting Options' for an updated version of the shared components.
{.is-warning}

[Boolean Data Type Prototype](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?page-id=3750%3A28605&node-id=3791%3A34140&viewport=1115%2C-449%2C0.4775923192501068&scaling=min-zoom&starting-point-node-id=3791%3A34140)

# User Experience
## Scenarios
### User sets a column to 'Boolean' data type
The user can set the column data type to 'Boolean' by accessing the 'Data Type Options' in the columns header menu.
Whether there are existing values or not, the outcomes will vary if they are valid boolean values.
If there are valid URL values, the system will convert them to boolean types. There are only two boolean values. They are True and False. However, we might map existing binomial values or integers as equivalents to true and false, for example, 'yes and no' or '0 and 1'.

If there are no valid boolean values, the system will prevent the change from being made. 

#### Setting Options
The following is an interactive representation of the various options that users can set for this type:
[Boolean Type Options](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?page-id=4260%3A37440&node-id=4270%3A41050&viewport=324%2C48%2C0.34&scaling=contain&starting-point-node-id=4270%3A41050)


### User enters a new 'Boolean' data type value
Depending on the configuration, the user will enter a 'Boolean' value with two different controls.
- Default Dropdown (TRUE, FALSE)
- Custom Dropdown (TRUE Custom Value, FALSE Custom Value)
- Checkbox (Checked, Unchecked)

### User filters a 'Boolean' data type column
Users can filter 'Boolean' data type columns by basic equality operators (is, is not) and whether the value is empty. 

### User groups a 'Boolean' data type column
Users can group 'boolean' data types columns simply by adding them to the group columns list. The function will create a group for each boolean value (TRUE, FALSE).

## Additional Changes
### Disable Unique Constraint for Certain Data Types
The user won't be able to disallow duplicate values for a 'Boolean' type column. The setting should appear disabled under the column header menu.