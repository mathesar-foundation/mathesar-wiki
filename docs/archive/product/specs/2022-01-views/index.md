# Views in Mathesar

## Overview
All data in Mathesar is stored in **[Tables](/archive/product/concepts/tables)**. However, users may not always want to analyze, edit, or otherwise work with data in the same way that it is stored. This might involve combining data from multiple tables or only looking at a subset of rows and columns from a single table.

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

- [01. Assumptions and Limitations](/archive/product/specs/2022-01-views/01-assumptions)
- [02. Feature Requirements](/archive/product/specs/2022-01-views/02-feature-requirements)
- [03. The Query Builder](/archive/product/specs/2022-01-views/03-the-query-builder)
- [04. Formulas](/archive/product/specs/2022-01-views/04-formulas)
    - [(a) Record Aggregations](/archive/product/specs/2022-01-views/04-formulas/4a-record-aggregations)
    - [(b) Random Generators](/archive/product/specs/2022-01-views/04-formulas/4b-random-generators)
    - [(c) Text Formulas](/archive/product/specs/2022-01-views/04-formulas/4c-text-formulas)
    - [(d) Number Formulas](/archive/product/specs/2022-01-views/04-formulas/4d-number-formulas)
    - [(e) Boolean Formulas](/archive/product/specs/2022-01-views/04-formulas/4e-boolean-formulas)
    - [(f) Date. Time, and Duration Formulas](/archive/product/specs/2022-01-views/04-formulas/4f-datetime-formulas)
    - [(g) List Formulas](/archive/product/specs/2022-01-views/04-formulas/4g-list-formulas)
    - [(h) Cumulative Formulas](/archive/product/specs/2022-01-views/04-formulas/4h-cumulative-formulas)
    - [(i) Regular Expression Formulas](/archive/product/specs/2022-01-views/04-formulas/4i-regex-formulas)
    - [(j) Custom Formulas](/archive/product/specs/2022-01-views/04-formulas/4j-custom-formulas)
- [05. View Structure](/archive/product/specs/2022-01-views/05-view-structure)
- [06. View Columns](/archive/product/specs/2022-01-views/06-view-columns)
- [07. Breaking Down DB Queries](/archive/product/specs/2022-01-views/07-breaking-down-db-queries)
- [08. Appendix](/archive/product/specs/2022-01-views/08-appendix)

## See also
- ["Views" Concepts page](/archive/product/concepts/views)
