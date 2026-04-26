# Views in Mathesar

## Overview
All data in Mathesar is stored in **[Tables](../../concepts/tables.md)**. However, users may not always want to analyze, edit, or otherwise work with data in the same way that it is stored. This might involve combining data from multiple tables or only looking at a subset of rows and columns from a single table.

- For example, tables are often optimized for reducing redundancy in data storage. It's hard to work with interrelated data and perform data analysis tasks using tables alone. On a day to day basis, users may want to work with data spread across different tables.
- Tables for data analysis are often stored in a denormalized format. Users may want to work with it by reducing the redundancies.

This is where **Queries** and **Views** come in – to help the user see the data how they want to see it, regardless of where it is stored.

**Queries** are requests for data. The output of a query results in a "virtual" table. Data is presented in rows and columns just like a table, but these rows and columns are calculated on the fly by pulling other data from wherever it is stored. Queries can involve combining data from multiple tables (or eventually other views), filtering, sorting, aggregating (grouping), or even creating entirely computed columns.

**Views** are saved queries. Whenever a view is loaded, it loads the latest data based on the underlying query.

### User Goals
The user goals for **Queries** are:

- To enable users to perform more complex lookups of data in a single table than can be achieved by filtering or sorting (e.g. finding all duplicate rows in a table)
- To enable users to perform lookups of data across multiple tables
- To enable users to work with subsets of data (e.g. fewer columns, rows, or both)
- To enable users to see aggregate views of data
- To help users answer questions about their data and perform basic data analysis

The user goals for **Views** are:

- To help users save commonly used queries
- To provide a better editing experience for related data (especially many-to-many relationships)

### Implementation
Under the hood, **queries** are `SELECT` SQL queries and **views** are PostgreSQL views.

This means that in order to work with Views in Mathesar, we need to translate concepts used in [PostgreSQL queries](https://www.postgresql.org/docs/14/queries.html) to our end users in a user-friendly way.

## Concepts and Features
We're introducing a number of new product concepts and features in this specification. They are expanded upon below, split into different pages for readability.

- [01. Assumptions and Limitations](./01-assumptions.md)
- [02. Feature Requirements](./02-feature-requirements.md)
- [03. The Query Builder](./03-the-query-builder.md)
- [04. Formulas](./04-formulas.md)
    - [(a) Record Aggregations](./04-formulas/4a-record-aggregations.md)
    - [(b) Random Generators](./04-formulas/4b-random-generators.md)
    - [(c) Text Formulas](./04-formulas/4c-text-formulas.md)
    - [(d) Number Formulas](./04-formulas/4d-number-formulas.md)
    - [(e) Boolean Formulas](./04-formulas/4e-boolean-formulas.md)
    - [(f) Date. Time, and Duration Formulas](./04-formulas/4f-datetime-formulas.md)
    - [(g) List Formulas](./04-formulas/4g-list-formulas.md)
    - [(h) Cumulative Formulas](./04-formulas/4h-cumulative-formulas.md)
    - [(i) Regular Expression Formulas](./04-formulas/4i-regex-formulas.md)
    - [(j) Custom Formulas](./04-formulas/4j-custom-formulas.md)
- [05. View Structure](./05-view-structure.md)
- [06. View Columns](./06-view-columns.md)
- [07. Breaking Down DB Queries](./07-breaking-down-db-queries.md)
- [08. Appendix](./08-appendix.md)

## See also
- ["Views" Concepts page](../../concepts/views.md)
