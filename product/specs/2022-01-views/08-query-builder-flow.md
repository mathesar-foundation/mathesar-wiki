---
title: 08. Query Builder Flow
description: 
published: true
date: 2022-02-06T00:00:00.270Z
tags: 
editor: markdown
dateCreated: 2022-02-05T23:04:47.283Z
---

> This page is still being written so the information below is incomplete.
{.is-warning}

This page describes the workflow to build a query, to be used during View Creation. 

# Example
To make the flow easier to understand, we'll use the following example schema. Each object below represents a table and an arrow represents a foreign key relationship. The direction represents where the foreign key column is defined.

> We'll use this formatting to follow each step below using this example.
{.is-info}


![movie_schema.png](/movie_schema.png)

# Flow

## Step 1: Selecting the First Column

We will first ask the user to select the first column to start the query. This first column will be used as the main reference column for the rest of the View. 

There are no restrictions at this point, we'll show the user every column from every table.

> Let's assume the user picks the **title** column from the **Movie** table here.
{.is-info}

### Scenario 1a: Filtering the First Column
The user can add relevant filters to the first column after it is selected.

> Let's assume the user only wants to see movies released before 2000 here.
{.is-info}

### Scenario 1b: Applying a Formula to the First Column
The user can apply a relevant formula to the first column after it is selected. We will show formulas that are applicable based on the data type of the column.
- For example, if it is a date column, we might show a formula to extract the year.
- For example, if it is a text column, we might show a substring function.

> Let's assume the user only wants to see movies released before 2000 here.
{.is-info}


## Step 2: Selecting the Second Column

Once the first column has been selected, the user can then pick a second column if desired. The columns available to the user will be restricted based on the choice they made for the first column. We will show:

1. All other columns in the same table as the first column (henceforth called "selected table").
> This means that all remaining columns from the **Movie** table will be available.
{.is-info}
2. If the selected table has any foreign key columns, then we'll show all columns from the tables that the foreign keys point to. 
    - We will follow this down up to three FKs deep.
> This means that all columns from the **Language** table will be available since **Movie** has a FK to **Language**.
{.is-info}

> If **Language** had an FK to another table, we would show those too.
{.is-info}
3. If any tables have FKs pointing to the selected table, we will show all columns from that table.
    - We'll follow those up to three FKs deep as well.
> This means that all columns from the following tables will be available: **Movie Country Map**, **Movie Company Map**, **Movie Genre Map**, **Movie Watch**, **Movie Character**, **Movie Crew**
{.is-info}

> This means that all columns from the following tables will be available: **Country** (through **Movie Country Map**), **Company**( through **Movie Company Map**), **Genre** (through **Movie Genre Map**), **Person** (through both **Movie Character** and **Movie Crew**), and **Crew Role** (through **Movie Crew**).
{.is-info}

> Other cases to handle:
> - tables with FKs to themselves
> - tables with multiple FKs to the same table

Once the user has selected a column, we will show them different options based on the type of column they have selected.

### Scenario 2a: The Same Table

This scenario is related to point 1 above. The user selects a column from the selected table.

> This mean the user has selected a column from **Movie**
{.is-info}

In this scenario, we don't need to ask the user any more questions, we can add the column right away. We can allow them to apply a formula or add a filter similar to the first column.

### Scenario 2b: A FK Related Table

This scenario is related to point 2 above. The user selects a column from table that the selected table has a foreign key relationship to (or a similar relationship up to 3 levels deep).

> This mean the user has selected a column from **Language**
{.is-info}

In this scenario, we also don't need to ask the user any more questions, we can add the column right away. We can allow them to apply a formula or add a filter similar to the first column.

### Scenario 2c: A Reverse FK Related Table

This scenario is related to point 3 above. The user selects a column with a direct reverse foreign key relationship to the selected table.

> This means a user has selected a column from **Movie Country Map**, **Movie Company Map**, **Movie Genre Map**, **Movie Watch**, **Movie Character**, or **Movie Crew** Let's assume it is is **Movie Watch**.
{.is-info}

This means that there could be multiple records related to a single record in the selected table. We need to ask the user how to summarize these records. We can have the following options
- List
- Count

Once the user has selected one of these, we can then add the column. We can allow them to apply a formula or add a filter similar to the first column.

### Scenario 2d: A FK from the Reverse FK Related Table (Only Reachable In One Way)

This scenario is related to point 3 above. The user selects a column with an FK from a table with the direct reverse foreign key relationship to the selected table. This table should only be reachable through one mapping table.

> This means a user has selected a column from **Country**, **Company**, or **Genre**. **Person** doesn't work here since there are 2 mappings to it.
{.is-info}

This means that there could be multiple records related to a single record in the selected table. We need to ask the user how to summarize these records. We can have the following options
- List
- Count

If the mapping table also has additonal fields, we also need to ask the user to specify any filters to figure out what data to summarize.

> See Scenario 2e below for an example.
{.is-info}

Once the user has selected one of these, we can then add the column. We can allow them to apply a formula or add a filter similar to the first column.

### Scenario 2e: A FK from the Reverse FK Related Table (Reachable In Multiple Ways)

This scenario is related to point 3 above. The user selects a column with an FK from a table with the direct reverse foreign key relationship to the selected table. This table can be reached through multiple mapping tables

> This means a user has selected the **Person** column which is reachable through either **Movie Character** or **Movie Crew**.
{.is-info}

Since there are multiple mapping tables associated, we need to ask the user to pick one.

> Imagine the user is creating a "Producers" column that lists all producers of a movie. This means the user will select **Movie Crew** as the mapping table.
{.is-info}

If the mapping table also has additonal fields, we also need to ask the user to specify any filters to figure out what data to summarize.

> Here we see that **Movie Crew** has an additional **role_id** column. We ask the user if they want to add a filter to that column , and they will add a filter that says the **role_id** column has to be the same as the ID of `producer` in **Crew Role**.
{.is-info}

Since there could be multiple records related to a single record in the selected table, we also need to ask the user how to summarize these records. We can have the following options
- List
- Count

Once the user has selected one of these, we can then add the column. We can allow them to apply a formula or add a filter similar to the first column.

### Scenario 2f: A Recursive Reverse FK Related Table

TBD.

## Alternate Step 2: Formula Columns
Instead of adding a column directly, the user should also be able to add a "Formula Column" which involves more than one source column. The flow for that will be different than selecting an existing column.

> This flow is not defined yet.
{.is-danger}
