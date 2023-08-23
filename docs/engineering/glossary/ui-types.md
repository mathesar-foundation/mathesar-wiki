# UI Data Types

Please see the ["Data Types" product concept page](/product/concepts/data-types) for more information about the idea behind UI data types (a.k.a. "UI types" for brevity).

## Goals
The main goal of the UI Data Type system is to create a better user experience for non-technical users on the frontend. We aim to do this by:
- **Making data types understood in simple, non-technical terms.**
  - e.g. users should not need to know or think about what a `DOUBLE PRECISION` is in order to set their column to accept decimal numbers.
- **Reducing cognitive load while picking a data type.**
  - A user should not need to look through every single data type to figure out how to set up their column. Setting up their column involves both data integrity and a consistent set of database operations.
  - e.g. if a user knows their data is numeric, they shouldn't have to look through every data type to figure out which ones are numeric and how they're different.

We'd like to minimize the number of UI Types so that the user can first make a decision about which UI Type to use and then adjust the parameters within that type to change the underlying PostgreSQL type if needed.

## Implementation
A Mathesar type can be thought of as a set of one or more PostgreSQL data types. Every PostgreSQL type should be mapped to exactly one UI type, but a UI type can be mapped to many PostgreSQL types.

Mathesar types are an abstraction only applicable to frontend clients, they should not be considered in any operations at the backend or database level. For example, filtering, sorting, and grouping operations happen using PostgreSQL types, not UI types.

UI types are defined in the backend instead of the frontend for two reasons:
- to enable alternate clients that play well with the abstractions we use for the "official" frontend
- to enable users to extend the type system by installing types in the backend and automatically getting the user experience offered by the frontend without having to write frontend code.

### Criteria to Define UI Types
We will need to extend the Mathesar type system over time as we support more data types. When doing so, we should follow these criteria for what PostgreSQL types can be grouped into a single UI type. These criteria assume that you have selected a set of PostgreSQL types and are now wondering whether they make sense together as a UI type:

- The set of types as a whole should be able to be described by a simple concept (e.g. **Number**, **Text**, **Date & Time**, **Email**)
- There should be a reasonable *default* type that can be picked from the set so that users can only pick a UI type and have the default database type apply. Applying the default database type should not cause any loss of data.
  - e.g. the **Number** UI type's default is `NUMERIC`, since it's general enough to cover most use cases.
  - e.g. the **Date & Time** UI type's default is `TIMESTAMP WITH TIME ZONE`, since it preserves all information.
- It should be possible to cast data between all PostgreSQL data types in the set.
- The types in the set should support the exact same filters and groups.

### List of UI Data Types
Current mapping of UI data types to PostgreSQL types.

We'll expand these over time as we support advanced functionality for more types in Mathesar.

| UI Data Type | PostgreSQL Data Type | Default | Notes |
|-|-|-|-|
| **Number** | `NUMERIC`, `SMALLINT`, `INTEGER`, `BIGINT`, `DECIMAL`, `REAL`, `DOUBLE PRECISION` | `NUMERIC` |  |
| **Percent** | `MATHESAR_TYPES.PERCENT` | `MATHESAR_TYPES.PERCENT` | Custom type implemented as domain around `DOUBLE PRECISION` |
| **Text** | `VARCHAR`, `CHAR`, `TEXT` | `TEXT` | |
| **Date** | `DATE` | `DATE` | |
| **Time** | `TIME WITH TIME ZONE`, `TIME WITHOUT TIME ZONE` | `TIME WITHOUT TIME ZONE` | |
| **Date & Time** | `TIMESTAMP WITH TIME ZONE`, `TIMESTAMP WITHOUT TIME ZONE` | `TIMESTAMP WITH TIME ZONE` | |
| **Duration** | `INTERVAL` | `INTERVAL` | |
| **Boolean** | `BOOLEAN` | `BOOLEAN` | |
| **Money** | `MATHESAR_TYPES.MONEY`, `MONEY` | `MATHESAR_TYPES.MONEY` if installed, else `MONEY` | `MATHESAR_TYPES.MONEY` is a custom type |
| **Email** | `MATHESAR_TYPES.EMAIL` | `MATHESAR_TYPES.EMAIL` |  |
| **URL** | `MATHESAR_TYPES.URI` | `MATHESAR_TYPES.URI` | Custom type |
| **List** | [PostgreSQL Arrays](https://www.postgresql.org/docs/13/arrays.html) (single dimension only) | `VARCHAR[]` | We should support all database and display options for whatever data type that the array is set to. |
| **Other** | `SMALLSERIAL`, `SERIAL`, `BIGSERIAL`, `BYTEA`, `POINT`,`LINE`,`LSEG`,`BOX`,`PATH`,`PATH`,`POLYGON`, `CIRCLE`, `CIDR`, `INET`, `MACADDR`, `MACADDR8`, `BIT`, `BIT VARYING`, `TSQUERY`, `TSVECTOR`, `JSON`, `JSONB`, `XML`, `PG_LSN`, `PG_SNAPSHOT`, `TXID_SNAPSHOT`, `INT4RANGE`, `INT8RANGE`, `NUMRANGE`, `TSRANGE`, `TSTZRANGE`, `DATERANGE`, multidimensional arrays, any other type that's detected in the DB | N/A, cannot be set at the moment. | These types are native PostgreSQL data types that we don't support any advanced functionality for yet. |

### Custom Types
Some common data types used by users (e.g. emails, URLs, etc.) do not have native PostgreSQL equivalents. For these data types, Mathesar ships with custom PostgreSQL types that users can install if they want.

## Further Reading
- The [Global Data Type Components design spec](/design/specs/global-data-type-components) shows the user experience of UI Data Types and PostgreSQL types in the UI.
- ["Mathesar Data Types definition" on GitHub Discussions](https://github.com/centerofci/mathesar/discussions/959)
