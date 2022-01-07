---
title: Data Types
description: About Data Types in Mathesar
published: true
date: 2022-01-06T19:59:45.711Z
tags: 
editor: markdown
dateCreated: 2022-01-05T18:05:57.778Z
---

# About

A **data type** is an attribute of a column in a [Table](/product/concepts/tables). It describes the kind of data that can be stored by a record in that column. Examples of data types include text, number, date, email address, etc.

## Data Types in Mathesar
All [Table](/product/concepts/tables) columns have a data type in Mathesar. By default, we use the text data type since it has the least restrictions, but you can change the data type to anything else. Here's an early design of what selecting a data type will look like:

![screen_shot_2022-01-06_at_2.46.23_pm.png](/screen_shot_2022-01-06_at_2.46.23_pm.png)

You can pick from a set of options and depending on what option you pick (in this example, it's **Number**), you can choose additional settings to configure your column correctly. These additional settings are optional. 

### Under the hood
Unlike [Databases](/product/concepts/databases), [Schemas](/product/concepts/schemas), [Tables](/product/concepts/tables), and [Views](/product/concepts/views), data types are not a direct representation of the column's configuration in the database. We've simplified data types within Mathesar to make them easier to use. Based on the settings you choose, we pick the correct underlying data type to use in the database. If you're curious, the underlying database configuration is shown as `Database Type` at the bottom of the menu (seen in the screenshot above)

# Usage
- We recommend that you take the time to set the correct data type for each of your columns to help ensure data quality.
   - For example, if you're storing people's ages in a column, setting the column to the `Number` type will ensure that everything saved in that column is a number.
- Columns of different data types supports different filters and groups based on the kind of data stored. For example, you can group columns storing dates by month and filter columns storing emails by the domain of the email address.
- **Note to Mathesar administrators**: Some Mathesar data types such as emails and URLs require custom database types to be installed in order to be available for use. This will be covered in installation instructions for Mathesar users once they are written.

# Future Plans
In the future, users will be able to plug in their own data types into Mathesar.

# Resources
- [Code-focused wiki page on Mathesar data types](/engineering/architecture/mathesar-types)
- [PostgreSQL documentation for data types](https://www.postgresql.org/docs/current/datatype.html).