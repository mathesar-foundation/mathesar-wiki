# Brent's work log archive: 2023-09

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
