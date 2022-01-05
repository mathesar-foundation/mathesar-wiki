---
title: Data Types
description: About Data Types in Mathesar
published: true
date: 2022-01-05T22:24:08.567Z
tags: 
editor: markdown
dateCreated: 2022-01-05T18:05:57.778Z
---

# About

A **data type** is an attribute of a column in a [Table](/product/concepts/tables). It describes the kind of data that can be stored by a record in that column. Examples of data types include text, number, date, email address, etc.

## Data Types in Mathesar
There are two kinds of data types within Mathesar:
- **Database Types**: These are the data types used under the hood by PostgreSQL (the database management software that Mathesar uses).
- **Mathesar Data Types**: These are "friendly" data types aimed at simplifying the choices a non-technical user needs to make. A single Mathesar data type might map to several database types or just one.

Some Mathesar data types such as emails and URLs require custom database types to be installed in order to be available for use. This will be covered in installation instructions for Mathesar users once they are written.

All [Table](/product/concepts/tables) columns have a data type in Mathesar. By default, we use the text data type since it has the least restrictions.

# Usage
- We recommend that you take the time to set the correct data type for each of your columns to help ensure data quality.
   - For example, if you're storing dates in a column, setting the column to the `DATE` database type will ensure that everything saved in that column is a real date. You'll be able to spot typos before they get saved. 
- Columns of different data types supports different filters and groups based on the kind of data stored. For example, you can group columns storing dates by month and filter columns storing emails by the domain of the email address.

# Future Plans
In the future, users will be able to plug in their own data types into Mathesar.

# Resources
- [Code-focused wiki page on Mathesar data types](/engineering/architecture/mathesar-types)
- [PostgreSQL documentation for data types](https://www.postgresql.org/docs/current/datatype.html).