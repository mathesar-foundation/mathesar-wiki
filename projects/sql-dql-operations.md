---
title: Remove SQLAlchemy from DQL operations
description: 
published: true
date: 2023-07-19T23:13:42.186Z
tags: 
editor: markdown
dateCreated: 2023-03-23T08:31:21.752Z
---

- **Name**: Remove SQLAlchemy from DQL operations
- **Status**: Draft
- **Theme**: Code quality, maintainability, performance, Removing SQLAlchemy

## Team

| Role                           | Assignee | Notes                                               |
|--------------------------------|----------|-----------------------------------------------------|
| **Owner**                      | Brent    |                                                     |
| **Approver (project plan)**    | Kriti    | *Needs to approve project plan*                     |
| **Approver (backend)**         | Brent    | *Needs to approve back end spec*                    |
| **Contributor (requirements)** | Brent    | *Creates product spec, requirements, GitHub issues* |
| **Contributor (requirements)** | Dom      | *Creates product spec, requirements, GitHub issues* |
| **Contributor**                | Anish    | *Coding and reviewing*                              |
| **Contributor**                | Dom      | *Coding and reviewing*                              |
| **Contributor**                | Mukesh   | *Coding and reviewing*                              |

## Problem

Data Query Language (DQL) operations are those that query the data stored in a database. The relevant SQL word is `SELECT`. These operations require knowledge of the database to work. E.g., a function needs a table's name to `SELECT` from it. Currently, we write most `SELECT` statements in Python using SQLAlchemy, necessitating the reflection of the database state into memory in Python and using that state to build queries.

Our current setup for this is:
- Inefficient (reflection is slow)
- Complicated (hard to maintain)
- Prone to bugs (managing state in Python memory is constantly tripping us up)

All of these problems are related to the fact that we're building the SQL queries to run DQL operations in Python.

## Solution

### Set up OID labeled views in database
Create a framework that sets up a view for each table in the database with an algorithmically derived name and column names. The view should have a name that can be determined if you have the underlying tables's OID. The columns of the view should have names determined by the attnums of the corresponding columns in the underlying table. This is already prototyped in the file `db/sql/2_msar_views.sql`.

### Create DQL functions in database
Create a function for each desired DQL operation on the databse using SQL or PL/pgSQL.
- Each such function should be overloaded to have the signature needed for calling from Python with minimal fuss, as well as the target signature.
- Each such function should have a main implementation which uses the most reasonable signature for the task at hand.
- This should rely heavily on the OID labeled views.

### Replace Python DQL functions with wrappers of DB functions, and custom query building.
Replace the current Python functions performing DQL operations with thin wrappers for these functions. Use an as-yet unknown query builder to compose complete queries when (if) needed.
- Be mindful of looking out for functions which may be deleted, rather than replaced, once this is done.
- Map the original Python function signatures to an appropriate function call of the database functions.
- Again, these should rely heavily on the OID labeled views.
- It's completely fine to create scaffolding functions at this point to avoid letting changes sprawl.
- After this phase, no SQLAlchemy imports should be used in any module whose functions are modified in this way, i.e., DQL operation modules.

Note that this section may take more lateral thinking than for the DDL and DML phases. The reason is that we're composing more ad-hoc DQL operations using the data explorer, and so some care needs to be used.

### Refactor and clean up results
Refactor to remove SQLAlchemy objects from calls using Python DQL functions:
- Remove any SQLAlchemy objects from DQL function signatures (This may require modifying callers slightly)
- Remove SQLAlchemy from the entire call stack calling a given function, all the way up to the API (within reason).
- Modify affected function signatures to avoid using `schema_name`, `(schema_name, table_name)`, or `(schema, table_name, column_name)` identifiers. Instead, prefer `schema_oid`, `table_oid` or `(table_oid, attnum)` identifiers (may require modifying callers slightly, or scaffolding).
- Delete any unneeded functions.

## Risks

- This is a major overhaul of the codebase. There's always a possibility of unforseen problems
- This will probably make the codebase less approachable for outsiders.
- The testing may be trickier (though current prototyping didn't require much changing of tests at all).
- The composition of operations involved with the data explorer will need to be carefully handled.

## Resources

TODO

## Timeline

**Note**: Parts of this timeline are delayed, since they're blocked by the removal of DDL, DML, and Brent's parental leave.

| Date       | Outcome                                      |
|------------|----------------------------------------------|
| 2023-03-20 | Prototyping work starts                      |
| 2023-05-05 | Implementation spec and prototyping complete |
| 2023-05-12 | Implementation spec approved                 |
| 2023-05-26 | All needed DQL SQL Functions written         |
| 2023-06-02 | All thin python wrappers written             |
| 2023-06-09 | Refactor and clean up complete               |
