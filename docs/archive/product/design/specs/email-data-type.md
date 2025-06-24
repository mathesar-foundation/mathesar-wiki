# Email Data Type

## Context
Email data types are custom Mathesar data types used to store email addresses. 

## Prototype
!!! warning "Warning"
    This prototype might be outdated due to global component updates. Please refer to the link under 'Setting Options' for an updated version of the shared components.


[Email Data Type Prototype](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?page-id=4260%3A37440&node-id=4270%3A39806&viewport=324%2C48%2C0.34&scaling=min-zoom&starting-point-node-id=4270%3A39806)

## User Experience
### Scenarios
#### User sets a column to 'Email' data type
The user can set the column data type to 'Email' by accessing the 'Data Type Options' in the columns header menu.
Depending on whether there are existing values or not, and if they are valid email values, the outcomes will vary:
If there are valid email values, the system will convert them to email types. A valid email will have a username and domain name joined by a '@' symbol.
If there are no valid email values, the system will discard the existing values and default to an empty cell.

##### Setting Options
The following is an interactive representation of the various options that users can set for this type:
[Email Type Options](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?page-id=4260%3A37440&node-id=4317%3A50925&viewport=324%2C48%2C0.34&scaling=min-zoom&starting-point-node-id=4270%3A39806)

#### User enters a new 'Email' data type value
The user might enter a new email value with a valid format. If the value is not a valid email, an error should be displayed, preventing the row from being saved.

#### User filters an 'Email' data type column
Users can filter 'email' data type columns by regular 'Text' type filters (except for length filters which are exclusive to text types) as well as 'Email' specific filters such as domain name.

#### User groups an 'Email' data type column
Users can group 'email' data types columns by first letter or domain.


### Additional Changes
#### New record row placement
The new record row, originally designed to sit at the bottom of the table, will now be on top. Change is due to confusing placement within groups and compensating for the pagination change impact on the usability of adding new records. 