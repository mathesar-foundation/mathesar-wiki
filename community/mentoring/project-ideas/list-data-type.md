---
title: List data type
description: 
published: true
date: 2023-02-03T22:36:58.656Z
tags: 
editor: markdown
dateCreated: 2023-02-03T16:53:57.798Z
---

## Classification
- **Difficulty**: High
- **Skills needed**: Python, SQL, Django
- **Skills that could be helpful**: Django, SQLAlchemy, Svelte, TypeScript
- **Length**: Long (~350 hours) for both frontend & backend, Medium (~175 hours) for backend only.

## The Problem
- The Mathesar UI allows users to configure the column types for their data, choosing between types like "Number", "Date", "Text", and so on. All data entered into the column is then validated against the rules according to the type. So for example, in a Number column, Mathesar will allow input of `2` but will reject input of `hello`.

So far, we've been assuming that users will only store a single point of data in any given table cell. However, PostgreSQL supports the ability to store an array instead of a single point of data, and we'd like to support that.

We already have support for arrays in explorations (and the Data Explorer), but those are read-only. This project is for adding support for lists to tables.

## Feature Description
### Creating columns
- "List" should be an available data type in addition to all of the others.

### Importing data
- Comma separated or tab separated values in cells should be correctly inferred as Lists

### Viewing and editing list data
List data could be displayed and edited in the following places. All of these need to be updated to view and edit lists correctly.
- Table cells
- Input fields on record pages
- Inputs to set a default value for a column
- Inputs for filter conditions
- Inputs to filter records within the record selector

**Viewing lists**
- Data of the "list" type should be shown as pills. 
- Please look at the way lists are shown in the Data Explorer as a reference.

**Editing lists**
- Users should be able to add and remove list items.
- Users should be able to edit the text of an existing list item.
- Errors should be handled and displayed if any of the operations fail.

### Filtering and grouping
1. We should support the following filters for List cells:
    1. is empty
    2. is not empty
    3. contains `<ITEM>`
    4. number of items greater than `<NUMBER>`
    5. number of items greater than or equal to `<NUMBER>`
    6. number of items equal to `<NUMBER>`
    7. number of items lesser than `<NUMBER>`
    8. number of items lesser than or equal to `<NUMBER>`
2. We should support the following custom grouping types for List cells:
    1. Number of list items

## Architectural Problems
- Mathesar may be connected to PostgreSQL databases that have columns with arrays of non-text data types or multi-dimensional arrays. We need a way to let the frontend know that those kinds of lists aren't supported (we should show them as "Other" in the UI).

## UX Design Problems
- How do we add and remove list items from cells?
- How do we edit the text of existing list items?

## Tasks
### Backend
1. Implement the List database type
1. Integrate the List data type with our data type inference logic.
1. Integrate the List data type with our existing APIs.
1. Build custom grouping functions for number of list items
1. Build custom filtering functions for lists
1. Integrate the filtering and grouping function with our API.
1. Figure out how to identify unsupported arrays in the API so that the frontend shows them as text.

### Frontend
1. Write a UX design document describing how lists will be edited. Then work with the front end team and product designer to solidify the UX design.
1. Implement the list viewing and editing behavior.
1. Ensure filtering and grouping works well.

## Expected Outcome
Users should be able to use List data types as described in "Feature Description"

## Application Tips
You may submit an application for only the backend portion of this project, or for both backend and frontend. Please make it clear which you're proposing.

- Demonstrate proficiency with the required skills.
- Present a preliminary API spec.
- Present a preliminary UX design document if you're proposing working on the frontend.
- Demonstrate an understanding of how Mathesar data types are implemented in the backend and APIs.

## Out of Scope
For the scope of this project, we will only support lists of text in the UI. Lists of other data types and multi-dimensional lists (lists of lists, etc.) out of scope.

## Resources
- [Previous spec for List data types](https://github.com/centerofci/mathesar/issues/978): *this is an old and deprecated issue, but might be useful.*
- Please review how multi-select fields work in Airtable.

## Mentors
**Primary Mentor**: TBD
**Secondary Mentor(s)**: Pavish
