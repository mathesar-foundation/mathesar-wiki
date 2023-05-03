---
title: List Data Type - Project Draft 
description: Draft for defining the list data type implementation project. 
published: false
date: 2023-05-03T21:47:28.256Z
tags: 
editor: markdown
dateCreated: 2023-05-02T21:44:56.744Z
---

**Name**: Adding support for list data type in Mathesar
**Status**: Draft 
**Theme**: List data type
> Options for status:
> **Draft**: The owner is still writing up the project.
> **In review**: The project has been written up, but hasn't been approved yet.
> **Approved**: The project has been approved, but work hasn't started yet.
> **In progress**: Work on the project has started.
> **Complete**: The project is over.
{.is-info}


## Team

| Role | Assignee | Notes |
|-|-|-|
| **Owner** | Maria | |
| **Approver (project plan)** | Kriti | *Needs to approve project plan* |
| **Approver (product)** | Kriti | *Needs to approve product spec and design* |
| **Approver (frontend)** | Pavish, Sean | *Needs to approve frontend spec* |
| **Approver (backend)** | Brent | *Needs to approve backend spec* |
| **Contributor (requirements)** | Brent, Glenn | *Creates product spec, requirements, GitHub issues* |
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

### Scope of the list data type
List data could be displayed and edited in the following places: 
- Table cells
- Input fields on record pages
- Inputs to set a default value for a column
- Inputs for filter conditions
- Inputs to filter records within the record selector


### Creating a column
- `List` should be an available data type in addition to all of the others. Therefore:
	- Users should be able to visualize it in the dropdown menu of all the available data types.
	- Users should be able to provide a default value, or set it to `null`, as Mathesar supports this for the other data types as welll.
- When importing data from a CSV file, *what should be inferred as list*?
	- `"{item1,item2,...}"`: this is what Postgresql infers as an array when importing data from a CSV file (note the double quotes).
  - `[item1,item2,...]`: this notation is allowed when inserting values in an array column in Postresql.
  
  
### Displaying data from lists
- Items of the “list” type should be shown as pills (as it is currently shown in the data explorer).

### Editing and deleting records
- Users should be able to edit the text of an existing list item.
- Users should be able to delete an item of a list.
	- Also a *whole list all at once*? This is, setting that field to `null` for a single record of the table.
- Users should be able to create a list; this is, fill an empty cell in a list data type column. 

### Error handling
- Errors should be handled and displayed if any of the operations fail.

### Filters 
We should support the following filters for List cells:
1. is empty
1. is not empty
3. contains `<ITEM>`
4. number of items greater than `<NUMBER>`
5. number of items greater than or equal to `<NUMBER>`
6. number of items equal to `<NUMBER>`
7. number of items lesser than `<NUMBER>`
8. number of items lesser than or equal to `<NUMBER>`
    
### Grouping
We should support the following custom grouping types for List cells:
1. Number of list items


## Risks
- Mathesar may be connected to PostgreSQL databases that have columns with arrays of non-supported data types (e.g.: geometric like polygons) or multi-dimensional arrays. We need a way to let the frontend know that those kinds of lists aren't supported. Should we show them as *"other"* in the UI?


## Resources
> This section collects project related resources. It's expected that there might not be anything here until the project plan is approved, and this section will grow over the project's timeframe.
{.is-info}

- **Issues**: [GitHub meta issue]()
- **Wiki pages**:
  - [Project description for GSoC 2023](https://wiki.mathesar.org/en/community/mentoring/project-ideas/list-data-type)
  - [Backend spec]()
  - [Frontend spec]()  

## Timeline
This project should take **13 weeks**.

| Date | Outcome |
| - | - |
| 2023-05-01 | Product specification starts | 
| 2023-05-10 | Implementation spec complete | 
| 2023-05-15 | Implementation spec approved | 
| 2023-03-22 | Design work complete |
| 2023-03-27 | Backend work complete |
| 2023-04-05 | Frontend work complete |
