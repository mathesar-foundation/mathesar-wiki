# 2024-01-04 staff meeting

## GSoC 2024 announcement

Sean wants to put an announcement on Github stating that we won’t be doing GSoC this year. See `#Mathesar - Internal` for proposed copy.

We’d put the announcement as a pinned issue on Github so it shows up at the top of our issues list when someone comes to the repo.

We could link the relevant wiki pages from the issue, or the issue from the relevant wiki pages…

Everyone agrees with the plan, Sean will take it up from there. Pin the issue, cross-reference.

## Basecamp + Design reviews location

Ghislaine requested people put design reviews in Basecamp for a recent spec as an experiment, but we've decided against doing that.
Current discussion will be ported to email, further discussion will happen there

Brent also has some tech spec related tasks in Basecamp with comments, is it okay to have comments in Basecamp?

- Persist things outside basecamp 
- Quick (ephemeral) notes are okay in Basecamp

## DB connection UI issue

Specs: https://wiki.mathesar.org/design/specs/new-db-connection-form/

- Pavish concerned with UX in case C
- Sean proposing to eliminate case C

Pavish’s comments: https://github.com/mathesar-foundation/mathesar/pull/3319#discussion_r1434348595

Current state:  

 - Need to choose a “bootstrapping connection” to create new ones
   - Look for any that match the hostname and port the user entered
   - Then the user selects the desired one
   - Case C is only possible when the hostname and port are found in a preexisting connection
- Historical context:
   - Case A was inspired by trying to more easily copy an existing credential to set up a connection, rather than setting it up from scratch
   - Case C was argued for by the back end team.
   - Brent is having second thoughts about having argued for that

DECISION: Remove Case C, document how to set up minimally-privileged user for use with  Mathesar connections

## Release 0.1.4 check in

### Needs docs work and review

Open [PR](https://github.com/mathesar-foundation/mathesar/pull/3227) for all docs work

- [Update docs with regard to MATHESAR_DATABASES][3378]
- [Make the docker compose file self documenting][3306]
- [Deprecate Build from scratch documentation][3169]
- [Remove guided installation section][3167]
- [Reframe docker compose installation][3166]

### Needs work from Anish

- [Update Constraints for Positive Integers in `oid` and `column_order`][3176]
    - Needs Anish to finish implementation

### Needs work from Pavish

- [i18n bugs][3359]
    - Needs Pavish to implement

- [Add loading and error indications in the database page][3330]
    - Has [PR][3351]
    - Needs Pavish to review

### Needs work from Brent

- [Internal server error when database connection fails][3329]
    - Needs Brent to implement

### Discussion

- [Simplifying setup environment variables][3355]
    - **Next steps:** We're going to wait until the docs are further along and then evaluate the user experience. At that point we'll respond to Adam and seek to close the issue.

- [The Database page should display an error when connection is invalid][3371]
    - We need to display errors when viewing the database page
    - Brent: this is a problem with our current architecture
        - This is why we see "Schemas (0)". There are 0 schema models associated with that connections model.
    - Sean: is it possible to connect to a DB successfully without seeing any schemas? — yes. There are even some scenarios in which you can't see the public schema.
    - Brent: This behavior is going to be completely changed when we don't have a schema model. In the new architecture this will be different.
    - This is not a release-blocker though.
    - **Next steps:** We'll bump this into the "High Priority" milestone.

- Improve failure scenario when attempting to create a connection with invalid credentials
    - This is a new issue we identified during the call
    - This is a problem because it's possible to save a connection that could later become valid. In that case, the database won't have our schemas installed.
    - We'd like to fix this by failing to save the connection if we can't connect to it.
    - **Next steps:** Sean will create a ticket for this
        - Milestone: v0.1.4
        - Assignee: Brent
    - We can move to a later milestone if it becomes too much work

- Disable modifying database name, host name, and port
    - This is a new issue we identified during the call
    - **Next steps:** Sean will create an issue for it

- [Bugs while deleting database connection][3361]
    - We're waiting on a contributor
    - **Next steps:** Anish will comment to move things along

### Blocked

- [Clean up django migrations before 0.1.4 release][3296]
    - Blocked on #3176

[3166]: https://github.com/mathesar-foundation/mathesar/issues/3166
[3167]: https://github.com/mathesar-foundation/mathesar/issues/3167
[3169]: https://github.com/mathesar-foundation/mathesar/issues/3169
[3176]: https://github.com/mathesar-foundation/mathesar/issues/3176
[3296]: https://github.com/mathesar-foundation/mathesar/issues/3296
[3306]: https://github.com/mathesar-foundation/mathesar/issues/3306
[3311]: https://github.com/mathesar-foundation/mathesar/issues/3311
[3329]: https://github.com/mathesar-foundation/mathesar/issues/3329
[3330]: https://github.com/mathesar-foundation/mathesar/issues/3330
[3355]: https://github.com/mathesar-foundation/mathesar/issues/3355
[3359]: https://github.com/mathesar-foundation/mathesar/issues/3359
[3361]: https://github.com/mathesar-foundation/mathesar/issues/3361
[3370]: https://github.com/mathesar-foundation/mathesar/issues/3370
[3371]: https://github.com/mathesar-foundation/mathesar/issues/3371
[3375]: https://github.com/mathesar-foundation/mathesar/issues/3375
[3378]: https://github.com/mathesar-foundation/mathesar/issues/3378
[3377]: https://github.com/mathesar-foundation/mathesar/pull/3377
[3351]: https://github.com/mathesar-foundation/mathesar/pull/3351
