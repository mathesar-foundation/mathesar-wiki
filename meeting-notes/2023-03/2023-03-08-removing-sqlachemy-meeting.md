---
title: Removing SQLAlchemy meeting 2023-03-08
description: 
published: true
date: 2023-07-19T23:32:39.678Z
tags: 
editor: markdown
dateCreated: 2023-03-08T15:38:12.185Z
---

Related to the "Removing SQLAlchemy" project, I think it would be good to get the back end team together to look at the 'big picture' w.r.t. performance and cleanliness in the back end of Mathesar. 

## Get buy-in on getting rid of SQLAlchemy

Proceeding with this project is going to be a huge pain. We should make sure we're all committed.

- SQLAlchemy enforces maintaining state in the Python layer
- We _want_ to not maintain that state
    - No Table objects (for state)
    - No Column objects (for state)
- SQLAlchemy is 'fat', opaque, stateful and too magic (Dom)
- Removing SQLAlchemy and have less or no states are two different problem
    - SQLAlchemy is the reason for the massive performance problems we have
    - Maintaining a state can also be done without SQLAlchemy and we might end up needing it based on our alogorithms and usecases(for exmaple, compiling a summary templates).
- Maintaining a state has more impact on developer velocity than the performance.

## Deal with concerns about removing SQLAlchemy 

We need to brainstorm about what problems this will entail, and figure out how to deal with them.

- Much harder to support dbs beyond Postgres
- If we keep OIDs as DB-level IDs, 
    - we will need to create some infrastructure on Postgres to translate between oids and names
- We'll have to write a query builder (or choose a suitable one)
- Makes the project less approachable
- It's currently everywhere in the codebase (VERY large project)
- We need to replace every possible piece of SQLAlchemy _that we use_.

## Can we split the "Remove SQLAlchemy" project?

If we split it, each piece should be self-contained and valuable by itself.

- Create SQLAlchemy-free translation between OIDs and Names


- From Dom's [email](https://groups.google.com/a/mathesar.org/g/mathesar-developers/c/9o5sPaqmups/m/I6iPSkHSBQAJ):
    - Reduce our Django code; use database identifiers on the frontend
    - Use only Postgres permissions for permissions
    - Replace SQLAlchemy with Psycopg3

## Dependencies discussion

What dependencies are there between the removal of SQLALchemy and other back end work?

## Brainstorm other possible performance improvements

(only if time)

We should keep these improvements focused on the back end, and take as an assumption that we're removing SQLAlchemy.

- Don't use OIDs in the code base
    - avoids a reflection round trip the easy way
    - Makes it impossible to have the front end update a renamed table with a new name (or does it?)
- Don't use Django IDs (for identifying database objects)


### Notes

- Removing SQLAlchemy and having less/no state are two different problem
    - SQLAlchemy is the reason for the massive performance problems we have
    - Maintaining a state can also be done without SQLAlchemy and we might end up needing it based on our alogorithms and usecases(for exmaple, compiling a summary templates). 
- Maintaining a state has more impact on developer velocity than the performance and Trying to fix both the problems will be a big undertaking and might take a long time.
- Suggestion (Mukesh): We can have a simple datastructure which would hold only the properties of database object and will contain functions that can abstract away the oid <-> name conversion logic as a replacement.
- We need to come up with a alternate for the replacing SQLAlchemy. None of the querybuilders fit with our requirement based on Brent's research and Mukesh agreed with it.