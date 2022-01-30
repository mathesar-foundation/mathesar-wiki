---
title: 06. Breaking Down DB Queries
description: 
published: true
date: 2022-01-30T23:33:26.276Z
tags: 
editor: markdown
dateCreated: 2022-01-24T23:01:36.210Z
---

This page goes through the [PostgreSQL documentation about queries](https://www.postgresql.org/docs/14/queries.html) and maps various concepts listed there to our data model. We'll follow the structure of the PostgreSQL docs.

## Table Expressions
See ["7.2 Table Expressions" on the PostgreSQL docs](https://www.postgresql.org/docs/14/queries-table-expressions.html)

| Clauses | Mapped To | Notes|
|-|-|-|
| `FROM` | "Sources" of columns | |
| `WHERE` | "Filters" | |
| `GROUP BY` & `HAVING` | "Aggregations" | |
| `GROUPING SETS`, `CUBE`, & `ROLLUP` | "Aggregations" | |
| Window function processing | "Formula" of columns | |
| Join columns | "Link" of columns | |

## Select Lists
See ["7.3 Select Lists" on the PostgreSQL docs](https://www.postgresql.org/docs/14/queries-select-lists.html)

| Clauses | Mapped To | Notes|
|-|-|-|
| Select-List Items | Related to "Sources" of columns | |
| Column Labels | Used to determine column name in Views | |
|  `DISTINCT` | "Aggregations" | |

## Combining Queries

See ["7.4. Combining Queries (`UNION`, `INTERSECT`, `EXCEPT`)" on the PostgreSQL docs](https://www.postgresql.org/docs/14/queries-union.html)

There is no direct mapping of query combinations to the Views UI in Mathesar, since they are internal to the query.

They will only be visible when the user looks at the raw SQL query.

## Sorting Rows
See ["7.5. Sorting Rows (`ORDER BY`)" on the PostgreSQL docs](https://www.postgresql.org/docs/14/queries-order.html)

This maps to View "Sorting".

## LIMIT and OFFSET
See ["7.6. `LIMIT` and `OFFSET`" on the PostgreSQL docs"](https://www.postgresql.org/docs/14/queries-limit.html)

These map to View "Row Limit" and "Row Offset".

## VALUES Lists
See: ["7.7 `VALUES` Lists" on the PostgreSQL docs"](https://www.postgresql.org/docs/14/queries-values.html)

These map to View column "Sources". They will show up as a computed source.

## WITH Queries
See ["7.8. `WITH` Queries (Common Table Expressions)" on the PostgreSQL docs](https://www.postgresql.org/docs/14/queries-with.html)

There is no direct mapping of CTEs to the Views UI in Mathesar, since they are internal to the query.

They will only be visible when the user looks at the raw SQL query.