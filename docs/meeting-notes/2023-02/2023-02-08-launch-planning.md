---
title: 2023-02-08 launch planning meeting
description: 
published: true
date: 2023-07-19T23:30:50.756Z
tags: 
editor: markdown
dateCreated: 2023-02-08T15:57:18.507Z
---

# General update and Q&A
Kriti gave an update on
- Launch goals
- Funding plan
- Usability testing strategy

## Launch goals
- Get early adopters that are really excited about Mathesar and can help us alpha-test it
- Post Mathesar on HN, Reddit
- Get people to install and use it
- Website ready
- Documentation for at least one way to install
- Only have stuff in Launch blockers that block user from deciding whether to install Mathesar
    - Small usability issues and bugs don't block users from deciding to install Mathesar
- Initial target users: Software engineers
    - Reducing target audience size
    - Only aiming now for HN-user types, engineers (since they are the ones deciding whether to install Mathesar)

## Funding
- For Non-profit projects, the important thing is impact
    - Theory of change
- Can't do anything until we launch
- Need to show that we've shipped something
- Need to show people are interested in it.
- Kriti wants to do pitches in March/April

## Usability testing
- Using tool: Playbook UX
- We provide tasks. People record themselves doing it.
- We also ask questions via the tool.
- Goal is to find people similar to initial target audience (HN denizens)
- Main focus is on high-impact changes which might affect adoption
- Also provides insights which we can do post-launch
- Current testing strategy is unmoderated. We might want to do some moderated tests later.
- We've been refining tests. First test didn't go great.
- We're also focusing on the right segment of users for the tests.
- Sean thinks usability tests on installation would be quite useful.
    - Kriti plans to find people on Upwork for that.
    - It's on the plan for launch.
- For more open-ended instructions, we'd need a bigger sample size to get good info.
- The test is designed as a narrative
    - Exploring existing Mathesar Con data set
    - Adding a table called 'Sponsors'
    - Assigning Sponsors to talks
    - Creating an exploration at prompt
- Each test is giving us a 20-minute video of someone using Mathesar

# Launch plan
We're going to launch on **Feb 27**.

Blockers NEED to get done before launch.

## Blockers
- Users & Permissions (Pavish, Rajat, Sean)
    - Pavish & Kriti met Tue to cut scope a bit
- Deployment (Brent, Dom, Mukesh)
    - Brent & Kriti met Tue to cut scope
    - Only "Deployment Type 1"
- Usability testing issues (Ghislaine)
    - https://github.com/centerofci/mathesar/issues/2413
    - More incoming – no major changes planned
- Deployment usability testing (Kriti)
- Demo video (Kriti)
- Update README (Kriti)
- Complete website (Kriti & Ghislaine)
    - Link to docs
    - Integrate demo video
- Reset migrations (???)
- Create and publish release (Kriti)
    - Think about versioning (semantic versioning may not be appopriate for applications)
- Document upgrade process (Brent)

## Nice to have
- Upgrades in UI (Sean)
- Additional deployment types (Brent, Dom, Mukesh)
- "High" items in Backlog milestone (Pavish, Rajat, Sean, Ghislaine)
- Pre-launch publicity (Kriti)
- Process for publishing releases on DockerHub 

## Process
- Currently ad-hoc process for launch
- We'll discuss improving velocity in a more permanent way after launch
- Considering meetings 2-3 times a week to stay focused.
    - Everyone agrees, we'll set these up.

## GSoC / community work
- We'll stop reviewing community work until launch.
- Anish will handle community communication until launch.
    - Kriti will support as needed.
    - Everyone else should ignore community work until we launch.
- If we get into GSoC, we'll review and update project ideas after launch.

## Next steps
- Update launch milestone in GitHub to be accurate.
- Kriti will set up meetings

# Current status
- Users and permissions
    - Try to get this done before any other frontend work, it's in blockers
    - Rajat's PR is open for styling
- Deployment
    - There's a preliminary writeup in #2034
    - New Docker setup for prod is finally merged
        - Brent will send email to mailing list with dev changes
    - install script is looking good, almost done (Mukesh)
    - Documentation is pending
        - Port needs to be documented so that people can run things on different ports if needed 
        - Make sure we're clear about using WSL in Windows
        - Make prerequisites of bash and Docker clear
    - Install script will be friendlier for Windows too
    - Documentation for happy path - ETA Friday or early next week
    - Next steps:
        - Get install.sh done and merged
        - Get Watchtower (upgrade library) done and working with the current setup
        - Documentation
    - Upgrade UI is blocked on discussion
        - Mukesh, Brent, Dom, Sean, Kriti should meet
    - Docker won't pull the new image unless you give it a "build" argument
    - Installation flow
    - Write up for user flow is in #2034
    - We need to make sure we're not building frontend files in the npm container
        - Use pre-built files
        - Double check run.sh - it might be cruft
        - We need to revert package lock changes
    - Make sure to involve frontend engineers in installation review (probably Pavish)
- Usability testing
    - Next steps
        - Finish writing notes for completed tests
        - Write up tasks for what we need to fix before launch
            - Critical
            - Easy to implement
        - Write up other, non-blocking tasks
- Deployment usability testing
    - Wait until we have docs
- Demo video
    - Going back and forth on feedback
    - Doing a new voiceover
    - We seem to have a voiceover sample that works
    - Should have v2 soon (hopefully final)
- Need to update `README.md` - not started
- Website
    - Changes implemented
    - Updating illustrations - in review
    - Once we have docs and demo video, need to integrate
- Not started:
    - Reset migrations
    - Create and publish release (Kriti)
    - Document upgrade process (Brent)