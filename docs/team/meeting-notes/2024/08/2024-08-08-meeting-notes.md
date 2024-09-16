# 2024-08-08 maintainer meeting

## Beta release: high level plan

Goal: team discussion on how we're approaching the beta, get to agreement and next steps.

### "Release candidate" approach

- We've been thinking of the beta as one big release.
- Instead, we can aim to get a release out ASAP, doesn't have to be perfect or "the beta".
- We can release a "release candidate" version that doesn't need all of the QA and polish that our final beta will need.
    - Gives us something to work towards in the short term.
    - Good opportunity to engage our community to help test.
- We can continue releasing "release candidate" versions until we are ready to release the actual beta version.
    - Each new release can have iterative improvements and bug fixes.
- We will discuss what's absolutely essential for the release.
    - We should bias towards cutting scope and getting something out.

### Scope of RC

- Think of the RC as an alpha release for the beta release
- We do need to have Mathesar functional for this initial release
    - But we don't have to be at feature parity with 0.1.7, can hide some things.
    - We don't have to have all bugs fixed.
- Demo will be left on 0.1.7, any work on demo should be done after the RC.
    - Lots of work to do to get the demo more reliable.
    - We are also considering getting rid of the demo to reduce maintenance burden.
    - This will be discussed further as part of the beta launch plan.
- We are not planning any publicity for the RC, just notifying our existing community.
- RPC backend work needs to be done, other than connections and users.
    - Are we keeping database connections?
        - No, we can delete that code.
    - We do need to update the types API
- Frontend needs to be functional.
    - We can hide some features, but there shouldn't be visible errors right away.
- Permissions work should be functional. 
- Updating documentation and user guides
    - We should do this so they're accurate, but we don't have to perfect them.

### Scope-related discussions
What is going to be such a terrible UX for the RC that it's worth blocking on? 

We can't have errors that block the user from doing critical things.

- Sharing tables and explorations
    - Should we hide this?
    - Backend implementation is quick, but there are some product decisions that need to be made.
        - Which role to use while sharing.
    - That's the meat of the work.
    - Decision: let's hide this feature for RC and do the product work for a future release (but before beta)
- Removing dead code in the backend
    - Nice to have, doesn't block RC.
    - Can be done for beta.
    - Can do this if backend is out of work and needs something to do.
        - Better than adding new features which could introduce bugs.
- Installation 
    - Documentation should be up to date for RC
    -   Brent will take the lead on this, will investigate what needs to be done and send out a proposal.
    - We need to make sure a fresh install with fresh conditions works really well, since this will be the default experience.
- UI updates for permissions
    - Current permissions UI doesn't account for DB superuser being able to take any action.
    - Installation flow might need UX updates to account for new permissions changes
    - We need to explain how permissioning for explorations work 
- Other UI updates
    - Record summary UI might need updates to go with new implementation
    - We should show FK ID for record summaries if we can't show the summary itself due to permissions issues.
- Import page - we don't show UI for selecting an owner
    - Tables are owned by user who created the import
    - Others may be able to see the table name but can't view the table
    - Transferring ownership after creation should still work, should suffice for RC 
- Column extraction - treat as the same thing as import page
- Table cells should be non-editable if permissions don't allow editing
    - This should be in place for the RC.

#### Defer until after RC

- Record summary templating
    - For the RC, record summaries will be read only.
    - User wouldn't be able to configure the template, just have default record summaries.
    - We can display an info message with a link to the GitHub issue
- Superuser permissions UX changes
    - The operations will still work without any UX changes, the user might just be confused about _why_ they're able to do something even though they're not the owner.
    - Design work would just be to provide information.
    - The frontend relies on the privileges provided by the backend to figure out what to disable, and the backend is providing the right information.
- Explorations permissions UX changes
    - Anyone can create explorations, it uses the role of the user who creates it.
    - Exploration will not run if they don't have privileges to see it.
    - Exploration editing if you don't have permissions is wonky
    - With some DB permission setups, users can end up in a state where they can create explorations that they can't run, since it uses their role.
