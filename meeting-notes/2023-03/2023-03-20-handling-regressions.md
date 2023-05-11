---
title: Handling regressions in 0.1.1
description: 
published: true
date: 2023-05-11T14:49:01.004Z
tags: 
editor: markdown
dateCreated: 2023-03-20T14:36:11.229Z
---

# 2023-03-20 Handling regressions in 0.1.1

Meeting attendees: Pavish, Sean, Rajat

## Brainstorm: Best strategy to revert the column_reorder changes
- If there aren't merge conflicts, we'll try to revert entirely
- If there are, we can comment it out
- When picking the feature, we'll open a new PR
- Sean will be commenting on the contributor's PR mentioning why we had to revert. We'll also ask them if they're interested in continuing it.

## Brainstorm: Best strategy to review full changesets for releases
- All of us will look at the full changeset ([PR](https://github.com/centerofci/mathesar/pull/2723/files)) and comment if we notice any red flags or have questions

## Brainstorm: Frontend testing strategy - E2E tests
- We're scratching everything clean and starting from point zero
- We'll rethink the entire testing strategy from the beginning
    - Do we need E2E test or do we come up with integ tests?
    - Do we rely on the backend or mock the APIs?
    - Since our routing and common data logic is shared between python and JS, what's the best way to run frontend tests?
    - If we do decided on E2E, do we go with playwright and have manual tests or use a tool like Cypress to make things easier for us?
- We'll think on this individually and have another call before `0.1.2`
    - It won't be possible to introduce a new testing strategy by then, but we can still decide on what it needs to be

## Brainstorm: Release process updates to prevent issues like these
- Staging should on develop (check if it is)
- A buffer period makes sense, but only if we're dog-fooding Mathesar more
    - The core team should be using Mathesar for something (the `develop` branch)
- Smoke tests should be improved. We'll think of testing User flows instead of the 'do-whatever-and-try-to-break' strategy. Eg., We can test with the user flow that we used for the demo video.
- Each PR should include information on the features it touches. This will help reviwers and during releases, when we do manual smoke tests.
- We'll continue to think on this and coming up with ideas


