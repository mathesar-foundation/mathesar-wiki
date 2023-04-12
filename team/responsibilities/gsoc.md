---
title: GSoC 2023
description: Administration of GSoC-related tasks and processes
published: true
date: 2023-04-12T17:57:10.089Z
tags: 
editor: markdown
dateCreated: 2023-03-23T17:40:32.478Z
---

## Introduction

Quick summary: it should be enough for any reader wanting to know what their responsibilities are (and to read the related notes) to check their role descriptions under [Phase-independent responsibilities](#phase-independent-responsibilities) and [Current phase](#current-phase).

This document lists the responsibilities, related instructions and guidelines for a GSoC program. GSoC is made up of multiple phases, each of which have different responsibilities. This document is structured accordingly. [Phase-independent responsibilities](#phase-independent-responsibilities) are listed, then phase-dependent responsibilities are divided into whether it's the current phase, a previous phase, or an upcoming phase. Between phases, the GSoC team roles, membership and responsibilities are variant. The rest of the document is under the [Details](#details) section, which holds guides, links and instructions, and it's linked as needed from the responsibility lists.


# Phase-independent responsibilities

## Owner

- Be an org admin for GSoC
- Be extremely familiar with the GSoC program, including
	- [GSoC mentor guide](https://google.github.io/gsocguides/mentor/)
	- All our [Mentoring](https://wiki.mathesar.org/en/community/mentoring) documentation and policies
- Keep an eye on any GSoC related emails and action items, and ensure the rest of the team completes any action items
- Keep an eye on GSoC related deadlines and timelines
	- See [Calendar](#calendar)
- Keep our custom GSoC calendar up-to-date
  - Includes keeping track of recurring tasks
	- See [Calendar](#calendar)
- Follow up on requests from GSoC (e.g. filling out forms about impact of GSoC on Mathesar), since it builds goodwill
- Generally keep an eye on GSoC process efficiency and make improvements to processes or documentation as needed
	- See [Periodic process reviews and reports](#periodic-process-reviews-and-reports)


# Current phase

## Ranking phase

Starts 2023-04-04, ends 2023-04-27.


### Team

| Role | Assignees |
|-|-|
| **Owner** (aka **Admin**) | Dominykas |
| **Candidate helper** | Anish, Rajat, Dominykas |
| **Mentor** | Anyone that's a mentor in a GSoC project idea |


### Responsibilities

#### Mentors

- Participate in final proposal review, when requested by the owner
	- See [final proposal review](#final-proposal-review)


#### Candidate helper

- Help candidates with their late contributions
	- During the ranking phase, candidates might still be making contributions, which might be useful when ranking their proposals
  - See [helping guidelines](#helping-guidelines)


#### Owner

- Facilitate final proposal ranking
	- See [final proposal review](#final-proposal-review)
- Make sure the rankings are submitted in a timely manner
	- Consider attempting to balance that against doing final reviews late in the phase so that candidates have more time to make contributions


# Previous phases

## Proposal phase

Starts 2023-03-20, ends 2023-04-04.


### Team

| Role | Assignees |
|-|-|
| **Owner** (aka **Admin**) | Dominykas |
| **Candidate greeter/helper** | Anish, Rajat, Dominykas |


### Responsibilities


#### Everyone

- Review draft proposals
	- Do so in a timely manner
  - Keep relevant spreadsheet/s up-to-date with the status of your reviews
  	- See [Internal draft proposal tracking spreadsheet](#who-is-responsible-for-a-review) section
  - Make sure that only a single mentor is responsible for a given review at any given time
  	- See [Who is responsible for a review](#who-is-responsible-for-a-review) section
  - See [Review instructions](#draft-review-instructions) section
- Enforce a no-early-issue-assigns rule during the GSoC proposals phase (ends April 4th)
  - See [no-early-issue-assigns](#no-early-issue-assigns)


#### Candidate greeter/helpers

- Perform greet/help daily
  - Greet, meaning notice new contributors and greet them
  - Help, meaning respond to requests for help or guidance
  	- On Matrix and Github
	- See [greet/help schedule](#greethelp-schedule) section
 	- See [greeting instructions](#greeting-instructions) section
 	- See [helping guidelines](#helping-guidelines) section
  
  
#### Owner

- Monitor GSoC draft applications and ensure they all get reviewed in a timely manner.
	- Follow up with other team members as needed.
- Keep track of issues that have already been assigned and un-assign them after 7 days of inactivity.
	- Anish is doing this, but it’s good to keep an eye on this.
	- https://github.com/orgs/centerofci/projects/1/views/42 may be helpful, it sorts by last activity.
- Ensure there are enough open issues for GSoC contributors to work on OR revise the applicant guide to remove the contribution requirement and come up with an alternate way to evaluate candidates (maybe have a standard backend and frontend task for everyone).


# Details

## Final proposal review

Performed in two passes. First pass is that the spammy or obviously unfitting proposals are filtered out. Likely performed by the owner. Second pass is where the mentors evaluate proposals for the projects they are mentoring. All of this is done in the [final proposal review spreadsheet](#final-proposal-review-spreadsheet). The final proposal rankings are derived by sorting the approved proposals on their overall scores.

### Final proposal review instructions

1. Go to the current [final proposal review spreadsheet](#final-proposal-review-spreadsheet)
2. Go to the sheet titled "Second pass"
3. Find a proposal that you are a reviewer of, and that you have not yet scored
4. Familiarize with the proposal's project idea by reading its wiki page
5. Inspect the proposal's PDF and score the proposal
       - if you're getting errors when trying to load the PDF, you might have to navigate to https://summerofcode.withgoogle.com/, log out (if you're logged in), and log in
6. Inspect the candidate's contributions in the issue tracker and score the candidate
       - notice the links to the candidate's PRs, issues created, and issues assigned
       - inspect all aspects of the candidate's activity in the issue tracker, not only the code contribution
7. Repeat from the beginning until you've scored all of the proposals you're a reviewer of
8. Notify the admin of you having completed the scoring, via the same channel through which you were requested to perform it (probably via an email thread)


## Final proposal review spreadsheet

- Current [2023 spreadsheet](https://docs.google.com/spreadsheets/d/1tMp8wJJhAnUIyXLdXCIcecYecDHJIb7U84neQQ0i8Fw) (private)
- Archived [2022 spreadsheet](https://docs.google.com/spreadsheets/d/1SAgETOHvNnVf-MBUqe_WLbOLsl8qDax35DOukaUueO8) (private)


## Draft proposal review

### Who is responsible for a review

The primary mentor for a project is responsible for getting the project's draft proposals reviewed. Primary mentors are encouraged to delegate part of their work to the secondary mentors, but, until that's coordinated, the primary mentor is responsible for the proposal getting reviewed. Motivation for this rule is to prevent someone expecting the other mentor to step up without solicitation and thus resulting in delayed reviews.

Who is currently responsible for a review is tracked in the [tracking spreadsheet](#internal-draft-proposal-tracking-spreadsheet).


### Internal draft proposal tracking spreadsheet

[This spreadsheet](https://docs.google.com/spreadsheets/d/1g6uLpyyUWpQna4UCyZ7zJiNuEV7RBnpQ-EblUDTFPws) gets a row added automatically for every draft proposal submitted via our submission form. It also tracks whether a review is pending, who is responsible for a pending review, and who and when reviewed a given proposal. Respective mentors are expected to keep all of this up-to-date.

Do not remove rows from the spreadsheet. You might be tempted to do this for multiple review requests for the same person, but that would impede admin's ability to track the submit-review process: for example, the admin needs to know if certain proposals are waiting for a review for a long time, and if all but the most recent are removed, the admin doesn't know when it was first submitted; if you remove all but the oldest, the admin doesn't know that the candidate is making repeated review requests.


### Draft review instructions

1. Use the [tracking spreadsheet](#internal-draft-proposal-tracking-spreadsheet) to tell which reviews you have pending
2. Read the proposal and provide feedback via Google Doc comments
3. (Recommended) Place general comments on the title of the proposal (or somewhere thereabouts); this seems to have become an unwritten rule (until now) amongst some of the mentors
4. Once done, add a general comment saying that the review is finished, so that the status of the review is not ambiguous to the candidate
5. (Recommended) Ask that the candidate resubmit via the same draft proposal form he originally used, when/if he wants to request a new review; this way the admin will be able to track and notify of new requests for review, otherwise it's the mentor's responsibility 
6. Update the [tracking spreadsheet](#internal-draft-proposal-tracking-spreadsheet) 


## Greeting instructions

Suggested process:

1. Notice new contributors
	- In Matrix, check the little visualizations above and below messages of new people joining to see who is new
2. Welcome them, whether they're active or engage first or not
3. Preemptively remind them of our resources for self-guidance:
  - the [applicant guide](https://wiki.mathesar.org/en/community/mentoring/applicant-guide)
  - or, the [contributing guide](https://wiki.mathesar.org/en/community/contributing)
4. Having provided a resource for self-guidance, encourage them to speak up if something is not clear.

Example in our Matrix General channel:

>`Welcome @practicat, @Joangie Marquez, @Mayank Arya, @shantanu oak, @krishav 👋 If you're here for GSoC, don't forget to check out our [GSoC candidate  guide](https://wiki.mathesar.org/en/community/mentoring/applicant-guide). If something is not clear, reach out!`


## Helping guidelines

A few things to keep in mind

- Be on the watch for problems that might affect a lot of people, or few people but gravely
- Don't do new contributors' work for them
- Don't be dismissive either
- Refer them to resources for self-guidance (namely our applicant or contributing guides)
- Politely remind of our expectation that contributors will be relatively self-sufficient and tolerant of minimal hand-holding


## Greet/help schedule

We aim to greet and help new contributors (mostly GSoC candidates) multiple times per day (between all of us, not each). This schedule should act as *a very rough guide*, in practice we'll often respond whenever we see a new message, but in case that's inconvenient, use this schedule as a guide for when to perform this task.

| Member | Approximate time |
|-|-|
| Dominykas | UTC 11:00 |
| Anish | UTC 4:30 |
| Rajat | UTC 4:30 |

Related [conversation thread](https://groups.google.com/u/1/a/mathesar.org/g/core-team/c/C9ktD96iG_s).


## Office hours

Office hours are public sync meetings we host where community members (GSoC candidates mostly) join to get help. Previous year such meetings only received community participation just before the end of the proposal period. We're currently planning to host these only during the last week of the proposal period.

We track community events, including office hours, [on this Wiki page](https://wiki.mathesar.org/en/community/events) and GSoC-related events in our [GSoC Calendar](#calendar).
	
  
## No early issue assigns

This rule should not be always applied. Its purpose is to maximize the number of issues candidates have available. Useful when number of issues available for candidates to prove themselves is low.

No-early-issue-assigns rule means that a contributor can be assigned to an issue only when he has a PR that reached some kind of completion (merged or killed).

See this [conversation thread](https://groups.google.com/u/1/a/mathesar.org/g/core-team/c/hFU729n8xDE) for the edge case this opens up where multiple PRs for the same issue compete to be merged

- This rule should only be applied when evaluating candidates
- Note to admin, make sure to evaluate whether number of issues is indeed low
- Note to admin, consider selecting a subset of issues to which this rule should apply
	- E.g. in 2023 we had too few backend issues, but sufficient number of frontend issues


## Calendar

[This Google calendar](https://calendar.google.com/calendar/embed?src=c_5a779de8f9e054a645c11926302c1222e4d81aa85c126c84eb23ef056d9b9408%40group.calendar.google.com) is used to track GSoC-related deadlines and related tasks.


## Periodic process reviews and reports

GSoC administration involves periodic process reviews and reports. They are scheduled in the [calendar](#calendar). This thread tracks resulting updates: https://github.com/centerofci/mathesar/issues/2733