- Upgrade experience from alpha version
- Making table creation patterns across new, imported, extracting column etc. consistent in terms of showing the same permissions-related options
    - Set owner, etc.
    - What happens if we don't implement - table will be created under user's role, and they can transfer ownership after creation
    - Column extraction is less of an issue than import since there's no liminal table
    - Moving columns will show a permission error if the user can't perform the operation but that's fine.
    - Operations from inherited roles will make the new table under the inherited role rather than the original role
        - We can fix this for beta, not RC. Implementation might be tricky.
        - Transfer ownership will still work for RC.
- Record selector - allow user to edit FK cell IDs if they can't see or edit record summaries.
    - We could also allow them not to edit the cell, but we should probably allow whatever PostgreSQL allows.
    - This has an interaction with Postgres REFERENCES permissions, although that's probably irrelevant to this issue.
    - Do nothing for the RC, probably not even for the beta, we'll figure this out then.
- Record summary display
    - How does this work if we don't work on it any more?
        - The frontend already shows numerical FK if the record summary isn't given.
        - Backend already returns columns that you have access to.
- Record page - how to deal with permissions issues
    - What if related tables are not visible?
    - Better UX for this can wait until after RC, current behavior is not catastrophic.
    - Current implementation will break if the user doesn't have access to some columns especially if there's a not null, both on the table and record page, but we can fix this for the beta, not the RC
    - We probably also need to show columns that the user doesn't have access to with a special UI, but this is for the beta too not the RC.
- Related records section on record page
    - Tables page changes should propagate to related records section
    - It'll show an error, no changes needed for RC
    - Frontend will still get the referent columns, so it will have enough information to render this.
    - Getting column names doesn't require permissions.

### Versioning the RC

- Maybe call it 0.2?
- Are we going to use semantic versioning?
    - Not sure if it's ideal for Mathesar anyway since we're not a library.
- Haven't put a lot of thought into this yet.
- We may have to do some code work to account for the version name if we change the pattern from our current versioning.
    - Let's figure out the version based on what will be the least amount of work, if we need a number and a dot, we'll do that.
- Tabling this discussion until later.

### Release process

- We'll generally follow our usual release process.
- We should update and run through the QA script.
    - Definitely needs to be updated to account for permissions.
    - Ghislaine will update the script.
- We don't necessarily have to fix most of the bugs we uncover during QA, since this is a testing release.
     - We'll triage the bugs on a case by case basis
     - We will fix them before the beta
- We don't need to do translations for this release.
- We will be doing QA internally for the RC, we're not going to look into outsourcing yet.
- All team members should be involved in QA.
- QA can be started before all of the frontend work is complete, we'll discuss how to structure that.
- We will create a QA plan.
- We need much more extensive QA than just the QA script, definitely for the beta, maybe for the RC.
    - High risk of regressions, we should spend time trying to find them.
- It's okay to only do the QA script for the RC, the aim of releasing it is to get people to help test, bugs are expected.

### Communicating about the RC

- If a new user installs Mathesar do we want them to try out RC or 0.1.7?
    - 0.1.7 for now, since RC will have bugs.
- We should make it clear that RC is a work in progress and is a testing build.
    - Things will be broken.
- Where do we communicate about this?
    - Concerns about giving users the wrong impression.
- We will be clear about it in blog, release notes, documentation, wherever we communicate about this.
    - It's something we can figure out when we get to it.
    - We are still in alpha, users don't expect us to be perfect.

### Overall beta planning

- We're first going to focus on planning the RC.
- We will plan remaining beta work after the RC is done.
    - Could involve more features that are critical for adoption (e.g. exporting)
    - Could involve integrations with PaaS services, etc.
    - Documentation and installation work.
    - Consider implementing a testing strategy.
