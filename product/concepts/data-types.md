---
title: Data Types
description: About Data Types in Mathesar
published: true
date: 2022-01-05T18:05:57.778Z
tags: 
editor: markdown
dateCreated: 2022-01-05T18:05:57.778Z
---

## Data Types
Each column in a table has an associated data type, which defines the type of data that can be stored.

Mathesar will accurately show the type of data in the user interface to all the native data types that Postgres supports. Users can change the data type of existing columns to any of these types. 

Mathesar also implements some custom types not available in PostgreSQL, as well as some custom filtering and grouping options for existing types. Only types for which we are implementing something custom are documented below; please consult [PostgreSQL documentation for the list of all native types](https://www.postgresql.org/docs/current/datatype.html).

### Native Types
These types are available in PostgreSQL, but have custom grouping options that we'll need to implement or create an interface for.

**All Text Types**
*Custom grouping options*: First letter of text

**All Numeric Types**
*Custom grouping options*: Range

We would like to calculate options for ranges based on the data stored. For example, if the data ranges from 0-100, we might want to offer grouping by 0-10, 10-20, etc., but if it ranges from 0 to 5,000,000,000, we would offer grouping by a different range.

**All Date & Time Types**
*Custom grouping options*: Support all grouping options supported by [the PostgreSQL EXTRACT function](https://www.postgresql.org/docs/current/functions-datetime.html#FUNCTIONS-DATETIME-EXTRACT).

### Custom Types
These types are entirely custom. Note that custom types are not available to use on pre-existing databases unless the user installs them separately.

**Email**
*Custom grouping options*: First letter of email address, email domain

**URL**
*Custom grouping options*: First letter of URL, domain TLD, protocol
