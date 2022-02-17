---
title: Suggest Candidate Columns to Create Separate Table
description: 
published: true
date: 2022-02-17T23:37:52.610Z
tags: 
editor: markdown
dateCreated: 2022-02-08T23:58:51.504Z
---

## The Problem
> This is related to [Break Columns out to New Table](/en/community/mentoring/project-ideas/break-out-columns), please read that project idea first.
{.is-info}


In order to normalize a data model, one needs to understand correlations between different rows in the data of a table.  For example, if there is a column `student email` that is dependent on a proper subset of the key `(class id, student id)` in some `class_rosters` table, then a separate `students` table with columns `(student id, student email)` should be created, and `student email` should be dropped from the original `class_rosters` table. This would potentially move the data model closer to achieving the Second Normal Form (2NF). We need to build functions that notice this sort of correlations.  Ideally, we'd start with functions that notice when a relation is not in 2NF (but _is_ in 1NF), and suggest fixes. If that's achieved, we'd then proceed to suggest fixes to achieve 3NF.

## Classification
- **Difficulty**: *High*
- **Skills needed**: PostgreSQL, Database theory, a bit of statistics.
- **Length**: Long (~350 hours)

## Tasks
- Research method of automatically determining the violating correlations disallowed by 2NF.
- Research whether a "hard rule" makes more sense, or whether it makes more sense to have some correlation score.
- Based on answers to the above, implement functionality so that we can call a python function that takes a table as input, and returns sets of columns that could be extracted.
- Repeat with 3NF as the goal.

## Expected Outcome
We should end up with python functions backed by SQL that let us determine whether a relation in a DB is in 2NF (or 3NF), and suggest column sets to extract to separate tables that would promote the data model to a higher normal form (at least the subset of the data model involving the relation in question).

## Application Tips
The successful candidate would understand the motivation for normalizing a database. They'd also understand some basics about stats and be able to relate the idea of correlations between columns of a table to how different sets of columns might be able to be extracted.

## Resources
- [relevant code](https://github.com/centerofci/mathesar/blob/afac35483cd56626778acf01df41cae9423636d5/db/tables/operations/split.py)
- [relevant tests](https://github.com/centerofci/mathesar/blob/afac35483cd56626778acf01df41cae9423636d5/db/tests/tables/operations/test_split.py)
- [Database normalization wikipedia page](https://en.wikipedia.org/wiki/Database_normalization)

## Mentors
- **Primary Mentor**: Brent Moran
- **Backup Mentor**: Kriti Godey

See our [Team Members](/en/team/members) page for Matrix and GitHub handles of mentors.