---
title: 2023-03-21 Plan for 0.1.2
description: 
published: true
date: 2023-03-21T21:50:12.873Z
tags: 
editor: markdown
dateCreated: 2023-03-21T19:08:22.422Z
---

**Attendees**: Pavish, Kriti

Main focus of the release is to improve Installation and fix any critical user-reported bugs.

Performance issues should be moved to 0.1.3. Non-installation projects should also be targeted for 0.1.3.

## Issues yet to be created/placed in milestone:
- Check-in with Mukesh to create issues for **items discussed during installation call**

## Must have (subject to discussion with Mukesh):
  - Being able to run docker image directly
  - Other deployment types already planned out
  - UI to simplify installation & connection to DB
  - Switch between multiple databases
  - Documentation related to installation

## Must have or atleast do analysis:
  - People asking for Kubernetes installation options
    - Check if this is feasible for 0.1.2
    - Kubernetes manifests and helm charts
  - A fat docker image with Postgres?
    - Seemingly lower priority (based on the installation call) but needs more thought
  - All new user reported issues which are less work and high impact
    - We'll add them to the milestone as users raise issues

## Nice to have (yet to create issues):
  - Modify upgrade UI to only show it in environments where one-click-upgrade is possible
    - Show instructions for other environments
  - Upgrades without docker?
    - We need to start thinking on how this would work
    - Even if we don't have a solution in 0.1.2, we need to start thinking about this

## To remove:
  - Remove the frontend performance issue out of 0.1.2
    - This will take time and we already have considerable frontend work planned for 0.1.2 for the installation UI.
    - We'll plan to take this up for 0.1.3

---
Also discussed,

## 0.1.1
- ETA Thursday
- Release notes will be reviewed today
- Perhaps enabling reordering columns can be part of Sean's usability improvements project?
    - Pavish will talk to Sean about it.
