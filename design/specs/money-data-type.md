---
title: Money Data Type Specs
description: 
published: true
date: 2021-08-24T21:05:45.277Z
tags: 
editor: markdown
dateCreated: 2021-08-05T09:14:25.201Z
---

# Context

Money Data Types allow users to manage monetary values, preceded by a currency symbol of their choice.

# Prototype

> This prototype might be outdated due to global component updates. Please refer to the link under 'Setting Options' for an updated version of the shared components.
{.is-warning}

[Figma Prototype for Money Data Type](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?page-id=3380%3A23047&node-id=3380%3A23048&viewport=-1070%2C505%2C0.4795173108577728&scaling=contain&starting-point-node-id=3380%3A23048)

# User Experience

## Scenarios

### The user sets the type of a column with existing values to 'Money.'

The user opens the menu for the desired column and selects the 'Data Type Options' menu item. From the list, they can set the type to money. Under advanced options, the user may set the currency and decimal places.

#### Setting Options

The following is an interactive representation of the various options that users can set for this type:
[Money Type Options](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?page-id=4260%3A37440&node-id=4270%3A40881&viewport=324%2C48%2C0.21&scaling=contain&starting-point-node-id=4270%3A40881&show-proto-sidebar=1)

### The user filters a 'Money' data type column

The user can choose from multiple filter options to filter monetary values. The options will be the same as those used for numeric types.

### The user groups a 'Money' data type column

The user might also choose to group the data based on the values of the 'Money' data type column.

# Review Notes

- For the MVP we'll assume the number locale format based on the selected currency. Eventually we can add options so that, for example, US dollars can be displayed with dot separators instead of commas. 
- All locales will be included whenever there's a locale-related option.

## Update 21 Feb 2022

### Remove option to change currency

The updated version will remove the option to change the currency from the money type. The data type menu will display only the current system locale. The system will inform the user that the selected currency will be updated if the locale settings are changed.

#### Updated Prototype

[Figma Prototype - Updated Money Type Display Options](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?page-id=7552%3A83433&node-id=7590%3A84021&viewport=241%2C48%2C0.46&scaling=contain)