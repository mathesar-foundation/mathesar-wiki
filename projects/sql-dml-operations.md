---
title: Move DML Operations to SQL Functions
description: 
published: true
date: 2023-03-15T00:00:00.000Z
tags: 
editor: markdown
dateCreated: 2023-03-15T00:00:00.000Z
---

- **Name**: Move DML Operations to SQL Functions
- **Status**: Draft
- **Theme**: Code quality, maintainability, performance, Removing SQLAlchemy

## Team

| Role                           | Assignee | Notes                                               |
|--------------------------------|----------|-----------------------------------------------------|
| **Owner**                      | Brent    |                                                     |
| **Approver (project plan)**    | Kriti    | *Needs to approve project plan*                     |
| **Approver (backend)**         | Dom      | *Needs to approve back end spec*                    |
| **Approver (backend)**         | Brent    | *Needs to approve back end spec*                    |
| **Contributor (requirements)** | Brent    | *Creates product spec, requirements, GitHub issues* |
| **Contributor (requirements)** | Dom      | *Creates product spec, requirements, GitHub issues* |
| **Contributor**                | Anish    | *Coding and reviewing*                              |
| **Contributor**                | Dom      | *Coding and reviewing*                              |
| **Contributor**                | Mukesh   | *Coding and reviewing*                              |

## Problem

Data Manipulation Language (DML) operations are those that manipulate the data stored in a database. Some relevant SQL words are `UPDATE`, `INSERT`, and `DELETE`. These operations require knowledge of the database to do their work. E.g., a function must know the name of a table to `INSERT` into it. Our current architecture requires reflecting the state of the database into memory in Python and using that state to build `INSERT` queries and the like.

Our current setup for this is:
- Inefficient (reflection is slow)
- Complicated (hard to maintain)
- Prone to bugs (managing state in Python memory is constantly tripping us up)

All of these problems are related to the fact that we're building the SQL queries to run DML operations in Python.

## Solution

### Create DML functions in database
Create a function for each desired DML operation on the databse using SQL or PL/pgSQL.
- Each such function should be overloaded to have the signature needed for calling from Python with minimal fuss, as well as the target signature.
- Each such function should have a main implementation which uses the most reasonable signature for the task at hand.

### Replace Python DML functions with wrappers of DB functions
Replace the current Python functions performing DML operations with thin wrappers for these functions.
- Be mindful of looking out for functions which may be deleted, rather than replaced, once this is done.
- Map the original Python function signatures to an appropriate function call of the database functions.
- It's completely fine to create scaffolding functions at this point to avoid letting changes sprawl.
- After this phase, no SQLAlchemy imports should be used in any module whose functions are modified in this way, i.e., DML operation modules.

### Refactor and clean up results
Refactor to remove SQLAlchemy objects from calls using Python DML functions:
- Remove any SQLAlchemy objects from DML function signatures (This may require modifying callers slightly)
- Remove SQLAlchemy from the entire call stack calling a given function, all the way up to the API (within reason).
- Modify affected function signatures to avoid using `schema_name`, `(schema_name, table_name)`, or `(schema, table_name, column_name)` identifiers. Instead, prefer `schema_oid`, `table_oid` or `(table_oid, attnum)` identifiers (may require modifying callers slightly, or scaffolding).
- Delete any unneeded functions.

## Risks

- This is a major overhaul of the codebase. There's always a possibility of unforseen problems
- This will probably make the codebase less approachable for outsiders.
- The testing may be trickier (though current prototyping didn't require much changing of tests at all).

## Resources

TODO

## Timeline

**Note**: Parts of this timeline are delayed, since they're blocked by the removal of DDL, and Brent's parental leave.

| Date       | Outcome                                      |
|------------|----------------------------------------------|
| 2023-03-20 | Prototyping work starts                      |
| 2023-04-28 | Implementation spec and prototyping complete |
| 2023-05-05 | Implementation spec approved                 |
| 2023-05-12 | All needed DML SQL Functions written         |
| 2023-05-19 | All thin python wrappers written             |
| 2023-05-26 | Refactor and clean up complete               |
