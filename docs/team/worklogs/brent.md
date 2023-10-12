# Brent's work log

## Actively working on

### Meetings

- 1:1 with Anish

### Infrastructure

- Update internal Mathesar installation

### Preexisting DB compatibility

- Splitting findings into projects with 'themes' so we can prioritize.

### Architecture

- Putting notes together into something coherent and consumable by others

### Marketing

- Keeping an eye on Syften notifications

## 2023-10-12

### Infrastructure

- Helped user with questions about AWS setup
- Updated internal Mathesar installation

## 2023-10-11

### Marketing

- Cleared out Syften notifications

### Self-improvement

- Read CRM docs

### Architecture

- Asynced with Mukesh about Serializers and access control in our app
- Did some more investiation and note-taking about current status of code base, changes

## 2023-10-10

### Architecture

- Asynced with Mukesh about python versions we need to support, and the implications of that
- Experimented with async options, looked at where it would be useful; ultimately decided it's not needed/useful (yet)
- Finished cataloging model data, redesigning model setup
- Looked into whether serializers will remain useful (a bit, in some cases)

### Infrastructure

- Checked internal installation; no update needed

## 2023-10-09

### Marketing

- Looked through posts about setting Mathesar up on AWS
- cleared out Syften notifications

### Architecture

- I'm confident at this point that the team supports having a tech architecture, minimizing state
- Talked with Dom about Connections, storing them, caching engines
  - SQLAlchemy engines are overcomplicated
  - Psycopg3 ones are simpler
- Incorporated ideas from other backend devs into architecture designs somewhat (ongoing)

## 2023-10-06

### Meetings

- 1:1 with Pavish
- 1:1 with Mukesh
- user call with Kriti

### Infrastructure

- Updated internal Mathesar installation

### Architecture

- Modified architecture ideas according to conversations with Mukesh and Pavish
- Took notes on
  - Ideas for more RPC-style setup for some endpoints
  - Ideas for DB connection handling

## 2023-10-05

### Marketing

- Cleared out Syften notifications

### Infrastructure

- Updated internal Mathesar installation

### Architecture

- Started comprehensive catalog of all metadata stored in models, notes on simplifications and modifications.
- Minor async discussions with team members to clarify my understanding of some parts of code base.

### Meetings

- 1:1 with Anish
- Team meeting

## 2023-10-04

### Infrastructure

- Quick one-off work to let Sean access the matrix DB

### Architecture

- Looked through serializers and viewsets, determining how we can simplify
- Async conversations to clarify my understanding of some complex software design choices.

### Email/messages

- Caught up on some developer conversations

## 2023-10-03

### Architecture

- Spent most of the day going through models, noting what we store vs. get from DB
- Took a "big picture" look at how requests move from the API down to the user DB(s) and back

### Meetings

- 1:1 with Kriti

### Marketing

- Cleared out Syften notifications

## 2023-10-02

Still dealing with tail end of moving disruption. Should be more productive, but still not 100%.

### Meetings

- 1:1 with Dom
- Asyced (a bit) with Mukesh

### Email/messages

- Responded to cycle retrospective
- Responded to question about installation

### User help

- Looked at installation request submission, messaged Kriti with recommendations

### Marketing

- Cleared out Syften notifications

## 2023-09-29

Still moving boxes around; not much desk time. 

### Infrastructure

- Checked status of internal Mathesar installation; no update required

### Marketing

- Cleared out Syften notifications

### Architecture

- Did some thinking about a "dream architecture" for Mathesar while moving boxes

## 2023-09-28

Still moving boxes around; not much desk time. 

### Meetings

- 1:1 with Anish; discussed architecture plans
- 1:1 with Pavish; talked about E2E testing project.

## 2023-09-27

Today was moving day. Attended meetings and did some thinking while carrying boxes.

## 2023-09-26

### Messaging, admin

- Brought Kriti's attention to domain renewal notice when she returns (probable phishing attempt).
- Participated in email threads

### Architecture

- Worked out more details of new architecture proposal

## 2023-09-25

### Misc. projects

- Wrote up stub project for avoiding regressions

### Email/messages

- Started conversation about handling permissions issues

### Marketing

- Went through Syften notifications

### Infrastructure

- Updated internal.mathesar.org
- Wrote meeting agenda item about setting up an infrastructure ongoing responsibility

## 2023-09-22

### Infrastructure

- updated internal Mathesar installation

### Meetings

- 1:1 with Mukesh

### Preexisting DB compatibility

- Worked on splitting into themed projects

### PR reviews

- https://github.com/centerofci/mathesar/pull/3121 (approved; merged)


