# Data Palettes

This proposal is heavily influenced by Sean's [Worksheets Product Spec PR](https://github.com/mathesar-foundation/mathesar-wiki/blob/worksheets_product_spec/docs/projects/worksheets/worksheets-product-spec.md), as well as the Product Strategy document. The Worksheets Product Spec PR seems well-organized, so I'll follow much of its organization, and also link to it where there isn't anything different here (since there's lots of overlap).

As with "worksheets", a "palette" is a user-facing abstraction combining the functionality of the table page and explorer into a single tool. Specifically, a palette is a space to combine and produce relations starting from the "primary sources" of tables, views, and other relations that persist in the database. Relations would be combined through joins to produce a relation. 

## High level goals

### Page Consolidation

This goal is the same with the section in [Sean's PR](https://github.com/mathesar-foundation/mathesar-wiki/blob/worksheets_product_spec/docs/projects/worksheets/worksheets-product-spec.md#high-level-goals), in the **Page Consolidation** section.

To reiterate here, this spec should combine the table page and exploration into one unified UI concept, so the user doesn't have to naviate multiple concepts for querying their data.

### Modular Architecture

As for worksheets, palettes would bring modularity to Mathesar, but the top-level container and interface for those modules is different. The "top level" concept of palettes is composition of transformations. You compose "operations" on relations to produce other relations. You can then use those as building blocks to build up ever more complex relation definitions (queries).

Operation types:

- joins
- filters
- ordering
- formulas
- summarizing
- SQL query (this is a bit special, more below)
- etc.

Because each operation takes relations as its main input (along with, e.g., filtering parameters), _and produces a relation as output_, they can be arbitrarily composed. The object the user would see, after setting up an operation and its parameters, would represent the resulting relation.

Note that "display" is _not_ an operation type. Any operation produces a relation, and that relation could be displayed in different ways. I'll go with Sean's terminology and suggestion and propose that we should initially just offer display of a relation as a "sheet", i.e., a grid of columns and rows in the obvious way. It should be possible to interact with any relation, run the query defining it, and see it as a sheet in the UI.

Modularity is achieved by ensuring that operation types take only relations and user input as parameters, and output only relations.

### Collaboration between technical and non-technical users

This is a main distinguishing goal of this proposal. The "palette" concept is specifically designed to let technical and non-technical users collaborate without either being forced to learn too much about the knowledge domain of the other.

Suppose Alice, a museum curator, wants to query for some information, but isn't sure how to construct the query. She goes to Bob, the DBA, and asks him to set up a relation for her. He isn't that into Mathesar's GUI, and can instead either create a view for Alice, which will then be available as a primary source in the palette, or he uses the "SQL Query" operation to simply write a raw SQL `SELECT` query. Alice can then use the resulting relation as the basis for her work. She can explore ways to combine that output via joins, or filter it, sort it, etc. Because each operation operates on a relation (or set of relations), she's free to do whatever she wants in her palette, starting from Bob's `SELECT` query. If she gets stuck, she can _go back to Bob_, and he can (with minimal understanding of Mathesar) then help her by writing another `SELECT` query that has as its possible `FROM` clause targets any primary source, as well as any relation currently in the palette. 

This lets Alice and Bob work together without Alice being required to understand SQL, and without Bob being required to learn some newfangled GUI tool when he's perfectly happy just writing a `SELECT` instead.

## Relations and Operations in more detail

Upon loading their palette for the first time, a user would see a number of relations in the UI, representing any persisted relations on the database to which they have access. These are their "primary sources". They should be able to easily see a sheet showing the data in a given relation by clicking on it (or whatever). By right clicking (or whatever), they should be able to see metadata about the relation, for example its name, its kind (e.g., table or view), its columns, their types, etc.

They can create a new relation by either using a context menu starting from a given relation (for filtering, for example), or by choosing an operation from some other menu (e.g., for setting up a join, or running a raw SQL query). That new relation, along with its dependencies are persisted in Mathesar, and available to then be used as the basis for future operations. They can also, as with any relation, display the data in that relation in a sheet by clicking on it. 

### Relation Type: Primary Source

As stated above, a primary source relation refers to an actual persisted relation on the underlying database. Initially, this would be a relation of the following kinds:

- table
- view
- materialized view
- foreign table

#### Editable relations

Initially, only a table will be considered "editable" and receive the extra UI elements in its sheet (described below).

### Derived Relations

All other relations are defined by an operation applied to some other set of relations. Typically, this will just be one other relation. They would be shown in the same place and in much the same way as other relations, with some UI element to distinguish the primary source relations.

### Dependencies between relations

This would be rudimentary at first, and would be based on the parameters given in the definition of any derived relation. This will make it easier to help the user track down the problem if one of their derived relations isn't working because some part of its source data has been dropped or altered.

Circular dependencies would not be allowed. A relation should only be able to refer to previously defined relations (for a first iteration).

It should be possible to, through some interation with a relation see either:

- Dependencies of that relation, 
- Dependents of that relation, or
- Both

### Key Operation Type: SQL Query

The main parameters for this are a `SELECT` query, a name for the resulting relation, and an optional list of dependencies. This would (naturally) run the given `SELECT` query, and make the resulting relation accessible for display, or for further composition. The reason for the optional dependency list is that we want some metadata there that lets us track when some relation used in the `FROM` clause of the query is deleted or otherwise changed.

A user should be able to create a SQL Query relation through some interaction with another relation. The SQL Query relation would be initialized with the query generating the other relation prefilled, and all dependencies of that relation also prefilled.

We would need some way to make sure that the SQL entered can't modify the database. My favorite option is to just let them enter whatever they want, and then discard any data modifications their query would have made (e.g., if it's an `INSERT` statement, or a data-modifying CTE) using transaction management. This gives an added benefit of allowing for a "dry-run" of a data-modifying statement, if they use the correct `RETURNING` statement.

