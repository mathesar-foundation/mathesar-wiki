---
title: Mathesar Data Types
description: Mapping Mathesar data types to PostgreSQL types
published: true
date: 2022-01-06T16:36:29.453Z
tags: 
editor: markdown
dateCreated: 2022-01-05T22:22:42.669Z
---

Please see the ["Data Types" product concept page](/product/concepts/data-types) for more information about the idea behind Mathesar data types (a.k.a. "Mathesar types" for brevity).

# Goals
The main goal of the Mathesar type system is to create a better user experience for non-technical users. We aim to do this by:
- **Making data types understood in simple, non-technical terms.**
  - e.g. users should not need to know or think about what a `DOUBLE PRECISION` is in order to set their column to accept decimal numbers.
- **Reducing cognitive load while picking a data type.**
  - A user should not need to look through every single data type to figure out how to set up their column.
  - e.g. if a user knows their data is numeric, they shouldn't have to look through every data type to figure out which ones are numeric and how they're different.

We'd like to minimize the number of Mathesar Types so that the user can first make a decision about which Mathesar Type to use and then adjust the parameters within that type to change the underlying PostgreSQL type if needed.

# Implementation
A Mathesar type can be thought of as a set of one or more PostgreSQL data types. Every PostgreSQL type should be mapped to exactly one Mathesar type, but a Mathesar type can be mapped to many PostgreSQL types.

We will need to extend the Mathesar type system over time as we support more data types. When doing so, we should follow these criteria for what PostgreSQL types can be grouped into a single Mathesar type:
- Grouped PostgreSQL types should be able to be described by a single concept (e.g. **Number**, **Text**, **Email**).
- There should be a reasonable *default* type that can be picked from the group of PostgreSQL types so that users can only pick a Mathesar type and have the default database type apply. Applying the default database type should not cause any loss of data.
  - e.g. the **Number** Mathesar type's default is `NUMERIC`, since it's general enough to cover most use cases.
  - e.g. the **Date & Time** Mathesar type's default is `TIMESTAMP`, since it covers data stored in both `DATE` and `TIME`, which are the other data types in the group.

Please note that filtering, sorting, and grouping options are associated with PostgreSQL types, not Mathesar types. For example, `DATE`, `TIME`, and `TIMESTAMP` support different filtering options, even though they are all associated with the **Date & Time** Mathesar type.

## Mapping
Current mapping of Mathesar types to PostgreSQL types.

We'll expand these over time as we support advanced functionality for more types in Mathesar.

| Mathesar Data Type | PostgreSQL Data Type | Notes |
|-|-|-|
| **Number** | `NUMERIC`, `SMALLINT`, `INTEGER`, `BIGINT`, `DECIMAL`, `REAL`, `DOUBLE PRECISION` | Can be displayed as percentages in the UI via display options. |
| **Text** | `VARCHAR`, `CHAR`, `TEXT` | |
| **Date & Time** | `TIMESTAMP WITH TIME ZONE`, `TIMESTAMP WITHOUT TIME ZONE`, `DATE`, `TIME WITH TIME ZONE`, `TIME WITHOUT TIME ZONE` | |
| **Duration** | `INTERVAL` | |
| **Boolean** | `BOOLEAN` | |
| **Money** | `MATHESAR_TYPES.MONEY`, `MONEY` | `MATHESAR_TYPES.MONEY` is a custom type |
| **Email** | `MATHESAR_TYPES.EMAIL` | Custom type |
| **URL** | `MATHESAR_TYPES.URI` | Custom type |
| **Other** | `SMALLSERIAL`, `SERIAL`, `BIGSERIAL`, `BYTEA`, `POINT`,`LINE`,`LSEG`,`BOX`,`PATH`,`PATH`,`POLYGON`, `CIRCLE`, `CIDR`, `INET`, `MACADDR`, `MACADDR8`, `BIT`, `BIT VARYING`, `TSQUERY`, `TSVECTOR`, `JSON`, `JSONB`, `XML`, `PG_LSN`, `PG_SNAPSHOT`, `TXID_SNAPSHOT`, `INT4RANGE`, `INT8RANGE`, `NUMRANGE`, `TSRANGE`, `TSTZRANGE`, `DATERANGE` | These types are native PostgreSQL functionality that we don't support any advanced functionality for yet. |
| **Custom** | *Any type that's detected in the DB but not on the list above lists.* | |

## Custom Types
Some common data types used by users (e.g. emails, URLs, etc.) do not have native PostgreSQL equivalents. For these data types, Mathesar ships with custom PostgreSQL types that users can install if they want.

## Resources
- The [Global Data Type Components design spec](/design/specs/global-data-type-components) shows the user experience of Mathesar Types and PostgreSQL types in the UI.
