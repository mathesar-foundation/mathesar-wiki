# Brent's work log archive: 2023-10

## 2023-10-31

### Meetings

- 1:1 with Kriti about AWS setup and other things

### User help / marketing

- worked on AWS setups for Mathesar
  - set up root account
  - read docs for account management
  - set up non-root developer account for myself
- Caught up a bit in Freshdesk

## 2023-10-30

### Infrastructure

- Updated internal Mathesar installation

### Hand off

- catching up on various last-minute info and organization from Dom and Mukesh

## 2023-10-27

### Meetings

- 1:1 with Mukesh
- User call: https://mathesar.freshdesk.com/a/tickets/1492
- Core team event

### PR reviews

- https://github.com/centerofci/mathesar/pull/3243 (merged)


### Infrastructure

- Keeping an eye on new pipeline setup
- Updated internal Mathesar installation



## 2023-10-26

### Meetings

- 1:1 with Anish
- User call prep meeting with Pavish and Kriti
- 1:1 with Kriti

### Infrastructure

- Finished pipeline fix
- Set up completely new branch protection rules
- Emailed dev list about necessary steps to get everyone's PRs passing the CI pipeline.
- ad-hoc syncing with Pavish about front end concerns w.r.t. the fix

### Marketing

- Caught up on various user help threads
- Cleared out Syften notifications

## 2023-10-25

### Infrastructure

- Continued work on pipeline issue.
- Checked on internal server

### Meetings

- Handoff meeting with Dom
- 1:1 with Kriti
- User call with AJP about setup of Mathesar on AWS

### Marketing

- Cleared out Syften notifications

## 2023-10-24

### Infrastructure

- Worked on solution to pipeline breakage,
- Monitored matrix server
- Checked on internal server (no action needed)

## Meetings
- 1:1 with Kriti

## 2023-10-23

### Meetings

- 1:1 with Dom
- Ad-hoc catch-up with Kriti about pipeline situation

### Infrastructure

- Finished fixing Matrix server
- Monitored the same Matrix server to make sure it was behaving
- Checked on internal.mathesar.org ; no action needed
- Noticed and started work on fixing major problem preventing some backend PRs from merging, and others from being properly tested.

## 2023-10-20

### Meetings

- 1:1 with Mukesh
- call with Kriti and AJP about Mathesar use cases

### Infrastructure

The entire day was consumed by trying to figure out what was broken with our Matrix server, and working on a fix.

## 2023-10-19

### Marketing

- Cleared out Syften notifications
- Sent follow up email to potential user via Freshdesk

### Architecture

- Compiling notes, thoughts, and results from Users and permissions II

## 2023-10-18

### Meetings

- Users and Permissions II

### Architecture

- Continued working on putting notes together into something coherent and consumable by others
- Prepped for users and permissions meeting

## 2023-10-17

### Meetings

- 1:1 with Sean about connections UI
- Meeting about permissions concepts and UX

### Architecture

- Wrote wiki page about new vision for permissions architecture.

### Preexisting DB compatibility

- Put together a quick issue in this space for a GSoC hopeful

### Marketing

- Cleared Syften notificatoins

## 2023-10-16

More architecture writing!

### Architecture

- Worked through model exposition cleanup
- Some messaging and emailing about various details
  - Started email chain about permissions concepts
  - Scheduled meetings for next day
  
### Marketing

- Cleared out Syften notifications

### Meetings

- Synced with Kriti

## 2023-10-13

Most of this day was heads-down working on architecture write-up.

### Architecture

- Initial pages of architecture write-up done, published in branch on wiki

### Meetings

- 1:1 with Mukesh
- Mathesar community event

## 2023-10-12

Most of this day was heads-down working on architecture write-up and reading `psycopg` docs.

### Architecture

- Worked on compiling various notes into something coherent and publishable.

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


