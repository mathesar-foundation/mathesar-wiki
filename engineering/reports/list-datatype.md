---
title: List data type report - 2023 internship
description: 
published: true
date: 2023-07-20T22:06:16.750Z
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
### Restricting the dimensions to one
#### Custom Mathesar Type
Similar data types like JSON and JSON Arrays have been implemented as custom data type classes in Mathesar. As such, they are reflected as Domains on the DB. Implementing Arrays in this way has some issues:
- As any data type can have its Array version, this implies that Mathesar will have to create a Domain column for every possible scalar type. 
- Other aspects tied to a data type, such as cast functions, will also be multiplied by this factor. 
- This can be dangerous for backwards-compatibility in the future; we would have to support both a constrained array version and a possibly unconstrained one.

#### Type decorator in SA
Another option was to implement the Array as a class that inherits from SA's TypeDecorator [2]. The catch here is to access to the dimension's argument handled by SA, and in compiling time, making sure that we pass a value of 1. Again, this workaround also has some disadvantages:
- Mathesar is currently trying to reduce its dependence on SQLAlchemy.
- We need to support columns being written to in the database via other clients (i.e., where the enforcement won't happen). That dimension can't be reflected from the database.

#### Custom module (middleware)

## Current state

### Backend
There is no new data type for arrays; the SA `Array` type, which was previously supported for aggregation transformations, is the one currently supported and used to map an Array column in a table. 

**CRUD operations**
Sending a patch request to an array column correctly updates the records in a table.

**Filters**
Some filters were already supported:

### Frontend
#### Creating an Array column
Any data type can have its version in Array. Therefore, it doesn't seem a good idea to list each possible Array type in the data types dropdown list:
- There will be a lot of options listed.
- The user can easily misread one list type and select a wrong one, for example, choosing List of Money instead of List of Email (both begin with *'List of ...'*).

A cleaner approach suggested by Ghislaine is to have a separate menu for the Array or List type.

This feature is not implemented.

#### Editing arrays in cells
Array columns are read-only, and 1-D arrays are rendered with pills (one item in one pill). 

**Idea:** When editing a cell, a first and basic approach would be that the user types in the array in the correct format (e.g with brackets, elements separated by commas). Then, as it happens for the other data types, when the user leaves a cell, a PATCH call is made to the API to update a particular record. 
Work regarding this approach can be found in [this branch](https://github.com/centerofci/mathesar/tree/array_edition). Here, cells of an Array column can be edited. Two types of components are handled: `TextInput` for when `editMode=True`, and ArrayCell otherwise. There are some issues:
When entering a new value, the Frontend sends to the backend a malformed array, for example:

```
# currently sent
request: {"125":"50000,200"}
# instead it should be
request: {"125": [50000,200]}
```

This is because making both components work in sync is complex. There is probably a mishandling of the TextInput value, and so the Array factory ends up with a string instead of an Array object. This has to be debugged.

Moreover, this approach is not considering the case of N-D arrays. In this case, it would be better to render them as plain text. N-D arrays are not used as much as 1-D arrays (people would prefer to go for a vector type instead), so their use cases will be, hopefully, rare. For a first step, it's not worth the effort to figure out how to design a proper UI for this multidimensional structure.


#### Deleting items
It is currently not possible to delete elements from an array. Also, the UI/UX has to be sorted out for this functionality. 
- Will users be able to delete individual items? Consider the added complexity to this task if the array is large; it's very easy for the user to loose sight of the element they want to eliminate.
- An easier and reasonable first approach is to let the user handle this through plain text edition. Also, we should think about the persona of the target users. It's more natural for a DB maintainer to just edit records through a form, using plain text.

#### Sorting elements
A drag-and-drop feature does not seem to be very useful to offer.
- Again, we should consider the complexity of this task for large lists.
- For sorting, for end users used to calc documents, making use of a formula to achieve this is more intuitive and comfortable. 

****
## Future work
- Make a cell of an Array column work correctly, so to be able to update records in an Array column.
- Support all the filering and sort operations at least in the backend.
- Make the frontend render the arrays as strings if they have more than 1 dimensions, which is possible to know right away, as the passed lists will have more than one bracket.


## References
1. [Postgres documentation on Arrays](https://www.postgresql.org/docs/current/arrays.html)
2. [TypeDecorators](https://docs.sqlalchemy.org/en/20/core/custom_types.html#sqlalchemy.types.TypeDecorator)