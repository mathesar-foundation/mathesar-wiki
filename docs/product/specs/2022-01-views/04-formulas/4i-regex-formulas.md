# (i) Regular Expression Formulas

These formulas use regular expressions. They are based on [PostgreSQL string functions](https://www.postgresql.org/docs/current/functions-string.html).

## Match
Returns the first text that matches a given regular expression.

- **Date Type**: Text
- **Variables Accepted**:
    - **Text**:
        - **Type**: Single Record Text-Like
        - **Description**: The text that will be checked
    - **Pattern**:
        - **Type**: Regular Expression
        - **Description**: The regular expression pattern that's being used to match
- **Editable?**: No
- **PostgreSQL Mapping**: `regexp_match` function

## Matches
Returns all matches in a text that matches a given regular expression.

- **Date Type**: List
- **Variables Accepted**:
    - **Text**:
        - **Type**: Single Record Text-Like
        - **Description**: The text that will be checked
    - **Pattern**:
        - **Type**: Regular Expression
        - **Description**: The regular expression pattern that's being used to match
- **Editable?**: No
- **PostgreSQL Mapping**: `regexp_matches` function

## Replace
Replaces matches of a given pattern with the replacement text.

- **Date Type**: Text
- **Variables Accepted**:
    - **Text**:
        - **Type**: Single Record Text-Like
        - **Description**: The text that will be checked
    - **Pattern**:
        - **Type**: Regular Expression
        - **Description**: The regular expression pattern that's being used to match
    - **Replacement Text**:
        - **Type**: Text
        - **Description**: The text that is replacing the pattern
    - **Number of Replacements**:
        - **Type**: Choice (first or all)
        - **Description**: Whether to replace all matches or just the first match
        - **Default Value**: first
- **Editable?**: No
- **PostgreSQL Mapping**: `regexp_replace` function

## Split
Splits text into a list using a regular expression as the delimiter

- **Date Type**: List
- **Variables Accepted**:
    - **Text**:
        - **Type**: Single Record Text-Like
        - **Description**: The text that will be split
    - **Pattern**:
        - **Type**: Regular Expression
        - **Description**: The regular expression pattern that will be used as the delimiter
- **Editable?**: No
- **PostgreSQL Mapping**: `regexp_split_to_array` function
