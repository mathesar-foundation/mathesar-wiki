---
title: 2023-03-02 launch check-in
description: 
published: true
date: 2023-03-06T16:39:28.172Z
tags: 
editor: markdown
dateCreated: 2023-03-06T16:37:26.083Z
---

# Publicity Plan
- [Draft document](https://docs.google.com/document/d/1s8WL0Uc9ak4jjHpOP6Mg0r2xsYN-SjbW5pcthF8ejLY/edit#) (not publicly accessible)
- Decide what we're posting when.
    - HN & CCI blog later
    - Rest TBD
- Decide how we're going to handle responding.
    - Coordinate on Matrix Marketing channel if we're responding
    - Tag people if you don't know the answer

# Demo server plan
- Load balancer not sorted out
    - Session stickiness doesn't work, user is switched to a new server when CPU limit is hit.
- Upgrade Postgres on demo server and use session timeout
    - Postgres 14 needed
- Brent will double check that demo server is in a good state now
- No more load testing on the demo server - treat as production now
    - Use mathesar.dev for testing if needed
- Mukesh will coordinate meeting for next steps
    - Dom, Pavish, Mukesh, Brent (optional, interested)
    - Discuss Postgres 14 / pgbouncer / vertical scaling of Postgres DB
        - OIDs may not work with pgbounder
    - Outcome: come up with a plan, present to Kriti for sign off

# Work Plan & Process
- What should we be working on for the next few days?
- How will we track work and priorities in GitHub?

## Notes
- Demo mode improvements
- Community
    - Community PR review
    - GSoC project idea review
- Upgrades
    - Figuring out upgrading docker-compose.yml and .env files
    - If auto-upgrade is not possible (for these two files), we should show that in the UI and ask user to manually upgrade
    - Make upgrade work with new database types etc.
- Documentation
    - Improve installation documentation
    - Documentation for getting library data 
    - Get docs out of codebase and into MkDocs
    - Demo mode documentation
    - Frontend & backend codebase structure
- Installation
    - Make Mathesar work with localhost DBs
        - Document edge cases and names
    - Figure out installation without Docker
    - Figure out some "one click/command deployment"
    - Figuring out installing a specific version
- Release process automation
- Users & Permissions - make frontend / backend consistent
- GitHub process
    - Release based milestones
    - 0.1.1 milestone for now
    - Use weekly iterations

# Further planning
What do we need to figure out now that we've launched? We won't talk about these now, but it would be good to get a list of things we need to talk about next week.

- Launch retrospective
- Permanent Git workflow
- Process for building new features

# Release process improvement idea
- **Added by**: Brent
- **Summary**: Given the current release debacle, I think we should have a testing of the release strategy.
- **Expected time**: 10-20 minutes

*This was deferred until later discussion. We'll discuss when we have a launch retrospective.*