## 2023-09-21

### Meetings

- 1:1 with Sean

### PR reviews

- https://github.com/centerofci/mathesar/pull/3121 (requested changes)

### Infrastructure

- Updated internal Mathesar installation

### Marketing

- Looked through Syften notifications

### Preexisting DB compatibility

- Worked on themed projects.
- Created local method for testing Mathesar performance under different network latency assumptions.

## 2023-09-20

### Infrastructure

- Updated internal Mathesar installation

### Preexisting DB compatibility

- Sent email with instructions for when https://github.com/centerofci/mathesar/pull/3206 gets merged
- Sent project update email
- Worked on performance testing, 
- Worked on splitting findings into themed projects

### Marketing

- Cleared out Syften notifications, noted a pattern on the marketing channel

## 2023-09-19

### Marketing

- Kept an eye on Syften notifications, cleared out inbox

### Infrastructure

- Updated internal Mathesar installation

### Preexisting DB compatibility

- Looked into performance when Mathesar's web service is not colocated with the DB
  - Terribly slow progress, because performance testing on the slow app took time

## 2023-09-18

### Infrastructure

- Updated internal Mathesar installation
- Reset demo load balancer

### PR reviews

- https://github.com/centerofci/mathesar/pull/3189 (approved)
  - This was extremely laborious, and took most of the day.

## 2023-09-15

### PR reviews

- https://github.com/centerofci/mathesar/pull/3186 (approved, merged)

### Preexisting DB compatibility

- Submitted PR to test compatibility with PG versions 13, 14, 15
  https://github.com/centerofci/mathesar/pull/3206

## 2023-09-14

### PR reviews

- Initial look through https://github.com/centerofci/mathesar/pull/3121
- Initial look through https://github.com/centerofci/mathesar/pull/3189

### Preexisting DB compatibility

- Completed scale testing, recorded results
- Verified composite type support, recorded results

## 2023-09-13

### Preexisting DB compatibility

- Asynced with Pavish about status
- Worked on scale testing

### Marketing

- Cleared out inbox of Syften notifications

### Infrastructure

- Investigated domain renewal notice

## 2023-09-12

### PR reviews

- https://github.com/centerofci/mathesar-wiki/pull/105 (approved)
- https://github.com/centerofci/mathesar-ansible/pull/42 (approved)

### Email/messaging

- Went through Dom's helpful feedback w.r.t. the SQL codebase from his project update
- Cleared out other notifications from social media

## 2023-09-11

### Meetings

- 1:1 with Dom

### PR reviews

- https://github.com/centerofci/mathesar/pull/3186 (requested changes)



### Bug hunt

- Found problem with FE, raised in FE channel, determined it's already known.

### Marketing

- Looked through Syften notifications, nothing interesting this round

### Preexisting DB compatibility

- Sent update email
- Started looking into composite type support (or lack of it)

## 2023-09-08

### Meetings

- 1:1 with Mukesh
- Catch up with Dom w.r.t. his PR #3186

### PR reviews

- Follow up on https://github.com/centerofci/mathesar/pull/3186

### Preexisting DB compatibility

- Continued testing of problems, added to [the meta issue](https://github.com/centerofci/mathesar/issues/3199)

## 2023-09-07

### Meetings

- 1:1 with Anish

### PR reviews

- https://github.com/centerofci/mathesar/pull/3186 (requested changes)
- https://github.com/centerofci/mathesar/pull/3121 (requested changes)

### Preexisting DB compatibility

- Continued testing of problems, added to [the meta issue](https://github.com/centerofci/mathesar/issues/3199)
- Decided _not_ to host test data; we determined it's not useful at the moment.

## 2023-09-06

Short day due to sick family

### Meetings
- Team meeting

### Email / messaging

- Replied to DB access email thread
  - First, I re-read the PostgreSQL docs about permissions, roles and `GRANT`
- Replied to E2E testing thread

## 2023-09-05

Short day due to sick family

### Marketing

- Cleared out inbox of Syften notifications, flagged interesting ones

### Preexisting DB compatibility
- Worked on organizing thinking for known problems
- Started Meta issue, tested DB versions

## 2023-09-04

Short day due to sick family.

### Meetings

- 1:1 with Pavish about preexisting DB project

### Preexisting DB compatibility

- Worked on organizing thinking for known problems

## 2023-09-01

### Meetings

- meeting with Mukesh about demo deployment
- 1:1 with Mukesh
- Core team event

### Release 0.1.3

- Successfully got the prod deployments deployed
- Spent most of the day fighting with demo setup

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
- Update [project description](/projects/sql-ddl-operations)
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
