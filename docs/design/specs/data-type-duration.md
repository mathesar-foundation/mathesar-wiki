# Duration Data Type Specs

## Context
Duration data types represent a period of time measured in hours, minutes, and/or seconds.

## Prototype 
!!! warning "Warning"
    This prototype might be outdated due to global component updates. Please refer to the link under 'Setting Options' for an updated version of the shared components.


[Duration Data Type Prototype](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?page-id=3652%3A28432&node-id=3652%3A28433&viewport=1951%2C518%2C0.7335814833641052&scaling=min-zoom&starting-point-node-id=3652%3A28433)

## User Experience
### Scenarios
#### User sets a column to 'Duration' data type
The user can set the column data type to 'Duration' by accessing the 'Data Type Options' in the columns header menu. Depending on whether there are existing values or not, and if they are valid duration values, the outcomes will vary:
If there are valid duration values, the system will convert them to duration types. For example, '120' might become '2:00' if interpreted as total minutes. If there are no valid duration values, the system will discard the existing values and default to an empty cell.

##### Setting Options
The following is an interactive representation of the various options that users can set for this type:
[Duration Type Options](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?page-id=4260%3A37440&node-id=4270%3A41231&viewport=324%2C48%2C0.34&scaling=min-zoom&starting-point-node-id=4270%3A41231&show-proto-sidebar=1)

#### User enters a new 'Duration' data type value
Depending on the duration format configuration, an empty cell will provide a placeholder format indicator such as 'h:mm' when the cell is in an active state. Depending on the format, the user might input a value using the exact format or in the unit values of minutes or seconds. For example, '240' will be formatted as '4:00.'

#### User filters a 'Duration' data type column
Users can filter 'duration' data type columns with the same options as 'Number' data type, and it also allows natural language expressions to be used, such as 'greater than 2 hours.

#### User groups a 'Duration' data type column
Users can group 'duration' data types columns by different duration units such as hours, minutes, or seconds. Users can also apply group by ranges, with the same control used for number types.
[Group by Ranges Control](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?page-id=4154%3A34308&node-id=4154%3A34363&viewport=324%2C48%2C0.51&scaling=min-zoom)

## Review Notes
#### Duration Range Controls
A control to define range duration is introduced as part of this spec. It consists of two select input controls that define both the minimum and maximum time units in which the system will represent duration. So, for example, given a duration of 5400 seconds, where the maximum is hours, and the minimum is minutes, the system will represent the value in the cell as '1h 30m'. If the maximum is also set to hours, then 1.5h should show, allowing users to select single unit formats.
Both the minimum and maximum fields will allow values depending on the state of the other. So, for example, if a minimum is set to hours, then a maximum value of minutes cannot be allowed.
