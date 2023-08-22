---
title: Brent's work log
description: 
published: true
date: 2023-07-20T02:44:18.336Z
tags: 
editor: markdown
dateCreated: 2023-07-07T01:56:13.743Z
---

## Actively working on

### Meetings
- 1:1 with Anish
- 1:1 with Aritra

### Release 0.1.3
- Making images
- Testing release

### Projects
- Going back through RSQLA 2, 3, 4 writeups and updating them

### Preexisting DB compatibility
- Start organizing some basic meta issues around known problems (we can add more)

### User help
- Conduct a round of follow-up with various users.

## 2023-08-23

### Meetings
- Team meeting

### Email
- *yet another* round of communication on various threads

### RSQLA1
- Started RSQLA1 email thread

### Preexisting DB compatibility
- followed leads from Sean, also found other sample DBs to test against
- Chatted with Kriti about hosting test DBs

## 2023-08-22

### Email
- Another round of discussion participation

### RSQLA1
- Worked on composing retrospective email

### Preexisting DB compatibility
- Minor change to project organization
- Going through Sean's feedback email w.r.t. realistic DB examples, trying to find others

## 2023-08-22

### Email
- More participation in massive email threads

### Bugfixes
- Fixed bug occurring due to upstream testing suite change.

## 2023-08-21

### Meetings
- 1:1 with Dom
- make-up meeting with Aritra

### Preexisting DB compatibility 
- Planning/looking through GH issues

### Email
- went through email, thinking and contributing to massive email threads

## 2023-08-18

### RSQLA1
- Finished clean up of meta issue

### Preexisting DB compatibility
- incorporated feedback from discussion into project
- started basic going through GH looking for related issues

## 2023-08-16

### RSQLA1
- Partial clean up of RSQLA1 meta issue

### Meetings
- Niche research discussion
- 1:1 with Anish

## 2023-08-15

### Projects
- Finished first draft of DB compatibility investigation project.

