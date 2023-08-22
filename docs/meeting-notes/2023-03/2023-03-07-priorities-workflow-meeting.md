---
title: 2023-03-07 priorities & workflow meeting
description: 
published: true
date: 2023-07-19T23:32:30.942Z
tags: 
editor: markdown
dateCreated: 2023-03-07T15:50:27.105Z
---

# Current top goal: user growth
**Goal** Get people using Mathesar!

This will help with sustainability (funding & future revenue).

How we do this:
- Find a way to track user growth
- Spread the word about Mathesar
- Help people set up Mathesar if they ask
- Fix issues people report and make releases quickly
- Base our roadmap on feedback we receive
- Do usability testing with existing users, feed any improvements into our release cycle
- Improving our community

## Questions & notes
- How do we know how many users we have?
    - We still need to figure out how to measure this.
    - We have analytics for the website, but this doesn't tell us how many people are using Mathesar
    - We are wary of putting any telemetry in the product itself
    - If we allow installation and distribution through Linux package repositories, we'd get some metrics on installation
    - Could track unique cloners from GH for any install method that uses `git clone`
- We should prioritize supporting users who are encountering difficulties with installation and deployment. This will help adoption.
- We should prioritize issues that people report (e.g. bugs etc)
- How are we going to get feedback from _non-users_ about features that are _preventing_ them from adoping Mathesar?
    - We have a roadmap which links to GH discussion topics. People can upvote the topics. This process is modeled after https://js.wiki/feedback/
- Rajat
    - "Do usability testing with existing users, feed any improvements into our release cycle" - I am curious how do we do this with a real user?
    Kriti: the way we've done it in the past... incentivise users with a gift card or similar. Then invite them to join a scheduled discussion session. "Rocket Surgery Made Easy", a short, easy-to-read book has some good advise here.
- Mukesh
    > "Fix issues people report and make releases quickly"
  -  Prioritizing features to build
        - We have features requests which would take us in a different direction, for example changing our current install script meant for easy one-click installation where users let us do the necessary steps needed to run mathesar to a detailed multi-step process where we inform the user what is being done. I don't want us to chase two rabbits at time. 
- Brent
    - We need to cultivate our user feedback
        - Consider where and how we're trying to get feedback
        - Try and present ourselves in a way to gather useful feedback
        - Guide users into giving useful feedback (problems, not features) 
- Pavish: SaaS userbase may not care about the same things as hosted version
- Anish
    - Will it help us to look at feedback from other mature alternatives like(Airtable, Baserow and so.) to prioritize what features we should implement? 
    - Maybe we can prioritise features that people have been asking for a long time but it hasn't yet been implemented.
    - Right now we'll prioritize feedback from people actually using Mathesar. But later we'll try to branch out and get more feedback from other users too.

# Project-based workflow
This is a new proposed structure for all new work in Mathesar.

Each new feature, or other initiative is a "project". Even funding can be a project!

## Attributes
Projects have the following attributes:
- **Responsibilities**
    - **Owner**: Person that's directly responsible for the project.
    - **Approver(s)**: People responsible for approving the project.
    - **Contributor(s)**: People working on the project.
- **Problem**: The problem solved by this project.
- **Outcome**: The expected outcome of this project.
- **Solution**: A spec or description of the solution.
- **Timeline**: Timeline for shipping this project.
- **Risks**: Any risks posed by the project, or the specific implementation.
- **Issues**: Associated GitHub issues
- **Wiki pages**: Associated wiki pages

## Process
- We set up a place on the wiki to document projects.
- We have regular meetings/emails to decide on what projects we're going to work on, and who will own them. 
- The owner writes up a document following the project template. The detail in the document should match the timeline of the project
    - e.g. a 1 week project needs less detail; a 6 week project needs more
- Contributors and approvers review & approve the project.
- We work on the project, cutting scope as needed to ship it within the timeline.

