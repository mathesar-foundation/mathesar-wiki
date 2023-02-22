---
title: 2023-02-21 launch check in
description: 
published: true
date: 2023-02-22T16:25:28.304Z
tags: 
editor: markdown
dateCreated: 2023-02-21T16:31:17.009Z
---

# General check in

## Users & Permissions
- There's a open PR with rest of pending items
- If we want to change UX as per Kriti's comments, won't take long
    - pending confirmation
    - let's go ahead with UX changes
- Hopefully merged today or tomorrow
- Docs for this are currently assigned to Kriti; 
- Don't include unconfirmed tables issue #2520
    - There's a PR -- pending review;
    - nice-to-have

## Installation & Deployment
- SSL wasn't working, but it's fixed
    - PR is in, not quite working, but it'll be sorted by tomorrow
    - Mukesh's approach is better
    - that will make deployment work on a server with a domain
- next priority: deployment type 2
    - connect existing database
    - not very difficult
- library.mathesar.org will be used for testing deployment types
- static files not loading issue was breaking Docker image, that's fixed
    - `master` builds Docker image that functions
- Usability testing: seems to be going well.
    - We can work on this after deployment type 2
- Deployment type 3:
    - Mostly should work, needs either documentation on environment variables, or convenience scripts to wrap commands in proper environment (e.g., read from .env file)

## Live demo
- Load testing has multiple issues
- When initializing multiple users at once, demo server doesn't return requests
- Front end issues are further out in the queue

## Website
- 404 page PR is submitted
- Integrating documentation is happening today

## Documentation
- Integrating into website
- Documenting type 2 and 3 deployments
- Update `README.md` (issue #2495)
- Ghislaine working on styling 
    - could integrate feedback from usability testers

## Usability improvements
- PRs are in for all blocking issues
- People should be reviewing today or tomorrow

## Upgrades
- Sean opened a PR over the weekend.
- The releases exist, but 
    - We should delete them
    - Merge the upgrades frontend PR #2514,
        - Change POST request to GET
    - Make some new releases,
    - Make sure it works through manual QA.

## Release
- Migrations are reset
- Create and publish first release

## Publicity
- The HN post is in the works

## Priorities per person

### Anish
- Reviewing #2520
- Community work
- QA for Users and Permissions

### Brent
- Testing deployment type 1 with SSL
- Deployment type 2
- Propose release process
- Implement deployment usability testing fixes as needed
- Website bio double-check

### Dom
- Rewrite upgrade endpoint from GET to POST in caddyfile 
- Demo bottleneck hunting

### Ghislaine
- Style Wiki and Documentation
- Update bios on website
- Alternative design for CTA
- Table rename prompt design

### Kriti
- Keep people unblocked
- Plan for QA and docs
- Write README, HN post, etc.

### Mukesh
- Get the analytics PR #2513 merged into the frontend codebase
- Start working on Deployment Type 3 work
- Log more analytic events

### Pavish
- Review and merge upgrades PR
- Get users & permissions PR merged - fix review comments if any
- Review other launch PRs
- Avoid merging / worrying about PRs not involved with launch

### Rajat
- General usability testing
- Docs for users and permissions
- QA for users and permissions

### Sean
1. PR review for Pavish/Rajat
1. Live demo usability improvements

# Testing Docker images, Github Releases
**Summary**: Follow up on [Brent's email](https://groups.google.com/a/mathesar.org/g/mathesar-developers/c/-AALJgNGxjQ/m/6DQ2QAWZEgAJ), decide on next steps

- Process proposed in email seems very bureaucratic
- Big picture: We need to know our master branch produce deployments that function.
- How often do we need to test that install.sh works?
- Should we test on every PR?
    - Setting up CI for this would be tricky
- Should we test before every release?
    - If we identify problems, it could take some time to diagnose and fix if the problem was introduced a long time before.
- Brent is interested in a using a separate _Docker_ repo (not a separate GitHub repo). We might need separate images for separate deployment types
- Kriti: I don't think manually testing every day before release is a priority. And I don't think setting up automated testing is a priority right now either.
- Main thing we need to discuss right now: What's the process for cutting a release?
- Do we really need a separate Docker repo to test the releaes?
    - We could use a separate tag in the same Docker repo.
    - We have the non-pro version of Docker. It's not great for managing tags.
- Brent: We should make it so that install.sh takes a tag name as an argument. Then the docs instructions would tell users to run install.sh with a tag name that we manually set into the docs content.
- Dom: we'll need to consider how the upgrade process works with Watchtower, may not work unless we use a consistent tag for latest version (rather than version number based tags).
- Lots of complexity to consider, can't resolve now.
- Next step: **Brent will write a wiki page proposing a step-by-step process for how to cut a release.**
    - We'll discuss once that's ready 
