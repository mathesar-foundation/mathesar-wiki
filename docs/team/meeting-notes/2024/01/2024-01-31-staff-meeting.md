# 2024-01-31 Staff Meeting

## Post-release work planning

From last meeting:

- [New connection creation flow does not handle schema creation failure scenarios](https://github.com/mathesar-foundation/mathesar/issues/3420)
- [Attempting to add connection with both Library Management and Movie Collection schema results in a 502](https://github.com/mathesar-foundation/mathesar/issues/3423)
- Docs
    - Sean: Polish on upgradees
    - Kriti, Sean: Holistic docs review
        - Look at [Pavish's notes](https://hackmd.io/@mathesar/BJv77x-9T)
    - Ghislaine: installation review
- **Sean**: clean up CHANGELOG content, including discussion with team
- **Brent & Pavish**: (Wednesday) update servers to latest release

From Basecamp:
https://3.basecamp.com/5718119/buckets/35537802/todosets/6848469202

Questions to answer:

- How do we handle docs updates after a release? Some options:
    - (A) Allow master to become out of sync with the docker images
    - (B) Publish new docker images without changing the version number
    - (C) Publish our docs from a separate git branch within the main repo
    - (D) Publish our docs from a separate repo
    - (E) Cut a new release when we make docs update
- Where do we publish the CHANGELOG? How do we want it to be formatted?
- What work do we need to do?
- Should we do a 0.1.5 or just update docs on master?
- Timing / deadline?
- Who is doing what?

### Discussion

- We'd like to do releases once per month but we have more work to do to make the testing process more efficient.
- We should try to release again at the end of February
    - Bug fixes
    - Figure out issue with Demo
    - i18n code work
    - Japanese translations
- We want to make docs changes ahead of time, not wait for 0.1.5
    - [Update "Connect to an external database server" docs](https://github.com/mathesar-foundation/mathesar/issues/3428)
    - Sean/Brent: clean up CHANGELOG content
    - Kriti, Sean: Holistic docs review
    - Ghislaine: installation review
    - Sean: Add links to the installation video
- Bug: Mathesar 0.1.4 cannot run in demo mode
    - We'll fix this and then deploy the demo site off of the develop branch
    - You need to set the demo flag in the environment variables. Then Mathesar will not run.
    - Brent will make a GitHub issue and assign it to Anish.
    - Anish will work on this ASAP
- Bug: [New connection creation flow does not handle schema creation failure scenarios](https://github.com/mathesar-foundation/mathesar/issues/3420)
    - Anish will work on this
- Bug: [Attempting to add connection with both Library Management and Movie Collection schema results in a 502](https://github.com/mathesar-foundation/mathesar/issues/3423)
    - Anish will work on this
- We need to make a release announcement
    - Kriti will work on this
    - write copy
    - publish
- Sean and Brent will coordinate details about the CHANGELOG
- How do we handle docs updates after a release? Some options:
    - Definitely don't want to new publish Docker images
    - Limit to: A, C, D
    - We'll go with with (A) Allow master to become out of sync with the docker images
- i18n schedule
    - Pavish is worried about not being able to finish the i18n changes by then end of February
    - We won't block the release on the i18n work. We can still release with some small bug fixes even if i18n isn't done.
- Planning work that we need to do soon:
    - users and permissions is blocking backend performance and architecture work
        - Kriti: users and permissions should take priority over i18n
- Deployment work & teardown
    - Brent (already tracked in basecamp)
- Brent: add basecamp task for tracking infrastructure and costs
- Sean: close milestone

## Structuring future meetings

How to structure our meetings for strategy, design, product, other processes

### Brainstorm

Meetings, purposes, timing

- "Big picture" product meetings for big new features
- Product approval meetings for tickets
- Design / UX sessions for small features
- Strategy meetings
- Architecture meetings
- Beta planning meeting

### Discussion

- Goals for February
    - we should focus on 0.1.5
    - no features, just bug fixes.
    - solidify plans for users and permissions
    - decide on architectural plans for backend performance improvements
    - have strategy discussions — e.g. how we want to grow our user base, whether we want to pursue a SaaS offering
- Permissions and worksheets
    - Hard to separate these into independent discussions
    - Pavish: want to prioritize making decisions on permissions first because we need that for the beta but we don't need worksheets for the beta
    - Kriti: yes, but we don't want to have to re-do permissions a third time. We need to take the worksheets discussion into account as well
- Structure of meetings
    - **architecture** discussions will happen via email
    - **Ticket approval** - 1 per month
    - **product meetings** (where we discuss large features, requirements, etc)
        - should happen every week
        - Adam will attend these as well
    - **product strategy**
        - Will happen during weekly team meetings
    - **beta planning**
        - Will happen during weekly team meetings
    - **UX sessions**
        - Kriti: maybe we don't need to do as many of these meetings
        - AdHoc meetings as needed.
    - **team meetings**
        - Kriti: let's keep this on the calendar every week but actually use the time for discussions like product strategy, beta planning, etc.
- Brent: we need to get better about testing in order to increase our release cadence
    - need to figure out the "build static files" issue
    - need to improve our CI testing matrix to test more Python versions
    - Kriti: we'll have more time to talk about these in more detail in our beta planning
