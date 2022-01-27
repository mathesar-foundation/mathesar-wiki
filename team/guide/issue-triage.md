---
title: Issue Triage
description: Guidelines for triaging new issues
published: true
date: 2021-12-17T11:59:01.136Z
tags: 
editor: markdown
dateCreated: 2021-08-31T15:44:09.044Z
---

Triaging an issue means setting all the appropriate fields on it.

## Responsibility

- Everyone creating issues should do their best to triage them at creation time.
- [Team](/team) members also [rotate](/team/guide/comms-assignee) responsibility for catching issues that were not triaged during creation.

## How to triage one issue

1. **Set required labels**

    | Prefix | Required count | Notes |
    | - | - | - |
    | `work:` | 1+ | All `work: design` issues should also be marked `restricted: design team` because only the design team can currently work on those. |
    | `type:` | 1 | |
    | `status:` | 1 | _Should not be `status: triage`_ |

1. **Set optional labels**
  
    Scan through the full labels list and apply other labels as necessary. Learn more about the [meaning of all our labels](https://github.com/centerofci/mathesar/labels).


1. **Verify Project and fields**

    Set the Project to "Mathesar".

    Within the project, ensure that the `status`, `priority`, and `work` fields are set.

    > The project is only accessible to [Team](/team) members, but all relevant information (such as status, priority, and milestone) should be available on individual issues. We will make this project public as soon as GitHub supports it.
    {.is-warning}

1. **Set milestone**

    If an issue is directly associated with a feature, put it in the milestone for that feature. Otherwise, put it in a "General Improvements" milestone according to priority. More urgent issues should go in this month's milestone, otherwise put it in a milestone in the next couple of months.

    If you don't know what milestone to put something in, talk to Kriti.

    Do not create any new milestones.

## Notes on Labels and Milestones

The list of available labels and milestones should only be changed in the `mathesar` repo. They are synced every day to the other repos related to the project using [this GitHub action](https://github.com/centerofci/mathesar/blob/master/.github/workflows/sync-github-labels-milestones.yml).