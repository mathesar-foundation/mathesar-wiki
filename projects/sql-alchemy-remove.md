---
title: Remove SQLAlchemy from codebase
description: 
published: true
date: 2023-03-15T00:00:00.000Z
tags: 
editor: markdown
dateCreated: 2023-03-15T00:00:00.000Z
---

- **Name**: Remove SQLAlchemy from codebase
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

SQLAlchemy is a fantastic piece of software, but it's becoming less suitable to our needs as the project evolves. In particular, we've found it to be weak and inefficient for our use case which doesn't assume a stable underlying data model at any point. This means we have to constantly reflect the database state in order to perform operations on it, and maintaining this reflection of the database has become more and more burdensome. 

Our use of SQLAlchemy in this project is slowing down development, and indeed slowing down the performance of the app in a massive way.

## Solution

We'll remove SQLAlchemy from our codebase. Note that at the point we undertake this project, it should already be gone from all DDL, DML, and DQL operations. What remains should be only Data Definition Description Language (D3L) operations. D3L operations are those that amount to DQL operations on metadata. That is, they query for metadata about database objects. An example is "list the tables in `my_database`". Another is "List the columns in `mytable` and their types". Hopefully, most of these functions will already have been removed during previous phases, but there are some which actually pack API calls (e.g., to list the schemas in a database).

### Create D3L functions in database
Many of these will already have been created during previous phases. This should just amount to batting cleanup. But, I expect some will still need to be created.
- Each such function should be overloaded to have the signature needed for calling from Python with minimal fuss, as well as the target signature.
- Each such function should have a main implementation which uses the most reasonable signature for the task at hand.

### Replace Python D3L functions with wrappers of DB functions.
Do _not_ replace or create functions that are no longer needed. Some common sense will be required here.
- Map the original Python function signatures to an appropriate function call of the database functions.
- It's completely fine to create scaffolding functions at this point to avoid letting changes sprawl.
- After this phase, no SQLAlchemy imports should be used in any module whose functions are modified in this way, i.e., D3L operation modules.

Note that this section may take more lateral thinking than for the DDL, DML, or DQL phases. The implementers will have to be careful to remove rather than create complexity.

### Refactor and clean up results

Refactor to remove SQLAlchemy from the codebase wherever it remains, and delete any unneeded functions (e.g., scaffolding).

After this part, the following should be true:
- No SQLAlchemy anywhere
- No getting a table name in Python unless returning it via the API to the front end.
- No getting a schema name in Python unless returning it via the API to the front end.
- No getting the schema of a table in Python unless directly needed for information going to the API.

Generally, at this point, the identifiers should be OIDs and attnums, and the only reason to know any other metadata about a database object should be to return it to the API.

## Risks

- This is a major overhaul of the codebase. There's always a possibility of unforseen problems
- This part of the larger project is a where we put the final bow on things. It should be carefully reviewed for style and maintainability.

## Resources

TODO

## Timeline

**Note**: Parts of this timeline are delayed, since they're blocked by the removal of DDL, DML, DQL, and Brent's parental leave.

| Date       | Outcome                                      |
|------------|----------------------------------------------|
| 2023-03-20 | Prototyping work starts                      |
| 2023-05-12 | Implementation spec and prototyping complete |
| 2023-06-26 | Implementation spec approved                 |
| 2023-06-09 | All needed D3L SQL Functions written         |
| 2023-06-16 | All thin python wrappers written             |
| 2023-06-23 | Refactor and clean up complete               |
