---
title: DML Operations
description: 
published: true
date: 2023-05-11T14:30:21.936Z
tags: 
editor: markdown
dateCreated: 2021-05-07T15:16:22.341Z
---

DML (Data Manipulation Language) operations involve adding (inserting), deleting, and modifying (updating) data in a database. This section deals with details about importing data, adding it to tables, and modifying/deleting records from tables.

# Goals
- User should be able to insert arbitrary data into tables.
- Given a table with an appropriate column set, a user should be able to import more data to that table.
- Given a table derived from a data import (say, of a CSV), and tables derived from that table through improved data modeling, a user should be able to modify any of the views of the data (i.e., one of the normalized tables, or the original non-normalized format), and maintain consistency.
  - A user may import a spreadsheet, then refine the data model to reduce redundancy (e.g., by splitting the table according to 2NF)
  - They might still want to import more data in the original format (say from an updated version of the original source).
  - They might want to also add data manually using the improved model.
- Undo. The user should be able to undo inserts (easy), deletes (kinda easy) and updates (a little more difficult).

# DML Function signatures
- These (as opposed to DDL functions) are allowed mutable types (e.g., an SQLAlchemy `Table` object as input and output)
- We'll prioritize speed and efficiency over safety and accuracy for these.
  - We expect these functions to be run quite often, and for reactivity to be essential.
  - All DML operations are transactional in PostgreSQL (and indeed in the SQL standard).
  - We expect these functions to be run quite often, and for reactivity to be essential.
