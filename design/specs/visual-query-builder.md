---
title: Visual Query Builder
description: 
published: true
date: 2022-03-08 18:02:53
tags: 
editor: markdown
dateCreated: 2022-03-08 18:02:58
---

## Context

This document specifies the design for a visual query builder named `Data Explorer` within the Mathesar application. Through using `Data Explorer`, users will be able to analyze data across one or multiple tables of a schema and save the result of those queries as views.

Additionally, users will be able to open existing views in `Data Explorer`, as long as the query commands and functions used to generate it are supported.

## Scenarios

## 1. Selecting the Base Table

The base table selection is the first step when starting a new query, and it will determine which columns and links are available as input columns.

The base table also determines the automatic joins that are performed when the user adds columns from linked tables.

### Changing the base table

The user should make base table selection at the start of the query building progress. Changing it after input columns have been selected will clear all progress.
A warning should be given to users so that they understand the consequences of making this change.

### 1.1 Base Table Options

The base table selector will display a list of all available tables in the current schema (Initially, this list will not show views. Exploration of views will be added in later iterations.)

To select a table, the user will find it on the list and click on the desired table option.

Selecting the base table will enable the interface controls for additional steps (e.g., column selection, filters), which were initially disabled. No action is available before a base table is selected.

Once a selection has been made, the user will be prompted to proceed with the input columns configuration, starting with column selection.

---
Wireframes

[Selecting a Base Table](https://share.balsamiq.com/c/esUftomoFsZiRhZDMYdoPP.png)

[Base Table Selected](https://share.balsamiq.com/c/me5CfGGeX3R35x2otLqbpu.png)

## 2. Creating the Input Table

The input table is created by selecting columns from the base table or creating new ones via formulas.

These columns are added to the result table based on the selection order. Users can rename columns as they wish.

By default, the system will name columns to indicate their source table and column according to the following [naming convention](#column-naming-convention).

Some options might be available for columns that link to multiple records, like filters and aggregations to help users define which data they want to show and how. The system will automatically detect the type of columns and present the available options to users.

### 2.1. Adding Input Columns

To start adding columns, the user clicks on the `Add Column` button located in the `Columns` section on the query configuration panel. This action will display the `Column Selector` component in the inspector panel.

The `Column Selector` will list all available columns and those in use, when applicable. Additionally, there will be a list of all formulas.

The columns in `Column Selector` are listed in a hierarchical structure based on the links that exist between the base table and other tables in both directions. Icons indicate whether the linked records are single or multiple.

Links are presented as expandable sections containing the columns from the linked tables.

When adding input columns, the user can add them using the list controls or drop the columns directly into the result table.

---
Wireframes

[Adding Columns](https://share.balsamiq.com/c/oyxTXxqSh8rLqU3JY71DWY.png)
[Added Column](https://share.balsamiq.com/c/7U9yahZtYWX2G5obkyivoz.png)

### 2.2 Adding Formulas

Formulas are used to generate new columns based on different parameters. A list of formulas is included as part of the column selector. Selecting a formula will open a form that users can fill out to determine the values of the new column.

Depending on the selected formula, different settings will be available.
More on formulas and specific details for each will be covered on a separate issue.

---
Wireframes

[Added Formula](https://share.balsamiq.com/c/vWfJ9sUYWJxed5Zo5WtPGi.png)

### 2.3 Filtering Input Column Values

Columns that link to multiple records can have filters applied to them to retrieve only values that match user-specified criteria. Multiple filters are allowed for each input column.

Filter options will be determined by the data type of the input column.

Filters can be added by clicking on the `Add Filter` option from the query configuration panel or directly from the results table column header menu.

---
Wireframes

[Added Input Filter](https://share.balsamiq.com/c/tK2hZy6FB4zVYpN56ejpBk.png)

### 2.4 Aggregating Input Column Values

Input columns can be aggregated in cases where a link might be referencing multiple values. In such cases, and based on the data type of the referenced column, the system will apply an automatic aggregation. Users can change the aggregation type at any moment.

[Added Input Aggregation](https://share.balsamiq.com/c/fNcbvQ1q5xMyni5JxBg3Rc.png)

### 2.5 Applying a Formula to an Input Column

Direct input columns can also be transformed into formulas. The available formulas will depend on the input column type.

To transform the input column into a formula, the user will select the `Apply Formula` option in the column header menu.

[Applying a Formula](https://share.balsamiq.com/c/nEzYaNKNTSv9EFwzwtfSof.png)

## 3. Transforming the Output Table

The output table refers to the resulting table from all input columns selected and added, including filters and aggregations. Transforming this output can be done by applying output filters, sorts, and summarizations to the result table.

### 3.1. Filtering the Output Table

Users can filter the output table by selecting any column from the result table and applying filters. The column selector, in this case, will only allow users to select input columns rather than the complete column list from the column selection step.

[Output Filter](https://share.balsamiq.com/c/dAVYnp8VnG2r2HzkSZ3rgp.png)

### 3.2. Summarizing the Output Table

Users can summarize the output table to get an aggregation of the column values grouped by a summary column.

To summarize the table, the user selects the `Summarize` option from the result transformations menu and chooses a summary column. The rest of the columns are automatically assigned an aggregation function which users can change at any point. The aggregations are inferred based on the data type of the output column.

[Output Summarization](https://share.balsamiq.com/c/rPMwwETnuQ8a4ut8NfmcDB.png)

### 3.3 Sorting the Output Table

Users can sort the output table by applying a sort to any of the result table columns.

To sort the table, the user selects the `Sort` option from the result transformations menu and adds it to the list. Once added, the user can set a column and a direction for the sort.

[Output Sorting](https://share.balsamiq.com/c/8TYP1XNz49tS7hHqujMmqS.pngs)

### 3.4 Adding a New Column to a Summarized Table

If the result table has transformations applied, new columns will be added automatically to the summarization steps and an aggregation set by default.

[New Column](https://share.balsamiq.com/c/kWyvRL822BdBubhT4ghzgA.png)

## 4. Previewing the Query Results

A preview, or query result table, should be visible while the user is in `Data Explorer`. The result table will change based on the different configurations, for example, if a user applies a filter, the system should refresh the table to show the output with the filter applied.

## 5. Saving the Query as a View

Under `Save Options`, the user can name the resulting query and choose to save it. This would save the view as a query that would be run every time the user opens it.

## 6. Troubleshooting and Resolving Errors

### The result table has no rows

The result table might be empty if a filter returns no values or if the base table is empty. Since queries will run every time the user opens a view, it is possible that the data has changed or that the filter criteria returns no matches.

Providing a count of rows and columns from the original base table would eliminate confusion around the data source (the table is not empty).

Additionally, users should be able to identify which input columns are filtered, see the applied criteria for each filter and remove the filters if needed.

### There are duplicate values

If a user adds a column with multiple records without an aggregation, values from other columns will be duplicated. Adding aggregations by default for columns with multiple records would help users discover this functionality.

The system can determine the aggregation formula based on the column's data type.

## 7. Other

### Column Naming Convention

As they are added to the query, columns should include source references as part of their names.

In cases where the column names match the patterns applied in Mathesar, we could detect redundant suffixes like `id` and strip them off for shortening the names (e.g. `sequel title` instead of `sequel_id title`).

Additionally, link hierarchy can be inclided. For example `sequel_prequel_sequel title` for a column named `title` added through Movie's `sequel_id`'s `prequel_id`'s `sequel_id`.

Users can change the default names at any time and still get the source information under the column details.
