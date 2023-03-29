---
title: GSoC 2023
description: Administration of GSoC-related tasks and processes
published: true
date: 2023-03-29T12:15:55.601Z
tags: 
editor: markdown
dateCreated: 2023-03-23T17:40:32.478Z
---

## Introduction

Document made up of following major sections: [Responsibilities](#responsibilities), [Details](#details). *Responsibilities* should be self-explanatory. The *Details* section, holds a fair amount of guides and resources, including a [calendar](#calendar) with various related deadlines and tasks.

Normally, it should be enough to read what's appropriate for you in the *Responsibilities* section. There you'll probably find links for whatever might concern you in the *Details* section.


# Team

| Role | Assignees |
|-|-|
| **Owner** (aka **Admin**) | Dominykas |
| **Candidate greeter/helper** | Anish, Rajat |


# Responsibilities

## Everyone

- Review draft proposals
	- Do so in a timely manner
  - Keep relevant spreadsheet/s up-to-date with the status of your reviews
  	- See [Internal draft proposal tracking spreadsheet](#who-is-responsible-for-a-review) section
  - Make sure that only a single mentor is responsible for a given review at any given time
  	- See [Who is responsible for a review](#who-is-responsible-for-a-review) section
  - See [Review instructions](#review-instructions) section
- Enforce a no-early-issue-assigns rule during the GSoC proposals phase (ends April 4th)
	- No-early-issue-assigns rule means that a contributor can be assigned to an issue only when he has a PR that reached some kind of completion (merged or killed)
	- Purpose is to maximize the number of issues candidates have available
  - See this [conversation thread](https://groups.google.com/u/1/a/mathesar.org/g/core-team/c/hFU729n8xDE) for the edge case this opens up where multiple PRs for the same issue compete to be merged


## All members

- Perform greet/help daily
  - Greet, meaning notice new contributors and greet them
  - Help, meaning respond to requests for help
	- See [greet/help schedule](#greethelp-schedule) section
 	- See [greet/help](#greethelp-instructions) instructions section
  
  
## Owner

- Be an org admin for GSoC
- Be extremely familiar with the GSoC program, including
	- [GSoC mentor guide](https://google.github.io/gsocguides/mentor/)
	- All our [Mentoring](https://wiki.mathesar.org/en/community/mentoring) documentation and policies
- Keep an eye on any GSoC related emails and action items, and ensure the rest of the team completes any action items.
- Keep an eye on GSoC related deadlines and timelines.
- Monitor GSoC draft applications and ensure they all get reviewed in a timely manner.
	- Follow up with other team members as needed.
- Facilitate a process of selecting GSoC students and projects once final applications are in.
	- e.g. see [this spreadsheet from last year](https://docs.google.com/spreadsheets/d/1SAgETOHvNnVf-MBUqe_WLbOLsl8qDax35DOukaUueO8/edit#gid=1794943298).
- Keep track of comments on new issues and assign issues to people when they ask.
	- The rest of the team should mostly be doing this, but it’s good to keep an eye on it.
- Keep track of issues that have already been assigned and un-assign them after 7 days of inactivity.
	- Anish is doing this, but it’s good to keep an eye on this.
	- https://github.com/orgs/centerofci/projects/1/views/42 may be helpful, it sorts by last activity.
- Follow up on requests from GSoC (e.g. filling out forms about impact of GSoC on Mathesar), since it builds goodwill
- Ensure there are enough open issues for GSoC contributors to work on OR revise the applicant guide to remove the contribution requirement and come up with an alternate way to evaluate candidates (maybe have a standard backend and frontend task for everyone).
- Generally keep an eye on GSoC process efficiency and make improvements to processes or documentation as needed.

# Details

## Draft proposal review

### Who is responsible for a review

The primary mentor for a project is responsible for getting the project's draft proposals reviewed. Primary mentors are encouraged to delegate part of their work to the secondary mentors, but, until that's coordinated, the primary mentor is responsible for the proposal getting reviewed. Motivation for this rule is to prevent someone expecting the other mentor to step up without solicitation and thus resulting in delayed reviews.

Who is currently responsible for a review is tracked in the [tracking spreadsheet](#internal-draft-proposal-tracking-spreadsheet).

### Internal draft proposal tracking spreadsheet

[This spreadsheet](https://docs.google.com/spreadsheets/d/1g6uLpyyUWpQna4UCyZ7zJiNuEV7RBnpQ-EblUDTFPws) gets a row added automatically for every draft proposal submitted via our submission form. It also tracks whether a review is pending, who is responsible for a pending review, and who and when reviewed a given proposal. Respective mentors are expected to keep all of this up-to-date.

Do not remove rows from the spreadsheet. You might be tempted to do this for multiple review requests for the same person, but that would impede admin's ability to track the submit-review process: for example, the admin needs to know if certain proposals are waiting for a review for a long time, and if all but the most recent are removed, the admin doesn't know when it was first submitted; if you remove all but the oldest, the admin doesn't know that the candidate is making repeated review requests.


### Review instructions

1. Use the [tracking spreadsheet](#internal-draft-proposal-tracking-spreadsheet) to tell which reviews you have pending
2. Read the proposal and provide feedback via Google Doc comments
3. (Recommended) Place general comments on the title of the proposal (or somewhere thereabouts)
4. Once done, add a general comment saying that the review is finished, so that the status of the review is not ambiguous to the candidate
5. (Recommended) Ask that the candidate resubmit via the same draft proposal form he originally used, when/if he wants to request a new review; this way the admin will be able to track and notify of new requests for review, otherwise it's the mentor's responsibility 
6. Update the [tracking spreadsheet](#internal-draft-proposal-tracking-spreadsheet) 


### Repeated reviews


## Greet/help instructions

### Greeting

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


### Helping

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


## Calendar

[This Google calendar](https://calendar.google.com/calendar/embed?src=c_5a779de8f9e054a645c11926302c1222e4d81aa85c126c84eb23ef056d9b9408%40group.calendar.google.com) is used to track GSoC-related deadlines and related tasks.


## Periodic process reviews and reports

GSoC administration involves periodic process reviews and reports. They are scheduled in the [calendar](#calendar). This thread tracks resulting updates: https://github.com/centerofci/mathesar/issues/2733

