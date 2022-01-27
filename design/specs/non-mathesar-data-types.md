---
title: Non-Mathesar Data Types
description: 
published: true
date: 2021-08-25T20:56:09.786Z
tags: 
editor: markdown
dateCreated: 2021-08-12T13:04:26.580Z
---

# Context
Non-Mathesar types are database types that don't have any special functionality within Mathesar. This could be because that functionality is not implemented, yet it's a standard Postgres type (Other), or because it's a custom data type and not included in standard Postgres data types (Custom).

## Limited Functionality
'Non-Mathesar' data type can be edited or added, but there are no particular data input or display features. 

# Prototype 
[Non-Mathesar Data Type Prototype](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?page-id=3981%3A32764&node-id=3983%3A33046&viewport=3203%2C274%2C0.7351959347724915&scaling=contain&starting-point-node-id=3983%3A33046)

# User Experience
## Scenarios
### User sets a column to 'Non-Mathesar' data type
Users cannot set 'Non-Mathesar' data types. Mathesar can only add these by connecting to an existing database.

### User enters a new 'Non-Mathesar' data type value
Users can edit the existing values of a 'Non-Mathesar' data type column as they would with [text string types](/design/specs/data-types-text).

### User filters a 'Non-Mathesar' data type column
Users can filter the existing values of a 'Non-Mathesar' data type column as they would with [text string types](/design/specs/data-types-text).

### User groups a 'Non-Mathesar' data type column
Users can group the existing values of a 'Non-Mathesar' data type column as they would with [text string types](/design/specs/data-types-text).

# Review Notes
## Adjust size of cells based on content length
As part of the implementation of data types, we need to consider how the table will display content such as a JSON document or other longer content formats.