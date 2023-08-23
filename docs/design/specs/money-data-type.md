# Money Data Type Specs

## Context

Money Data Types allow users to manage monetary values, preceded by a currency symbol of their choice.

## Prototype

> This prototype might be outdated due to global component updates. Please refer to the link under 'Setting Options' for an updated version of the shared components.
{.is-warning}

[Figma Prototype for Money Data Type](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?page-id=3380%3A23047&node-id=3380%3A23048&viewport=-1070%2C505%2C0.4795173108577728&scaling=contain&starting-point-node-id=3380%3A23048)

## User Experience

### Scenarios

#### The user sets the type of a column with existing values to 'Money.'

The user opens the menu for the desired column and selects the 'Data Type Options' menu item. From the list, they can set the type to money. Under advanced options, the user may set the currency and decimal places.

##### Setting Options

The following is an interactive representation of the various options that users can set for this type:
[Money Type Options](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?page-id=4260%3A37440&node-id=4270%3A40881&viewport=324%2C48%2C0.21&scaling=contain&starting-point-node-id=4270%3A40881&show-proto-sidebar=1)

#### The user filters a 'Money' data type column

The user can choose from multiple filter options to filter monetary values. The options will be the same as those used for numeric types.

#### The user groups a 'Money' data type column

The user might also choose to group the data based on the values of the 'Money' data type column.

## Review Notes

- For the MVP we'll assume the number locale format based on the selected currency. Eventually we can add options so that, for example, US dollars can be displayed with dot separators instead of commas. 
- All locales will be included whenever there's a locale-related option.

### Update 23 Feb 2022

#### Compatibility with Postgres Money Type

Mathesar will allow users to view columns set to Postgres money type as a money type column. However, it will not allow users to set an existing column to Postgres money data type. To change from Postgres money data type to the custom Mathesar money type, the user would have to set the column to Number or other data type and then choose money again.

##### Postgres Money Type Prototype

[Figma Prototype - Postgres Money Type](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?page-id=7552%3A83433&node-id=7646%3A84762&viewport=241%2C48%2C0.33&scaling=contain)

#### Support for Multi-Currency through custom Mathesar Money Type

Mathesar's custom money data type will allow users to set any currency and customize various display options. The custom money data type will be the only money type option that can be set in Mathesar. With Postgres money type being available only for existing database columns set to this type.

##### Custom Mathesar Money Type Prototype

[Figma Prototype - Custom Mathesar Money Type](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?page-id=7552%3A83433&node-id=7590%3A84021&viewport=241%2C48%2C0.46&scaling=contain)

##### Scenario: A user sets a field to money data type

- The user sets a column type to `Money.`
- The user opens the data type menu and goes to the `Display` section.
- The user sees the default currency selected and [additional options](#currency-format-options) are displayed.
- Changing any of the default options for a currency will set the currency to custom. For example, changing the symbol for US dollar from `$` to `USD`.
- Changing to any other currency will update the values of the formatting options to those corresponding to the currency.

##### Currency Format Options

- Select Currency Symbol: Users can set the symbol that will be displayed along with the number.
- Symbol Location: Users can select the position for the currency symbol. The options are 'Beginning' or 'End'.
- Decimal Symbol: Options are '.' or ','
- Digit Grouping: Options are '123456789','123,456,789','123456,789' or '12,34,56,789'
- Digit Grouping Symbol: Options are 'none','thin space','.' or ','
