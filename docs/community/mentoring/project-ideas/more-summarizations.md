---
title: Add more summarization functions
description: Extend the summariation function options in the Data Explorer
published: true
date: 2023-07-19T23:44:26.988Z
tags: gsoc
editor: markdown
dateCreated: 2023-02-06T05:46:45.937Z
---

## Classification
- **Difficulty**: Easy
- **Skills needed**: Python, SQLAlchemy, JavaScript, Svelte, PostgreSQL
- **Length**: Medium (~175 hours)

## The Problem

The Mathesar Data Explorer enables an action called "Summarize" that let a user view a summary of their data, which is in fact an aggregation of some column(s), grouped by some other column(s). Currently, the only possible aggregation functions are counting or listing.

## Feature Description

We want to add more summarization (aggregation) functions to the Mathesar Data Explorer. The functions should either come from the [PostgreSQL aggregate functions](https://www.postgresql.org/docs/13/functions-aggregate.html), or the implementer could [create their own](https://www.postgresql.org/docs/13/sql-createaggregate.html). Functions to prioritize are:

- Summing numeric columns
- Joining array (list) columns into a single array (list)
- Merging JSON Object columns
- Statistical aggregations (Mean, Median, Max, Min)

## UX Design Problems

The only real UX issue to solve here is how to present the different options in a way that is understandable to the user. It may be that the current drop-down list needs to be enriched somehow. It's possible that the implementer could want to do an aggregation that needs some kind of presentation of the output, but that's doubtful.

## Tasks

- Determine which summarization functions to add by consulting the documentation and proposing ideas to the mentors.
- Determine whether any UI/UX concerns will arise from the chosen functions.
- Implement the back end functions for each summarization function chosen.
- Add the summarization functions to the Data Explorer UI, handling any UX concerns.

## Expected Outcome

We should have at least 3 (preferably more) new summarization functions in the Data Explorer by the end of the internship.

## Application Tips

- Demonstrate proficiency with the required skills.
- Present some preliminary research into which summarization functions make sense _and why_.
- Make sure to demonstrate an understanding of what an aggregation function does, and why they're useful.
- Try to provide examples showing why each aggregation function researched might be useful.

## Resources
- https://www.postgresql.org/docs/13/functions-aggregate.html
- https://www.postgresql.org/docs/13/sql-createaggregate.html
- https://www.postgresql.org/docs/13/xaggr.html

## Mentors
**Primary Mentor**: Brent Moran
**Secondary Mentor(s)**: Sean Colsen
