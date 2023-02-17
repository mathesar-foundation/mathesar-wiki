---
title: 2023-02-17 launch check in
description: 
published: true
date: 2023-02-17T15:56:27.332Z
tags: 
editor: markdown
dateCreated: 2023-02-17T15:55:23.616Z
---

# Upcoming meetings
- Monday's launch check in is moved to Tuesday because of US holiday
- Next week's community team event is moved one week since we have a lot to do before launch. It's now on March 3.

# General check in

## Users & Permissions
- PRs open for items assigned to both Rajat and Sean.
- Pavish should have PRs ready by Monday.
- QA: Anish is working on the document. We could start it on Tuesday.

## Installation & Deployment
- Docs and install script are done. Kriti will take a look at it after it's merged.
- We'll get feedback from people from Upwork once ready.
    - Kriti has interviewed and selected a bunch of people to test the installation process.
- Next steps: implement installation with connecting existing DBs, and setting up domains
    - Kriti will make sure issues exist for these
    - Update existing Deployment Type 2 issue

## Live demo
- Analytics PR is merged.
- Mukesh is trying to figure out how to integrate it with the FE.
- Next steps: Kriti will deploy and test it.

## Website
- There's a PR to update CTAs, to inform about the sass version, docs integration etc.,
- Most blockers are complete.

## Documentation
- Need to add HTTPS redirect
- Improvements waiting to be merged

## Usability improvements
- All remaining issues are assigned.

## Upgrades
- Sean: Coming along well. No additional help is needed at the moment.
- There's a bit of work on the FE since the logic is shifted to FE.
- There should be a PR on Monday.
- Inorder to test, there should be atleast two releases published to GH.

## Release
- Brent is assigned to resetting migrations and creating first release
- ETA early next week

## Publicity
- Kriti is coming up with plans for publicity.
    - HN, email posts, social media posts etc.,
- We'll discuss about how to distribute comments on thread between team members next week.

## Priorities per person

### Anish
- QA plan for users & permissions
- Usability issues

### Brent
- Keep an eye on deployment/documentation feedback
- Double-check that we can deploy (type 1) on GCP, with domain, https etc. work
- Reset migrations
- Publish 2 test releases (comms with Sean)
- Update script/docs to handle deployment type 2

### Dom
- Upgrade support for Sean
- Load testing live demo

### Ghislaine
- Website & design

### Kriti
- A number of things related to usability testing, website, publicity, sponsorship etc.,

### Mukesh
- Analytics
- Help Brent with installation
- Talk to Kriti if further work needed

### Pavish
- Users & Permissions issues

### Rajat
- Users & Permissions review
- Usability issues

### Sean
- Upgrades
- Live demo

# Version number format
- **Added by**: Sean
- **Summary**: I need to know the format we're using for the version number. With our recent decesion to push more upgrade logic to the front end, the front end needs to parse the version number to determine whether the latest version is an upgrade.

### Notes
- Kriti did some research on versioning, let's use SemVer
- First testing release 0.0.1, second testing release: 0.0.2
- First actual alpha release: 0.1.0

# Frontend analytics guidance
- **Added by**: Mukesh
- **Attendees**: Mukesh, Sean, Pavish, Kriti (partial)
- **Summary**: Need input from frontend team to decide on architecture to implement custom events for demo server.

### Notes
- Decided against implementing analytics in the backend because frontend has a lot of events that are not visible to backend.
- Kriti: if this is going to be very complicated to implement, we can skip it for launch.

*Further notes coming soon*