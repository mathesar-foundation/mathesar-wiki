---
title: Text Data Type
description: 
published: true
date: 2021-08-18T13:44:48.418Z
tags: 
editor: markdown
dateCreated: 2021-07-21T10:04:10.817Z
---

# Context
Text data types allow users to add letters, symbols, or numbers as field values. The text data type is also the default type for new columns within Mathesar. 

## Permitted Characters
Text data type lets users enter almost any character (letter, symbol, or number).

# Prototype
[Text Data Type Figma Prototype](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?page-id=2965%3A22194&node-id=3026%3A19273&viewport=-2010%2C270%2C1.0617244243621826&scaling=contain&starting-point-node-id=3026%3A19273)

# User Experience

## Scenarios
### User sets text data type options
Each data type contains options that are specific to the selected type. Users can click on the data type dropdown and access them on the data type menu to access these options.

### User changes the text data type
From the data type menu, users can also choose to change the data type. Clicking on change data type will open a menu with the complete list of data types. 

### User filters a text data type column
Users can filter text data type columns based on the alphanumeric values of each field. When a text type column is filtered, the specific options for text will show under the filter parameters. 

### User sorts a text data type column
Users can sort records based on the values of text data type fields. The available options allow users to sort in alphabetical order in both ascending and descending orders.

### User groups a text data type column
Users can group records based on the values of text data type fields. The available options allow users to group by first letter or word of field values.

## Review Notes
### Filter, Sort and Group Actions
The design for filter, sort and group actions might require some updates to make the status of applied configurations more visible. Originally, these configurations were shown in a consolidated panel, but the solution is not optimal for some use cases. For example, when providing troubleshooting options, we might enable a filter to show affected rows, but the User, might not know how to return to the filter. A proposed solution is to iterate on the design for the filter, sort, and group features to optimize for discoverability and visibility of status.

### Preventing changes that produce errors
Some changes like column constraints or data type configurations might produce errors if the content in the columns is invalid. Rather than allowing the change and triggering error warnings in all affected records, we want to prevent the change and guide users towards modifying the column content until it's valid. 
