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

### Email
- Catch up on dev mailing list

### PR reviews:
- [SQL for links creation #2986](https://github.com/centerofci/mathesar/pull/2986)
- [Add Peak Month aggregation function. #3006](https://github.com/centerofci/mathesar/pull/3006)

### Meetings
- 1:1 with Dom
- List project meeting

### RSQLA1 project work:
- Work on column alteration DDL functions
- Write belated project update email

### List project work
- Discuss with Maria how to report to the others how the project turned (is turning) out.
- Meeting Monday

### Summarization project work
- Discuss with Aritra which array summarizations we should do
- Discuss with Aritra which transforms would have good synergy with aggregations


## 2023-07-14

### Meetings
- 1:1 with Mukesh

### RSQLA1 project work:
- async with Anish about state of [SQL for links creation #2986](https://github.com/centerofci/mathesar/pull/2986)
- Worked on column alteration DDL functions

### Summarization project work
- Set up Aritra to proceed with some preprocessing to get more out of current aggregations.


## 2023-07-13

### Meetings
- 1:1 with Anish
- Summarization project meeting with Aritra and Sean

### RSQLA1 project work:
- Followed up with Anish about plan for splitting work moving forward.
- Update [project description](/en/projects/sql-ddl-operations)
- Started on Column altering DDL functions

### Summarization project work:
- Discuss with Sean and Aritra which summarization functions we want to pursue next.


## 2023-07-12

### PR Reviews:
- [SQL for links creation #2986](https://github.com/centerofci/mathesar/pull/2986) (requested changes)
- [Add Peak Day of Week aggregation function. #3004](https://github.com/centerofci/mathesar/pull/3004) (commented)

### RSQLA1 project work:
- Reviewed remaining pieces, cross-referenced with [RSQLA1: Move DDL Operations to SQL Functions #2737](https://github.com/centerofci/mathesar/issues/2737)
  - only one minor change was required; it's already pretty up-to-date
- Asynced with Anish about how to divide work

### Summarization project work
- Completed evaluation for GSoC
- Discussed compostition and so on w.r.t. summarization in [this PR](https://github.com/centerofci/mathesar/pull/3004)

### User help:
- Responded to form inquiry in [Freshdesk ticket](https://mathesar.freshdesk.com/a/tickets/733)


## 2023-07-11

This was a short day for me.


### Meetings:
- Installation Planning

### PR reviews
- [Add `Peak Time` aggregation function. #2981](https://github.com/centerofci/mathesar/pull/2981) (merged)


### RSQLA1
- Follow up on PR [Table create ddl #3016](https://github.com/centerofci/mathesar/pull/3016) (merged)

### Summarization project work:
- Back-and-forth async with Aritra about the SQL portion of his time aggregation PR.

### Installation planning:
- Thought and discussion about what to do regarding DB credential storage.


## 2023-07-10

### Meetings:
- Met with Aritra about time aggregation summarization
- 1:1 with Dom
- Met with Maria about list type

### PR reviews:
- [Add `Peak Time` aggregation function. #2981](https://github.com/centerofci/mathesar/pull/2981) (requested changes)

### Email
- Caught up on core team mailing list

### Summarization project work:
- Synced with Aritra about review of his PRs.

### List data type project work:
- Asynced with Maria about how to proceed with list type work
- Synced with Maria about List type.

### RSQLA1 Project work:
- Submitted [Table create ddl #3016](https://github.com/centerofci/mathesar/pull/3016)
- Responded to comments and feedback on the same PR.

## 2023-07-07

### Meetings:
- Sync with Mukesh
- Core team event

### List data type project work:
- Async with Maria about how to proceed with new ideas after yesterday's meeting

### PR reviews:
- [Cleaner consolidated logic for adding constraints #2976](https://github.com/centerofci/mathesar/pull/2976) (merged)
- [Add `Peak Time` aggregation function. #2981](https://github.com/centerofci/mathesar/pull/2981) (requested changes)
- [Add Peak Day of Week aggregation function. #3004](https://github.com/centerofci/mathesar/pull/3004) (requested changes)
- [Add Peak Month aggregation function. #3006](https://github.com/centerofci/mathesar/pull/3006) (requested changes)

### User help:
- Investigate and comment on [Error while update & import #3002](https://github.com/centerofci/mathesar/issues/3002)
- Open issue to improve documentation [Make permissions requirements clear for gunicorn user #3013](https://github.com/centerofci/mathesar/issues/3013)

### Summarization project work:
- PR reviews

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
