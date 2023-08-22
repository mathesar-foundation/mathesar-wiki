# (c) Text Formulas

These formulas operate on text and text-like types. They are based on [PostgreSQL string functions](https://www.postgresql.org/docs/current/functions-string.html).

# Character Count
Returns number of characters in the text

- **Date Type**: Integer
- **Variables Accepted**:
    - **Text**:
        - **Type**: Single Record Text-Like
        - **Description**: Text to count
- **Editable?**: No
- **PostgreSQL Mapping**: `length` function


# Concatenate
Concatenates two strings together.

- **Date Type**: Text
- **Variables Accepted**:
    - **Text 1**:
        - **Type**: Single Record Text-Like
        - **Description**: First text
    - **Text 2**:
        - **Type**: Single Record Text-Like
        - **Description**: Second text
- **Editable?**: No
- **PostgreSQL Mapping**: `||` operator 

# Contains
Checks if a text contains another text

- **Date Type**: Boolean
- **Variables Accepted**:
    - **Base Text**:
        - **Type**: Single Record Text-Like
        - **Description**: Container text to check
    - **Text**:
        - **Type**: Single Record Text-Like
        - **Description**: Contained text
    - **Case Sensitive?**:
        - **Type**: Boolean
        - **Description**: Whether the checking should be case sensitive
        - **Default Value**, False
- **Editable?**: No
- **PostgreSQL Mapping**: Use `LIKE` operator


# Lowercase
Converts text to lowercase

- **Date Type**: Text
- **Variables Accepted**:
    - **Text**:
        - **Type**: Single Record Text-Like
        - **Description**: Text to convert
- **Editable?**: No
- **PostgreSQL Mapping**: `lower` function

# Overlay
Overlays a string at the specified position with another string

- **Date Type**: Text
- **Variables Accepted**:
    - **Base Text**:
        - **Type**: Single Record Text-Like
        - **Description**: The text that will be processed
    - **Starting Position**:
        - **Type**: Integer
        - **Description**: Starting position of text to be replaced
    - **Overlay Text**:
        - **Type**: Single Record Text-Like
        - **Description**: Text to overlay on the base text 
    - **Count**:
        - **Type**: Integer
        - **Description**: Number of characters to replace
        - **Default Value**, Length of the Overlay Text
- **Editable?**: No
- **PostgreSQL Mapping**: `overlay` function

# Repeat
Repeats a string a given number of times.

- **Date Type**: Text
- **Variables Accepted**:
    - **Text**:
        - **Type**: Single Record Text-Like
        - **Description**: Text to repeat
    - **Number of Repetitions**:
        - **Type**: Integer
        - **Description**: Number of times to repeat the text
- **Editable?**: No
- **PostgreSQL Mapping**: `repeat` function

# Replace
Replaces all occurrences of a substring with another string.

- **Date Type**: Text
- **Variables Accepted**:
    - **Base Text**:
        - **Type**: Single Record Text-Like
        - **Description**: The text that will be processed
    - **Text to be Replaced**:
        - **Type**: Single Record Text-Like
        - **Description**: The substring to replace
    - **Replacement Text**:
        - **Type**: Single Record Text-Like
        - **Description**: Text that will be used as the replacement
- **Editable?**: No
- **PostgreSQL Mapping**: `replace` function

# Reverse
Reverses the text

- **Date Type**: Text
- **Variables Accepted**:
    - **Text**:
        - **Type**: Single Record Text-Like
        - **Description**: Text to reverse
- **Editable?**: No
- **PostgreSQL Mapping**: `reverse` function

# Starts With
Returns a boolean that indicates whether a string starts with another string

- **Date Type**: Boolean
- **Variables Accepted**:
    - **Base Text**:
        - **Type**: Single Record Text-Like
        - **Description**: The text that will be checked
    - **Potential Starting Text**:
        - **Type**: Single Record Text-Like
        - **Description**: The text that is being compared with the beginning of the base text
- **Editable?**: No
- **PostgreSQL Mapping**: `starts_with` function

# Substring
Gets a substring of text at the given position

- **Date Type**: Text
- **Variables Accepted**:
    - **Base Text**:
        - **Type**: Single Record Text-Like
        - **Description**: The text that will be processed
    - **Starting Position**:
        - **Type**: Integer
        - **Description**: Starting position of text to be extracted
        - **Default Value**: 0
    - **Count**:
        - **Type**: Integer
        - **Description**: Number of characters to extract
        - **Default Value**: Length of string - starting position
- **Editable?**: No
- **PostgreSQL Mapping**: `substring` function with this signature: `substring ( string text [ FROM start integer ] [ FOR count integer ] ) → text`


# Title Case
Converts text to title case.

- **Date Type**: Text
- **Variables Accepted**:
    - **Text**:
        - **Type**: Single Record Text-Like
        - **Description**: Text to convert
- **Editable?**: No
- **PostgreSQL Mapping**: `initcap` function

# Trim
Trims characters from the start or end of text (or both).

- **Date Type**: Text
- **Variables Accepted**:
    - **Base Text**:
        - **Type**: Single Record Text-Like
        - **Description**: The text that will be processed
    - **Trim Location**:
        - **Type**: Choice (Options: "Start", "End", "Both")
        - **Description**: Where the trimming will happen
        - **Default Value**: Both
    - **Characters to Trim**:
        - **Type**: Single Record Text-Like
        - **Description**: Characters to trim. The text provided will be treated as a list of characters; they will not be treated as a single word (e.g. `xyz` will trim any of `x`, `y`, and `z`)
        - **Default Value**: Space (` `)
- **Editable?**: No
- **PostgreSQL Mapping**: `trim` function

# Uppercase
Converts text to uppercase

- **Date Type**: Text
- **Variables Accepted**:
    - **Text**:
        - **Type**: Single Record Text-Like
        - **Description**: Text to convert
- **Editable?**: No
- **PostgreSQL Mapping**: `upper` function