- We won't discuss post-RC work now.
- We'll probably have a soft launch and a hard launch for the beta.
    - The RC is not the soft launch.
- We'll discuss more at later meetings.

### Design and product work needed for the beta
Collected from above discussions.

- Updating UI for the DB superuser
- Updating UI for explorations - explaining how permissions work (also on Ghislaine's work)
- Update post-installation UI to account for permissions
- Update record summary template configuration UI
- Ghislaine's document: https://hackmd.io/yVmQevNwTHa93R0VnzWEMw

### What do we need for the next release ("RC")?
Collected from above discussions.

- Set users expectations if a new user is trying out Mathesar and sees that things aren't functional
    - In the UI
    - In the release notes
- QA script update
- Run through the QA script on the app
- RPC backend work done (as we've specced out, no connections or users, etc.)
    - Delete RPC functions for connections
- Ensure that numerical FKs are returned if the user doesn't have access to see related table for record summaries
- Frontend to be functional - whatever that entails
    - Moving things to RPC APIs
- Non-public permissions fully done
- Update user guide on permissions (Ghislaine volunteered for this)
- Hide shares?
    - Will this speed up release?
    - Yes, probably
        - Pavish: we need product level work on this to account for multiple shares with different users 
        - Brent: Backend implementation is quick, but the product level work is still pending, so we can't start implementing.
            - How we're going to decide what role we're using
        - We can also defer RPC backend changes
        - Sean is fine with temporarily hiding them, Ghislaine is too. Anish too.
- Fix critical bugs from frontend consuming the RPC 
- Installation documentation updates + any associated work on the product.
    - Brent will figure this out and let the team know proposal for changes, discuss with Pavish.
- Table cell editing working correctly with permissions

### What do we need between the next release ("RC") and the beta?
Collected from above discussions.

This is not a comprehensive list, this will be informed by our GTM work and further discussions after we release RC.

- Design and product work (see above)
- Work on shares.
- Remove vast swathes of dead code in the backend
- Translations
- Outsourcing QA?
- Very thorough QA, hammer at the app beyond the QA script
- Performance/stress testing
- testing strategy
    - We have a bunch of tests, but no overall strategy; so we have a slow testing suite that misses many things
    - We should try to at least have a strategy in mind (if not completely implemented)
- Smoothing upgrades

### Action items
- Ghislaine to update the QA script to add permissions
- Kailash to flag the discussion about the beta release candidate name
- Brent to draft a proposal for the installation work.

## Velocity & mindset discussion

Open ended discussion inspired by our development process over the last few months. Shifting from a feature-based mindset and "it would be easy to build this" to a user-based mindset "what does the user want to do?"

- This is not intended to be a final or comprehensive discussion, just an idea to think about. We'll discuss again closer to beta.
- Everything we do should be as simple as it can be. Related to all workflows. Important to build things simpler and tighter across the process.
    - Including tightening scope.
- Don't have multiple competing goals.
    - e.g. component library for the frontend, DB library for the backend
    - These might not be the best examples, because modularity has its own benefits and should be a goal.
    - Another example was a usable REST API, making the frontend do more work to so we could architect an easier API for imaginary users.
    - Modularity is a good goal, but encapsulation can go too far.
        - We don't need to encapsulate Postgres functionality that the frontend isn't using.
        - Cut as many corners as we can in lower level things, don't handle all edge cases yet.
        - Agreed with broader concept, but negotiating with frontend sometimes takes more time than just implementation.
             Also consider maintenance burden.
    - Return values in RPC functions are not used by frontend, null returns would make future refactors easier by avoiding dependency chasing.
    - Another example was the idea of reflecting types dynamically in the frontend, increased code complexity and time, but never done.
- The goal is to release the simplest thing for the user.
- There's a difference between modularity being a goal and having multiple product / release goals when building a feature.

Lots of strong opinions, but we ran out of time here, we will pick up the discussion in a future meeting closer to beta.  
