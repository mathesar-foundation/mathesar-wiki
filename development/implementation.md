---
title: Implementation
description: Notes related to implementation details.
published: true
date: 2021-04-23T11:45:31.370Z
tags: 
editor: markdown
dateCreated: 2021-04-20T20:34:57.900Z
---

This document will hold the beginnings of some notes about tech, including design and implementation ideas.

> This information is outdated and mainly preserved for historical purposes.
{.is-warning}

We'll refer to tables, schemas, databases, etc. defined by the user through the interface (as opposed to service model tables) as UD-{tables|schemas|databases|etc.}
 
# Logic placement
It's not yet clear which logic should live where. For example, we could implement "undo" logic either in PostgreSQL, or in python. If implemented in PostgreSQL, we'd get lots of tools (triggers, etc.) that could help us keep the data model consistent automatically, and ensure transactions work properly. However, this logic (i.e., any logic implemented in the DB itself) would be extremely difficult to test, and probably somewhat unapproachable for contributors. Any logic implemented in python would be more testable and approachable, but we'd lose lots of the actual DB functionality, and probably end up reimplementing things like triggers, etc.

# Multitenancy
TODO: This will be important to get correct, but we need to do some reading; this is a somewhat novel situation.

# DDL operations (Data Layer)
Recall that DDL operations are those involving creating, altering, or dropping (deleting) database objects like:
- Tables
- Views
- UDFs (functions)

The main interest we'll have in these operations in this context is to allow the user to refine or modify their data model, and have that model reflected in the underlying DB model. We'll mostly focus on table (table) creation and manipulation, since that's the main expected operation of this type.

## Goals
- User should be able to create tables
- User should be able to define tables in terms of already existing tables (e.g., joins, or by splitting columns out of a table)
- User should be able to recover previous models. For DDL ops, it's not clear this should be an "undo" flow. The user might start with one big table, normalize their DB schema to reduce repetition for some manual input, then want to see everything back on one big table again. It's more of having different models with the same underlying data.
  
## Implementation options
1. Map table creation, deletion or modification directly to underlying tables (create, drop, or alter)
	- Conceptually simple
	- Implementation of mapping new input in the original import format to the refined data model would be difficult (maybe this part could be done in python?).
	- If we avoid supporting the initial import format, this would be the "best" design (i.e., the most aligned with standard DBA practices)
	- If we want to support the initial import format, this would result in massive data duplication.
	- If we want to support the initial (or any multiple) input format, we'd need triggers all over the place to ensure data consistency.
	- Could be improved by keeping a table with a "script" of the DDL operations that transformed the initial import model into the current model.
1. Map table operations to underlying materialized views.
	- In Postgres, materialized views are standard tables, but they come with a couple of extra methods that let you regenerate them if you want.
	- Would be good, if we want to emphasize the ability to input more data in the original format and have it show up in the improved data model, since we'd be able to regenerate the tables with the new data included upon some appropriate command.
	- The previous point is only true if there are no intermediate steps or tables; otherwise, we need to either:
	 - keep the intermediate views / tables, or
	 - keep a "script" to regenerate everything
	- An alternative would be to automatically generate `WITH` statements as we create these views. It would be a bit gross SQL-wise, but would have the desired functionality.
	 - Starting from Materialized View A (MVA), with a \dt+ containing `WITH` statements to generate MVA from the original input format, we add a `WITH` statement encoding MVA, along with an appropriate query to generate MVB from MVA.
	 - It's not clear this would be functionaly distinct from keeping the "script" to regenerate everything, but it's somehow cleaner.
	 - Is it possible to use recursive CTEs to handle continued input? Research needed.
	- Would lend itself to a kind of natural analysis of the steps taken to get to the current data model.
	- Would be difficult to support both input into the improved data model, and also input in the original format. We'd have to set up some intricate system of triggers to make sure data was consistent in the various places it would be stored.
1. Map table operations to underlying (non-materialized) calculated views.
	- The triggers from the previous options would apply here as well. In fact, they'd be enforced by PostgreSQL at this point, since it won't let us insert into these views in most cases otherwise.
	- This is the "safest" route, in that we'll have the DB system there to help us enforce consistency.
	- This will feel the most performant for small(ish) data, since everything would be done lazily.
	- This will quickly become the _least_ performant option for large data sets under many circumstances, since we'd be recalculating all the transformations to produce a given data model any time it was queried.
1. Hybrid approach (Brent's favorite at the moment)

	For tables that we intend the user to be able to insert into, it might be best to use materialized views, with the intricate set of triggers in place to keep things consistent. It should be possible to iteratively generate these triggers as the user creates new tables under most (maybe all? not sure...) circumstances. For other tables, where input to the table makes no sense, we might want to just call them "views" even in the UI, and use normal views (or materialize them if desired for performance). An example of this would be a view involving aggregation of data from another table. It doesn't make sense to insert into such an aggregation.

# Data Input and Modification operations (Data Layer)
This section deals with details about importing data, adding it to tables, and modifying/deleting records from tables.

## Goals
- User should be able to insert arbitrary data into tables.
- Given a table with an appropriate column set, a user should be able to import more data to that table.
- Given a table derived from a data import (say, of a CSV), and tables derived from that table through improved data modeling, a user should be able to modify any of the views of the data (i.e., one of the normalized tables, or the original non-normalized format), and maintain consistency.
  - A user may import a spreadsheet, then refine the data model to reduce redundancy (e.g., by splitting the table according to 2NF)
  - They might still want to import more data in the original format (say from an updated version of the original source).
  - They might want to also add data manually using the improved model.
- Undo. The user should be able to undo inserts (easy), deletes (kinda easy) and updates (a little more difficult).

## Undo / Audit Implementation 
We should keep an audit table for each table/view that's modifiable in a user's database. Two options are possible for this implementation:
1. Use triggers to record logs of each modification at the DB level.
	- See https://wiki.postgresql.org/wiki/Audit_trigger_91plus
2. At the python (service) level, record each operation on the DB and its success on another table.

The advantage of (1) is that we get transactions and consistency guarantees from the DB system. However, this may involve a fair bit of logic, and it won't be tested if it's in the DB rather than python.

For the Audit table itself, our current favored options are:
1. A global audit table with one row per record that's ever existed in a user's database (or schema). The row would have an identifier for the record, and metadata about its history (and location in the DB):
	- last modified
	- created
	- modification history
2. A per-table audit table with the same info as above; easier to find relevant records, and probably a faster join with the relevant table. Downside is we can't track records split across multiple tables, or moved from table A to table B.
3. A global audit table, and a per-table audit (materialized) view for performance.
