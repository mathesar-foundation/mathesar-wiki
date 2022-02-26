---
title: (d) Number Formulas
description: 
published: true
date: 2022-02-26T00:06:18.605Z
tags: 
editor: markdown
dateCreated: 2022-02-25T02:36:20.010Z
---

These formulas operate on text and text-like types. They are based on PostgreSQL [mathematical functions and operators](https://www.postgresql.org/docs/9.1/functions-math.html) and [comparison operators](https://www.postgresql.org/docs/9.1/functions-comparison.html).

# Absolute Value
Returns the absolute value of the provided number.

- **Date Type**: Number
- **Variables Accepted**:
    - **Number**:
        - **Type**: Single Record Number-Like
        - **Description**: Input number
- **Editable?**: No
- **PostgreSQL Mapping**: `abs()` function or `@` operator

# Add
Adds two numbers together.

- **Date Type**: Number
- **Variables Accepted**:
    - **Number 1**:
        - **Type**: Single Record Number-Like
        - **Description**: First number
    - **Number 2**:
        - **Type**: Single Record Number-Like
        - **Description**: Second number
- **Editable?**: No
- **PostgreSQL Mapping**: `+` operator 


# Ceiling
Returns the ceiling (nearest integer greater than or equal to) of the provided number.

- **Date Type**: Number
- **Variables Accepted**:
    - **Number**:
        - **Type**: Single Record Number-Like
        - **Description**: Input number
- **Editable?**: No
- **PostgreSQL Mapping**: `ceil` or `ceiling` function.

# Comparison
Compares two numbers and returns the result

- **Date Type**: Boolean
- **Variables Accepted**:
    - **Number 1**:
        - **Type**: Single Record Number-Like
        - **Description**: First number
    - **Number 2**:
        - **Type**: Single Record Number-Like
        - **Description**: Second number
    - **Comparison**:
        - **Type**: Choice (choices: `>`, `>=`, `=` `!=`, `<=`, `<`)
        - **Description**: Comparison to use
- **Editable?**: No
- **PostgreSQL Mapping**: `>`, `>=`, `=` `!=`, `<=`, `<` operators

# Cube Root
Returns the cube root of the provided number.

- **Date Type**: Number
- **Variables Accepted**:
    - **Number**:
        - **Type**: Single Record Number-Like
        - **Description**: Input number
- **Editable?**: No
- **PostgreSQL Mapping**: `cbrt()` function or `||/` operator

# Divide
Divides a number by another number.

- **Date Type**: Number
- **Variables Accepted**:
    - **Number**:
        - **Type**: Single Record Number-Like
        - **Description**: Number to divide
    - **Number to Divide By**:
        - **Type**: Single Record Number-Like
        - **Description**: Number to divide by
- **Editable?**: No
- **PostgreSQL Mapping**: `/` operator. Note that we should convert integers to decimals before dividing.

# Factorial
Returns the factorial of the provided number.

- **Date Type**: Number
- **Variables Accepted**:
    - **Number**:
        - **Type**: Single Record Number-Like
        - **Description**: Input number
- **Editable?**: No
- **PostgreSQL Mapping**: `!` or `!!` operator

# Floor
Returns the floor (nearest integer less than or equal to) of the provided number.

- **Date Type**: Number
- **Variables Accepted**:
    - **Number**:
        - **Type**: Single Record Number-Like
        - **Description**: Input number
- **Editable?**: No
- **PostgreSQL Mapping**: `floor` function.

# Logarithm
Calculate the logarithm of a number.

- **Date Type**: Number
- **Variables Accepted**:
    - **Number**:
        - **Type**: Single Record Number-Like
        - **Description**: Input number
    - **Base**:
        - **Type**: Single Record Number-Like
        - **Description**: Base to use for the logarithm
        - **Default Value**: 10
- **Editable?**: No
- **PostgreSQL Mapping**: `log` function

# Logarithm (Natural)
Calculate the natural logarithm of a number.

- **Date Type**: Number
- **Variables Accepted**:
    - **Number**:
        - **Type**: Single Record Number-Like
        - **Description**: Input number
- **Editable?**: No
- **PostgreSQL Mapping**: `ln` function

# Modulo
Divides a number by another number and returns the remainder

- **Date Type**: Number
- **Variables Accepted**:
    - **Number**:
        - **Type**: Single Record Number-Like
        - **Description**: Number to divide
    - **Number to Divide By**:
        - **Type**: Single Record Number-Like
        - **Description**: Number to divide by
- **Editable?**: No
- **PostgreSQL Mapping**: `%` operator or `mod` function.

# Multiply
Multiplies two numbers together.

- **Date Type**: Number
- **Variables Accepted**:
    - **Number 1**:
        - **Type**: Single Record Number-Like
        - **Description**: First number
    - **Number 2**:
        - **Type**: Single Record Number-Like
        - **Description**: Second number
- **Editable?**: No
- **PostgreSQL Mapping**: `*` operator 

# Power
Calculate the exponent of a number.

- **Date Type**: Number
- **Variables Accepted**:
    - **Number**:
        - **Type**: Single Record Number-Like
        - **Description**: Input number
    - **Power**:
        - **Type**: Single Record Number-Like
        - **Description**: Power to raise the input number to
- **Editable?**: No
- **PostgreSQL Mapping**: `power` function or `^` operator

# Round
Round to a given decimal place.

- **Date Type**: Number
- **Variables Accepted**:
    - **Number**:
        - **Type**: Single Record Number-Like
        - **Description**: Input number
    - **Decimal Place**:
        - **Type**: Integer
        - **Description**: Decimal places to round to
        - **Default Value**: 0
- **Editable?**: No
- **PostgreSQL Mapping**: `round` function 


# Square Root
Returns the square root of the provided number.

- **Date Type**: Number
- **Variables Accepted**:
    - **Number**:
        - **Type**: Single Record Number-Like
        - **Description**: Input number
- **Editable?**: No
- **PostgreSQL Mapping**: `sqrt()` function or `|/` operator

# Subtract
Subtracts a number from another number.

- **Date Type**: Number
- **Variables Accepted**:
    - **Number**:
        - **Type**: Single Record Number-Like
        - **Description**: Number to subtract from
    - **Number to Subtract**:
        - **Type**: Single Record Number-Like
        - **Description**: Number to subtract
- **Editable?**: No
- **PostgreSQL Mapping**: `-` operator 

# Truncate
Truncate to a given decimal place.

- **Date Type**: Number
- **Variables Accepted**:
    - **Number**:
        - **Type**: Single Record Number-Like
        - **Description**: Input number
    - **Decimal Place**:
        - **Type**: Integer
        - **Description**: Decimal places to truncate to
        - **Default Value**: 0
- **Editable?**: No
- **PostgreSQL Mapping**: `trunc` function 
