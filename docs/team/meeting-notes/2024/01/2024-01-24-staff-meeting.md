# 2024-01-24 Staff Meeting

## Release check in

Issues list: https://github.com/mathesar-foundation/mathesar/issues?q=is%3Aopen+is%3Aissue+milestone%3Av0.1.4

Docs work is ongoing, Brent and Sean have done work on it.

Not many regressions identified.

**GitHub issues**

- [Incorrect Z index for sheet header cells within table widget](https://github.com/mathesar-foundation/mathesar/issues/3396) 
    - might be bumped out since it's very minor
- [Array cells not styled correctly](https://github.com/mathesar-foundation/mathesar/issues/3402)
    - cannot reproduce
    - probably frontend issue, all the info for the data explorer is returned in one API response, and column names are correct, so backend seems to be working fine
        - seems like stores are messed up in some way in development mode due to vite hot reloading
    - not easy to reproduce, so we'll close it
    - everyone please keep an eye out for seeing plain text instead of pills, we can try to reproduce
- We need to resolve open TODO remove the initial connection for Docker compose
    - issues
        - [Unified Docker image starts with a connection already added · Issue #3415 · mathesar-foundation/mathesar](https://github.com/mathesar-foundation/mathesar/issues/3415)
        - [Docker compose installation has a preconfigured connection · Issue #3416 · mathesar-foundation/mathesar](https://github.com/mathesar-foundation/mathesar/issues/3416)
    - might break tests
    - should be easy, hopefully
    - assign to Brent
- [Update process for docker compose is wrong · Issue #3404 · mathesar-foundation/mathesar](https://github.com/mathesar-foundation/mathesar/issues/3404)
    - needs to be re-tagged as docs, Sean will do the cleanup
    - Brent hasn't made progress since he's been working on infrastrucuture
        - Brent will put infra scripts in mathesar-scripts repo

**Basecamp issues**

- Anish is now out
    - Assign his issues to Brent
- It's okay to make docs updates after the release
    - We don't need to make a new Docker image
    - Choose between master / Docker image not being in sync or having to change Docker without version changes
    - We should currently be pushing docs changes whenever we want
        - We won't push a new Docker image for docs changes for now
    - For the long term, we want to be making new patch releases if we update docs, but we'll do this for the beta 
- QA testing (users)
    - Ghislaine went through library demo and task based testing
    - No new things found
    - Patrons data set is not in the Google Drive
        - Ghislaine had to make a new patrons data set
        - The data sets are in the data playground
    - It's really slow especially after import etc.
        - internal.mathesar.org is really slow because of external DB connection
    - Sean reached out to Adam, he's probably not going to have time before the release
    - Anish is also assigned to test out the UI, he should be able to get to that next week
- QA testing (installation)
    - Pavish says docs are incomplete, some TODO sections
        - connecting to external DBs
        - Brent will double check this
    - Pavish has some suggestions for docs, but wants to wait until docs are complete
        - Pavish will write them down in HackMD
    - We edit the YML file instead of environment variables, but should we mention that environment variables will override YAML config
        - Obvious to Docker users, but might be worth a one line mention, also say you can hardcode variables
        - Link to Docker Compose docs
    - Sean has been working on docs
    - Pavish will put this in a HackMD doc and will create a Basecamp todo to look at it, or will push changes directly to the doc
    - Pavish will finish testing external DB
    - Kriti hasn't started testing yet
        - No changes planned for build from scratch, no need to wait for docs changed
    - Still waiting to test upgrades until docs are done
        - Need to do a new build
        - Wait until Docker Compose changes done, may also have bugs from user call today
- Priorities (too much stuff assigned to Brent)
    - Upgrade docs first, so upgrades can be tested ASAP
    - MATHESAR_DATABASES thing - Pavish will do this
        - Need to be picked up if it's an environment variable
        - Doesn't need to exist in prod docker compose
        - Docker run command already doesn't use it
            - Root out the default in the code and remove it
            - Hopefully tests won't break since it's also setup in tests
    - Pushing to mathesar-scripts is also deprioritized

## Freshdesk workflow

Potential questions (written by Kriti)

- Should we be using Freshdesk?
- Do we need a ticketing system / shared email inbox at all?
- Should Syften notifications be going to Freshdesk?

### Discussion

- Nobody seems to be using Freshdesk
- Brent:
    - I don't like the UI. Hard to find tickets. Weird stuff about emailing.
    - It _is_ useful to have a list of users we've contacted where we can see when they've replied.
        - Kriti: If we don't have Freshdesk, we'll need to have this somewhere else
    - marking a ticket as "closed" doesn't really make sense in the context of the installation requests because we want to continue following up with them

### Conclusion

- Kriti will figure out a workflow with no new tools
    - Perhaps we can leverage Basecamp more for some of this workflow

