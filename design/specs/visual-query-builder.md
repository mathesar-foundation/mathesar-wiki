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

This document specifies the design of a visual query builder within the Mathesar application called `Data Explorer`. Users will be able to analyze data across one or more schema tables using 'Data Explorer,' and the results of those queries will be saved as views.

Users will also be able to open existing views in `Data Explorer` if the query commands and functions used to generate them are supported.

Read the [Views Product Spec](https://wiki.mathesar.org/en/product/specs/2022-01-views) for a more in-depth explanation of this feature.

## Scenarios

## 1. Selecting the Base Table

When starting a new query, the first step is to select the base table, which determines which columns and links are available as input columns.

When a user adds columns from linked tables, the base table determines the automatic joins that are performed.

### Changing the base table

The user should choose a base table at the start of the query building process. Changing it after the input columns have been selected will result in the loss of all progress.

A warning should be issued to users so that they are aware of the implications of making this change.

### 1.1 Base Table Options

The base table selector will show a list of all the tables that are currently available in the schema. (At first, this list will not display views. View exploration will be added in later iterations.)

To choose a table, the user must first locate it on the list and then click on the desired table option.

When you select the base table, the interface controls for additional steps (e.g., column selection, filters) that were previously disabled will become available. Before selecting a base table, no action is available.

After making a selection, the user will be prompted to continue with the input column configuration, starting with column selection.

---
Wireframes

[Selecting a Base Table](https://share.balsamiq.com/c/esUftomoFsZiRhZDMYdoPP.png)

[Base Table Selected](https://share.balsamiq.com/c/me5CfGGeX3R35x2otLqbpu.png)

## 2. Creating the Input Table

The input table is built by selecting columns from the base table or by generating new ones using formulas.

Based on the order of selection, these columns are added to the result table. Columns can be renamed by users as they see fit.

The system will name columns by default to indicate their source table and column using the [naming convention](#column-naming-convention).

Some options, such as filters and aggregations, may be available for columns that link to multiple records to help users define which data they want to show and how. The system will automatically detect the type of column and present users with the available options.

### 2.1. Adding Input Columns

To begin adding columns to a query configuration panel, the user must first select the `Add Column` button situated in the `Columns` portion of the query configuration panel. The `Column Selector` component will be displayed in the inspector panel as a result of this action.

The `Column Selector` will display a list of all available columns as well as those already in use, if available. In addition, a complete list of all formulas will be available.

The columns in `Column Selector` are listed in a hierarchical structure based on the links that exist in both directions between the base table and other tables. The icons indicate whether the linked records are a single or multiple record collection.

Links are presented as expandable sections containing the columns from the linked tables.

When adding input columns, the user can add them using the list controls or drop the columns directly into the result table.

---
Wireframes

[Adding Columns](https://share.balsamiq.com/c/oyxTXxqSh8rLqU3JY71DWY.png)

[Added Column](https://share.balsamiq.com/c/7U9yahZtYWX2G5obkyivoz.png)

### 2.2 Input Column Sources

Once the input columns have been added, the user can inspect them by selecting each from the result table or the list of columns in the query configuration panel, respectively. A section titled 'Source' will be included in the details for each column. The source column, table, and links will all be listed in this portion of the panel.

The source will include `Links` only for data sourced via tables connected to or from the base table.

---
Wireframes

[Column Sources](https://share.balsamiq.com/c/ewCxvkjS8VoScKfgb9hFos.png)

### 2.3 Adding Formulas

Formulas are used to generate new columns based on different parameters. To access the list of formulas, the user start the `Add Column` process and selects the option `From Formula` at the top of the inspector panel. Selecting a formula will open a form that users can fill out to determine the values of the new column.

Depending on the selected formula, different settings will be available.
More on formulas and specific details for each will be covered on a separate issue.

Columns generated from formulas will display a formula icon indicator in the column header.

---
Wireframes

[Added Formula](https://share.balsamiq.com/c/vWfJ9sUYWJxed5Zo5WtPGi.png)

### 2.4 Filtering Input Column Values

Columns that link to multiple records can have filters applied to them to retrieve only values that match user-specified criteria. Multiple filters are allowed for each input column.

Filter options will be determined by the data type of the input column.

Filters can be added by clicking on the `Add Filter` option from the query configuration panel or directly from the results table column header menu.

Columns with filters applied will display a filter icon indicator in the column header.

---
Wireframes

[Added Input Filter](https://share.balsamiq.com/c/tK2hZy6FB4zVYpN56ejpBk.png)

### 2.5 Aggregating Input Column Values

In cases where a link may refer to multiple values, input columns can be aggregated. In such cases, the system will perform automatic aggregation based on the data type of the referenced column. Users can change the type of aggregation at any time.

Aggregated columns will have an aggregation icon indicator in the column header.

---
Wireframes

[Added Input Aggregation](https://share.balsamiq.com/c/fNcbvQ1q5xMyni5JxBg3Rc.png)

### 2.6 Applying a Formula to an Input Column

Direct input columns can also be transformed into formulas. The available formulas will depend on the input column type.

To transform the input column into a formula, the user will select the `Apply Formula` option in the column header menu.

---
Wireframes

[Applying a Formula](https://share.balsamiq.com/c/nEzYaNKNTSv9EFwzwtfSof.png)

## 3. Applying Transformations to the Result Table

The result table refers to the resulting table from all input columns selected and added, including filters and aggregations. Transforming this output can be done by applying output filters, sorts, and summarizations to the result table.

### 3.1. Filtering the Output Table

Users can filter the output table by adding a filter step to any column from the result table. The column selector, in this scenario, will only allow users to select input columns rather than the whole column list from the column selection stage.

---
Wireframes

[Output Filter](https://share.balsamiq.com/c/dAVYnp8VnG2r2HzkSZ3rgp.png)

### 3.2. Summarizing the Result Table

The `Summarization` step enables users to generate a summarized version of the result table. When added, the system will group the table values based on a summary column of their choice. The summary can be done using the summary column's exact values or by using the summary column's data type's available grouping options.

To summarize the table, the user selects the `Summarize` option from the result transformations menu and adds the step. Once added, the remaining columns are automatically assigned an aggregation function, which users can change at any time. The data type of the output column is used to infer aggregates.

---
Wireframes

[Output Summarization](https://share.balsamiq.com/c/rPMwwETnuQ8a4ut8NfmcDB.png)

[Summarization Options](https://share.balsamiq.com/c/x2iwVBT3NwzmKyhnxSiJku.png)

### 3.3 Sorting the Output Table

Users can sort the output table by applying a sort to any of the result table columns.

To sort the table, the user selects the `Sort` option from the result transformations menu and adds it to the list. Once added, the user can set a column and a direction for the sort.

---
Wireframes

[Output Sorting](https://share.balsamiq.com/c/8TYP1XNz49tS7hHqujMmqS.png)

### 3.4 Adding a New Column to a Summarized Table

If the result table has transformations applied, new columns will be added automatically to the summarization steps and an aggregation set by default.

---
Wireframes

[Adding New Column](https://share.balsamiq.com/c/kWyvRL822BdBubhT4ghzgA.png)

## 4. Deleting a Result Transformation Step

To delete a result transformation step, the user can click on the `Delete` button present in each step item. Deleting a step means that the system will undo all transformations made through that step, and the result table will reflect the updated output.

In circumstances where subsequent steps rely on columns resulting from a deleted step, the system will display error warnings for every failed step. The table output will only reflect the output generated by those stages without errors.

---
Wireframes

[Deleting a Transformation Step](https://share.balsamiq.com/c/XeNAKGz1UnDMfscSTLDVp.png)

## 5. Previewing the Query Results

A preview, or query result table, should be visible while the user is in `Data Explorer`. The result table will change based on the different configurations, for example, if a user applies a filter, the system should refresh the table to show the output with the filter applied.

## 6. Saving the Query as a View

Under `Save Options`, the user can name the resulting query and choose to save it. This would save the view as a query that would be run every time the user opens it.

## 6. Troubleshooting and Resolving Errors

### The result table has no rows

The result table could be empty if a filter returns no results or if the base table is empty. Since queries will run every time the user opens a view, it is possible that the data has changed or that the filter condition returns no results.

Providing a count of rows and columns from the original base table would eliminate confusion around the data source (the table is not empty).

Additionally, users should be able to identify which input columns are filtered, see the applied criteria for each filter and remove the filters if needed.

### There are duplicate values

If a user adds a column with multiple records without an aggregation, values from other columns will be duplicated. Adding aggregations by default for columns with multiple records would help users discover this functionality.

The system can determine the aggregation formula based on the column's data type.

### An input column used in a formula has been deleted

If a user deletes an input column utilized in a formula, then that formula column needs to display the error and prompt the user to resolve it. The user can simply replace the affected column with another one or delete the formula column.

## 7. Other Considerations

### Column Naming Convention

Input column names, when constructed, should have generated names that reference the source of the columns. For example, a column `full_name` from the `Person` table, linked by the column `actor_id` in `Movie` would be named `movie_actor full_name`.

In cases when the column names fit the patterns employed in Mathesar, we might detect unnecessary suffixes like `id` and strip them out for shortening the names (e.g. `sequel title` instead of `sequel_id title`).

Additionally, link hierarchy can be included. For example `sequel_prequel_sequel title` for a column named `title` added through Movie's `sequel_id`'s `prequel_id`'s `sequel_id`.

Users can alter the default names at any time and still see the source information under the column details.
