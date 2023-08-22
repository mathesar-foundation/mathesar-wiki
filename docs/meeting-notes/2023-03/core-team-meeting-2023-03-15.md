---
title: Core team meeting 2023-03-15
description: 
published: true
date: 2023-07-19T23:33:26.208Z
tags: 
editor: markdown
dateCreated: 2023-03-15T16:30:56.637Z
---

**Date**: 2023-03-13
**Attendees**: All core team members + Anish


## Bigger-picture plan for Mathesar
General plan: 
- Things are still in flux
- Figuring out how to grow the project
- Figuring out what our structure should be
- Trying to get to a small core of users that really like us over competition
- Brent:
    - What's the nature of intended (hopeful) user base?
        - Big institutions e.g. Smithsonian?
        - Bunches of home users
        - SaaS
- Kriti:
    - For initial phase, targeting home users
    - Main aim is to have self-hosted version; SaaS is just to support self-hosted
- Pavish:
    - For v1 are we going to focus on stabilizing current feature set?
    - For v1 are we going to be developing new features?
- Kriti:
    - Didn't mean to imply no new features
    - New features should be rooted in user feedback
    - Whose problems are being solved best by us currently, and how can we enhance that / support those users better.
- Pavish:
    - With home users, it's going to be hard to understand them (compared to SaaS)
- Kriti:
    - We don't need to grow right now
    - We need a small committed core of users
    - We have a mailing list we haven't tapped
    - We could survey them
    - Someone on Reddit:
        - Want to build a small DB-backed app for a radio station
        - One requirement: uploading files
    - Joi:
        - Wants to have a file storage type (image-specific in his case)
- Sean:
    - tension between two quite different use-cases for Mathesar
        - standalone: Mathesar is the reason there's a postgres DB
        - admin: Postgres already exists, and Mathesar is included on top
    - Picking a use-case, putting all effort into one bucket
        - Better for that use case
        - More useful for some users, but cuts others out
- Kriti:
    - We want to make mathesar work for all those use cases (in the end)
    - We should use one use-case to focus on once we know which is best
    - At the moment, we don't have enough info to decide.
    - We've seen examples of both
    - Slight inkling is to focus on connecting DBs.
- Mukesh:
    - Still figuring out our niche
    - How much data do we need to figure it out?
- Kriti:
    - Tracking feedback and understanding users should be a top priority
    - We don't have to stop feature development
    - Should focus on features useful for multiple cases
    - These use cases converge down the road: mathesar-only users at the beginning might want to integrate with other tools
- Mukesh:
    - spreading thin slows down trajectory
- Brent:
    - Want to continue async
- Rajat:
    - We need to record user info/attributes:
        - titles,
        - companies,
        - etc.
- Kriti:
    - Not recording that yet.
- Brent volunteers to maintain ongoing HackMD moving forward. Will start an email thread, too.
- Ghislaine:
    - Wants to make sure we're still innovating; need to leave space for our own imagination, not always chasing user feedback.

## Selecting projects
- Sean wants to get rid of some rows in projects table
    - Releases
    - Understand Mathesar Users    
- After we decide who owns various ongoing things, we'll figure out tracking
- Selected projects
    - Funding
    - Removing SQLAlchemy
    - Localization
    - Installation improvements
    - GSoC
    - User feedback process
    - Frontend performance (Tables)
    - File & image types

## Assigning responsibilities

### Notes

- We assigned one owner to each responsibility.
- We _started_ assigning helpers to responsibilities too, but we didn't have enough time to finish. We'll continue this process async.
- **Next steps**: Sean will add some content to the wiki, documenting all this and providing a starting point for project-specific information to grow.

### Interests and assignments

