---
title: (c) Text Formulas
description: 
published: true
date: 2022-02-24T00:56:57.446Z
tags: 
editor: markdown
dateCreated: 2022-02-24T00:56:57.446Z
---

These formulas operate on text and text-like types. They are based on [PostgreSQL string functions](https://www.postgresql.org/docs/current/functions-string.html).

# Variable Types
To reduce repetition in the formula definitions, variable types are defined here and only the type name is referenced in the list.

| Type Name | Description |
|-|-|
| text-like | A column or a literal string. Columns can be of any data type but the data in them will be treated like text. |
| integer | An integer literal or column with data type integer |

# Formulas

## Character Count
Returns number of characters in the text

- **Date Type**: Integer
- **Variables Accepted**:
    - **Text**:
        - **Type**: Text-like
        - **Description**: Text to count
- **Editable?**: No
- **PostgreSQL Mapping**: `char_length` (`character_length`) function


## Concatenate
Concatenates two texts together.

- **Date Type**: Text
- **Variables Accepted**:
    - **Text 1**:
        - **Type**: Text-like
        - **Description**: First text
    - **Text 2**:
        - **Type**: Text-like
        - **Description**: Second text
- **Editable?**: No
- **PostgreSQL Mapping**: `||` operator 

## Lowercase
Converts text to lowercase

- **Date Type**: Text
- **Variables Accepted**:
    - **Text**:
        - **Type**: Text-like
        - **Description**: Text to convert
- **Editable?**: No
- **PostgreSQL Mapping**: `lower` function

## Uppercase
Converts text to uppercase

- **Date Type**: Text
- **Variables Accepted**:
    - **Text**:
        - **Type**: Text-like
        - **Description**: Text to convert
- **Editable?**: No
- **PostgreSQL Mapping**: `upper` function

---

## Template
Description

- **Date Type**: Blah
- **Variables Accepted**:
    - **Foo**:
        - **Type**: Text-like
        - **Description**: Blah
- **Editable?**: No
- **PostgreSQL Mapping**: Blah
