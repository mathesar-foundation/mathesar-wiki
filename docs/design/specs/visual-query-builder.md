# Data Explorer

## Context

'Data Explorer,' Mathesar's visual query builder, is described in this document. Users can analyze data, link data from other tables, and transform it using this feature.

### Mathesar Queries vs. SQL Queries

The queries generated in the 'Data Explorer' will be listed and saved as queries within Mathesar. In contrast to standard database queries, "Mathesar queries" are not stored as SQL commands. This Mathesar-specific object was created because otherwise, it would be impossible to reproduce user configurations.

Read the [Views Product Spec](https://wiki.mathesar.org/en/product/specs/2022-01-views) for a more in-depth explanation of this feature.

## Accessing Data Explorer

'Data Explorer' will be accessible in several ways because it is an essential step in numerous user flows.

There are many ways to access 'Data Explorer.' The navigation updates specification goes into detail about each one.

[Updates on the Navigation](/design/specs/navigation-updates#data-explorer)

## Scenarios

## Selecting the Base Table

The base table determines which columns and links are available as input columns. When a user adds columns from linked tables, the base table also determines the automatic joins performed.

### Table Links

Tables can be linked to the base table using foreign keys that can be located in the base table or in other tables. The columns from all linked tables are shown in the column list and grouped according to the corresponding source table.

For each foreign key column, a collapsible list is automatically added to the list. Once expanded, a list of all the columns in the source table is displayed.

#### Join Types

Although SQL has additional join options, the system will restrict joins to 'LEFT JOIN' type alone, in order to simplify things for less technical users and make it easier for them to learn the new concepts.

### Changing the base table

The user should set a base table at the start of the query building process. Changing it after the input columns have been selected will result in losing all progress.

A warning should be issued to users, so they know the implications of making this change.

### Base Table Options

The system will show all schema tables in the base table selector.

To choose a table, the user must first find it in the list and then click on it. They can also use the search box in the table selection menu to locate the table by filtering the list by table name.

After making a selection, the name of the base table is displayed in the selector, and previously disabled interface elements in 'data explorer' become interactive.

After selecting a base table, the user will be directed to the next stage, column selection.

---
Wireframes

[Selecting a Base Table](https://share.balsamiq.com/c/esUftomoFsZiRhZDMYdoPP.png)

[Base Table Selected](https://share.balsamiq.com/c/me5CfGGeX3R35x2otLqbpu.png)

## The Input Table

The input table is built by selecting columns from the base table or generating new ones using formulas.

### Adding Input Columns

To add columns to a query configuration panel, the user must first select the `Add Column` button in the `Columns` portion of the query configuration panel. Due to this action, the `Column Selector` component will be displayed in the inspector panel. The `Column Selector` will display a list of all available columns and those already in use. In addition, a complete list of all formulas will be available.

The columns in `Column Selector` are listed in a hierarchical structure based on the links that exist in both directions between the base table and other tables. The icons indicate whether the linked records are a single or multiple record collection.

Links are presented as nested sections containing the columns from the linked tables.
When adding input columns, the user can add them using the list controls or drop the columns directly into the result table.

#### Column Selection Modes

Depending on the interaction, columns may be selected in a variety of ways:

Selection Mode | Interaction
--- | ---
Single Selection| Click a list item
Drop Single Column| Click and drag list item to drop area
Multiple Selection| Click + Shift Key to select first and all items in between. For non-contiguous items, Click + Control Key.

#### Naming Convention

The system will default name columns to indicate their source table and column using the [naming convention](#column-naming-convention).

#### Columns with Multiple Records

Depending on how tables are linked, some columns might contain multiple records associated with a record in the base table. Specific functionality to manage those records should be available to users.

Functionality | User Goals
--- | ---
Filter| Show only a subset of the linked records
Aggregate| Display the multiple records as a combined record
Display Formats| Change the way each record item is displayed
Sort| Change the order in which the linked records are displayed
Limit| Limit the number of linked records

#### Data Type Changes

When columns are added to the input table, their data type may differ from the source. A 'Text Type' column, for example, will change to a 'Text List Type' or 'Number Type' when added as a multiple record column due to automatic aggregation.

---
Wireframes

[Adding Columns](https://share.balsamiq.com/c/oyxTXxqSh8rLqU3JY71DWY.png)

[Added Column](https://share.balsamiq.com/c/7U9yahZtYWX2G5obkyivoz.png)

### Input Column Sources

Once the input columns have been added, the user can inspect them by selecting each from the result table or the list of columns in the query configuration panel. The panel will include a section titled 'Source' in the details for each column. The source column, table, and links will all be listed in this panel portion.

The source will include `Links` only for data sourced via tables connected to or from the base table.

---
Wireframes

[Column Sources](https://share.balsamiq.com/c/ewCxvkjS8VoScKfgb9hFos.png)

### Adding Formulas

Formulas are used to generate new columns based on different parameters. To access the formulas list, the user starts the `Add Column` process and selects the option `From Formula` at the top of the inspector panel. Selecting a formula will open a form that users can fill out to determine the values of the new column.

Depending on the selected formula, different settings will be available.
More on formulas and specific details for each will be covered in a separate issue. Columns generated from formulas will display a formula icon indicator in the column header.

---
Wireframes

[Added Formula](https://share.balsamiq.com/c/vWfJ9sUYWJxed5Zo5WtPGi.png)

### Filtering Input Column Values

Columns that link to multiple records can have filters applied to them to retrieve only values that match user-specified criteria. Multiple filters are allowed for each input column.

Filter options will be determined by the data type of the input column.

Users can add filters by clicking on the `Add Filter` option from the query configuration panel or directly from the column header menu in the results table.

Columns with filters applied will display a filter icon indicator in the column header.

---
Wireframes

[Added Input Filter](https://share.balsamiq.com/c/tK2hZy6FB4zVYpN56ejpBk.png)

### Aggregating Input Column Values

In cases where a link may refer to multiple values, input columns can be aggregated. In such cases, the system will perform automatic aggregation based on the data type of the referenced column. Users can change the type of aggregation at any time.

Aggregated columns will have an aggregation icon indicator in the column header.

---
Wireframes

[Added Input Aggregation](https://share.balsamiq.com/c/fNcbvQ1q5xMyni5JxBg3Rc.png)

### Applying a Formula to an Input Column

Direct input columns can also be transformed into formulas. The available formulas will depend on the input column type.

The user will select the `Apply Formula` option in the column header menu to transform the input column into a formula.

---
Wireframes

[Applying a Formula](https://share.balsamiq.com/c/nEzYaNKNTSv9EFwzwtfSof.png)

## Applying Transformations to the Result Table

The result table refers to the resulting table from all input columns selected and added, including filters and aggregations. Users can transform this output by applying output filters, sorts, and summarizations to the result table.

### Filtering the Output Table

Users can filter the output table by adding a filter step to any column from the result table. The column selector, in this scenario, will only allow users to select input columns rather than the whole column list from the column selection stage.

---
Wireframes

[Output Filter](https://share.balsamiq.com/c/dAVYnp8VnG2r2HzkSZ3rgp.png)

### Summarizing the Result Table

The `Summarization` step lets users generate a summarized version of the result table. When added, the system will group the table values based on a summary column of their choice. The summary can be done using the summary column's exact values or the data type's available grouping options.

To summarize the table, the user selects the `Summarize` option from the result transformations menu and adds the step. Once added, the remaining columns are automatically assigned an aggregation function, which users can change at any time. The data type of the output column is used to infer aggregates.

---
Wireframes

[Output Summarization](https://share.balsamiq.com/c/rPMwwETnuQ8a4ut8NfmcDB.png)

[Summarization Options](https://share.balsamiq.com/c/x2iwVBT3NwzmKyhnxSiJku.png)

### Sorting the Output Table

Users can sort the output table by applying a sort to any result table columns.

To sort the table, the user selects the `Sort` option from the result transformations menu and adds it to the list. Once added, the user can set a column and a direction for the sort.

---
Wireframes

[Output Sorting](https://share.balsamiq.com/c/8TYP1XNz49tS7hHqujMmqS.png)

### Adding a New Column to a Summarized Table

If the result table has transformations applied, new columns will be added automatically to the summarization steps and an aggregation set by default.

---
Wireframes

[Adding New Column](https://share.balsamiq.com/c/kWyvRL822BdBubhT4ghzgA.png)

## Deleting a Result Transformation Step

To delete a result transformation step, the user can click on the `Delete` button present in each step item. Deleting a step means that the system will undo all transformations made through that step, and the result table will reflect the updated output.

When subsequent steps rely on columns resulting from a deleted step, the system will display error warnings for every failed step. The table output will only reflect the output generated by those stages without errors.

---
Wireframes

[Deleting a Transformation Step](https://share.balsamiq.com/c/XeNAKGz1UnDMfscSTLDVp.png)

## Previewing the Query Results

A preview, or query result table, should be visible while the user is in `Data Explorer.` The result table will change based on the different configurations. For example, if a user applies a filter, the system should refresh the table to show the output with the filter applied.

## Saving the Query as a View

Under `Save Options`, the user can name the resulting query and choose to save it. This would save the view as a query the system would run every time the user opens it.

## Troubleshooting and Resolving Errors

### The result table has no rows

The result table could be empty if a filter returns no results or if the base table is empty. Since queries will run every time the user opens a view, it is possible that the data has changed or that the filter condition returns no results.

Providing a count of rows and columns from the original base table would eliminate confusion around the data source (the table is not empty).

Additionally, users should be able to identify which input columns are filtered, see the applied criteria for each filter and remove the filters if needed.

### There are duplicate values

If a user adds a column with multiple records without an aggregation, values from other columns will be duplicated. Adding aggregations by default for columns with multiple records would help users discover this functionality.

The system can determine the aggregation formula based on the column's data type.

### An input column used in a formula has been deleted

If a user deletes an input column utilized in a formula, that formula column must display the error and prompt the user to resolve it. The user can replace the affected column with another one or delete the formula column.

## Other Considerations

### Column Naming Convention

Input column names, when constructed, should have generated names that reference the source of the columns. For example, a column `full_name` from the `Person` table, linked by the column `actor_id` in `Movie,` would be named `movie_actor full_name.`

When column names fit the patterns employed in Mathesar, we might detect unnecessary suffixes like `id` and strip them out to shorten the names (e.g., `sequel title` instead of `sequel_id title`).

Additionally, the generated name can include a link hierarchy. For example `sequel_prequel_sequel title` for a column named `title` added through Movie's `sequel_id`'s `prequel_id`'s `sequel_id`.

Users can alter the default names at any time and still see the source information under the column details.

## Inspector Panel Modes

The inspector panel can be displayed in various modes depending on the currently active and selected objects. For example, clicking on a column will change the inspector's content to show the details for that column.

Inspector displays query details and saves options by default.

### Column Selection

The column selection mode is activated by clicking on the `Add Column` option in the column selection step. When active, this inspector mode will list columns:

- from the base table
- from tables with links in the base table
- from tables with links to the base table

---
Questions

- How will users know where to begin when using Data Explorer?
- Is it possible to disable aggregation by default?
- Should we display the primary key id from the base table?
- How do we handle a view that is out of sync, where objects may be modified outside Mathesar?
- Where are edit actions performed? What can be modified in a view or data explorer?
- What if we only showed Mathesar views and kept non-Mathesar views hidden?
- How are the view and query connected if you save a view associated with the query at that time?
- When a view query changes, how can we tell?
