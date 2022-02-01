---
title: GSoC 2022 Project Ideas
description: 
published: true
date: 2022-02-01T09:40:51.232Z
tags: 
editor: markdown
dateCreated: 2022-01-18T19:32:54.047Z
---

## Template

> Please use this template while adding new project ideas.
{.is-info}

### The Problem
*Describe the problem that the project is expected to solve.*

### Classification
- **Difficulty**: *Low/Medium/High*
- **Skills needed**: *List of technologies or other skills needed*
- **Length**: *Medium (~175 hours) / Long (~350 hours)*

### Tasks
*A list of tasks that the intern is expected to complete as part of their work. Be specific about research, code, etc.*

### Expected Outcome
*Describe the expected outcome of the project.*

### Application Tips
*Tips for writing a successful proposal to complete this project. This could include what specific questions to answer or what details could help the application stand out.*

### Resources
*A list of links to documentation/code/wiki pages, etc. relevant to the project idea.*

### Mentors
*List of mentors for this project.*

-----------

## Automatic Hint Reflection

### The Problem
We're currently working on a hint system that would allow us to assign useful information to functions and types. Currently, the hints are compiled by-hand. We've discussed the possibility to reflect function properties automatically, which would allow us to also assign (at least some) hints to functions automatically. The automatic reflection is not essential, but it could be a significant quality-of-life improvement. Its implementation seems too expensive for the core team to take up in the near term. Further, it's fairly isolated from the rest of Mathesar, which is good for new contributors.

### Classification
- **Difficulty**: High
- **Skills needed**: PostgreSQL, SQL
- **Length**: *Long (~350 hours)*

### Tasks
- Research what is the intersection between the things that would be useful for Mathesar to automatically reflect and what *can* be automatically reflected;
- Create an accurate picture of what cases the automatic reflection will fully cover and in what cases information (hints) will have to be supplemented manually;
- Figure out when to reflect and how to cache the reflections so as to minimally burden the wider system with more state;
- Do the implementation.

I would expect the above tasks to be performed at least somewhat asynchroniously.

### Expected Outcome
An automatic PostgreSQL function (and possibly type) property reflection mechanism tailored to automatically finding useful hints for the hint system.

### Application Tips
See Tasks.

### Resources
TBD

### Mentors
Dominykas