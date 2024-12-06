# 2024-02-12 beta planning meeting

## Pre-meeting

Please review [the "Beta" HackMD](https://hackmd.io/xHWKXnMnRlyxYFt3XIzFQQ) ahead of time and think about how we can ship a minimum possible beta.

Goals of the meeting:

- Decide what we're building for beta
- Decide rough timeline for beta
- Confirm monthly release plan
- Figure out what needs to be fleshed out and who's working on what
    - Everyone should leave the meeting with a clear sense of priorities
- If we're working on other things (e.g. i18n), figure out how that ties in to the beta plan


## Notes

- Is everyone agreed generally that the beta is focused on performance and (maybe) usability. No big new features. Basically get Mathesar to the point where we can recommend it to more users?
    - Yes, everyone agrees.
- Why beta?
    - Big goal is to grow our user base. Currently this is hard because we can't recommend it to a lot of users (due to alpha status, performance issues). We need it to perform better before we can do that.
- Brent: do we want forms for beta? Kriti: no. We should probably build this shortly after beta.
- Order of operations
    - Pavish: how much difference do we want/foresee between beta and 0.1?
        - Kriti: not sure
        - Pavish: I would think we wouldn't want to add too many features in this window
        - Kriti: I'm not even thinking about v1.0 yet. We need more information before we make these decisions.

### Performance

- We're doing the backend architecture work
- We'll have new APIs. This will involve some frontend work to make the frontend utilize the new APIs.
- There is a major perf issue when the service layer and DB layer are on separate machines. We should clarify what sort of installation setups we are aiming for. We should try to target installation scenarios where Mathesar doesn't perform quite as well
- **Decision: Brent has this in hand, will think more about if what work is necessary and if there's anything that can be cut**

### Usability

- It would be nice to have a use case that we can aim for. Maybe CRM, maybe Basecamp. It would be nice to have one use case where we can switch our core workflow over to Mathesar.
- Usability should also consider performance in different installation setups
- Sean: not sure if it's worth making the beta depend on us moving our workflow over because we want to recommend Mathesar to people with pre-existing PG DBs.
- Pavish: do we want to have a "user flow" like we did for the library demo?
- Kriti: we don't necessarily need to fix _every_ usability issue
- Brent: it would be nice to have a use case that motivates us to use the DB outside of Mathesar too.
- Kriti: it would be good for someone to come up with more scripts/stories soon
- Kriti: I don't think the dogfooding has to be the end-all-be-all. It doesn't need to cover every feature.
- Sean suggests that we talk about "dogfooding" as a topic separate from the beta
- **Decision: Sean will map out some of the improvements we'd need for the CRM use case and the Basecamp use case. Then Sean and Kriti continue discussion from there.**

### Permissions

- We need to get rid of our current permissions system and move to a system that's backed by PostgreSQL permissions
- Kriti: do we _really_ need it for the beta. Agree that we need to do this at some point. What's the argument for blocking the beta on this?
- Brent: permissions are blocking architecture. Architecture is blocking performance.
- Brent: getting the permissions sorted out is going to be the main part of the work for beta.
- **Decision: we need this for beta. We'll continue figuring out _how_ to do it in separate meetings.**

### Installation

- Should we try to have a debian package?
    - Pavish: this would be a lot of work. Might not be worth aiming for. Our stack is not well-suited for this. I don't think we should put a lot of effort into this. Not a high priority.
    - Brent: Agree. We should tune up the installation types we already have. Make the images smaller, leaner. Unless people are absolutely screaming for it, I don't think we should add any other installation methods.
    - Kriti: seems fine to drop this. We could do it after beta. Curious why it would take a lot of work, but we should talk about that separately.
- Should we make it `pip` installable?
    - Brent: suggested this
    - Kriti: We'll discuss this later
- Should we relax the need for NodeJS to install?
    - Pavish: yes, we should aim for this
    - Brent: yes, this is worth doing.
- Do we need to make any improvements to the upgrades process?
    - Adding automatic testing of upgrades
- Users need to currently go through upgrade sequentially
    - If we do a lot of versions, this is a real pain for users
    - We should document this sequential requirement better
    - We should also make it easier for users to upgrade to the latest version
        - Have checkpoints if needed, like Nextcloud
    - Starting from beta, people need to be able to upgrade easily from any version
    - No point doing this for previous versions
- Support a wider postgres and python range
    - Kriti: Seems like python 3.11 wouldn't be too hard to support
    - Brent: should be a low bar to support python 3.6+
    - Kriti: not as concerned about supporting older versions. More concerned about supporting newer versions.
    - Brent: new newest version of Mathesar has to support the latest version of python?
    - Brent: how do we decide what the cutoff is for older versions of python?
        - Kriti: We should do a little research on this to make a decision. Maybe a 2 year grace period.
- Do we want to make certain deployment types easier, e.g. kubernetes?
    - Pavish: asked about this
    - Kriti: not sure we need this
    - Investigate PaaS as a prerequisite to wide publicity
- Depends on if we're publicizing Beta 
- Brent: PaaS should be straightforward so long as our image is set up correctly.
- Pavish: Mostly this task involves a bunch of QA work, testing our image out with different platforms.
- Anish: it would be good to reduce our 3rd party dependencies. This would help us support more python versions.
- **Decision:**
    - **We'll set up pipelines for testing what installation methods we have**
    - **We'll build static files during release so admins don't need NodeJS**
    - **We'll make sure our upgrades process doesn't require people to perform sequential upgrades _after_ beta**
    - **We'll investigate kubernetes, PaaS, and pip install once we're closer to beta**
    - Next steps:
        - **Brent** spec out pipeline issues
        - **Pavish** work on static files issue
        - **Anish**: Work on Python/Postgres version support + reduce dependencies
            - Do research into figuring out what strategy we should have for supporting older versions, based on other projects
            - Add PG 16 to testing matrix

### Backups/PG upgrades

- Kriti: do we want this?
- Brent: this is a big feature. It would be nice though.
- Brent: PostgreSQL has been releasing quite frequently. This is not good for us because it's hard for people to upgrade.
- Kriti/Brent: the main work here is having a script that dumps your database + dumps a mapping between names and OIDs.
- Pavish: I'm comfortable with leaving this out of the beta.
- Kriti: we need to document this limitation.
- Brent: I would argue for doing this. This will be easier after our backend architectural upgrades.
- **Decision: we'll investigate this after new backend architecture work is done, but not commit to it**

### Stability

- Pavish: I want to have multiple QA scripts for us to run through before each release.
- More testing of installation
- Kriti: we need more automation in order to help us release more confidently.
- Brent: would be nice to have more pipelines set up soon — especially for the release _immediately after_ the beta.
- Kriti: If we could utilize these sorts of automations _sooner_, then it will help us put more time into the beta.
- What exactly do we want?
    - Written user-flows for manual QA
    - E2E tests
- Sean: the main reason we abandoned the E2E tests was due to the backend performance issues.
- Kriti: as a minimum, we should compose the written user-flows. If we have more time (which we probably won't), then we should automate it by building E2E tests
- Brent: Is it worth trying to make our release notes process faster?
    - Sean: let's wait and see how it goes with 0.1.5. I think it will be faster.
- **Decision: we'll write user flows for manual QA testing**
    - Make sure to update every month
    - Assign to Ghislaine

### Error handling

- Kriti: Do we want impvove error logging?
- Pavish: there are two separate problems: logging errors somewhere vs showing error to users.
- Brent: With the Docker setup, the logging is great. With the "Build from scratch" installation method, the logging is not great. There _are_ logs, but it's not clearly documented how to find/use them.
- Brent: We could have more sophistocated logging handling. I wouldn't bother for beta though.
- Kriti: we should at least improve our documentation for beta.
- Pavish: We should improve error display for users
    - Brent: let's wait to evaluate this until after the transition to the RPC API. I think this will automatically improve after that transition.
- Kriti: is this something we really _need_ for beta? Can't we improve this after beta?
- Kriti: our overall goal for beta is to have enough information to troubleshoot bugs.
- Brent: I think we're already doing well enough on this goal for beta.
- Sean: we need to find some of these categories to say "no" to. Let's not focus on this.
- **Decision: we won't focus on this**

### API

- Do we want to document the API?
- Brent: RPC framework is going to change everything and hopefully make the API more self-documenting.
- Do we want our API to be stable?
- Sean: suggest that we hold off on advertising that we have an API until it's stable
- Pavish: there's a lot to figure out here with regard to tokens and auth.
- Brent: I would not block Beta on stabilizing the API.
- Kriti: At some point we should have an API-focused release.
- **Decision: We'll still consider our API to unstable. We won't attempt to document it.**

### To discuss in more detail later

- New features
    - View support
- Documentation improvements (figure out requirements)
- Version numbering scheme
- Docs updates vis-à-vis versioning
- do we want pip installation?
- **Kriti will keep an eye on this**

## Timeline

- We'll figure out after permissions + usability have more clarity
    - This is our first priority
- We'll prioritize work and release at the end of every month
- Work for everyone:
    - Brent: permissions with Pavish, write issues for automating release testing for install/upgrade, figure out architecture
    - Pavish: figure out permissions, static files
    - Kriti: put this all in basecamp, ensure we talk about rest of "more detail later" issues
    - Sean: write use cases for Basecamp/CRM
    - Anish: work on reducing dependencies, Python/Postgres support 
    - Ghislaine: work on user scripts for QA
- Not scheduling next call yet, will be after we have more clarity on permissions / usability items
- Other things we're working on:
    - Sean is working on frontend refactor as a low priority
    - i18n:
        - Some frontend work – Sean's working on it as a low priority
            - Affects 2-3% of the UI, will be untranslated
        - We need to order translations (Pavish & Kriti)
        - Release Japanese translations in 0.1.5, QA afterwards
    - Kriti will talk to Ghislaine about her current work
    - Anish is working on debugging a performance issue (in 0.1.5)
        - That takes top priority
    - Anish is working on improving infrastructure for demo
        - This goes under release automation, although we didn't talk about it earlier
        - This should take priority over Postgres / Python / dependencies since it will free up more of our time sooner 
    - Brent is working on deploying 0.1.4 to demo
        - This is high-priority
