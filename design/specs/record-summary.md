---
title: Record Summary
description: 
published: true
date: 2022-07-18T19:10:39.506Z
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
![image](/assets/design/specs/record-summary/179570423-e41b54e2-ebd7-4e73-acb2-8337ec6bb2db.png)

### Record Page
The summary on a record page serves as both a header and a representation of linked records.
![image](/assets/design/specs/record-summary/179571077-3ab610ff-d0ca-4d70-b840-e760dd567edb.png)

### Table Row
A summary is also shown at the row level to identify the records.
![image](/assets/design/specs/record-summary/179571476-4fa60138-3acf-4b69-9c32-cc1468cdf965.png)

## Components

### Summary Expression Builder
By default, the value of the record's first non-primary-key field is set as the record summary. In most circumstances, however, the user will want to customize the record summary to include a non-default or extra column or characters.

A component that allows users to enter columns, choose them as they type, and combine these columns with other symbols or letters in the correct order is required for this.

The expression input component will enable users to enter in any letters and will verify if the content matches an existing column as they type. For example, if a user starts typing "Check," the menu will automatically filter to any columns that begin with "Check," such as "Checkouts." The best match will be highlighted automatically, and the user may select it by hitting Tab.

Once inserted, the columns will be highlighted in color to differentiate them, whilst the characters will remain in plain text. To remove parts of the expression, the user must hit the backspace key, which will erase a single character or an entire column if applicable. Please note that is not possible to delete a character or column without deleting all the characters or columns after it.

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
