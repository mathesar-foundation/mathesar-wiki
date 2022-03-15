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

## Starting Points

`Data Explorer` is meant to be a part of multiple flows like the creation of new views, the inspection of existing ones, and as a way to explore data for goals beyond view creation. For this reason, different starting points are considered from which `Data Explorer` might be accessed.

### User opens the Data Explorer to create a new view

#### From Scratch (Top Navigation)

- In the `Schema Browser` view, a user clicks on the `Data Explorer` navigation item located in the top navigation bar.
- `Data Explorer` opens, and the layout changes. The schema explorer sidebar is hidden, as well as any open table.

#### From a Table (Sidebar Navigation or Open Table)

- From an open table, a user clicks the `Create View from [Table Name]` button located in the toolbar. This action will open `Data Explorer` and automatically set the table as `Base Table` and select all direct columns.
- In the `Schema Browser` view, a user opens the contextual menu for a table navigation item and selects `Create view from Table`. This action launches `Data Explorer` and automatically sets the selected table as `Base Table` and adds its direct columns to a `Select Column` step.
- The system will also add link columns if present in the `Base Table`. However, it won't include link columns referencing the `Base Table` from other tables. The system will set the values for link columns to the referenced table's primary key by default.
- The user can then choose to remove or add additional columns.

### User opens the Data Explorer to inspect an existing view

#### From an open view

- From an active view tab, a user can inspect a view by clicking on the `Open in Data Explorer` button in the toolbar area.
- Views need to use supported query commands and functions to be inspected in `Data Explorer` with full functionality. When queries are not supported, an option to see the underlying query will be available.

#### From a view navigation item

- In the `Schema Browser` view, a user opens the contextual menu for a view navigation item and selects the option `Open in Data Explorer`. This action will open `Data Explorer` and display the properties of the selected view.

## Base Table

Views require a base table to be set so that the available columns and links can be listed for selection.

### User sets the base table for a new view

- For users starting a new view from scratch, `Base Table` selection will be the first required step.
- Once `Data Explorer` is launched the user will be prompted to make a selection. The system will list all tables from the active schema. See *Wireframe 1* for an example of the base table selection prompt.
- Once the `Base Table` is selected, a second step for `Select Columns` is automatically added and the user is prompted to continue with the view creation process.
- At this point, the result table is empty.

[Wireframe 1](https://share.balsamiq.com/c/jp7WFu663j6sbfKNknuq5Z.png)

### User inspects the base table for an existing view in Data Explorer

- When inspecting an existing view, a user can find the `Base Table` as the first step of the `Workflow Sidebar`.
- The `Base Table` step cannot be removed, only edited, causing all subsequent steps to be cleared.

[Wireframe 2](https://share.balsamiq.com/c/wTEzQcBamoBBWBSSF5Cmuy.png)

### User opens a view where the base table is missing

- If a user deletes the base table for a view, they should be able to open the view in `Data Explorer` and either resolve the error by replacing the base table with an identical one or clear the workflow and start over.

## Worflow: Column Selection

In the column selection step, users select columns from or linked to the base table of a view.

### User adds a direct column

- Direct columns will be those with values contained directly in the `Base Table` rather than linked from other tables via foreign key relationships.
- To add a direct column, the user can click on the `Add` button inside a `Select Column` workflow item and click on any column listed under the `Base Table Columns` section.
- Direct columns will always be listed at the top of the column list in the same order as the base table.

[Wireframe 3](https://share.balsamiq.com/c/hNWzHEM9ksGGp5ZcPixLrA.png)

### User adds a linked column

- To add a linked column, the user can click on any column listed under the `Base Table Links` or `Linked to Base Table` sections. Linked columns are listed under the tables for which a link to or from the `Base Table` exists.
- The linked column can then be expanded to show all possible values for that field. The default value points to the primary key of the referenced table, however, the user might choose to display values from any other column.

[Wireframe 4](https://share.balsamiq.com/c/hNWzHEM9ksGGp5ZcPixLrA.png)

### User adds multiple select column steps

- Users might want to add more than one `Select Columns` step.
- Take a scenario where formula columns were created for the purpose of using them in other computed columns. The user might want to remove them from the result table. Using an additional select column that follows those `Add Formula Column` steps a user can define the columns to be included.

## Workflow: Add Formula Column

In the `Add Formula Column` step, users apply formulas to generate new columns.

### User adds a formula column

#### From the Worflow Sidebar

- To add a formula column, the user can click on the `Add` button located on top of the `Workflow Sidebar` and select the `Generate Column` option.

[Wireframe 5](https://share.balsamiq.com/c/qYNJBmBwdaTDhn7Hdhf9kP.png)

#### From the result table

- To add a formula column

### User adds a formula column from an existing column

### User deletes a formula column

## Filtering

In the `Filter` step, users apply filters to columns in the result table.

### User adds a filter step

- A user can filter selected columns at any point in the workflow by adding a `Filter` step.
- The filter step will let users select any columns present in the result table until that point, including formula columns if available.
- Once a column is selected, the user will have all the filtering conditions available for each data type. See [Filters Protoype](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?page-id=4612%3A39411&node-id=4612%3A39412&viewport=324%2C48%2C0.23&scaling=contain&starting-point-node-id=4612%3A39412&show-proto-sidebar=1).
- A user might apply multiple filters to the same or other columns in the result table.
- A user can add more than one filter step.

[Wireframe 6](https://share.balsamiq.com/c/t8zJwPzsCvVqsDuAkQSXmk.png)

## Summarization

In the `Summarize` step, users set a summary column and perform aggregations on the result table.

### User adds a summarization step

- A user can summarize the result table at any point in the workflow by adding a `Summarization` step.
- The summarization step will let users set a column as the summary column. By doing so, The system will aggregate the rest of the columns.
- The summary column might or might not be a part of the result table—any formula columns created before the summarization step can be set as a summary column.
- Once a summary column is set, the aggregated columns will be listed, each with a suggested aggregation function. Users can change the suggested functions.
- A user can add more than one summarization step.

[Wireframe 7](https://share.balsamiq.com/c/2e6TYLVzqf4pssmfpNqacx.png)

## Results Table and Previewing

### User previews the result table for all steps

- The result table (preview) by default contains the output of all steps in the workflow sidebar. Changing any of the steps or adding new ones will automatically affect the table's contents.

### User previews the output of a specific step

- Users can temporarily change the preview to show the workflow's output at a particular point.

[Wireframe 8](https://share.balsamiq.com/c/5zwJEcEV7ob2TTwTU3TBgX.png)

### User creates a view from the output of a step

## Layouts

### Data Explorer Layout

The `Data Explorer` layout is optimized for displaying the different steps and results of a query. It cannot be embedded into a modal or shown alongside components from the `Schema Browser` layout like the list of tables or tabs area.

### The Workflow Sidebar

The workflow sidebar contains a list of all the steps needed to produce the result table for a view.

## User Experience

### Step-based query builder

The step-based nature of the query builder will allow users to explore and preview the result table at various intermediate states.

### Data-type specific options

In all cases, where options like filters or formulas are specific to a particular data type, the interface will hide options that don't apply. Users should be able to select from valid options whenever possible.

We do so by...

### Multiple starting points

`Data Explorer` will be a central part of many flows in Mathesar. For that reason, users should be able to launch it under different contexts and understand how to modify or remove any pre-populated steps or settings.

We do so by...

## Interactions

### Workflow

### Autocomplete

### Drag and drop
