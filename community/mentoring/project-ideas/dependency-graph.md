---
title: Construct Dependency Graph for Database Objects
description: 
published: true
date: 2022-02-17T23:45:43.592Z
tags: 
editor: markdown
dateCreated: 2022-02-09T00:12:13.312Z
---

## The Problem
We'd like to be able to know what other database objects depend on a database object like a Schema or a Table.

This is useful in various situations
- To show to the user in the frontend before they decide to delete a `Schema` or a `Table`.
- To show how a `View` was constructed 
- To get a high level overview of the Data Model

## Classification
- **Difficulty**: Medium
- **Primary Skills needed**: PostgreSQL, Python, Pytest, Django
- Secondary skills needed (or willing to learn): UX design, Front End Development Knowledge
- **Length**: Long (~350 hours)

## Tasks
- Build a python API to query for a database object dependency.
- Extract dependency information from [System Catalog tables](https://www.postgresql.org/docs/8.4/catalogs.html) for the queried object
- System Catalog Tables does not contain the dependency information of a function as functions are stored as text on the database. So [pglast](https://github.com/lelit/pglast) should be used to extract dependency information from the function body.
- Build Dependency graph based on the dependency information.
- Add Django dependency API to resources [listed in this issue](https://github.com/centerofci/mathesar/issues/398), making use of the underlying python dependency API

### Bonus Tasks
- UI Graph View - Using the Dependency API, create a component on the frontend to visualize the dependency graph.

## Expected Outcome
There should an appropriate python api backed by SQL functions which would take in the `oid` or `name` of the database object whose dependency graph has to be constructed along with some filtering parameters to limit the listed dependent objects and return a hierarchical dependency graph which contains information of the dependent object. The dependency query varies based on the type of the database object, so the queries for each type should be split into composable `CTE` for readability.   

## Application Tips
A good candidate would be someone who has good understanding of SQL, and align themselves with the goals of Mathesar. They should be willing to do a fair amount of research both in terms of UX and engineering. They will be working full-stack and would either know or be motivated to learn the necessary technologies in order to complete the project.

## Resources
- [Reference code](https://wiki.postgresql.org/wiki/Pg_depend_display)
- [Relevant discussion](https://github.com/centerofci/mathesar/issues/398)

## Mentors
- **Primary Mentor**: Mukesh Murali
- **Backup Mentor**: Brent Moran

See our [Team Members](/en/team/members) page for Matrix and GitHub handles of mentors.
