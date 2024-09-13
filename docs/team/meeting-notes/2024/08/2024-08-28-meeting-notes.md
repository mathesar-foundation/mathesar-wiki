# 2024-08-28 maintainer meeting

## Record summaries update and plan

- We've already decided won't have record summaries editable for the "RC", but we do want them editable for the beta.
- Brent will explain the plan for what needs to be implemented to make summaries editable, in case it needs to be implemented when he's out.
- Goal for meeting:
    - Agree on plan.
    - Decide who will implement if we need to when Brent is out.

### Discussion
- Team is in agreement that it's fine to have record summaries not be editable for the "RC".
- Sean will look into the bare minimum change we can make to the UI that makes it clear that record summaries aren't editable / won't lead the user down a dead end. 
    - Doesn't have to be a perfect UX.
    - Could be as simple as hiding a section inside the table inspector.
- We will need to communicate to users in the RC release notes that this feature is temporarily not working.
- Sean will be the person to implement once Brent is gone.
- Brent, Anish and Sean will discuss technical implementation details in a separate call.

## Installation work plan

Brent investigated how well installation is working with the new permissions setup, [his report is here](https://hackmd.io/TTrZ6EPiQrKmmu3Vb0FHEg) (doc is private to Mathesar staff).

Good news: we'll need to make fewer changes than originally anticipated.

Goal of discussion: figure out a clear plan for installation-related work for the initial "RC" testing release.

###  Work needed for installation configuration changes

How much work do we need to ensure we don't need a superuser to install Mathesar?

- Not much.
- Current docs already say you don't need to be a superuser, just a database owner.
- We could make it even clearer, but that seems like work for the final beta, not the RC.
- For the beta, we should audit the documentation to make sure we're explaining the permissions we need in a friendly and obvious way.
    - 'What user you use Mathesar with' vs 'What user you install Mathesar with' needs to be explained
    - Superuser role should be made clear
    - We should also put some work into testing installation without a superuser

### Work needed for upgrades

Should we put effort into automating upgrades from 0.1.7 to RC?

- We'd need some sort of wizard or clearly documented manual steps.
- Automating it will be very hard.
- The way we store database information has changed.
    - Do we delete database connections and ask the user to reenter?
        - They could lose data if they don't have their database password anymore.
        - Not having their DB password seems like an edge case, do we need to even consider it?
        - Even if it's an edge case, consequences are potentially dire.
        - They'll also lose explorations and metadata connected to DBs.
        - We could build the backup and restore function we've been talking about forever...
    - What will the experience look like if we migrate some database information?
        - Will we need new UI?
        - No, the admin will see a list of databases, but they'll need to go to the roles configuration UI and configure a role.
            - What if they don't have create role privileges?
        - Could be a confusing experience.
- Do we even need to support upgrades?
    - RC is not really an "upgrade", it's a testing build.
    - We won't be at feature parity with 0.1.7, we won't have done thorough QA.
    - This release is not for users who want the next version of Mathesar.
    - People shouldn't be thinking of this as an upgrade.

**Conclusion**

- We won't put any work into upgrades for the RC.
- We won't be treating the RC as the "next" release.
    - Maybe publish to a separate Docker repo, definitely don't use the "latest" tag
    - Postgres, Python, etc. use the same Docker repo for testing builds, just use tags to differentiate
    - We could even consider an invite-only release
- Less work, better communicates the release purpose.

### Documentation updates for "from scratch" install

Brent ran into a 500 error when testing the "from scratch" install, who should work on resolving this?

- This is actually an error with the static file setup, not Mathesar.
- We don't have pre-built static files for current develop, but we will when we do the release.
    - That should fix the error.
- No documentation updates should be needed.
- Our usual installation testing process for releases should be enough, it's already tracked in docs and Basecamp.
- Anish is most likely to work on this (not because of backend expertise, just based on workload).

### Documentation accuracy updates

We need to go through docs.mathesar.org and ensure our documentation is accurate.

- Ghislaine will update user-facing documentation.
- One of the engineers will update admin-facing documentation, depending on availability.
    - Should we be setting the `OWNER` role here?  https://docs.mathesar.org/installation/build-from-source/#installation-steps
- This needs to happen before RC.

### Onboarding UI changes 

Do we need any changes in our onboarding user flow to account for the new permissions setup?

We walked through the current process.
- Once the user creates the superuser, they go to the database page.

**Conclusion**: Nothing here blocks RC, we should probably consider improving usability for beta.

### New documentation

We need to make new documentation for how permissions work. Ghislaine will work on this as part of her work on user-facing documentation.

### Access to Mathesar schemas for `PUBLIC` "role"

The Mathesar schemas `msar` and `_msar` should both be set up so that `PUBLIC` has access.

- `PUBLIC` is a pseudo role that every role on the database automatically gets.
    - It's not shown as a role in the roles table, so needs special handling.
- We want to set this up for current objects, but also for any object we create in those schemas in the future.
- Examples of things namespaced under these schemas:
    - Our TLD table 
    - Functions
    - Sequences
- Options for setting up `PUBLIC` access:
    - Get rid of everything and recreate after setting up default permissions.
        - This is part of the long term upgrade strategy, with some caveats.
    - Go through and do permissions on a per-object basis.
    - Figure out how to upgrade SQL functions.
- Getting rid of everything is a problem because we store e.g. record summaries / expressions / templates here.
    - We need a strategy for how to drop things and what to use `CASCADE` for.
- Can we get away with doing it on a per object basis for now?
    - We don't have many tables
    - Postgres automatically grants usage on types and execute on function - this covers a majority of what we have currently.
    - We can just do it manually for now.
- Idea: could we have `PUBLIC` be the owner?
    - `PUBLIC` is not a true role, not sure if this would work.
    - We'd need to think through how that would work with upgrades.
    - Upgrades need the same role as original installation, that's a requirement, we're okay with that.

### Installation plan outcomes

**For "RC"**

- Update documentation
    - UI documentation (Ghislaine)
    - Installation document (fixing inaccurate - whoever's free on the engineering team)
- Testing install (Anish)
- Double check `PUBLIC` permissions for usage on types and execute on function will work (Brent)
- individually update permissions on tables and usage on schemas for `PUBLIC` (Brent to create an issue)

**For Beta**

- audit documentation for minimal permission usage
    - also explain that what Mathesar is installed with isn't what Mathesar uses day to day
- Consider migration / upgrade path from alpha or beta
- Consider onboarding UI changes
- `PUBLIC` permissions / ownership - full implementation
