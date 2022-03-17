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

This document specifies the design for a visual query builder named `Data Explorer` within the Mathesar application. Through `Data Explorer`, users will be able to analyze data across one or multiple tables of a schema and save the resulting tables as views.

Additionally, users will be able to open existing views in `Data Explorer`, as long as its query commands and functions are supported.

## Scenarios

## 1. Selecting the Base Table

The base table selection is the first step when starting a new query, and it will determine which columns and links are available for selection.

The base table also determines the automatic joins that are performed when the user adds columns from linked tables.

### Changing the base table

Once the input table has been created, changing the base table will result in the loss of all progress.

### 1.1 Base Table Options

The base table selector will display a list of all available tables in the current schema. Initially, this list will not include views which will be added in later iterations.

To select a table, the user will find it on the list and click on the desired table option.

Selecting the base table will enable the interface controls for adding additional steps, which were initially disabled. No action is available before a base table is selected.

Once a selection has been made, the user will be prompted to proceed with the input table configuration, starting with column selection.

[BASE TABLE SELECT WIREFRAME]

## 2. Creating the Input Table

The input table is created by selecting columns from the base table or creating new ones via formulas.

Various options are available for input columns, including filters or aggregations that can help users control which data they want to show and how.

These options can be set for all input columns, including formulas. Some options like aggregations might only be available for columns that link to multiple values. The system will automatically detect this and present the available options to users.

### 2.1. Selecting Input Columns

When selecting input columns, the user can add them using the list controls or drop the columns directly into the result table from the column selector.

The column selector component will display all columns from the base table, as well as columns from any table linked or containing links to the base table.

#### Direct Columns

Direct columns are columns from the base or linked tables that contain the actual stored values, these can be selected directly and added as input columns.

Any non-direct column from the base table that was set as a link in the base table will not be available for selection.

[COLUMN SELECTOR WIREFRAME]

#### Link Columns

Link columns have foreign key constraints and hold the primary key values that link to other tables. These columns aren't selectable as direct columns. Instead, the tables that they link to are represented as expandable list groups. Inside each group, users can select the linked table columns. The join will determine the values.

Link columns can exist in the base table or in other tables as links to the base table. However, the same pattern applies to any link column.

The design should support multiple levels of nesting, depending on how the tables are linked.

[COLUMN SELECTOR WIREFRAME]

### 2.2 Adding Formulas

During column selection, the user can add a new column by using formulas to generate its values. Available formulas will be included as part of the column selector, and dropping them into the result table will prompt users to set the formula settings for the selected formula.

Depending on the selected formula, different settings will be available. Formulas will use the column selector component for settings that require the selection of columns. However, the system only list those with data types accepted by the formula.

[WIREFRAME SHOWING FORMULA COLUMN]

### 2.3 Filtering Input Column Values

All input columns can have filters applied to them in order to retrieve only values that match user-specified criteria. Multiple filters are allowed for each input column.

Filter options will be determined by the data type of the input column.

Filters can be added by clicking on the `Add Filter` option from the input column properties panel or directly from the input table column header menu.

[WIREFRAME SHOWING ACTIVE FILTER ON INPUT COLUMN]

### 2.4 Aggregating Input Column Values

Input columns can be aggregated in cases where a link might be referencing multiple values. In such cases, and based on the data type of the referenced column, the system will add an automatic aggregation. Users can change the aggregation type at any moment.

[WIREFRAME SHOWING AGGREGATED INPUT COLUMN VALUES]

### 2.5 Applying a Formula to an Input Column

Direct input columns can also be transformed into formulas. The available formulas will depend on the input column type.

To transform the input column into a formula, the user will select the `Apply Formula` option in the column header menu.

[WIREFRAME SHOWING CONTEXTUAL MENU AND OPTIONS]

## 3. Transforming the Output Table

The output table refers to the resulting table from all input columns selected and added, including filters and aggregations. Transforming this output can be done by applying output filters and summarizations to the result table.

### 3.1. Filtering the Output Table

Users can filter the output table by selecting any column from the result table and applying filters. The column selector, in this case, will only allow users to select input columns rather than the complete column list from the column selection step.

### 3.2. Summarizing the Output Table

Users can summarize the output table to get an aggregation of the column values grouped by a summary column.

To summarize a table, a user selects the `Summarize` option and sets a summary column. The rest of the columns are automatically assigned an aggregation function which users can change at any point. The aggregations are inferred based on the data type of the output column.

## 4. Previewing the Query Results

WIP

## 5. Saving the Query as a View

WIP

## 6. Troubleshooting and Resolving Errors

WIP
Potential errors and how users might resolve them.

## 7. Alerts and Error Prevention

WIP
Describe situations were users will be alerted, for example, a filter that returns no results, a change to an input column that is not compatible with an output filter or summary etc.

## 8. Data Explorer Onboarding Considerations

WIP
Describe how users will be introduced to the various concepts in data explorer.
