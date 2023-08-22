# (g) List Formulas

These formulas operate on list types. They are based on PostgreSQL [array functions and operators](https://www.postgresql.org/docs/9.1/functions-array.html) and [row and array comparisons](https://www.postgresql.org/docs/9.1/functions-comparisons.html).

# Append
Adds a list item to a list

- **Date Type**: List
- **Variables Accepted**:
    - **List**:
        - **Type**: Single Record List-Like
        - **Description**: List to add to
    - **Item**:
        - **Type**: Single Record-Like of the data type of the list items
        - **Description**: List item to add
- **Editable?**: No
- **PostgreSQL Mapping**: `||` operator or `array_append` function

# Concatenate
Turns two lists into one big list.

- **Date Type**: List
- **Variables Accepted**:
    - **List 1**:
        - **Type**: Single Record List-Like
        - **Description**: First list
    - **List 2**:
        - **Type**: Single Record List-Like
        - **Description**: Second list
- **Editable?**: No
- **PostgreSQL Mapping**: `||` operator 

# Contains List
Checks if all items in a list are also in another list.

- **Date Type**: Boolean
- **Variables Accepted**:
    - **Container List**:
        - **Type**: Single Record List-Like
        - **Description**: List that contains items to check
    - **Contains List**:
        - **Type**: Single Record List-Like
        - **Description**: List whose items should be contained in the other list
- **Editable?**: No
- **PostgreSQL Mapping**: `@>` operator 

# Contains Item
Checks if a specific item is in a list.

- **Date Type**: Boolean
- **Variables Accepted**:
    - **List**:
        - **Type**: Single Record List-Like
        - **Description**: List that contains items to check
    - **Item**:
        - **Type**: Same as data type of the List
        - **Description**: Item to check
- **Editable?**: No
- **PostgreSQL Mapping**: `IN` construct 

# Overlap
Checks if two lists have any items in common.

- **Date Type**: Boolean
- **Variables Accepted**:
    - **List 1**:
        - **Type**: Single Record List-Like
        - **Description**: First list
    - **List 2**:
        - **Type**: Single Record List-Like
        - **Description**: Second list
- **Editable?**: No
- **PostgreSQL Mapping**: `&&` operator 

# Convert to Text
Converts a list into text.

- **Date Type**: Text
- **Variables Accepted**:
    - **List**:
        - **Type**: Single Record List-Like
        - **Description**: List to turn into text
    - **Delimiter**:
        - **Type**: Text
        - **Description**: What to use to separate list items
        - **Default Value**: `, `
    - **NULL text**:
        - **Type**: Text
        - **Description**: What to show null values as
        - **Default Value**: `` (NULL values will not be shown at all)     
- **Editable?**: No
- **PostgreSQL Mapping**: `array_length` function 

# Length
Returns the count of a list

- **Date Type**: Integer
- **Variables Accepted**:
    - **List**:
        - **Type**: Single Record List-Like
        - **Description**: List to count
- **Editable?**: No
- **PostgreSQL Mapping**: `array_length` function 
