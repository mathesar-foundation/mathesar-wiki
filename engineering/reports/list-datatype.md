---
title: List data type report - 2023 internship
description: 
published: true
date: 2023-07-18T21:35:57.429Z
tags: 
editor: markdown
dateCreated: 2023-07-18T19:34:24.849Z
---

In this report we will talk about the scope and goals of the project:  List data type. Considerations and difficulties are also discussed, as well as the project's current state. Finally, a future work line is given.

## Introduction
The `List` data type project was conceived with the goal of adding support of the `Array` Postgres type to Mathesar. The features originally proposed to be implemented are detailed in the [project's page](/en/projects/list-datatype).

### Preliminaries
An `Array` is not a data type per se, but a data structure that holds values of a certain data type. It is not supported by all the SQL databases, but Postgres does. A common array is a structure characterized by having a length and dimension. E.g.
```
a = [1, 1, 3] # a has length=3 and dimensions=1   
b = [[1, 1], [2, 3]] # b has dimensions=2
c = [[[1, 1, 1]]] # c has dimensions=3
```
If you've worked with Python's numpy, you can think of dimensions as the number of available axis. Note that the notion of length becomes blurry if we're not in 1-D; should we count the number of items at the inner dimension? SQL works with the `array_length` function, which needs to be passed the `dimension` as an argument, so it returns the number of items at that dimension.

### Arrays in PostgreSQL
The implementation of Arrays in PostgreSQL is tricky, and for our project, it brought a big overhead. From [1]: *"... the current implementation ignores any supplied array size limits, i.e., the behavior is the same as for arrays of unspecified length. The current implementation does not enforce the declared number of dimensions either. "* 

Problems:
1. We cannot be sure now that all the values in an ARRAY column will have the same dimensions and length.
2. Users can create ARRAY columns with N-dimensions back with Postgres, and Mathesar would have to figure out how to render them.
3. Any display option that the Frontend usually handles per column would now need to be processed per cell.
4. We cannot give users the chance to create a `List` column with a fixed number of dimensions, and assure them that all the records will comply with that number of dimensions. 
4. In general, now Mathesar has to be prepared to support N-dimensional arrays.

### SQL Alchemy (SA) support
This library supports the handling of arrays, and it implements it as a data type class with an `item_type` attribute that specifies the true data type in the DB. 
The Array class also uses an optional `dimensions` argument, with a default value of 1. This does not actually reflects into an ARRAY column enforced to be 1-dimensional in the DB; it's just a hack of the library to traverse the arrays more efficiently when converting them to Python's lists. 
> **Attention**, SQL Alchemy needs to work with the psycopg2 DB API to manipulate arrays. 
{.is-warning}

 
## Methodology
### Restricting the dimensions
#### Type decorator in SA

#### Custom Mathesar Type

#### Custom module (middleware)

## Current state

### Backend
There is no new data type for arrays; the SA only `Array` type, which was previously supported for aggregation transformations, is the one currently supported. 
#### CRUD operations
Sending a patch request to an array column correctly updates the records in a table.
#### Filters
Some filters were already supported:

### Frontend
Cells of an Array like column can be edited, but the handling of TextInput in edit mode and ArrayCell components elsewise is complex. When entering a new value, the Frontend sends to the backend a malformed array, for example:

```
# currently sent
request: {"125":"50000,200"}
# instead it should be
request: {"125": [50000,200]}
```

## Future work
- Make a cell of an Array column work correctly, so to be able to update records in an Array column.
- Support all the filering and sort operations at least in the backend.
- Make the frontend render the arrays as strings if they have more than 1 dimensions, which is possible to know right away, as the passed list will have more than one bracket.


## References
1. [Postgres documentation on Arrays](https://www.postgresql.org/docs/current/arrays.html)