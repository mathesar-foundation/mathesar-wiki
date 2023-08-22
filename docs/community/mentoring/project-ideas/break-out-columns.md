---
title: Break Columns out to New Table
description: 
published: true
date: 2023-07-19T23:42:18.655Z
tags: 
editor: markdown
dateCreated: 2022-02-08T23:55:59.574Z
---

## The Problem
One of Mathesar's goals is to encourage users to store data in [normalized](https://en.wikipedia.org/wiki/Database_normalization) tables. However, users that are not familiar with relational databases may not set up their data correctly to begin with.

A user may have a column in their table which would be better as a separate table, linked by a foreign key relationship. For example, if they have a `Students` table in a database for a school district with a `School Name` column, it's likely that such a column could be a separate `Schools` table, and the students would be linked to their schools by a foreign key in the `Students` table linking to the primary key in the `Schools` table. Setting this up by hand would be tedious.

## Classification
- **Difficulty**: Easy
- **Skills needed**: PostgreSQL, Python, Pytest, Django
- **Length**: Medium (~175 hours)

## Tasks
- Determine the current state of the solution in the code base in the `db/tables/operations/split.py` file.
- Double check the tests for the current solution and find any bugs.
- Fix any bugs found, add tests if needed.
- Connect the splitting functionality to the API so it can be called.
- If there's time, we will also attack the table merging logic in the `db/tables/operations/merge.py` file.

## Expected Outcome
There should be an appropriate API endpoint (to be determined in collaboration with the Mathesar team) that lets a caller give a `database`, `schema`, `table`, and `column` as either a query parameter string or POST (depending on the design we choose).  The result should be the extraction of the column, creation of a new table consisting of a copy of that column (including data) plus the default Mathesar `id` primary key column, and the replacement of the extracted column in the original table with a foreign key column linking to the `id` column of the new table.  The foreign key column should be populated so that the natural join between the original and new tables results in the extracted data being matched up with the rows of the original table correctly.

## Application Tips
The successful candidate will be able to understand and articulate the usefulness of automatically extracting a column to a separate table. They'd thus be able to design and implement tests that ensure the expected behavior is actually satisfied by the current functions.  Finally, they'd either know or be willing to learn about Django in order to be able to wire things up.

## Resources
- [relevant code](https://github.com/centerofci/mathesar/blob/afac35483cd56626778acf01df41cae9423636d5/db/tables/operations/split.py)
- [relevant tests](https://github.com/centerofci/mathesar/blob/afac35483cd56626778acf01df41cae9423636d5/db/tests/tables/operations/test_split.py)

## Mentors
- **Primary Mentor**: Brent Moran
- **Backup Mentor**: Kriti Godey

See our [Team Members](/en/team/members) page for Matrix and GitHub handles of mentors.
