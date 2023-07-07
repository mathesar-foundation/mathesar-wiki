---
title: Brent's work log
description: 
published: true
date: 2023-07-07T01:20:50.913Z
tags: 
editor: markdown
dateCreated: 2023-07-07T01:20:50.913Z
---

## Actively working on

### PR reviews:
- [Cleaner consolidated logic for adding constraints #2976](https://github.com/centerofci/mathesar/pull/2976)
- [Add `Peak Time` aggregation function. #2981](https://github.com/centerofci/mathesar/pull/2981)
- [Add Peak Day of Week aggregation function. #3004](https://github.com/centerofci/mathesar/pull/3004)
- [Add Peak Month aggregation function. #3006](https://github.com/centerofci/mathesar/pull/3006)

### Meetings:
- Sync with Mukesh
- Core team event

### RSQLA1 project work:
- Update [project description](/en/projects/sql-ddl-operations)
- Update and clean [RSQLA1: Move DDL Operations to SQL Functions #2737](https://github.com/centerofci/mathesar/issues/2737)

### List data type project work:
- Async with Maria about how to proceed with new ideas after yesterday's meeting

### Summarization project work:
- PR reviews
- Catch up with Aritra about next steps

### Installation help:
- Need to catch up briefly with Kriti about how to proceed on that under the new 'User Help' framework. Still have some pending tickets.

### Code:
- Get PR submitted for the table creation DDL SQL functions.

## 2023-07-06

### PR reviews:
- [Cleaner consolidated logic for adding constraints #2976](https://github.com/centerofci/mathesar/pull/2976)
- [Add `Peak Time` aggregation function. #2981](https://github.com/centerofci/mathesar/pull/2981)

### Meetings:
- Met with Anish w.r.t. his PR #2976, discussed how to organize the code
- Mathesar weekly meeting
- Met with Maria, Aritra, and Sean about arrays in Mathesar and how to proceed on that project.
- Met with team members about the Installation project

### Code:
- wrote some SQL layer tests for table creation SQL function.
- fixed minor bugs in the same.

### Pondering:
- Thought about how to enforce array dimensionality without relying on type system
- Thought a bit about how to wire Mathesar up to read-only databases and non-Postgres databases using Foreign Data Wrappers
