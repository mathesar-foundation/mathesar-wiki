# 2023-12-20 staff meeting

## Release 0.1.4 checkin

### DB connections
- Sean thinks it's going well.
- Brent thinks it's going well on the backend. Dealing with some error handling stuff.

### Installation
- New docker setup has some issues with the unified docker image. Brent & Anish are working on it. PR open, should be ready once its merged.
- There's a large open PR for documenation and a number of open issues in the milestone. Brent wants to get the docs PR ready before checking the individual issues.
	- Anish is working on the Docs.
	- Docs for upgrades and env-variables are still pending.

### Current open items
This is before we can get to the testing and release process.

- DB connections
    - Backend PR needs to be merged
    - Frontend PR needs to be merged
    - Backend review work
- Docker Compose
    - Merge PR
- Documentation
    - Finish upgrade and environment variables docs
    - Global review of docs
- Fix migrations
- i18n bugs 
    - How to spot: snakecase variable names in UI
- Milestone: https://github.com/mathesar-foundation/mathesar/milestone/72
    - We'll review in January
- Bug assigned to Varsha - Anish is taking over if it's not done by January

We're getting there!

## Remote.com

For contractors outside of the U.S., we're setting this up for payment and invoicing
- Anish should send a personal email to Adam
- Currently in progress

## Basecamp workflow

- Closing Basecamp Setup project
- Ensure everyone is familiar with current projects
    - Should we merge any projects?
    - Are we missing any projects?
- Shared expectations for:
    - assigning tasks
        - People seem to be okay with this, getting notifications
        - When asking multiple people to do the same thing, try to make one task per person for easier tracking if they each need to complete the task separately
        - assign multiple people to the same task when either could check it off and it would be totally done.
    - how often to check Basecamp
        - once per day(ish)
    - how to communicate via Basecamp
        - Kriti likes to comment on things as appropriate.
    - setting due dates
        - People should set their own due dates, except if there's an external constraint.
- We'll continue to iterate on how we use Basecamp in the future

### Notes
- Maybe we want to try https://app.githelpers.com/ for integrating GitHub tasks into Basecamp
- You can "stack" projects by dragging them onto each other
- Kriti has projects organized into "Ongoing" and "Time-limited"
- Release projects
    - Brent thinks they should be multiple projects
    - Kriti likes being able to see progress on how far we are from being able to release
    - Sean worries that we won't see code-related tasks in the release tracking
    - Kriti had a good idea about multiple ToDo lists for a given project to organize sub lists
    - Brent worries that we will have a hard time organizing non-todo-list pieces within larger projects
    - Sean thinks the release project should track actual "release process" work, rather than release content.
- Sean hasn't really liked Basecamp so far
    - Negatively affecting productivity
    - Points out we could try using Mathesar for this
    - Will troubleshoot some problems with Basecamp with Kriti later
- Talk about the product backlog process next year
- TODO clean up installation improvement (split into 0.1.4 specific, move rest into backlog project)
- TODO clean up hill charts and needles

## Product strategy discussion
Should we have one this week? No.

An email to ponder over the break would be helpful. Kriti will work on this.
