---
title: 03. The View Query
description: 
published: true
date: 2022-01-30T23:32:52.662Z
tags: 
editor: markdown
dateCreated: 2022-01-24T22:55:38.596Z
---

In some cases, we will be able to break down a View's Query into simpler parts that the user can edit. Here's how I think we should model those simpler parts in our API and UI. Each heading represents an attribute of a View Query.

Here's an example table named `Movies` that I'll use to illustrate the attributes below.

| ID | Title | Year | Genre |
|-|-|-|-|
| 1 | The River Wild | 1994 | Thriller |
| 2 | Don't Look Up | 2021 | Comedy |
| 3 | Daylight | 1996 | Action |
| 4 | Jason Bourne | 2016 | Action |

## Editable
A View Query is **editable** if we can break it down into the simpler parts described below. Otherwise, the View Query cannot be edited and we won't have any filters, sorts, or aggregations to show.

## Filters
A View Query can have filters applied. These filters are not necessarily related to the columns that are present in the view.

Using the example table above, imagine a view created from the query `SELECT ID, Title FROM Movies WHERE Year > 2000;` This will return this view: which is filtered by Year even though it's not a column in the View.

| ID | Title |
|-|-|
| 2 | Don't Look Up |
| 4 | Jason Bourne |

## Sorting
Views can have sorting applied. These sorts are not necessarily related to the columns that are present in the view.

Using the example table above, imagine a view created from the query `SELECT ID, Title FROM Movies ORDER BY Year;` This will return this view, which is ordered by Year even though it's not a column in the View.

| ID | Title |
|-|-|
| 1 | The River Wild |
| 3 | Daylight |
| 4 | Jason Bourne |
| 2 | Don't Look Up |

## Aggregations
These are functions applied to the view as a whole (rather than to individual columns). 

Using the example table above, imagine a view created from the query `SELECT Genre FROM Movies GROUP BY GENRE;`

| Genre |
|-|
| Thriller |
| Comedy |
| Action |

## Row Limit
This is the number of rows the View is limited as per its Query.

## Row Offset
This is the number of the first row of the result of the Query that the View's rows start at.







