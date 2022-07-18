---
title: Record Summary
description: 
published: true
date: 2022-07-18T17:50:28.793Z
tags: 
editor: markdown
dateCreated: 2022-07-18T17:49:31.605Z
---

## Context 
Record summaries are strings that represent a record's data. They are specified by users and can include variable values from the record's fields, or include symbols and text characters.

## Usage
There are several views and parts of the application that make use of the record summary. Examples are when records are linked from a table, or when breadcrumb navigation indicates a record location.

The following are some of the most common use cases for record summaries that must be taken into account for this design:

### Table Links
In tables, summaries are used to represent the records that are linked via a foreign key.
![image](https://user-images.githubusercontent.com/845767/179570423-e41b54e2-ebd7-4e73-acb2-8337ec6bb2db.png)

### Record Page
The summary on a record page serves as both a header and a representation of linked records.
![image](https://user-images.githubusercontent.com/845767/179571077-3ab610ff-d0ca-4d70-b840-e760dd567edb.png)

### Table Row
A summary is also shown at the row level to identify the records.
![image](https://user-images.githubusercontent.com/845767/179571476-4fa60138-3acf-4b69-9c32-cc1468cdf965.png)

### The summary expression
Record summaries are constructed using an expression that takes the value of the record's first non-primary-key field.
This expression can be customized by the user to add any symbol or column values that they desire.
The expression is set at the table level, meaning that all records from that table will be represented in the same way across the product.

The value of the first non-primary-key field of a record is used as a default for the record summary. It is possible for the user to change this expression to add any symbol or column values that they feel appropriate.
Using this formula, all records in a particular table will be treated identically. Changes to a record's expression are reflected in all of its occurrences.

### The expression input component
An input component is provided in the table settings for creating the expression. The user has the option to type or select columns, and also add additional symbols, in this input. As the user types, the auto-complete pattern of the interaction suggests columns. In order to distinguish them from the text symbols, columns are displayed as tag-like objects with a distinct background color.

## User Flow

1. The user opens the settings panel for a table and finds the 'Display Options' section\
    By default the toggle is set to use a default summary. The default value is set to the first non-primary-key field.

    <img width="321" alt="image" src="https://user-images.githubusercontent.com/845767/175492420-77a0f46a-1026-4088-ba00-9061bb7b414e.png">

2. The user enables the 'Custom Summary' option
    As they enable the option, the custom expression contains the default value. The user can delete it or add other columns.

    <img width="320" alt="image" src="https://user-images.githubusercontent.com/845767/175492662-0a675593-d028-44da-8b64-d7a002e28174.png">

3. The user inserts a column
    As the user types, values for matching columns are displayed in a list. 

    <img width="318" alt="image" src="https://user-images.githubusercontent.com/845767/175507760-af004d5f-99a0-42a8-98cd-701dba3883f5.png">
    <img width="323" alt="image" src="https://user-images.githubusercontent.com/845767/175508253-4bdb3f1a-f7ce-4c95-ae26-b87f41dcdbbd.png">

    <img width="318" alt="image" src="https://user-images.githubusercontent.com/845767/175507760-af004d5f-99a0-42a8-98cd-701dba3883f5.png">

4. The user inserts a symbol
    The user can insert a symbol and it will be incorporated into the string. 

    <img width="323" alt="image" src="https://user-images.githubusercontent.com/845767/175508152-631812c6-c0fe-4777-a8ff-47f6b76fa531.png">
