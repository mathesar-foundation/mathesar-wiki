---
title: Mentor Guide
description: 
published: true
date: 2022-04-04T22:38:57.678Z
tags: 
editor: markdown
dateCreated: 2022-02-09T22:27:25.246Z
---

This guide only covers Mathesar-specific processes and guidelines. For a more general overview of what mentorship entails, please read [the Google Summer of Code Mentor Guide](https://google.github.io/gsocguides/mentor/).

Mentoring programs are usually structured into the following stages:
1. Preparing project ideas
2. Applying for the mentoring program
3. Accepting contributions from applicants
4. Reviewing proposals from applicants
5. Choosing mentees
6. Planning with mentees
7. Working with mentees

# Preparing project ideas
We need a list of potential project ideas that applicants can submit a proposal to implement. 

Project ideas should be:
- a self-contained feature or improvement for Mathesar
- scoped so that a single person can reasonably implement it in the timeframe of the mentoring program
	- For GSoC, this is either 350 hours or 175 hours
- not time-sensitive or critical (there is no guarantee that the project will ship)
- compatible with our existing product roadmap

Once you've come up with a project idea, please:
1. Flesh it out using our [Project Idea Template](/en/community/mentoring/project-idea-template).
2. Add it to the [Project Ideas](/en/community/mentoring/project-ideas) page.

If you're wondering if your project idea makes sense, discuss it on Matrix with other team members first before writing it down.

> **See also:** The ["Defining a Project (Ideas List)" page of the GSoC mentor guide](https://google.github.io/gsocguides/mentor/defining-a-project-ideas-list)

# Applying for the mentoring program
Once we have fleshed our our project ideas, Kriti will submit Mathesar's application to the mentoring program. While we wait to hear back, you should:
- create a set of `good first issue` tasks suitable for first-time contributors to the codebase.
- mentally prepare to deal with increased communication work.

# Accepting contributions from applicants
Once the mentoring program (e.g. Google) announces the organizations participating in the program, potential applicants will start communicating with us. This stage of the program is the most intense.

You should:
- welcome new contributors and help them get started with:
	- applicant information
	- local project setup
	- finding issues to contribute to
- review PRs quickly
- answer questions about the project ideas and the product.

## Communication Tips
- Point people to public channels and away from email and DMs so that others can answer questions too.
- You may get low effort questions like "how do I get started?". Don't try to guess what people mean, ask for more specific questions.
	- In general, the effort involved in helping someone should be proportional to the effort they put in.
- If you find yourself answering the same questions often, update the relevant documentation so you can point people to it instead.
- Do not give individual applicants information about competing applications (e.g. how many proposals we got for a particular project idea).

# Reviewing proposals from applicants
Applicants will start working on draft proposals and sharing them with you a few weeks before the deadline. You are responsible for reviewing all proposals for which you are the primary mentor.

You should:
- track draft proposals and review status in our [our internal spreadsheet](https://docs.google.com/spreadsheets/d/1FSahyG8f6pkWj_hv7oMi6g49ANIpKJWDVtUS-Qwz0ZQ/)
- ask applicants to submit proposals through the Google Summer of Code website so that we can keep track of them.
- review proposals in 1-2 days if possible.
- ask for review from other team members if you think it would be useful. 

## What does reviewing involve?
- Reviewing involves leaving comments on the proposal to help the applicant improve the proposal before final submission.
- Review comments should focus on finding problems with the proposal, not suggesting specific solutions.
- Comments should mostly be in the form of:
	- Questions about something unclear.
	- 1-2 sentence explanations about why something doesn't make sense.
	- 1-2 sentence statements describing what's missing in a section.
	- Suggestions for areas of the codebase to contribute code to (to strengthen confidence in the proposal).
- Questions to ask yourself during review:
	- Does the applicant understand the project idea?
	- Is the implementation plan:
		- technically feasible?
		- technically *desirable*?
	- Is the implementation timeline realistic (including time needed to learn new skills and get familiar with the codebase?
	- Does the timeline include concrete deliverables?
	- Has the applicant thought through design and UX issues?
	- Are the applicant's code contributions strong enough that you feel confident that they can follow through on their plan?

# Choosing mentees
After the final proposals are in, you'll meet with the rest of the Mathesar team and decide which proposals are strong enough to accept. 

This is an internal decision, we do not communicate with applicants about their proposals at this point.

During this period, you should:
1. finalize mentorship for each project
2. alk to co-mentors to create a plan for how to collaborate on each project, e.g. 
	1. Will one of you be the primary mentor or will all of you be equally involved? 
	2. How will checkins and notes be shared?

# Working with the mentees
At this point,
1. We've decided which applications to accept
2. The mentoring program has approved our selection
3. The accepted mentees have been announced

## Welcoming the mentee
- Reach out to your mentee ASAP and welcome them to the project.
- Have an introductory call with the mentee and get to know each other. 
	- Ask them questions about themselves and talk about yourself too.
- Ensure that the mentee is added to our [Team Members](/en/team/members) and has the correct GitHub and wiki permissions.

## Finalizing the project plan and workflow
Before work on the project gets underway, you should:
- collaborate with your mentee to finalize the implementation details and weekly deliverables for the project
- create a document to keep any project information and notes, include:
  - an up-to-date implementation plan and weekly milestones
  - the mentee’s contact information and emergency contact
  - all meeting notes
  - any other project-relevant information.
- share the project document with co-mentors and the organization admin
- set up regular meetings: 
  - a weekly video call for the mentors to check-in with the mentee
  - a monthly call with the Mathesar organization admin to check in with the mentee.
- decide with the mentee on the workflow the project will follow. e.g.
  - Does the mentee understand regular git workflow (e.g. pull requests, branches, reviews)?
  - Does the mentee understand the code review process?
  - How often should code be committed?
  - How often should your mentee give you progress reports?
  - What is the best way for the mentee to get your attention when they are stuck?

## Mentoring Period
You're now ready to mentor!

### Weekly check-ins
- Take good notes so that your backup mentor can pick up where you left off easily if you’re unavailable.
- Make sure the mentee is on-track with their weekly milestones and if not, work with them to figure out why and come up with a plan.
- Ask how the mentee is doing generally.
- Praise things they are doing well and provide constructive criticism on the things they could improve on. Both of these are important.

### Ongoing work
- Review all work/code promptly. You should aim to review within 1 business day.
  - If your mentee is blocked on their work for some other reason, help them become unblocked as soon as possible.
- Check in on Matrix with the mentee once every day or two. 
	- Remember that mentees are inexperienced and may not know they are stuck, when to ask for help, and/or how to articulate problems well.

### Feedback
- Submit your required program evaluations on time.
- Ask for feedback on your mentorship every few weeks.
- Your mentee might like to present their work at a CCI research meeting and get some feedback. It's up to you to facilitate this.

### Troubleshooting
Talk to the program coordinator proactively if you're not sure what to do. Some things to pay attention to:
- Your mentee is not active and engaged regularly.
- Your mentee is not communicating enough or misses a check-in.
- You have concerns or even just a bad feeling about something.
- You have feedback or questions about any part of the program process.
- You'd like feedback about how your mentoring is going
