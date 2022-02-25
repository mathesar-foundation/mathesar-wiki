---
title: Data Types
description: About Data Types in Mathesar
published: true
date: 2022-02-25T02:18:07.141Z
tags: 
editor: markdown
dateCreated: 2022-01-05T18:05:57.778Z
---

# About

A **data type** is an attribute of a column in a [Table](/product/concepts/tables). It describes the kind of data that can be stored by a record in that column. Examples of data types include text, number, date, email address, etc.

Different data types have their own filters, groups, and other functionality available to help you work better with information of that type.

Examples of filtering include:
- numbers based on whether they're greater than `2000`
- dates based on whether they're before or after `today`
- URLs based on whether they're `.com` or `.net`.

Examples of grouping include: 
- text based on first letter (`A`, `B`, `C`, etc.)
- numbers based on ranges (e.g. `1-100`, `101-200`, etc.)
- emails based on domain names (e.g. `gmail.com`, `outlook.com`, etc.)

## Data Types in Mathesar
All [Table](/product/concepts/tables) columns have a data type in the Mathesar UI. By default, we use the text data type since it has the least restrictions, but you can change the data type to anything else. Here's an early design of what selecting a data type will look like:

![screen_shot_2022-01-06_at_2.46.23_pm.png](/assets/product/concepts/data-types/screen_shot_2022-01-06_at_2.46.23_pm.png)

You can pick from a set of options and depending on what option you pick (in this example, it's **Number**), you can choose additional settings to configure your column correctly. These additional settings are optional. 

### Under the hood
Unlike [Databases](/product/concepts/databases), [Schemas](/product/concepts/schemas), [Tables](/product/concepts/tables), and [Views](/product/concepts/views), data types are not a direct representation of the configuration in the database. We've simplified data types within Mathesar to make them easier to use. Based on the settings you choose, we pick the correct underlying data type to use in the database. If you're curious, the underlying database configuration is shown as `Database Type` at the bottom of the menu (seen in the screenshot above)

# Usage
- We recommend that you take the time to set the correct data type for each of your columns to help ensure data quality. For example, if you're storing people's ages in a column, setting the column to the `Number` type will:
   - Ensure that everything saved in that column is a number. You can't accidentally save someone's age as `34b` or `thirty four`.
   - Give you access to operations that work on numbers. You can add up everyone's ages, average them, find all the rows belonging to someone older than `25`, group rows by age groups, and so on.
- **Note to Mathesar administrators**: Some UI data types such as emails and URLs require custom database types to be installed in order to be available for use. This will be covered in installation instructions for Mathesar users once they are written.

# Future Plans
In the future, users will be able to plug in their own data types into Mathesar.

# Resources
- [Code-focused wiki page on UI data types](/engineering/architecture/ui-types)
- [PostgreSQL documentation for data types](https://www.postgresql.org/docs/current/datatype.html).