### PR reviews
- [Fix NaN:NaN error while aggregating duration column #3136](https://github.com/centerofci/mathesar/pull/3136) (merged)
- [Tests for alter table #3139](https://github.com/centerofci/mathesar/pull/3139)

### SQL code update functionality
- Tested to make sure there are no problems updating from v0.1.2 to current develop w.r.t. SQL code changes.

### Comms
- Wrote email about managing package versions


## 2023-08-14

### Meetings
- (very long) 1:1 with Dom

### Projects
- asynced with Ghislaine to set up meeting for niche research project
- Started draft of "Postgres DB compatibility investigation" project


## 2023-08-11

### Misc research
- Deep dive into ramifications of installing things on the DB, or avoiding it.

### Comms
- Start email thread on dev mailing list for “Should we install things on the DB?” discussion


## 2023-08-10

### Meetings
- 1:1 with Anish
- Team meeting
- Summarization project meeting with Aritra


### Comms
- Wrote up thoughts about whether we should install things on the DB
- Wrote up thoughts about Column moving project
- Other meeting prep

## 2023-08-09

### Meetings
- 1:1 with Dom
- Weekly meeting

### Projects
- Wrote up project proposal draft for finishing and improving column extraction/moving and table merging logic

### SQL updating
- Made a prototype to experiment with dropping old SQL functions with manual cascade for safety


## 2023-08-08

### Meetings
- Long catch up with Mukesh about his open PRs, and column moving logic

### Comms
- Cleared out email inbox
- Cleared out GH inbox
- Wrote/sent update for RSQLA1
- Wrote long email about project ideas
- Async discussion with Anish about what he could work on during the cool down

## 2023-08-07

### Meetings
- Met with Ghislaine about use cases

### PR reviews
- [Remove db superuser requirement #3117](https://github.com/centerofci/mathesar/pull/3117) (approved; awating product approval)
- [Wiring sql functions for links and tables #3130](https://github.com/centerofci/mathesar/pull/3130) (merged)

## 2023-08-04

### Meetings
- 1:1 with Dom w.r.t. dynamic defaults
- 1:1 with Mukesh
- Core team event

### RSQLA1
- Fixed an issue with column altering for Anish's PR
- Added comments and merged [Move table splitting logic to SQL #3119](https://github.com/centerofci/mathesar/pull/3119)
- Did a deep dive into column merging logic; determined that moving it to SQL is a bad idea at this juncture.


## 2023-08-03

This was a short day for me

### PR reviews
- [Add pldebugger to dev db #3126](https://github.com/centerofci/mathesar/pull/3126)
- [Add Postgres to Mathesar docker image #3121](https://github.com/centerofci/mathesar/pull/3121)

### Meetings
- 1:1 with Anish

## 2023-08-02

### Meetings
- ad-hoc catch up with Mukesh to discuss data losing bug in column merging logic
- Team meeting

### PR reviews
- [Tests for links & constraints ddl #3120](https://github.com/centerofci/mathesar/pull/3120) (merged)

### RSQLA1 project work
- Found bug in column moving logic, discussed with Mukesh, made plan for proceeding
- Fixed another bug with PR: [Properly detect identity columns #3125](https://github.com/centerofci/mathesar/pull/3125)

### Bugfixes
- PR [Repeat failed tests #3118](https://github.com/centerofci/mathesar/pull/3118) is merged after some chnages
  
### Ad-hoc
- Helped Rajat with how to install `gettext` in containers for his translations project.


## 2023-08-01

### Meetings
- 1:1 with Kriti

### Misc. Bugfixes
- Started PR [Repeat failed tests #3118](https://github.com/centerofci/mathesar/pull/3118) to sort out intermittent test failures

### PR Reviews
- [Remove db superuser requirement #3117](https://github.com/centerofci/mathesar/pull/3117)

### RSQLA1
- Submitted PR [Move table splitting logic to SQL #3119](https://github.com/centerofci/mathesar/pull/3119)


## 2023-07-31

### Bugfixes
- Made a quick PR [New linting rule #3116](https://github.com/centerofci/mathesar/pull/3116#event-9965300582) to fix an issue arising from an update in `flake8`.

### PR Reviews
- [SQL tests for schema ddl #3098](https://github.com/centerofci/mathesar/pull/3098) (merged)
- [Fix the error when list aggregation on mathesar custom array #3106](https://github.com/centerofci/mathesar/pull/3106)

### 2023-07-28

### Meetings
- Caught up with Anish
- 1:1 with Mukesh
- Installation planning meeting V

### RSQLA1 project work:
- Got table splitting working, but exposed a bug in how defaults are reflected.
- Organized next week's work with Anish

### User help
- Submitted PR [Remove pglast, use SQL function instead #3107](https://github.com/centerofci/mathesar/pull/3107), fixing [Does not work on windows #2961](https://github.com/centerofci/mathesar/issues/2961)

## 2023-07-27

### Meetings
- Summarization project meeting

### Summarization project work
- Meeting with Aritra and Sean
- Helped Aritra sort out weird bug when aggregating custom types to arrays.

### RSQLA1 Project work:
- Started on table splitting functions


### 2023-07-26

This was a short day; I got trapped in town for awhile.

### Meetings
- 1:1 with Dom
- Team meeting

### Comms
- Caught up on email and messaging

### GH admin:
- commented on and read through relevant issues

### RSQLA1 project work:
- Discussed PR with Dom.
- Merged PR: [Add DDL functions for altering columns #3097](https://github.com/centerofci/mathesar/pull/3097).

### List project work
- Read through Maria's slides and report; offered feedback

## 2023-07-25

### RSQLA1 project work:
- Submitted PR: [Add DDL functions for altering columns #3097](https://github.com/centerofci/mathesar/pull/3097)
- Caught up with Anish about his progress.


## 2023-07-24

### Github admin
- cleared out GH inbox to make it useful again

### RSQLA1 project work:
- Discovered and fixed tricky bug in type string builder function.

### PR reviews
- [Add Peak Month aggregation function. #3006](https://github.com/centerofci/mathesar/pull/3006) (merged)
- [Add SQL files to the pytest workflow #3082](https://github.com/centerofci/mathesar/pull/3082) (merged)

### List project work
- Read through Maria's report for the list project, provide feedback
- Asynced with Maria about report write-up and presentation


## 2023-07-21

### Meetings
- 1:1 with Mukesh

### RSQLA1 project work:
- Getting python layer for column alteration DDL organized, tested.

### List project work
- Caught up with Maria about report, and her plans for presenting in team meeting next week

### Summarization work
- Participated in the [email thread](https://groups.google.com/a/mathesar.org/g/mathesar-developers/c/oLPQWtxYXg8/m/YCd_wVm8BQAJ) about preproc functions.


## 2023-07-20

### Meetings
- 1:1 with Anish
- Summarization project meeting

### Infrastructure
- Create issue for automating internal.mathesar.org deployment.

### Summarization project
- Meeting about summarizations; will proceed with a couple of list aggregations
- Discussed how to proceed with Kriti async.

## 2023-07-19

### Meetings
- Team meeting

### PR reviews
- [Add Peak Month aggregation function. #3006](https://github.com/centerofci/mathesar/pull/3006) (requested changes)
- [SQL for links creation #2986](https://github.com/centerofci/mathesar/pull/2986)

### RSQLA1 Project work
- Tidying up and documenting column alteration DDL SQL functions

### Infrastructure
- updating internal.mathesar.org to newest `develop` version.

### User help
- Did a quick look through code using `pglast` and replied to [Does not work on windows #2961](https://github.com/centerofci/mathesar/issues/2961)


## 2023-07-18

This day was heads-down coding.

### RSQLA1 project work:
- Worked on column alteration DDL functions


## 2023-07-17

### Misc email
- Caught up on developer mailing list

### Meetings
- 1:1 with Dom
- List project meeting with Maria

### RSQLA1 project work:
- Sent project update email
- Worked on column alteration DDL functions

### List project work
- Discussed with Maria how to report to the others how the project turned (is turning) out.

### Summarization project work
- Caught up on preproc discussion on Matrix channel.


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