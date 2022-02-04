---
title: Views
description: About Views in Mathesar
published: true
date: 2022-02-04T03:54:55.705Z
tags: 
editor: markdown
dateCreated: 2021-11-16T22:07:54.178Z
---

# About

Views are "virtual tables". Data is presented in rows and columns just like a table, but these rows and columns are calculated on the fly by pulling other data from wherever it is stored.

Views can involve combining data from multiple tables or other views, filtering, sorting, aggregating (grouping), or even creating entirely computed columns.

Under the hood, views are defined by a database (SQL) query. 

## Views in Mathesar
We expect that [Tables](/product/concepts/tables) will be used for entering simple data quickly and Views will be used for looking at data, creating reports, or editing inter-related data easily.

You should use Views when you'd like to:
- see data aggregated across multiple tables in one place.
- bookmark a subset of data in a table (e.g. filtered, sorted, or grouped data)
- summarize data (e.g. have a column that shows counts of records in a table)
- compute data (e.g. subtract the value of one column from another column and show the result in a new column)


# Usage
[Tables](/product/concepts/tables) that are structured to avoid data duplication (i.e. are properly [normalized](https://en.wikipedia.org/wiki/Database_normalization)) are not the most useful for seeing the most relevant information in a single place.

## Views vs. Tables
To think about the difference between Views and [Tables](/product/concepts/tables), here's an example. Imagine you want to track your movie watches in Mathesar. Questions you might be thinking about are:
- On what day of the week do I usually watch movies?
- When did I last see Brad Pitt in a movie?
- How many movies did I watch that were released in the 90s vs. the 2000s.
- What was the last foreign movie I watched?

### Table Structure
In order to track the data necessary to answer these questions, here's a possible structure for your tables:

#### Movies
| ID | Title | Release Year | Primary Language |
|-|-|-|-|
| 13 | Thelma & Louise | 1991 | English |
| 22 | Meet Joe Black | 1998 | English |
| 33 | Crouching Tiger, Hidden Dragon | 2000 | Mandarin |
| 41 | Crazy Rich Asians | 2018 | English |
| .. | .. | .. | .. |

#### Actors
| ID | Name |
|-|-|
| 34 | Michelle Yeoh |
| 45 | Brad Pitt |
| 71 | Geena Davis |
| 83 | Zhang Ziyi |
| .. | .. |

#### Movie Actor Map
| ID | Movie ID | Actor ID |
|-|-|-|
| 67 | 13 | 45 |
| 68 | 22 | 45 |
| 69 | 33 | 34 | 
| 70 | 41 | 34 |
| 89 | 13 | 71 |
| 97 | 33 | 83 | 
| .. | .. | .. |

#### Movie Watch
| ID | Movie ID | Date |
|-|-|-|
| 91 | 13 | 2021-10-13 |
| 100 | 22 | 2021-10-01 |
| 104 | 33 | 2021-09-23 | 
| 190 | 41 | 2021-08-12 |
| 203 | 13 | 2019-01-20 |
| .. | .. | .. |

### The Role of Views
As is obvious, none of these tables answer your questions by themselves, even when filters, sorts, or aggregations are applied to an individual table. Also, when you watch a new movie, logging it would involve adding data to four separate tables. The job of views is to simplify that.

Imagine a view with this structure:

| ID | Title | Actors | Last Watched | Times Watched | Language | Release Year | 
|-|-|-|-|-|-|-|
| 13 | Thelma & Louise | Brad Pitt, Geena Davis | 2021-10-13 | 2 | English | 1991 |
| 22 | Meet Joe Black | Brad Pitt | 2021-10-01 | 1 | English | 1998 |
| 33 | Crouching Tiger, Hidden Dragon | Michelle Yeoh, Zhang Ziyi | 2021-09-23 | 1 | Mandarin | 2000 |
| 41 | Crazy Rich Asians | Michelle Yeoh | 2021-08-12 | 1 | English | 2018 |
| .. | .. | .. | .. |

Once you have set up this view, you could filter and sort to get answers to your questions, or add new movie watches easily by adding all relevant data from one place.

# Future Plans
In the future, we will offer alternate display modes for Views (e.g. calendar, map, kanban, etc.).