### Key Operation Type: Formula Column

This would be a mechanism for a user to write an SQL snippet defining a column to add to a relation, thereby creating a new relation. The parameters would be a relation, an SQL snippet defining the new column (`e.g., CONCAT(first_name, last_name)`), and an alias for the new column (e.g., `full_name`).

### Key Operation Type: Join

This is the main way for a user to combine columns from multiple tables to create a relation. It takes a list of relations, and a list of join pairs specifying how those relations should be joined. We could eventually provide different join types, but I imagine `LEFT OUTER` would suffice initially. Note that the user doesn't have to explicitly define dependencies for this operation, since they can be inferred from the other parameters.

### Other Operations:

Filters, ordering, summarizing (aggregation), etc. should be obvious by now. Each takes a single relation, as well as user input parameters, and results in a relation. We could also have basic formulas available as operations (e.g., add two columns).

## Editing primary source data via sheets

The main mechanism for editing data would be via a sheet display for a primary source that is "editable". For now, a sheet would be defined as "editable" if it displays the data of a primary source table. We'd lean heavily on mechanisms that currently exist in Mathesar's record selector. The elements for editing would be available whenever a displayed sheet is editable.

### `INSERT`

This works basically the same as in the record selector, but the search is precise rather than fuzzy. You type into text boxes for each column, and if no record matching exists, you get the option to `INSERT` one. We do _not_ attempt to create the record immediately and update it as the user inputs data (as in the current flow). In many ways this is smoother than the current setup which throws errors everywhere whenever there's a `NOT NULL` constraint or a `UNIQUE` violation, etc. 

### `UPDATE`

Initially, you'd use the same precise filtering (on equals) as for `INSERT` above. You define a filter by typing queries into the text boxes for each column. Through some interaction, you choose a column (or set of columns), the values to set, and then "commit" the update.

### `DELETE`

Same as update, but you just delete the records matching the filter.

## Editing other relation data via sheets

For non-primary-source relations, the editing process is: you click (double-click, whatever) a cell, and the record selector UI described above opens to the primary source table for the cell, conveniently filtered to match the data in that cell. From there, the editing process is the same, except now you also have the context of the cell in the relation you clicked to help you edit (if desired).

Eventually, this could be extended to situations where a cell is derived (e.g., its an aggregation result) by opening the record selector, but filtered to show all data involved in calculating that cell.

## DDL

This would have the same operations we currently offer, but they'd be available from some context menu available from the primary source relation object. E.g., for extracting columns, you'd choose those columns on that relation, and see them highlighted on the sheet associated with that relation if it's open.

## Key Differences from worksheets

- Top level concept is composition of operations on relations.
- DML is quite different: It uses a specific display (sheets with inline filtering), and provides that display when editing in other contexts.
- SQL queries are "under" the overall relation definition concept. They aren't a top-level operation.
- There is no distinction between "easy mode" for non-technical users and "power mode" for technical users.

## Key Improvements from Data Explorer

- Query definitions are no longer chained together as linearly dependent operations.
- Editing is accessible from query results
- Can view a sheet of intermediate relations in some query definition
- Provides full SQL `SELECT` query capability for users who want it.
- More powerful joining.

## Aside: Power console

When discussing this with Pavish, he noted that it might be useful for some users to access a "console" mode that would be just a `psql` console available in the browser. The output would also be in the console. If a user wanted to persist a query created in the console beyond the typical "scroll back through command history", or use the UI to then work with the resulting relation in a data palette, they should be able to easily open an operation of the SQL Query type with their most recently-run query filled in. They should also be able to, through some interaction with a given relation in their Palette, be able to open the complete SQL query associated with that relation in the power console. They could modify that query, then (as a first iteration) save it as a SQL Query operation.
