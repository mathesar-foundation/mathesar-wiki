---
title: Automatically suggest improvements to table normalization
description: 
published: true
date: 2023-02-06T16:37:22.459Z
tags: 
editor: markdown
dateCreated: 2023-02-03T16:34:34.998Z
---

## Classification
- **Difficulty**: High
- **Skills needed**: PostgreSQL, Database theory, a bit of statistics.
- **Length**: Long (~350 hours)

## The Problem
Imagine a user imports the following data into Mathesar:

| ID | Book Title | Author |
|-|-|-|
| 1 | Matilda | Roald Dahl |
| 2 | Charlie and the Chocolate Factory | Roald Dahl |
| 3 | Catch 22 | Joseph Heller |
| 4 | James and the Giant Peach | Roald Dahl |

We have functionality that allows Mathesar users to extract columns out into a new table to help normalize data. We want to make this functionality more discoverable by suggesting columns that would be good to make their own table. In the example provided, that would be "Author", since it has the same data repeated in three records.

## Feature Description
In order to normalize a data model, one needs to understand correlations between different rows in the data of a table.  For example, if there is a column `student email` that is dependent on a proper subset of the key `(class id, student id)` in some `class_rosters` table, then a separate `students` table with columns `(student id, student email)` should be created, and `student email` should be dropped from the original `class_rosters` table. This would potentially move the data model closer to achieving the Second Normal Form (2NF). We need to build functions that notice this sort of correlations.  Ideally, we'd start with functions that notice when a relation is not in 2NF (but _is_ in 1NF), and suggest fixes. If that's achieved, we'd then proceed to suggest fixes to achieve 3NF.

## Tasks
- Research method of automatically determining the violating correlations disallowed by 2NF.
- Research whether a "hard rule" makes more sense, or whether it makes more sense to have some correlation score.
- Based on answers to the above, implement functionality so that we can call a Python function that takes a table as input, and returns sets of columns that could be extracted.

Repeat with 3NF as the goal.

If time permits, you can also:
- Create an API that exposes this functionality. Given a table, the API should provide normalization suggestions for that table.
- Create the UI that displays these suggestions in the product.

## Expected Outcome
We should end up with Python functions backed by SQL that let us determine whether a relation in a DB is in 2NF (or 3NF), and suggest column sets to extract to separate tables that would promote the data model to a higher normal form (at least the subset of the data model involving the relation in question).

We'd also like an API that exposes these functions and frontend work to display normalization suggestions in the UI, but these can be treated as stretch goals.

## Application Tips
The successful candidate would understand the motivation for normalizing a database. They'd also understand some basics about stats and be able to relate the idea of correlations between columns of a table to how different sets of columns might be able to be extracted.

## Resources
- [Research report on this topic written by a previous intern](https://docs.google.com/document/d/11IrRS3Et9pybmDcuLroQfN75S6V3YjdaQU4ExKVFXnM/edit#heading=h.kk1966kbedef)

## Mentors
**Primary Mentor**: Brent
**Secondary Mentor(s)**: Dom
