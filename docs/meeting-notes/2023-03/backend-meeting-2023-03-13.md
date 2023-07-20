---
title: Backend meeting 2023-03-13
description: 
published: true
date: 2023-05-11T14:47:32.350Z
tags: 
editor: markdown
dateCreated: 2023-03-13T17:00:56.033Z
---

**Date**: 2023-03-13
**Attendees**: Anish, Brent, Dominkyas, Mukesh, Sean


- Brent - Having gone back and forth between oids and names, it looks like solving this issue or figuring our the solution won't be a easy and quick task. So we should be okay with having a data structure as mentioned by Dom in his email
- Dom - When will the tuple be converted.
- Brent - Have converter function that converts oid/names -> data structure. Will be useful in case we want to 
- Sean - Moving to names will be heavier lift.
- From product perspective, we should be open for concurrent operations(realtime collaboration) . So we can't use names
- It would be better if we can have one datastructure throughout the frontend till the database functions. But having the conversion on the database might be a pain.
- Having a datastructure doesn't seem to give a proper value add
- It also needs a conversion on the database, similar to using `oid` and have postgres functions convert it but more painful as it needs a frontend changes too.
- Move possible python functions to Postgres functions
- We are learning the features to implement based user feedback. So the solution should be flexible. 

Action Items
- Figure out the functions that can be moved to postgres and write issues - Anish & Brent
- Figure out how we want to write SQL in python - Mukesh
- Figure out how to introduce `oid, names, attnum` data structure - Brent
- Kicking holes in issues and ideas: Figuring out the pros/cons of these things. - Dom 