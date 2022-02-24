---
title: (b) Random Generators
description: 
published: true
date: 2022-02-24T18:31:17.180Z
tags: 
editor: markdown
dateCreated: 2022-02-23T01:43:47.593Z
---

These formulas generate random data.

# Random Number

- **Data Type**: Integer or Decimal, depending on variable.
- **Description**: Generates a random number based on supplied parameters.
- **Variables Accepted**:
    - **Lower Bound**:
        - **Type**: Decimal
        - **Description**: The lower bound for the random generator.
        - **Default Value**: 0.0
    - **Upper Bound**:
        - **Type**: Decimal
        - **Description**: The upper bound for the random generator.
        - **Default Value**: 1.0
    - **Allow Decimals?**:
        - **Type**: Boolean
        - **Description**: Whether to allow generation of decimals.
        - **Default Value**: TRUE
- **Date Editable?**: No

## Implementation
We should build a custom function using the `random()` PostgreSQL function. 

[Docs are here](https://www.postgresql.org/docs/current/functions-math.html), see Table 9.6.

# Random UUID

- **Data Type**: UUID
- **Description**: Generates a random UUID
- **Variables Accepted**: None
- **Date Editable?**: No

## Implementation
The `gen_random_uuid()` PostgreSQL function. 

[Docs are here](https://www.postgresql.org/docs/current/functions-uuid.html).