## Questions & notes
- Kriti wants to not be involved in everything. She can be involved in prioritization. Projects will be more autonomous.
- Pavish:
    - How do we decide on the timeline on writing up the document?
        - Based on the RFC I wrote for Users & Permissions, this takes considerable time, since planning it out was the major part of the work.
    - Would the project detail cover implementation details?
        - What is the depth of information covered here?
    - What happens to the timeline calculation when we hit a roadblock during implementation?
    - We might need someone to do manual QA on the projects, if applicable, and it's better if they're not the owner or the contributors.
- Pavish concerned about the time it takes to write the specs
    - Writing the full technical spec is part of the project implementation
    - Kriti: specs don't need to be too involved for smaller projects. Could be similar to what we write for a GSoC project idea
- Mukesh
    - Can we add a pre-requisite attribute? This will give us an idea of the timeline. 
    - Sean: I think projects should be as self-contained as possible.
    - Kriti: Sure -- the project attributes listed above are only the "required" attributes. We can add other attributes to specific projects as needed.
- Projects can only have one owner
- Brent: What if we want to have _ongoing_ projects without a clear end date?
    - e.g. "Improving Mathesar's compatibility with pre-existing databases"
    - Kriti: All projects should have a specefic desired outcome
    - Consider a "theme" attribute to projects
    - No ongoing project
- Kriti: We should try to scope projects to take 3 - 4 weeks to complete

# Release strategy
- When should we do releases?
- Options:
    - Specific cadence
    - When a project gets merged
    - When an important bug fix gets merged
- How do we decide when a bug fix is important enough to cut a release?
- Releases should have owners
    - Decide what goes into the release
        - What should be prioritized for the release
    - Coordinate with everyone involved
    - Make the release
    - Team agrees with each release having an owner
- Should we have a regular schedule for releases?
- Sean: I think we should wait a bit before planning out how we do releases
- Mukesh: do we want to do "Themed releases"?
- Kriti will take responsibility for the next release. She will delegate heavily
- Pavish: minor versions would be better suited for a regular schedule. Major releases could be done without a regular schedule

# Specific project ideas
I'm not suggesting we prioritize all of these right now. This is just to give an idea of what projects could be, and pick priorities from them. We could even add others.

- Funding - high priority
- Sponsorships
- Localization of UI - contractual obligation
- SaaS version of Mathesar
- Demo server improvements - low priority
- Removing SQLAlchemy
- Using Postgres users for users & permissions
- User growth & understanding user feedback
    - Decide on metrics for user growth
        - Should be driven by questions we have
    - We need to have a more specific project here (e.g. "grow Mathesar to X users")
- Installation improvements
    - We need to have a more specific project outcome here
- Community improvement projects
    - e.g. GSoC org admin
    - e.g. go through old issues and update them to be relevant from contributors
    - e.g. revamp community team with clear roles & responsiblities for each type of community member
    - e.g. document frontend & backend codebase structure
    - e.g. establish process for issue & PR triage
- Individual features on our roadmap

## Questions & notes
- Kriti will start an email thread about project ideas to help us plan
- Pavish:
    - I think we should prioritize ironing out issues when connecting with existing DBs. Based on the comments, a number of users were primarily interested in using Mathesar for their existing DBs (we have to take into account that these users are primarily developers).
        - We currently do not support multi-column PKs.
            - I saw somewhere a contributor is attempting to fix an issue related to this, but that just disables editing tables which has multi-column PKs. This might be fine for a while.
        - We need to improve the reflection & metadata mechanism, a button to manually reload may not be feasible for the first stable release.

## Git workflow
We need to decide on our permanent Git workflow for releases.

Options:
- [git flow](https://nvie.com/posts/a-successful-git-branching-model/)
    - This is our current workflow with our `develop` branch
- [GitLab release flow](https://docs.gitlab.com/ee/topics/gitlab_flow.html#release-branches-with-gitlab-flow)

*Not discussed at the meeting, will be discussed via email.*

## Release testing strategy
- **Added by**: Brent
- **Summary**: Given the current release debacle, I think we should have a testing of the release strategy.
- **Expected time**: 10-20 minutes

*Not discussed at the meeting, will be discussed via email.*

