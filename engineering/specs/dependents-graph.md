This spec describes the goals of the dependents graph feature and the details of its implementation.

## Overview
Dependents Graph is a feature for returning a graph of dependent objects for a chosen Mathesar object (representing a single database object). At the time of writing, it’s possible to get dependents for:

- Schemas
- Tables
- Table columns

This can be easily extended and added to other types if their support appears in Mathesar since the entry point for the query is just the object OID ([almost always](https://www.postgresql.org/docs/current/datatype-oid.html) the unique identifier of any object in the database).

As possible dependent objects, it returns:

- Tables
- Views
- Table constraints
- Indexes
- Triggers
- Sequences
- Functions (as direct schemas' dependents)

For each dependent object, a new set of dependents is constructed. The depth of the graph is artificially limited to 10, but the limit can be changed.

For Mathesar-supported types, the graph returns its Django id (like the table’s `14`). OIDs return along with names, for all other types of objects. 

### Example:

```json
[
    {
        "obj": {
            "objid": 147774,
            "type": "view",
            "name": "superauthors"
        },
        "parent_obj": {
            "id": "14",
            "type": "table"
        },
        "level": 1
    },
    {
        "obj": {
            "id": "40",
            "type": "table constraint"
        },
        "parent_obj": {
            "id": "14",
            "type": "table"
        },
        "level": 1
    },
    {
        "obj": {
            "id": "38",
            "type": "table constraint"
        },
        "parent_obj": {
            "id": "14",
            "type": "table"
        },
        "level": 1
    },
    {
        "obj": {
            "objid": 147832,
            "type": "view",
            "name": "topauthors"
        },
        "parent_obj": {
            "objid": 147774,
            "type": "view",
            "name": "superauthors"
        },
        "level": 2
    }
]
```

This example represents a shortened version of the graph returned for a `Table` with an id `14`. You can see it by the properties of the `parent_obj` object of the first level of dependents. Since one of its dependents is a `View` with an OID `147774` , you can see one of its dependents on the second level.

*The actual graph will be much larger and include dependents for the other objects of the `14`th and all the other objects.*

It’s possible to exclude specific types from the response using query parameters: `exclude=table&exclude=view`.

### Possible relations:

| Referent type    | Dependent types                         |
|------------------|-----------------------------------------|
| Schema           | Table, View, Type, Function, Sequence   |
| Table            | View, Table constraint, Index, Trigger  |
| View             | View                                    |
| Column           | Table constraint, Index, View, Sequence |
| Table constraint |                                         |
| Type (domain)    | Column, Function                        |
| Function         | Trigger                                 |
| Index            | Table constraint                        |

## UI
*Still under consideration*

When trying to delete one of the objects, a pop-up window should appear showing all the dependent objects that prevent a user from deleting it. Objects with their own dependents will have toggles to show them. By default, they should be collapsed, displaying just the first level. 

An example from Kriti:

![Schema deletion.png](/assets/engineering/specs/dependents-graph/Schema%20deletion.png)

An iteration based on a previous mockup which utilizes graph capabilities also:

Option 1:

![schema_del1](/assets/engineering/specs/dependents-graph/schema_del1.png)

Option 2:

![schema_del2](/assets/engineering/specs/dependents-graph/schema_del2.png)

## Implementation details

### API

At the API level, these queries return:

- Django ID and the type of the object for supported database objects (schemas, tables, table columns and table constraints)
- Name, type and OID of all the other objects

Getting Django IDs for supported types happens in the serializer.

**Filtering**

A simple backend filter that allows specifying types to exclude from the result.

Exclusion of those types will remove their dependents from the graph. A different kind of filter that “hides” some nodes but keeps the hierarchy of the graph is about to be implemented in the UI layer.


### DB

The main source for dependents is the internal system catalogue called `pg_depend`. It stores all dependents, but we return just the `automatic` and `normal` ones ([PostgreSQL: Documentation: 14: 52.18. pg_depend](https://www.postgresql.org/docs/current/catalog-pg-depend.html))

There is one case of implied dependency. It uses the `pg_rewrite` table to identify how views depend on other objects through the stored there rewrite rules .

The main query for getting all dependents is generated in two steps:

1. `UNION` all CTEs, each of them representing dependents of a specific type (table, constraint, view, etc.)
2. Recursive CTE that unions the base CTE (dependents of a requested object) and recursive part that queries dependents for all objects of the previous level

Each row has its own dependency chain that helps to track the already included dependent objects and omits self-referencing or infinite loops.

Each dependent-type CTE is a single lateral join between the `pg_depend` table and the `pg_identify_object` function. The function returns the type and name of the object.

**Column dependents**

Each object in the `pg_depend` is presented as a separate row, except the table column. Instead, there are maybe multiple entries with the same `refobjid` (the OID of the referenced object) but with different `refobjsubid`. The latter represents the *attnum* of the column. That’s why looking for dependents of a column object is slightly different. To do it properly, the `refobjsubid` column must be used.

## The `has_dependents` query

There is a separate query that checks whether the specific object has any dependents. It’s a separate one that just looks for dependents of a specific type. If any returns `True`.