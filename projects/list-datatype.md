---
title: List Data Type - Project Draft
description: Draft for defining the list data type implementation project.
published: true
date: 2023-05-29T22:20:23.485Z
tags: 
editor: markdown
dateCreated: 2023-05-02T21:44:56.744Z
---

**Name**: Adding support for list data type in Mathesar
**Status**: Draft 
**Theme**: List data type

## Team

| Role | Assignee | Notes |
|-|-|-|
| **Owner** | Maria | |
| **Approver (project plan)** | Kriti | *Needs to approve project plan* |
| **Approver (product)** | Kriti | *Needs to approve product spec and design* |
| **Approver (frontend)** | Pavish, Sean | *Needs to approve frontend spec* |
| **Approver (design)** | Ghislaine | *Needs to approve design spec* |
| **Approver (backend)** | Brent | *Needs to approve backend spec* |
| **Contributor (requirements)** | Brent, Ghislaine | *Creates product spec, requirements, GitHub issues* |
| **Contributor (design)** | Ghislaine | *Creates designs* |
| **Contributor (backend)** | Maria | *Creates backend specs and implements backend* |
| **Contributor (frontend)** | Rajat | *Creates frontend specs and implements frontend* |
| **Contributor (backend review)** | Brent | *Reviews backend code* |
| **Contributor (frontend review)** | Pavish | *Reviews frontend code* |

## Problem
The Mathesar UI allows users to configure the column types for their data, choosing between types like "Number", "Date", "Text", and so on. All data entered into the column is then validated against the rules according to the type. So for example, in a Number column, Mathesar will allow input of `2` but will reject input of `hello`.

So far, we've been assuming that users will only store a single point of data in any given table cell. However, PostgreSQL supports the ability to store an array instead of a single point of data, and we'd like to support that.

We already have support for arrays in explorations (and the Data Explorer), but those are read-only. This project is for adding support for lists to tables.

## Solution

### Creating a list column
#### From the table page
- `List` should be an available data type in addition to all of the others. Therefore, users should be able to visualize it in the dropdown menu of all the available data types.
![data_types_dropdown.png](/assets/projects/list-datatype/data_types_dropdown.png)
- Users should be able to provide a default value, or set it to `null`, as Mathesar supports this for the other data types as well.

#### Importing a file
- When importing data from a CSV file, *what should be inferred as list?*
	- `"{item1,item2,...}"`: this is what Postgresql infers as an array when importing data from a CSV file (note the double quotes).
  - `[item1,item2,...]`: this notation is allowed when inserting values in an array column in Postresql.
  
  
### Displaying data from lists
- Items of the “list” type should be shown as pills (as it is currently shown in the data explorer).
![visualizacion_columna.png](/assets/projects/list-datatype/visualizacion_columna.png)


### Editing and deleting records
- Users should be able to create a list; this is, fill an empty cell in a list data type column. A list can be created by separating items with a comma. Example:

From the record page:

![input_box.png](/assets/projects/list-datatype/input_box.png)

By double clicking a cell from the table page:

![llenar_celda.png](/assets/projects/list-datatype/llenar_celda.png)

- Users should be able to edit the text of an existing list item. ***Two possible ways are***: 
	 - **Clicking a single pill, and so the user will edit the text in that pill.**
   - **Displaying the content of the list as a text with comma-separated items, and so the user would edit the list as if they are editing a text.**
- Users should be able to delete an item of a list.
	- Also a *whole list all at once*. This is, setting that field to `null` for a single record of the table.

### Error handling
- Errors should be handled and displayed if any of the operations fail.

### Filters 
We should support the following filters for `List` cells:
1. is empty
1. is not empty
3. contains `<ITEM>`

Regarding the length of the list in a cell:
1. number of items greater than `<NUMBER>`
2. number of items greater than or equal to `<NUMBER>`
3. number of items equal to `<NUMBER>`
7. number of items lesser than `<NUMBER>`
8. number of items lesser than or equal to `<NUMBER>`
    
### Grouping
We should support the following custom grouping types for List cells:
1. Number of list items


## Risks
- Mathesar may be connected to PostgreSQL databases that have columns with arrays of non-supported data types (e.g.: geometric like polygons) or multi-dimensional arrays. We have to let the frontend know that those kinds of lists aren't supported, and display them as text.
- CSV files can be bad-formatted; we have to show a message to the user indicating this error or parse the uknown format as a text column (if possible).
- Lists can be large (e.g. starting from the dozens of items). **Should we truncate the number of pills displayed in a cell?**

## Resources
> This section  will grow over the project's timeframe.
{.is-info}

- **Issues**: [GitHub meta issue]()
- **Wiki pages**:
  - [Project description for GSoC 2023](https://wiki.mathesar.org/en/community/mentoring/project-ideas/list-data-type)
  - [Frontend spec](https://wiki.mathesar.org/en/projects/list-datatype/frontend-specs)
  - [Backend spec (nothing here yet)]()

## Timeline
This project should take **13 weeks**.

| Date | Outcome |
| - | - |
| 2023-05-01 | Product specification starts | 
| 2023-05-19 | Implementation spec complete | 
| 2023-05-24 | Implementation spec approved | 
| 2023-06-22 | Design work complete |
| 2023-07-03 | Backend work complete |
| 2023-07-05 | Frontend work complete |
| 2023-07-20 | Documentation complete |

## Future work
- Have different designs for item's display appearance, depending on their data type. Consider for example polygons; how should we display them?
- Convert any column to a list column. E.g user can change the data type `money` of a column, to `list of money`. In [PostgreSQL](https://www.postgresql.org/docs/current/arrays.html), an array can be of any of its built-in data types. 
- Support operations between `list` columns. E.g.: users can define a new `list` column as the result of concatenating the items of two other `list` columns. This can be extended to a functionality similar to inserting formulas in cells of a spreadsheet (like in Excel, Calc).
- Sort a `list` column with a custom expression. E.g.: for a numerical list column, sort the column based on the average of the lists.

