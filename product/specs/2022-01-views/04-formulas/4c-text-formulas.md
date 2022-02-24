---
title: (c) Text Formulas
description: 
published: true
date: 2022-02-24T01:14:40.566Z
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
| choice | A selection from a pre-determined list of choices |

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
Concatenates two strings together.

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

## Overlay
Overlays a string at the specified position with another string

- **Date Type**: Text
- **Variables Accepted**:
    - **Base Text**:
        - **Type**: Text-like
        - **Description**: The text that will be processed
    - **Starting Position**:
        - **Type**: Integer
        - **Description**: Starting position of text to be replaced
    - **Overlay Text**:
        - **Type**: Text-like
        - **Description**: Text to overlay on the base text 
    - **Count**:
        - **Type**: Integer
        - **Description**: Number of characters to replace
        - **Optional**, If this is not provided, it defaults to the length of the Overlay Text
- **Editable?**: No
- **PostgreSQL Mapping**: `overlay` function

## Substring
Gets a substring of text at the given position

- **Date Type**: Text
- **Variables Accepted**:
    - **Base Text**:
        - **Type**: Text-like
        - **Description**: The text that will be processed
    - **Starting Position**:
        - **Type**: Integer
        - **Description**: Starting position of text to be extracted
        - **Optional**: Defaults to 1 if not provided.
    - **Count**:
        - **Type**: Integer
        - **Description**: Number of characters to extract
        - **Optional**: If this is not provided, the substring will be extracted until the end of the string.
- **Editable?**: No
- **PostgreSQL Mapping**: `substring` function with this signature: `substring ( string text [ FROM start integer ] [ FOR count integer ] ) → text`


## Trim
Trims characters from the start or end of text (or both).

- **Date Type**: Text
- **Variables Accepted**:
    - **Base Text**:
        - **Type**: Text-like
        - **Description**: The text that will be processed
    - **Trim Location**:
        - **Type**: Choice (Options: "Start", "End", "Both")
        - **Description**: Where the trimming will happen
        - **Optional**: Defaults to "Both" if not provided.
    - **Characters to Trim**:
        - **Type**: Text
        - **Description**: Characters to trim. The text provided will be treated as a list of characters; they will not be treated as a single word (e.g. `xyz` will trim any of `x`, `y`, and `z`)
        - **Optional**: If this is not provided, the default is a space.
- **Editable?**: No
- **PostgreSQL Mapping**: `trim` function

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
