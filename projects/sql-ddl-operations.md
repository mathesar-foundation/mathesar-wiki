---
title: Move DDL Operations to SQL Functions
description: 
published: true
date: 2023-04-10T14:11:43.471Z
tags: 
editor: markdown
dateCreated: 2023-03-23T08:31:13.306Z
---

- **Name**: Move DDL operations to SQL functions
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

Data Definition Language (DDL) operations are those that manipulate the actual data model on the database. Some relevant SQL words are `CREATE`, `ALTER`, and `DROP`. These operations require knowledge of the database to do their work. E.g., a function must know the name of a table to `ALTER` it. Our current architecture requires reflecting the state of the database into memory in Python, then manipulating that state's representation in Python, then stamping that representation back down onto the database.

Our current setup for this is:
- Inefficient (reflection is slow)
- Complicated (hard to maintain)
- Prone to bugs (managing state in Python memory is constantly tripping us up)

All of these problems are related to the fact that we're building the SQL queries to run DDL operations in Python.

## Solution

### Create DDL functions in database
Create a function for each desired DDL operation on the databse using SQL or PL/pgSQL.
- Each such function should be overloaded to have the signature needed for calling from Python with minimal fuss.
- Each such function should have a main implementation which uses the most reasonable signature for the task at hand.

### Replace Python DDL functions with wrappers of DB functions
Replace the current Python functions performing DDL operations with thin wrappers for these functions.
- Be mindful of looking out for functions which may be deleted, rather than replaced, once this is done.
- Map the original Python function signatures to an appropriate function call of the database functions.
- It's completely fine to create scaffolding functions at this point to avoid letting changes sprawl.
- After this phase, no SQLAlchemy imports should be used in any module whose functions are modified in this way, i.e., DDL operation modules.

### Refactor and clean up results
Refactor to remove SQLAlchemy objects from calls using Python DDL functions:
- Remove any SQLAlchemy objects from DDL function signatures (This may require modifying callers slightly)
- Remove SQLAlchemy from the entire call stack calling a given function, all the way up to the API (within reason).
- Modify affected function signatures to avoid using `schema_name`, `(schema_name, table_name)`, or `(schema, table_name, column_name)` identifiers. Instead, prefer `schema_oid`, `table_oid` or `(table_oid, attnum)` identifiers (may require modifying callers slightly, or scaffolding).
- Delete any unneeded functions.

## Risks

- This is a major overhaul of the codebase. There's always a possibility of unforseen problems
- This will probably make the codebase less approachable for outsiders.
- The testing may be trickier (though current prototyping didn't require much changing of tests at all).

## Resources

[Meta-issue tracking this project](https://github.com/centerofci/mathesar/issues/2737)

## Timeline

**Note**: Parts of this timeline are delayed due to Brent's parental leave.

| Date       | Outcome                                      |
|------------|----------------------------------------------|
| 2023-03-20 | Work starts                                  |
| 2023-03-24 | Implementation spec and prototyping complete |
| 2023-03-31 | Implementation spec approved                 |
| 2023-04-28 | All needed DDL SQL Functions written         |
| 2023-05-05 | All thin python wrappers written             |
| 2023-05-12 | Refactor and clean up complete               |
