**Attendees**: Core team, Anish

## Funding update
*Notes from this section are private. Core team members can access the notes in [this HackMD document](https://hackmd.io/nAjDAopkSQKEcR7L_A__pg).*

## Projects approval check in
- Postgres compatibility
    - Project already approved
    - very few changes, no ne
- Niche research
    - More changes to push, but was waiting to understand the state of the wiki migration
    - Ghislaine will update the thread once changes are pushed
- Installation improvements
    - first week will be cleaning up from 0.1.3
    - Removing some of the research work as per feedback
    - Should be enough time, with Anish's help
    - We have a one-week buffer in the schedule
    - Mukesh will update the email thread once project changes are pushed

## Project prioritization
- Release 0.1.3
- Installation improvements
- Niche research
- Postgres compatibility
- Ad hoc

Discussion:
- What about 0.1.4?
    - Not prioritizzed here since it will be done in the cooldown after the cycle
- Everything we merge in during the cycle should be "release-ready"
    - We'll cut the release with whatever is done
- Brent: feature flags will help with release cadence
- Mukesh: what about experimental features?
    - Docker image was possible to use, but needed more testing. Would be nice to publish as 'experimental'
- Kriti will be out for 4 weeks starting next week (if possible)
    - Thus, we'll provisionally extend the cycle by one week
    - Kriti's vacation: 2023-08-28 - 2023-09-25 (Hopefully)
    - Cycle work period: 2023-08-21 - 2023-09-22
    - Cycle cool down: 2023-09-25 - 2023-10-06
    - Thus, 0.1.4 should release around 2023-10-05
- After the call, Kriti will add some calendar events to tell us which week of the cycle we're in.
- Sean: Would be nice to name the cycle something absolute rather than relative
    - For now, we can name them after the release
    - Official cycle name for _this_ cycle: Cycle 0.1.4
    

## Release 0.1.3 check in
- Who can take this over from Rajat?
    - Brent will take this over
- Also do we have anyone taking over repo admin?
    - Sean will take this over
- It's important to test the images 
    - especially make sure login and import upload pages work
    - Pavish will help release owner know what to test
- Issue: https://github.com/centerofci/mathesar/issues/3149
- Thread: https://groups.google.com/a/mathesar.org/g/mathesar-developers/c/Uvjw95NeSUg/m/XZtkM0O8BQAJ
- Double-check the superuser creation process for this release

## Ongoing conversations check in
- Should we install things on the user database
    - We're going to go ahead with installing things on the target DB
    - Brent will update the thread with this conclusion
- Dealing with XY problem with user feedback
    - First goal was to notify people that this is a problem
    - Currently, this is continuing as an open-ended discussion with people trading ideas
    - Kriti wants us to make sure that everyone understands the point of the thread, don't assume.
- Criteria for closing user reported tickets
    - Next step is to create a wiki page documenting some guidelines for communicating with users
    - Help address the XY problem
    - Initial wiki page will be sparse
    - Sean will notify team when wiki page is up so team can look it over and give feedback
- Package version management
    - Pavish is working on that on the front end
    - Brent will update the email thread with conclusions so far, and prompt with unconcluded questions
    - Brent will start an email about supporting postgres/python versions
- RSQLA1 retro
    - Brent would like to discuss this at a relatively slow cadence
- Product level permissions discussion to account for related entities
    - Also can be discussed slowly
    - May be worth a dedicated research project

Not yet started
- i18n retro
    - Rajat is unavailable, and we should probably wait to start it until all the work is merged
- Installation 0.1.3 retro
    - Mukesh will start this soon
