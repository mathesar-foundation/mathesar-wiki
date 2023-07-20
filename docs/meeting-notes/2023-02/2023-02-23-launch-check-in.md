---
title: 2023-02-23 launch check in
description: 
published: true
date: 2023-05-11T14:46:18.791Z
tags: 
editor: markdown
dateCreated: 2023-02-23T20:03:18.420Z
---

# General check in
- Two working days left!
- Kriti extended current iteration to 2023-02-27
- Some items in Launch nice-to-haves are moved to next week's iteration (e.g. load testing optimizing reflection)
- Only left things in the current milestone that seem to have a reasonable chance of getting done
- This view is up to date: https://github.com/orgs/centerofci/projects/1/views/47
- What if demo site is not ready for lots of traffic?
    - We still launch. If it crashes, then oh well. Demo is just a nice-to-have.

## Users & Permissions
- QA plan is coming along.
- Rajat will review the QA plan.
- Anish and Rajat will handle the QA work.
- Will be done by tomorrow
- Mukesh and Anish are doing some review work for users and permissions
- Reviewers are encouraged to push changes to the PR just so we can get the PRs merged quickly

## Documentation
- Still some outstanding work for documenting users and permissions
- Kriti is reviewing users & permissions docs
- Sean reviewing README PR

## Installation & Deployment

- Deployment type 2 is working, tested locally, tested on GCP test server. PR is submitted, awaiting review.
- Documented differences (in same PR) so users can understand the permissions needed by the user.
- We have hired someone from Upwork to write some more installation docs

## Live demo
- We need to discuss some design/UX issues 
- Timing for improvements to live demo: We are okay pushing some imprvements to the live demo after the release, but we want to get as much in before the release as possible
- Load balancer is in progress
    - Need to figure out how to determine when to scale.
- We'll chat about load balancing implementation details later
- We're hoping to have some improvements completed tomorrow

## Website
- Waiting to work out installation issues before we integrate the docs

## Upgrades
- Still need to QA the upgrade process

## Release
- no updates

## Publicity
- no updates

## Misc
- Issue with "Schemas (0)" displaying sometimes for demo users and local installations
    - Sean experiencing this locally too
    - We've had some reports from live demo users that have hit this bug
    - Sean will hop on a call today with a back-end engineer to troubleshoot

## Priorities per person

### Anish
- Finish all the QA testing tasks 
- Takeover #2520
- Community work

### Brent
- Recreating schema missing/uncreatable bug
- Solving schema missing / uncreatable bug
- Writing up release plan
- Keeping an eye on Deployment type 2 reviews, working towards merge

### Dom
- Test in-app updating (with real Github releases)
- Fix Arxiv dataset in demo
- Work on reflection in demo

### Ghislaine
- Update style for docs
- Alternative design for CTA

### Kriti
- Help move forward installation and deployment
- Help with upgrades if needed
- Demo analytics testing
- Publicity work

### Mukesh
- Review deployment type 2
- Work on Load balancer for demo server
    - Have a basic loadbalancer setup
    - Figure out the health check to scale theinstances
    - Point the mathesar domain to the loadbalancer IP

### Pavish
- Test Upgrades
- On-call for Users & Permissions issues
- Add more Analytics events

### Rajat
- Review the QA plan
- Do the remaining QA items for users and permissions
- Review related changes on users and permissions documentation. 


### Sean
- Live demo usability
    - [Figure out how to navigate from the live demo back to Mathesar.org](https://github.com/centerofci/mathesar/issues/2468)
    - [Allow users to sign up for Mathesar mailing list from live demo](https://github.com/centerofci/mathesar/issues/2494)
- Review [Deployment docs](https://github.com/centerofci/mathesar/pull/2497)
- Review [README updates](https://github.com/centerofci/mathesar/pull/2536)

## Upgrade testing procedure
**Participants**: Pavish, Dom, Sean, Kriti
**Summary**: figure out how to test upgrades and who's going to work on it.

- Preparation:
    - **Dom**: Make sure there are two releases (both on Github and Dockerhub)
        - with different versions strigs/tags in code, in git and in docker
    - **Dom**: Figure out steps to switch between releases in dev
        - so that we can trigger in-app updating and then "rewind"

- Testing process:
    1. **Dom** Call the upgrade endpoint to double-check that it still works
    3. **Pavish** Install that release locally and test upgrade

https://github.com/centerofci/mathesar/issues/2534 has been updated accordingly

## Live Demo navigation changes UX
**Participants**: Sean, Kriti, Ghislaine

Sean, Kriti, and Ghislaine looked at in-progress work and finalized UX for changes to the live demo banner. Related issues:
- https://github.com/centerofci/mathesar/issues/2468
- https://github.com/centerofci/mathesar/issues/2494

## Live Demo load-balancing strategy
**Attendees**: Kriti, Mukesh, Dom, Brent, Sean

- We need to figure out when we trigger adding a new server in our autoscaling policy
- Lots of back and forth discussion
- Because of reflection bugs, demo server will be unresponsive once we hit a certain number of DBs created, even if there's only a single user using it.
    - It is unclear if we can use memory / CPU / number of processes as an indicator of this
        - Dom thinks we can't
        - Unresponsiveness _should_ be able to be correlated with something
    - We could add an endpoint that indicates if there are too many databases and use that as a healthcheck to trigger scaling up
    - It would be best if we didn't need to add a new endpoint and we could use an existing indicator
- Conclusion: Mukesh will load test as needed and identify the best metric
    - Dom pushed the latest tests to `mathesar-scripts` repo
- Setting up infrastructure is the most important thing, we can change autoscaling policy anytime


## Schema bug - debugging session
**Participants**: Brent, Sean, Kriti, Mukesh

- Related to https://github.com/centerofci/mathesar/issues/2523
- Sean screenshared and showed bug happening locally
    - This is because demo mode is broken, https://github.com/centerofci/mathesar/issues/2559 created to track it
- Brent identified issue happening for production, because of collectstatic
- Ideally, we should be building static files as part of the release, not during install process
- Brent will figure it out tomorrow, he has enough info