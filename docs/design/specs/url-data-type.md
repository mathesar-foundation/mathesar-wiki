# URL Data Type

## Context
URL data types are custom Mathesar data types used to store URLs.

## Prototype 
> This prototype might be outdated due to global component updates. Please refer to the link under 'Setting Options' for an updated version of the shared components.
{.is-warning}

[URL Data Type Prototype](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?page-id=3750%3A28604&node-id=3763%3A30987&viewport=1049%2C-592%2C0.2776779234409332&scaling=contain&starting-point-node-id=3763%3A30987)

## User Experience
### Scenarios
#### User sets a column to 'URL' data type
The user can set the column data type to 'URL' by accessing the 'Data Type Options' in the columns header menu.
Depending on whether there are existing values or not, and if they are valid URL values, the outcomes will vary:
If there are valid URL values, the system will convert them to URL types. For example, a valid URL could be:

`www.website.com`
`http://www.website.com`
`mailto:name@website.com`
`name@website.com`
`www.website.com/?url=has-querystring`

If there are no valid URL values, the system will discard the existing values and default to an empty cell.

##### Setting Options
The following is an interactive representation of the various options that users can set for this type:
[URL Type Options](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?page-id=4260%3A37440&node-id=4270%3A39962&viewport=324%2C48%2C0.34&scaling=min-zoom&starting-point-node-id=4270%3A39962&show-proto-sidebar=1)

#### User enters a new 'URL' data type value
The user might enter a new 'URL' value with a valid format. If the value is not a valid URL, an error should be displayed, preventing the row from being saved.

#### User filters an 'URL' data type column
Users can filter 'URL' data type columns by regular 'Text' type filters (except for length filters which are exclusive to text types) as well as 'URL' specific filters such as hostname.

#### User groups a 'URL' data type column
Users can group 'URL' data types columns by first letter, URI scheme, or URI host.
