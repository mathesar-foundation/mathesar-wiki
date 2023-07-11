---
title: 2023-07 backend fixes
description: 
published: true
date: 2023-07-11T09:10:22.038Z
tags: 
editor: markdown
dateCreated: 2023-07-07T14:08:52.280Z
---

**Name**: 2023-07 backend fixes
**Status**: Draft 
**Theme**: -

## Team
> We probably don't need to be this detailed for everything; this is just to show the range of options.
{.is-info}

| Role | Assignee | Notes |
|-|-|-|
| **Owner** | Dom | |
| **Approver (project plan)** | Kriti | *Needs to approve project plan* |
| **Contributor (backend review)** | Mukesh | *Reviews backend code* |

## Problem

Time for some fixes!

Kriti [compiled](https://groups.google.com/a/mathesar.org/g/mathesar-developers/c/0vahYjcTkjE/m/t8I5s0hcAgAJ) a list of minor backend issues in order of importance:

- [~~Remove the lazydict dependency #2960~~](https://github.com/centerofci/mathesar/issues/2960) (since fixed)
- [Add support for `citext` column type #2959](https://github.com/centerofci/mathesar/issues/2959)
- [~~Does not work on windows #2961~~](https://github.com/centerofci/mathesar/issues/2961) (should be considered part of the removing sqlalchemy theme)
- [Demo users should only see their own database #2983](https://github.com/centerofci/mathesar/issues/2983)
- [StatementError when using the Record Selector to search by a partially-entered UUID #2724](https://github.com/centerofci/mathesar/issues/2724)
- [Fix API handling of multi-column UNIQUE and PK columns #2245](https://github.com/centerofci/mathesar/issues/2245)
- [Incorporate field name into error messages when relevant · Issue #1370](https://github.com/centerofci/mathesar/issues/1370)
- [Keep `today` as `today` in column default value · Issue #2754](https://github.com/centerofci/mathesar/issues/2754)

I also created this issue to compliment the one for implementing `citext`, since the originating bug report reported both of these types being unsupported and that blocking the reporter's use case: [Add support for `point` column type #3007](https://github.com/centerofci/mathesar/issues/3007).

## Solution

Will start with block-prone issues. If or when I am blocked on any of these issues, I will work on the block-proof issues. Once block-prone issues are resolved, I will work on the remaining block-proof issues. If I were to do it the other way around, I'd risk being blocked with nothing to do.


### Block-prone issues

Issues that likely need coordination with others.

I expect each of these to take roughly 3 days to complete.

- [Fix API handling of multi-column UNIQUE and PK columns #2245](https://github.com/centerofci/mathesar/issues/2245)
- [Incorporate field name into error messages when relevant · Issue #1370](https://github.com/centerofci/mathesar/issues/1370)
- [Keep `today` as `today` in column default value · Issue #2754](https://github.com/centerofci/mathesar/issues/2754)

### Block-proof issues

Issues that likely *do not* need coordination with others.

I expect each of these to take roughly 1 day to complete.

- [Add support for `citext` column type #2959](https://github.com/centerofci/mathesar/issues/2959)
- [Add support for `point` column type #3007](https://github.com/centerofci/mathesar/issues/3007)
- [Demo users should only see their own database #2983](https://github.com/centerofci/mathesar/issues/2983)
- [StatementError when using the Record Selector to search by a partially-entered UUID #2724](https://github.com/centerofci/mathesar/issues/2724)

### Time budgeting and progress estimation

I included rough estimates of how much time each issue should take. That will be usable as a guide on whether I'm on track.

The project budget is 20 days (4 weeks). Current estimate of total time required to submit PRs for above issues is 13 days (3 block-prone issues 3 days each, plus 4 block-proof issues 1 day each). The remaining 7 days is buffer time (1/3 of budget).

## Risks
- Finishing the tasks too early
	- The prefered risk, since I can then pick up additional work
- Not finishing the tasks in time
	- The worse risk, since not finishing in time will either leave work unfinished or interfere with the break period (and/or next cycle)

## Resources

- **Issues**: [GitHub meta issue](https://github.com/centerofci/mathesar/issues/3022)


## Timeline
This project should take **4 weeks**.

| Date | Outcome |
| - | - |
| 2023-07-10 | Work starts |
| 2023-07-19 | Half-way mark (50% of work should be done) |
| 2023-07-31 | Buffer time starts |
| 2023-08-07 | Work ends |