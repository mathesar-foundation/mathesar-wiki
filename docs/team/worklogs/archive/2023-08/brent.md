# Brent's work log archive: 2023-08

## 2023-08-31

I've been lax about filling these in for a few days. My work has involved 

- the release, 
- hunting related bugs, and 
- deployment of the release. 

I'm resetting to get back on track.

### Meetings
- Met with Ghislaine to discuss user niche

### Deployment
- Deployed new version to mathesar.ito.com
- Deployed new version to cci.mathesar.org
- Double-checked staging.mathesar.org
- Worked on demo deployment

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
- PR [Repeat failed tests #3118](https://github.com/mathesar-foundation/mathesar/pull/3118) is merged after some changes
  
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

