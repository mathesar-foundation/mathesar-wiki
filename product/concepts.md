---
title: Concepts
description: Glossary of Mathesar terms
published: true
date: 2021-05-07T20:26:53.035Z
tags: 
editor: markdown
dateCreated: 2021-05-07T15:21:44.337Z
---

This page is a reference for concepts related to Mathesar. It is intended to be the primary source of information for how the product is supposed to work.

> This page describes how Mathesar **will** behave. We are still in early development, so most features are not implemented yet.
{.is-warning}

# Databases
At its core, Mathesar provides a friendly user interface to PostgreSQL databases. Mathesar can be configured to provide an interface to multiple databases, but users will only be working with one database at a time.

# Schemas
PostgreSQL schemas are logical groupings (a.k.a. namespaces) of tables, views, and other database objects within databases.

If a user is using Mathesar for a few unrelated applications, we encourage them to have a single database with multiple schemas.

# Tables
PostgreSQL tables are a collection of related data, consisting of columns and rows. All data is stored in tables.

To avoid duplicating data, we encourage users to set up many small tables that are related to each other.

# Views
Views are the result of a stored SQL query on the data stored in tables. Views can involve combining data from multiple tables, filtering, sorting, aggregating (grouping), and so on.

We expect that most users will work with data in views more often than working directly with tables, since users will probably want to see related data from across tables easily.

# Data Types
Each column in a table has an associated data type, which defines the type of data that can be stored.

Mathesar will accurately show the type of data in the user interface to all the native data types that Postgres supports. Users can change the data type of existing columns to any of these types. 

Mathesar also implements some custom types not available in PostgreSQL, as well as some custom filtering and grouping options for existing types. Only types for which we are implementing something custom are documented below; please consult [PostgreSQL documentation for the list of all native types](https://www.postgresql.org/docs/current/datatype.html).

## Native Types
These types are available in PostgreSQL, but have custom grouping options that we'll need to implement or create an interface for.

### All Text Types
*Custom grouping options*: First letter of text

### All Numeric Types
*Custom grouping options*: Range

We would like to calculate options for ranges based on the data stored. For example, if the data ranges from 0-100, we might want to offer grouping by 0-10, 10-20, etc., but if it ranges from 0 to 5,000,000,000, we would offer grouping by a different range.

### All Date & Time Types
*Custom grouping options*: Support all grouping options supported by [the PostgreSQL EXTRACT function](https://www.postgresql.org/docs/current/functions-datetime.html#FUNCTIONS-DATETIME-EXTRACT).

## Custom Types
These types are entirely custom. Note that custom types are not available to use on pre-existing databases unless the user installs them separately.

### Email
**Custom grouping options**: First letter of email address, email domain

### URL
**Custom grouping options**: First letter of URL, domain TLD, protocol

