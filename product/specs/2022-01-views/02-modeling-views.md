---
title: Views: Modeling Views
description:
published: true
date: 2022-01-13T19:49:54Z
tags: 
editor: markdown
dateCreated: 2022-01-13T19:49:54Z
---

Here's how I think we should model views in our backend and API. Each heading represents an attribute of Views.

Before I get into attributes, here's an example table named `Movies` that I'll use to illustrate different types of Views.

| ID | Title | Year | Genre |
|-|-|-|-|
| 1 | The River Wild | 1994 | Thriller |
| 2 | Don't Look Up | 2021 | Comedy |
| 3 | Daylight | 1996 | Action |
| 4 | Jason Bourne | 2016 | Action |

## Query
This is the SQL query that defines the view. This is **required**.

## Columns
Output columns of the View's Query, they will be shown in the UI.  At least one column is **required** for a view.

Column attributes are defined [in a separate page](/product/specs/2022-01-views/03-modeling-view-columns.md).

## Rows
These are the output rows of the View's Query. Rows are **not required**, Views can contain 0 rows.

## Filters
Views can have filters applied. Unlike Tables, view filters are not necessarily related to the columns that are present in the view.

Using the example table above, imagine a view created from the query `SELECT ID, Title FROM Movies WHERE Year > 2000;` This will return this view: which is filtered by Year even though it's not a column in the View.

| ID | Title |
|-|-|
| 2 | Don't Look Up |
| 4 | Jason Bourne |

**Note**: This only describes what's stored at the View query level. The UI will allow additional filtering that is not "saved" to the query.

## Sorting
Views can have sorting applied. Unlike Tables, view sorting is not necessarily related to the columns that are present in the view.

Using the example table above, imagine a view created from the query `SELECT ID, Title FROM Movies ORDER BY Year;` This will return this view, which is ordered by Year even though it's not a column in the View.

| ID | Title |
|-|-|
| 1 | The River Wild |
| 3 | Daylight |
| 4 | Jason Bourne |
| 2 | Don't Look Up |

**Note**: This only describes what's stored at the View query level. The UI will allow additional sorting that is not "saved" to the query.

## Aggregations
These are functions applied to the view as a whole (rather than to individual columns). 

Using the example table above, imagine a view created from the query `SELECT Genre FROM Movies GROUP BY GENRE;`

| Genre |
|-|
| Thriller |
| Comedy |
| Action |

**Note**: This only describes what's stored at the View query level. The UI will allow additional aggregations that are not "saved" to the query.

## Row Limit
This is the number of rows the View is limited as per its Query.

Please note that this is different from pagination; it represents a limit in the database.

## Row Offset
This is the number of the first row of the result of the Query that the View's rows start at.

Please note that this is different from pagination; it represents a limit in the database.

## Groups
Groups are similar to table grouping, they sort and then visually group rows into sections. They are a Mathesar-specific frontend concept and do not reflect anything related to the database or the View's Query.







