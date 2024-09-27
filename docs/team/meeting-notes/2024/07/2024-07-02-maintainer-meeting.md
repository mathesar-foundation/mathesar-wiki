# 2024-07-02 maintainer meeting

## Changes to DB function signatures

I [Sean] think we need a consistent approach to changing DB function signatures. Based on this [thread](https://github.com/mathesar-foundation/mathesar/pull/3637#pullrequestreview-2153802729), Anish and I seem to have different expectations. This potentially affects the experience of Mathesar administrators wishing to upgrade to Mathesar beta, so I think it's worth a brief discussion.

### Discussion
- Changes to arguments (e.g., name, type, return types) in database functions can't be handled by using `CREATE OR REPLACE`.
    - Would cause errors.
- Approaches:
    - We could have an upgrade script that drops all functions in the Mathesar namespaces one at a time, without cascading.
        - If time is limited, could drop all functions in bulk without cascading.
    - We could drop entire schemas with `CASCADE` to ensure a known state.
        - This would remove everything and avoid having to worry about function mismatches later.
        - Could add warning to developers about this approach.
- Dropping schemas shouldn't be a repeated thing, we should send out email notifications to the dev list if we need to do this once.
    - This is the most robust solution, but can't be frequent.
- Safer approach: if a database function signature is being changed, the PR should include a drop function statement for the old signature, placed just above the new one.
    - Can manage changes without drops using `CASCADE`
    - Avoids using `CREATE OR REPLACE` for functions that could otherwise fail due to type mismatches.
    - Good temporary solution
- Also need to clean up lingering old functions / schemas, could be good to outsource to a contractor.

### Conclusion
- When changing a function signature, include a drop function command in your PR.
- Figure out plan to clean up old functions / schemas

## Order of operations for beta work

We are very close to our beta deadline and have many interdependencies in our remaining work. We need to sort out our plan for what order we'll be doing things in and for checking in regularly and eliminating blockers.

### Current state

Priorities:

- Backend RPC refactor
- Frontend needs to switch to using back end
- Backend work for permissions
- Front end work for permissions

**To do later:** Upgrade testing

Main source of blockers:

- Frontend for RPC being blocked by backend not being ready
- Backend of permissions & RPC refactor endpoints operating in the same area
- Frontend for permissions & RPC refactor endpoints operating in the same area

Ideas:

- Finish the databases endpoints first and get rid of the connections endpoints and functions
- Sean and Pavish can work in parallel on the same thing instead of splitting RPC and permissions work if needed

### Maintaining parallel APIs

Currently we are maintaining the REST API while building out the RPC API.

- Biggest problem is that there's two different systems and outputs of one don't work with input of the other
    - We do have some scaffolding to help
- Previously, we agreed on prioritizing keeping the frontend fully functional, so we are still maintaining the REST APIs.
    - Do we want to keep doing this?
    - It is a bunch of work.
    - Removing the REST APIs would break most stuff, but will clear a lot of cruft and allow us to move faster on the backend.
    - High risk / high reward.
        - It means we can't ship anything if we don't fix everything.
    - Breaking stuff / deleting things seems safer from one perspective: we know what's broken, we're not assuming.
- We could move everything over to RPC without worrying about breaking the frontend
    - Delete everything in the service layer instead of deprecating it.
    - Don't need to move users API (not really connected to rest of the app)
- Records API may be able to be hedged.
    - It's not wired to models like other things.
    - We can maybe do this via REST if needed.
- Connections too, but we're not going to be using connections at all.
- Explorations and data modeling APIs will be difficult.
- We won't know what's relevant in the common data variable without deleting it and seeing what breaks.
- We can prioritize things on a page by page basis and get one frontend page working at a time.

**Decision**: Let's not maintain the REST API.

### Permissions backend work

- Pavish was planning to do database backend, but there's no reference point for Django DB changes being changed via RPC functions and needs an example.
    - Doesn't feel comfortable establishing a new pattern in the backend codebase.
    - Tables metadata endpoint was just merged, this might serve as the example Pavish needs.
- Connection ID needs to be replaced by database ID.
    - There's already some sort of backend scaffolding function to bridge these.
- Current connection model is the only way to create credentials
    - We need to replace these, blocking Pavish.

**Blockers:**

- Database credentials creation backend - blocking Pavish
- Schemas need to be updated in the common data variable (see common data discussion item below)
    - Keep the keys, only return schemas and connections, everything else can be empty
        - Connections doesn't use schemas anyway.
    - Breaking everything else is fine.

### RPC frontend transition

Sean is working on this.

- Sean [outlined this approach](https://github.com/mathesar-foundation/mathesar/issues/3621), but likes Pavish's approach better
- Needs some things with common data, discuss when we get to that item in the agenda.
- Start with DB page, then schema page
    - Sean will rewrite the above issue in terms of pages instead of phases, and write a list of RPC functions needed per page
- Brent and Anish can stay ahead of Sean once there's a list of functions
    - Brent likes this, it aligns with current approach
    - As long as records & users can be put off until the end
    - It might require a little bit of extra work on the records and users - use REST for now, switch to RPC if we have time.
    - Frontend shouldn't need any connective scaffolding, though.
- There's enough pages to work on first that we don't have to figure out records or users today
    - Users page frontend changes can be saved until the end.
    - Table page should be prioritized, too central to the app to put off.
- Let's just decide right now that we won't be migrating records or users, we can rethink this at some point, but let's not assume we're rethinking it.
- How much work does it take to switch to tables / columns to using attnums and oids instead of Django IDs?
    - Frontend still submits numeric ID, scaffolding needs to be done is filtering column ID, use attnum to get name, delete all id --> attnum getters, and the output also needs to be modified to use attnums instead of column identifiers.
        - All pretty simple.
        - Output modifiers are simple.
- We are committing to not transitioning records & users to RPC.
- This work will be organized as part of the GitHub issue above, it will be marked as blocking whatever pages it blocks.
- Explorations pages - are we doing these in RPC?
    - SQLAlchemy removal is not a huge priority here.
    - Main issue is that the base table model won't exist. Don't want to do scaffolding for permissions.
        - Postgres has functions for getting table permissions / column permissions that we can use.
        - Also we need to do this for columns in the table page that the user doesn't have permissions to, so we'll need to handle this if we're not migrating the records endpoint.
        - Maybe we should also do records and only defer users.

### Current work
- Brent is working on columns metadata, will be done today
    - Although will need another round for adding metadata at some point
- Sean is working on:
    - Constraints backend REST --> RPC, pretty far along. Almost done, might be easier to finish than to switch tasks right away.
    - Frontend RPC implementation, next step is the tables endpoint, lots of things to do. List / add / patch / delete, putting them into place on the schema page.
        - Frontend code is messy, trying to figure out quickest path through. Might take a bit.
- Pavish would like to work on homepage & database page - both transitioning and adding permissions stuff
    - Homepage is fine, doesn't stop on Sean's toes
    - Database page - Sean has done some work on it, Pavish should build on top of this.
        - Sean is laying the groundwork in transitioning from REST to RPC, and Pavish will fill out the APIs / functions / etc. to add additional data.
        - Pavish will work on top of the PR that Sean made.
    - Pavish will have 1:1 call with Brent to coordinate on backend work, Sean and Pavish talked enough right now to be unblocked.
- Ghislaine is working on the DB page and homepage - we'll be finalizing both of those this week.
    - Ghislaine and Kriti will do a design session to progress this.
- Brent/Anish should make the change for schemas common data in Sean's RPC frontend branch.
    - Code to modify is in `views.py`.
    - We can ignore permissioning common data for now.
    - We will hardcode an empty list for everything except schemas and connections.

### Conclusion & action items
- Decisions:
    - We are committing to not transitioning users to RPC.
    - We'll be making common data changes (see below)
    - We need to make a decision on whether to transition records and explorations, is scaffolding and handling permissions issues faster than migrating the endpoints to RPC?
        - Decide on Monday.
    - Sean will refactor the GitHub issue organizing backend work by page.
    - We are establishing a new Mon - Thu quick daily standup at 10 AM
- Priorities per person:
    - Anish
        - common data changes
        - Take over constraints if needed
        - Joinable tables next, used on a few pages and more complex.
        - Types next.
    - Brent
        - Finish up columns metadata changes.
        - Database endpoints - databases.list and other endpoints
        - Other issues from 3639
        - Explorations
    - Ghislaine
        - DB page
        - Home page
        - Admin page (new)
        - Schema page
        - Table page + public sharing UI changes.
        - We need a place for people to understand who to talk to about getting access to a particular DB / table / schema / role group.
    - Pavish
        - Break up [this list](https://github.com/mathesar-foundation/mathesar/issues/3639) into Brent and Pavish sections
        - Roles endpoints
            - roles.list
        - Database privileges list
        - collaborators.list
    - Sean
        - Get constraints work up on GitHub.
        - Refactoring the GitHub issue.
        - Frontend RPC work continued.

## common_data

**Sean**:

I made a PR to [use schemas RPC APIs in the front end](https://github.com/mathesar-foundation/mathesar/pull/3648) but the `common_data` part doesn't work because the backend is still [using the deprecated code](https://github.com/mathesar-foundation/mathesar/blob/55cc2a9185607732c5a45d8e59d325b1265c9838/mathesar/views.py#L28) to supply the schemas list there. I have a vague recollection of listening to a TL;DV recording of Pavish and Brent discussing some plans for refactoring of `common_data`. I want to make sure we're all on the same page about our plans for `common_data`. And I want us to figure out who would be the best person to kick off these changes to that part of the codebase.

### Discussion
- We need to just keep updating common data to use the latest RPC endpoints as we complete them.
    - We can do it everything module by module.
    - Backend needs to provide one example for schemas, everything else can be done by whoeever's implementing other pages.
- Is everything in common data used?
    - We'll figure this out as we go.

## Weekly async check-in workflow

- Kailash will no longer be doing the team check-ins on Matrix since Kriti is back to doing regular 1:1s, plus we're now doing daily check-ins.

- It's good to have this process in place, we may implement it again if Kriti has temporary time restrictions.

- Does anyone have any feedback about the process?
    - No.
