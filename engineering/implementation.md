---
title: Architecture
description: Documents describing the technical design of Mathesar
published: true
date: 2021-05-07T15:07:57.500Z
tags: 
editor: markdown
dateCreated: 2021-04-20T20:34:57.900Z
---

> This information is somewhat outdated. See the ["Architecture" category on GitHub discussions](https://github.com/centerofci/mathesar/discussions/categories/architecture) for more recent implementation notes.
{.is-warning}

This document will hold the beginnings of some notes about tech, including design and implementation ideas.

We'll refer to tables, schemas, databases, etc. defined by the user through the interface (as opposed to service model tables) as UD-{tables|schemas|databases|etc.}
 
# DDL operations (Data Layer)
Recall that DDL operations are those involving creating, altering, or dropping (deleting) database objects like:
- Tables
- Views - UDFs (functions)

The main interest we'll have in these operations in this context is to allow the user to refine or modify their data model, and have that model reflected in the underlying DB model. We'll mostly focus on table (table) creation and manipulation, since that's the main expected operation of this type.

## Goals
- User should be able to create tables
- User should be able to define tables in terms of already existing tables (e.g., joins, or by splitting columns out of a table)
- User should be able to recover previous models. For DDL ops, it's not clear this should be an "undo" flow. The user might start with one big table, normalize their DB schema to reduce repetition for some manual input, then want to see everything back on one big table again. It's more of having different models with the same underlying data.

## DDL function signatures
- Since DDL operations do not consistently support transactions, we should prioritize safety and correctness for these functions.
- In python, these functions should take non-immutable types (e.g., strings) as input, and return non-immutable types as outputs.
- Ideally, these immutable types should be strings.
  - This will enhance safety of these functions, and guarantee that they check the DB themselves for its state before commencing any changes.
  - This will also enable better composability of these functions (it's easy to chain functions together that have the same output type (or tuples of it) as input type)


# DML operations (Data Layer)
This section deals with details about importing data, adding it to tables, and modifying/deleting records from tables.

## Goals
- User should be able to insert arbitrary data into tables.
- Given a table with an appropriate column set, a user should be able to import more data to that table.
- Given a table derived from a data import (say, of a CSV), and tables derived from that table through improved data modeling, a user should be able to modify any of the views of the data (i.e., one of the normalized tables, or the original non-normalized format), and maintain consistency.
  - A user may import a spreadsheet, then refine the data model to reduce redundancy (e.g., by splitting the table according to 2NF)
  - They might still want to import more data in the original format (say from an updated version of the original source).
  - They might want to also add data manually using the improved model.
- Undo. The user should be able to undo inserts (easy), deletes (kinda easy) and updates (a little more difficult).

## DML Function signatures
- These (as opposed to DDL functions) are allowed mutable types (e.g., an SQLAlchemy `Table` object as input and output)
- We'll prioritize speed and efficiency over safety and accuracy for these.
  - We expect these functions to be run quite often, and for reactivity to be essential.
  - All DML operations are transactional in PostgreSQL (and indeed in the SQL standard).
  - We expect these functions to be run quite often, and for reactivity to be essential.
