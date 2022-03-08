---
title: (h) Cumulative Formulas
description: 
published: true
date: 2022-03-08T22:21:12.529Z
tags: 
editor: markdown
dateCreated: 2022-02-26T00:35:38.877Z
---

These formulas show cumulative values that build on previous rows.

# Previous Row
Shows data from a previous row, in case you want to see it side-by-side with the current row.

- **Date Type**: Same as Input Column
- **Variables Accepted**:
    - **Column*:
        - **Type**: Query Column Reference
        - **Description**: Column to show
    - **Offset**:
        - **Type**: Integer
        - **Description**: How many rows back to go
        - **Default Value**: 1
- **Editable?**: No
- **PostgreSQL Mapping**: We need to write a custom function.

# Rolling Average
Shows an average of the data in a given column over the past X rows.

- **Date Type**: Decimal
- **Variables Accepted**:
    - **Column*:
        - **Type**: Single Record Number-Like
        - **Description**: Column to use for the average
    - **Number of Rows**:
        - **Type**: Integer
        - **Description**: How many previous rows to average
- **Editable?**: No
- **PostgreSQL Mapping**: We need to write a custom function.

# Percentage Change
Shows the percentage changed from the previous value in the row.

- **Date Type**: Decimal
- **Variables Accepted**:
    - **Column*:
        - **Type**: Single Record Number-Like
        - **Description**: Column to check changes
- **Editable?**: No
- **PostgreSQL Mapping**: We need to write a custom function.

# Percentile
Shows the percentile of the current value compared to all values in the column.

- **Date Type**: Decimal
- **Variables Accepted**:
    - **Column*:
        - **Type**: Single Record Number-Like
        - **Description**: Column to check
- **Editable?**: No
- **PostgreSQL Mapping**: We need to write a custom function.

# Running Total
Shows the running total of all values in the column so far.

- **Date Type**: Same as input column
- **Variables Accepted**:
    - **Column*:
        - **Type**: Single Record Number-Like
        - **Description**: Column to check
- **Editable?**: No
- **PostgreSQL Mapping**: We need to write a custom function.