| Responsibility           | Anish | Brent | Dom  | Ghislaine | Mukesh | Pavish | Rajat | Sean | Kriti |
| --                       | :--:  | :--:  | :--: | :--:      | :--:   | :--:   | :--:  | :--: |  :--: |
| ♻️ User feedback         | ❕    | ♟️     | ❕   | ✅        | ⭐      | ⭐     | ⭐     | ❕   | ❕  |  ️️
| ♻️ Team management       | ❕    | ❕     | ❤️   | ❕        | ❕      | ❕     | ❕     | ✅   | ❕  |
| ♻️ Marketing             | ⭐    | ❕     | ❤️   | ⭐        | ❕      | ⭐     | ✅     | ❤️   | ❕  |
| ♻️ Repo admin            | ❕    | ❕     | ❤️   | ❕        | ❕      | ✅     | ❤️     | ❤️   | ❕  |
| ♻️ Release management    | ❕    | ❤️     | ❤️   | ❕        | ⭐      | ✅     | ❤️     | ❕   | ❕  |
| ♻️ Assisting installs    | ❕    | ♟️     | ❤️   | ❕        | ✅      | ❤️     | ❤️     | ❤️   | ❕  |
| 🏆 GSoC admin            | ⭐    | ⭐     | ✅   | ❕        | ⭐      | ❕     | ⭐     | ❕   | ❕  |
| 🏆 Improve install       | ⭐    | ⭐     | ❕   | ❕        | ✅      | ♟️     | ⭐     | ❕   | ❕  |
| 🏆 Funding               | ⭐    | ❕     | ❕   | ⭐        | ⭐      | ⭐     | ❕     | ⭐   | ✅  |
| 🏆 Removing SQLAlchemy   | ❕    | ✅     | ❕   | ❕        | ❕      | ❕     | ❕     | ❕   | ❕  |
| 🏆 Localization          | ❕    | ❕     | ❕   | ❕        | ❕      | ❕     | ✅     | ❕   | ❕  |
| 🏆 User feedback process | ❕    | ❕     | ❕   | ✅        | ❕      | ❕     | ❕     | ❕   | ❕  |
| 🏆 FE performance        | ❕    | ❕     | ❕   | ❕        | ❕      | ✅     | ❕     | ❕   | ❕  |
| 🏆 File & image types    | ❕    | ❕     | ❕   | ❕        | ❕      | ❕     | ❕     | ✅   | ❕  |

Key:

- Types
    - ♻️ Ongoing responsibility
    - 🏆 Project responsibility
- Decisions
    - ✅ = Owner
    - ♟️ = Helper
- Preferences
    - ❤️ = Want to own or help
    - ⭐ = Want to help
    - ❕ = Not interested

### Definitions

Ongoing responsibilities are defined as:

- **Marketing**
    - Receive the firehose of Syften notifications
    - Eagerly reply to to threads as needed, seeking to ameliorate people's concerns and amplify people's excitement.
    - Generate new posts periodically (once our installation process is improved)
    - Make improvements to Mathesar.org as needed (running all changes by Kriti first)
    - Monitor "hello@mathesar.org" and "Request a free install" form and follow up with people as needed.
    - Track publicity for archival purposes
    - Forward noteworthy publicity to the rest of the team as needed

- **Repo admin**
    - Receive the firehose of GitHub notifications and take action on items as necessary.
    - Triage new issues and PRs
    - Actively shepherd PRs towards closing to help prevent them from going stale
    - Troubleshoot GitHub actions and make improvements where necessary

- **Release management** 
    - Decide what goes in each release
    - Decide when to release
    - Publish each release, delegating tasks as needed
    - Keep the team informed so that everyone knows the correct release to target with new tickets and new PRs
    - Document our release process and support the team with questions about it
    - Document our git branch strategy and support the team with questions about it
    - Keep our broader goals and strategies in-mind, potentially planning multiple major/minor/point releases ahead.
    - Decide when to update the staging and demo servers and delegate that work as needed

- **Team management**
    - Schedule and facilitate team meetings
    - Monitor people's standups and hold regular 1/1 meetings with all team members ensuring everyone is productive, happy, and accountable
    - Schedule team/community events and make sure they have facilitators

- **Assisting installs**
    - Help find notable use cases for Mathesar, and drive whatever needs to be built to make those use cases work.
        e.g. we talked about using Mathesar in the Chelsea Project to share wastewater data. someone needs to look at the data, get it into Mathesar, talk to Sam to get her requirements for what she wants sharing to look like, break it down into features for Mathesar, etc.
    - there’s other use cases too that Kriti doesn't have the bandwidth to follow up on



