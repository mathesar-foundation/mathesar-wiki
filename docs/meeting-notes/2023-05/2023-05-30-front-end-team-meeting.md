---
title: 2023-05-30 Front End Team meeting
description: 
published: true
date: 2023-07-19T23:34:28.998Z
tags: 
editor: markdown
dateCreated: 2023-05-30T16:46:34.205Z
---

## At a high level, what should we focus on right now?

- We should prioritize features
- We shouldn't take up any big refactoring right now because we lack a clear picture for the product work that we'd like to take up in the coming year. Once we get a clearer picture, we can consider taking up some of the refactoring becaus we'll be better informed of our direction.

## What we're working on

- Rajat: i18n, which should last a while. Filling in gaps with PR review and smaller work.
- Pavish: vacation soon. Hoping to take up a new project upon returning from vacation. Hoping to decide on that project within the next week. Considering sharable forms and sharable tables/explorations.
- Sean: Will need a new project in the next week or two. Not sure what it will be yet.

### Front end performance project

- Pavish was planning to work on this, but has decided to defer it in favor of feature-related work
- Perf problems:
    - impact loading and scrolling
    - impact dev mode more the prod mode
    - are worse with lots of columns
- Fixing the perf problems will require significant refactoring, and it would be nice to take that refactoring work up once we have a better idea of the other features we plan to build

## Potential feature work

- Explorations. Lots to improve here, but we need more user input for this.
- Sean: charts/graphs
    - Pavish: We need to understand more about the product direction
    - Sean: chicken/egg problem
    - Rajat: also interested in this
- file/image types

## Potential refactoring to do later

- Rajat: some work on sheet selection
    - clarify UX specs, adding more detail
    - refactor code to use better data structures which are less prone to bugs
    - Sean: agree. This has been our the most bug-prone area of our front end code
- Pavish: Stores refactor.
    - It's been hard for new contributors to make PRs that follow our patterns.
    - We'll need to discuss this in depth
- Pavish: Reduce requests by combining them via new endpoints

## Other topics we should discuss soon

- Sean: "Granular vs coarse reactivity"
    - We decided to schedule this topic for the next meeting
- Rajat: Testing.
    - We'll plan a separate meeting for this.
- We also did a quick pass over the numerous other small agenda items and agreed that none of them are pressing enough to discuss soon.

## Next meeting

- Scheduled for 2023-06-30


