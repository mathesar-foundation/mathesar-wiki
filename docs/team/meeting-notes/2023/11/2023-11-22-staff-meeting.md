## 2023-11-22 staff check in

## Team check in

### Adam
- Working on transition stuff
- Sam rotating out, Kriti/Adam taking over
- Main things working on:
    - New US payroll platform
    - New international contractor platform
- Lots of annoying administrative stuff

### Anish
- Working on docker compose file for installations
- Need to set up custom domain for testing
- Working aligning documentation with the new docker compose file changes

### Brent
- Less work time this week due to personal stuff
- API documentation project has been ended because it's too much work to get it to completion, associated communication
- DB connection endpoints - for 0.1.4 release
    - Some experimenting with RPC standards, not ad-hoc
    - Not worth the time right now to do proper RPC
    - DRF action endpoint instead

### Ghislaine
- last week, had first design session
- working on bulk linking  (many to many)
    - exploring different options
    - Discussed some options with Brent
    - A lot of things were cleared up on a technical level
    - Will discuss with Pavish next
- preparing results of bulk linking discussions for next design sessions
- Next, moving on to other usability issues
- Monthly ticket planning meeting could be for design/prioritization?
    - Probably do this in a separate meeting

#### Response
- Sean has lots of thoughts about the many-to-many problem, will be away for the next week, wants to be involved
- Monthly meeting Sean's organizing is to be a "Product Approval" meeting
    - Connected to new GH workflow
    - Wants to have the meeting just for product approval, separate from prioritization
- Sean and Ghislaine will have a call to discuss these meetings

### Kriti
Last week mainly focused on org transition.
- Board meeting
- Administrative and IT work
- 1:1s and unblocking work as needed
- User call
    - Mathesar for Scrabble tournaments

FYI
- We've received the first installment of the grant
- Org name change in process
    - Mathesar Foundation, Inc.
    - Board voted on Wednesday to change name
    - Filed with MA
    - Now waiting for response
    - After that, we need to change name with bank, etc.
- New board: Sam, Ian, Kriti + board treasurer Adam
- Kriti is CEO

Next week
- Focusing on admin work for the next few days
- Product/strategy work after that

### Pavish
**General**:

- I was out sick for a couple days, so progress was slower than usual. 

**I18n**:

- The [PR to replace typesafe-i18n with svelte-i18n](https://github.com/mathesar-foundation/mathesar/pull/3302) was reviewed and merged.
- I raised a PR to [add django translations and instructions for maintainers](https://github.com/mathesar-foundation/mathesar/pull/3321).
- I spent some more time thinking about automation and translation workflow. My suggestions are below, we can discuss this async.
- Automation:
  - Went through multiple open-source repos to find their degree of automation, including: CC-legal-tools-app, CiviCRM extentions, Django-docs.
  - Their main automation is around pushing translations for a particular branch and automatically syncing with that branch. We already have this.
  - None of them have branch level sync between git repo and transifex. I attempted a POC to implement this, but then I decided against it:
    - Transifex only allows one branch per project (not per resource) for open-source projects. We cannot implement a branch-level sync with our repo without upgrading to Premium.
    - Even if we did have Premium, the effort needed to implement this is high and doesn't seem worth it.
    - As mentioned above, I haven't found other open-source project that seem to have implemented this.
- Translation workflow:
  - Not having branch level sync limits our options, which actually makes our workflow simpler.
  - The resources within Transifex should always be considered 'prod' resources.
  - They will be linked directly to one of our branches, either the 'develop' branch, or the 'master' branch. I prefer the `develop` branch.
  - Whenever translation files in the branch changes, our automation scripts will push the changes to Transifex and when they are translated and reviewed to about 50%, it will pull them into our repo. We could also run this as a daily sync operation.
  - Release process:
    - We pull all translated files into develop (automation should take care of this).
    - We make a release branch, which should contain all translations from develop.
    - If we make changes/fixes in the release branch, we should merge the changes into develop, and then merge the translation commits into the release branch.
    - We do not wait for missing translations after we freeze the release branch. If we want translations, we will wait until they are present in develop, before freezing the release branch.
- Translating the app
  - I will be doing this inbetween my other tasks, throughout the upcoming week.

**0.1.4**

- DB connections
  - I will be working on the DB connections home page. I had a chat with Sean on Friday, and went through the requirements. I haven't begun work on it yet, I will be starting on it tomorrow.
- Migration script cleanup
  - I haven't begun work on it. I will start it when I have the time in the upcoming week.

### Sean
- DB connections work
    - This is going well.
    - I've begun work on the [New DB connection form](https://github.com/mathesar-foundation/mathesar/pull/3319) even though it requires me to get out ahead of the backend a bit.
    - I've handed the [other front end changes](https://github.com/mathesar-foundation/mathesar/issues/3297) off to Pavish, and he'll be working on that while I'm away.

- GH tickets
    - I've [proposed](https://groups.google.com/a/mathesar.org/g/mathesar-developers/c/JXMBCsOmKao) some adjustments to our GitHub process. I'm actually really excited about this. I think it's going to help move our tickets along better.
    - I spent lots of time cleaning up GitHub tickets, particularly ones marked as "draft". Much of this cleaning work, though "completed" is yet to be actually "pushed" (so to speak) to GitHub. Basically I have a bunch of lists of tickets that requires specific label changes, and I'll be applying these changes en masse after my workflow proposal is approved.
    - I've also prepared a [queue of tickets to discuss at December's product approval meeting](https://hackmd.io/8LGLy7ByRtKKBNrshqMcow)

## Misc. team workflow issue discussion
We should set up regular calls to discuss the following:
- Product specs
    - This could be like the "design sessions" but focused on "product specs"?
    - Permissions / architecture 
- Implementation specs
- Product strategy
    - Higher level
- User research & help check-ins
- Community growth / contributors, etc.
- Prioritization
    - beta planning work

We already have calls for
- Ticket review
- Design sessions

Questions
- What frequency should each call be?
- Who should be involved?
- Who should facilitate?
- Should we still have the weekly meeting?

### Notes
Meetings based on ticket needs

- Triage
    - Covered by repo admin process - no meeting needed
- Product approval
    - Covered in monthly ticket reviews
- Implementation specs
    - We'll do a one-off meeting during weekly meeting on the 6th and see how that goes
- UX design
    - Covered in design sessions
- Technical approval
    - Async
- Unblocking
    - Async
- User feedback 
    - Async

Meetings based on other needs

- Strategy
    - Kriti will facilitate
    - Everybody should attend
    - First iteration in December, figure out cadence
- Product "big picture" meeting
    - "Big Picture"
    - E.g., workspaces
    - Architecture
    - Once a week
    - Pavish will schedule / facilitate
    - At the end, discuss what we'll talk about next
    - Everyone should attend
- Prioritization
    - deferred until January
- Community growth meeting
    - One in December to talk about GSoC
    - Further cadence decided then
- User research & help check-ins
    - Deferred until January
    - We have enough info for the strategy now
    - It's okay to lose some users now to focus on long term stability

## Decision making process
We want to avoid everyone being involved in every decision.

We should set up "areas of responsibility" with no more than 2 people per area.
Decisions should be made by people with responsibility. Everyone else is welcome to observe or provide input.
If a decision involves multiple areas, we will union the people involved.

e.g. bidirectional navigation did not need to involve backend

What areas and owners can we identify now?

### Notes
We agreed that this is a good idea.
Kriti will follow up via email with an initial list of areas and owners.

## Task management workflow
Quick update: Kriti will be working on this.
We might just try Basecamp and see how that goes.
