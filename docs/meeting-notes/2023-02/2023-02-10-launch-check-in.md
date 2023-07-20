---
title: 2023-02-10 launch check-in
description: 
published: true
date: 2023-05-11T14:45:47.966Z
tags: 
editor: markdown
dateCreated: 2023-02-10T15:55:45.786Z
---

# General check in
- **GH project**: Kriti updated the GH project, made issues for things we need to do. GH proj should be primary source of truth.
- **Users/Perms:** Pavish has assigned out all the rest of the work. It's coming along nicely. Should be completed by the end of next week. No other back-end issues are blocking Users/Perms FE work now. Mukesh is on standby to fix backend issues if needed. We should do some manual QA testing after we're done.
- **Installation**: Docker setup merged. Install script in draft PR form. We adjusted some tasks within GH during the meeting. We're focusing only on "Deployment type 1". Maybe Dom could work on other deployment types?
- **Updates** Still working on Watchtower.
- **Docs** Brent has started working on docs content. Docs content is so far limited to install process. Still need to flesh out the "wrapper" docs content, with top-level stuff.
- **Usability testing**: Finished first round. [See notes](https://hackmd.io/isRhxp4fQoKHaJ457r1FOg) Nothing seems to be blocking the launch so far. We have things to work on later though. 
- **Deployment testing** Blocked on docs being done. We're working on getting machines for Mac/Linux/Windows to test on various platforms based on instructions in docs.
- **Demo video**: New voiceover is done. They're working on the edit.
- **Website**: Looking good. New illusstrations are done. Basically the website is done!
- **Funding**: Kriti set up GH sponsors and OpenCollective. Still some more work to do as far as fleshing out profiles and funding platforms being integrated into other things
- **Other tasks**: (in case anyone runs out of work)
    - Load-testing the demo site?
    - Other deployment types?
    - We'll chat as-needed to figure this out.
- **Need to create tasks for**:
    - We need to find some time to QA Users & Permissions thoroughly after work is done
    - Users & Permissions documentation
        - Might also do in-app documentation

# How do permissions affect edits to metadata
- **Summary**: We have user roles: "Manager", "Editor", and "Viewer". Can an Editor modify metadata like Explorations, and column display settings? I predict that some users will want to grant this permission and some will not. Short of adding another role, we should take our best guess as to the behavior that most users will want, making sure we're all on the same page as a team.

## Notes
- Editors _can_ edit metadata. 
- Schema/table names and descriptions are _not_ considered metadata (since they're stored in the user database).
- We may want more granular permissions later, but we hope this will be okay for now

# Planning for upgrades via UI
- **Summary**: tie up the loose ends with the design for the in-app upgrade process

## Notes
- Disagrements on fetching latest version info
    - Kriti doesn't want a cron job since it adds deployement complexity. Instead, we could fetch latest versions when an admin user is logged in.
    - Dom has already impelented caching. Is the cron job already implemented?
        - Cron job is not implemented
    - Mukesh suggests we send requests from the frontend in a loop with some timeout which triggers fetching latest versions.
    - Final decision is to not have a cron job.
- UX for updates
    - Would contain 'Last checked time'.
    - Would have a button that says 'Check for updates now'.
    - TTL checks for latest versions is left upto the frontend team for now.
- Sean and Dom will decide on next steps and update GitHub issues with the latest plan