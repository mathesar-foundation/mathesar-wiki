# 2024-06-04 maintainer meeting

**Attendees**: Sean, Brent, Anish

## Identifier terminology

**Question**: What terminology do we want to use for the identifiers of database objects? How consistent do we want to be with that terminology across our stack? For example, we will be identifying schemas by their Postgres oid values. Do we want to call this an `oid`? Or an `id`? And if we don't care about consistency, then this question becomes relevant separately at the DB layer, the service layer, the API layer, and the front end. The question probably applies to DB objects that we current manage: schemas, tables, columns, and constraints. And it potentially would apply to other DB objects we might manage in the future such as views. It's also worth considering that columns require _two_ identifier values: the table oid and the column attnum.

Brent brought this up [during a PR review](https://github.com/mathesar-foundation/mathesar/pull/3599#discussion_r1615669259).

### Discussion
- Brent:  Don't care, but have a slight preference for using `oid` and `attnum` in the RPC layer.
    - Sean: we currently use IDs, not OIDs in the frontend.
    - Brent would like to use the campsite principle i.e. change code as we encounter it, rather than doing it all at once.
    - Brent doesn't care what the frontend does, only cares about API layer.
- Sean asked about deleting tables, will we use table ID?
    - Brent: Will we ever need table OID and schema OID in the same call?
        - Doesn't seem that relevant to current discussion, discussion moved away from this topic.
    - Sean: Should we prefix the name with "table_[ID]" or "table_[OID]", or no prefix?
        - Brent: prefixing is fine.
    - Anish: there's a function that just says "schema" without any ID, do we need to change that?
    - Brent: Maybe skip the whole ID / OID thing altogether, only use "table", seems simpler, arguments are typed, so we know it's an integer.
    - Sean cares more about consistency than the standard we actually decide on, we should have a standard though.
    - Anish likes schema_oid more than schema.
        - Sean would naturally expect an object if the key was just "schema"
    - Anish will be tasked with thinking about this more and documenting this in the code standards section of the wiki
        - Brent: Don't spend too much time on it.
    - Not related to architecture, should go in a "code standards" page on the engineering wiki or in this page https://wiki.mathesar.org/engineering/code-review/backend/
        - Wiki is messy right now, that's fine
        - We can reorganize the wiki after beta

### Conclusion
We need a decision on `schema` vs `schema_id` vs `schema_oid` vs `id` vs `oid` - what convention to use for function names, keyword arguments / parameters, etc.

Anish will decide, document it here: https://wiki.mathesar.org/engineering/code-review/backend/

## Architectural overhaul issues are not auto-closed

I (Sean) noticed that [this issue](https://github.com/mathesar-foundation/mathesar/issues/3596) was not automatically closed when its associated PR was merged. I think this is because the PR wasn't merged into _develop_. Brent and I agreed to organize the architectural overhaul work using these nested meta issues and task lists, and that plan was based (in part) on the assumption that the issues would auto-close (giving us an easy way to track our work). I wonder if it's worth re-evaluating that work-organizing strategy now. Or is there an easy way to get these issues to auto-close? Perhaps we should just merge all this stuff into `develop`? We're not actually breaking anything yet. And the more I've been thinking about it, the more I think we're actually going to need to make all the front end RPC implementation changes in _one_ giant PR (I can explain why).

### Discussion
- This is a workflow issue.
- Issues aren't auto-closing because we're not using the `develop` branch, so they're staying open even if the work is done.
- Maybe we should delete the separate branch and just break `develop`?
- The previous workflow plan was based on a workflow where APIs were transitioned one-by-one, so develop would be broken for longer.
    - But it's difficult to do since the frontend needs a bunch of different APIs at once.
- But if we're doing this incrementally, then `develop` will only be broken in small bits, we can delete the architecture branch.
- We need to figure out when we can call the RPC work good enough for the frontend to start working on it, make shims between REST and RPC endpoints if needed.
    - All APIs won't be done by deadline, so we need to figure out a stopping point that's not "all APIs"
- We're changing SQL functions, not really service layer functions, so this will break `develop` 
- You can't change the return type of SQL functions, you have to drop and re-create them.
    - Using a more aggressive strategy to replace SQL functions would solve Anish's qualm.
    - Only thing affected by more aggressive strategy is if someone uses our SQL functions in their table definitions, which seems unlikely.
- We're spending a lot of time merging various branches, so let's just get rid of the separate branch and merge it into `develop`
    - Sean will do this today, make sure CI passes, etc.
    - Brent thinks it should just merge clean.

### Conclusion
We'll get rid of the architecture branch and just use `develop`. Sean will do this today.

## Service layer testing strategy

To follow up on a [discussion](https://github.com/mathesar-foundation/mathesar/pull/3598#issuecomment-2120941065) in GitHub, I (Sean) think it would be nice to make sure we're all on the same page about what sort of test coverage we're aiming for on python functions.

With the example in that discussion, I'd like to _not_ add a test right now. Perhaps we would go back and add tests for these functions later on. I have a hunch that we're going to end up changing these functions around quite a bit before beta. I want to get the broad strokes wired together as quickly as possible. As Brent [said](https://github.com/mathesar-foundation/mathesar/pull/3598#issuecomment-2124873775), these tests are "kind of a pain to put together", so I don't think they're worth worrying about right now.

### Discussion
- Sean: Tests seem weird and hard to write / not that useful, do we need them now? We might end up changing the RPC functions around a bunch before beta, do we need tests at all? Seems like it's slowing us down.
- Brent would rather take them out later if needed, because having these small simple functions to test will make it easier to move things around with confidence.
    - We don't have E2E tests, etc.
- Sean: Won't release QA help?
    - Brent: We're not releasing for a while.
- Brent: These are very simple tests, no Django machinery, no test database, etc.
    - Sean: this seems to be decreasing usefuless
    - Brent: yes, but if we had functional tests or frontend hooked up, we wouldn't need this, but gives us peace of mind now
    - Sean doesn't get the tests yet and would like to make PRs without understanding the tests for the sake of speed
        - Brent is fine with that for moving fast, although PR validation will take more time on his end for manual validation, but he has a Python script that makes it easier to set up RPC client, etc.
- Brent: Once we have functional tests, we can get rid of these tests, but we don't want to pause to figure out how to set up functional tests reliably right now.

### Conclusion
Brent would like tests would be there, but will merge PRs even if Sean doesn't write them.

## Moving quickly by ignoring some details

We've been going around on some PRs that I don't think we should be. The goals of the architectural overhaul are:

- Get state out of the service layer
- Move all possible logic to DB functions
- Improve performance
- Change the API to RPC style

The goals are not:

- Improve code quality (yet)
- Improve code organization (yet)
- Improve variable/function names (yet)
- etc.

I think we're failing to realize the former because we're bogged down in the latter (myself included). I'd like to discuss.

### Discussion

Brent:

- Most of our PR review comments have not been goal-oriented, we're trying to improve performance and get rid of state in the service layers.
- We should all be keeping this in mind, only request changes for egregious stuff.
- RPC API structure - okay to be a bit fiddly about consistency
- Variable names, variable orders, etc. - let's not worry about this
- Aim for 1 review loop at the most
- Let's be concerned less with consistency.
- We're all guilty of this.
- We're not moving as fast as we should, everyone agrees.
- Plea: let's not hold up PRs for consistency, only for egregious stuff.
- We're removing so much code! Defer cleanup work until there's less code everywhere, will even be easier to clean up.

Sean:

- Sentiment makes sense.
- Sean is new to the codebase, it's useful to know how people are doing things, useful to have these discussions.
    - There are undocumented code standards that Brent/Anish have sort of agreed on.

Brent: 

- All the libraries we use are inconsistent about variable order, etc.
- It's good to discuss or write things down, but let's not hold up PRs.
- When Sean can do things in A vs. B, Brent is fine with Sean just picking one of the two ways, rather than asking ahead of time.

Sean:

- Since Brent is not ahead of Sean / Anish, he's not setting the standard as much for some things, Anish and Sean are doing things differently.

Brent:

- That's fine, we can merge both!
- Some mantras that he should probably write down:
    - at most one user DB call and one internal DB call per RPC endpoints

Anish is good with moving fast.

### Conclusion
Everyone agrees!
