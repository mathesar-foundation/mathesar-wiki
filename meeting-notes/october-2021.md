---
title: October 2021 meeting notes
description: 
published: true
date: 2021-10-26T22:44:57.598Z
tags: 
editor: markdown
dateCreated: 2021-10-05T21:04:00.985Z
---

# 2021-10-26

Please see [2021-10-26 weekly discussion](https://github.com/centerofci/mathesar/discussions/762) on GitHub Discussions.

# 2021-10-19

Please see [2021-10-19 weekly discussion](https://github.com/centerofci/mathesar/discussions/739) on GitHub Discussions.

# 2021-10-15

Topic: Views prototype design review
Attendeees: Brent, Ghislaine, Kriti, Pavish, Sean

Action items:
- Need to add full create view flow to the prototype
- Add setting lookup columns to the prototype
- Make sure to add all Figma flows to the prototype from other issues as well
- We need different flows for one-to-many and many-to-many relationships in views
    - Perhaps ask the user what type they want
        - They should also be able to modify this later
    - Don't automatically make mapping tables for one-to-many relationships
- Separate relationships from views
    - When user wants to create a relationship, ask if you want to:
        - link to one record: create a FK in the current table
        - link to multiple records: create a FK in the other (related) tables
        - many to many: create a mapping table
    - Then we can suggest creating a view to show the summary view
    - Views can have summary columns
- Create new design issues and update existing issues for Views 
- We'll close existing design discussions and open new ones
- Set up calls for reviewing future designs as needed (review async first)

Feedback:
- Views should be about specific columns, not a whole table
    - (for some use cases)
- Saving filters, sorts, etc. is also views, so that involves a whole table
- Don't constrain view creation to just one flow since they serve so many purposes

Improvements to process:
- Be on the same page about the schema we're working with
    - e.g. we were all modeling track-album-artist differently in our heads, made talking about it difficult
- Define design tickets in terms of user scenarios
    - Also specify functionality and technical constraints 

# 2021-10-12

Please see [2021-10-12 weekly discussion](https://github.com/centerofci/mathesar/discussions/727) on GitHub Discussions.

# 2021-10-08

- Kriti's availability
    - Kriti's workload has been too heavy, leaving little time for focused work.
    - Initiatives like 'Comms Assignee' useful to make workload more manageable.
    - More PR reviews to be delegated to team members.  -- using the 'assign' functionality
- Milestone deadlines
    - All deadlines moved to end of December to reduce bureaucracy, deadlines are mostly for priority.
- Weekly planning
    - Weeks will not be planned in advance, people should just move tasks to active when they need work 
- New project walkthrough
    - New GitHub project to start being used internally, public availability pending.
    - New project to eventually replace current projects view.
- UCB design project
    - We're working with UCB student design class on a project 
    - image view plugin design
        - let users view images linked to within Mathesar
- Hiring update and plan
    - Backend interviews ongoing 
    - Interviews will happen in parallel with code tasks

# 2021-10-05

Please see [2021-10-05 weekly planning](https://github.com/centerofci/mathesar/discussions/693) on GitHub Discussions.
