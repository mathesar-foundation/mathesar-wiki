# 2023-08-10 team meeting

**Attendees**: Anish, Brent, Dom, Ghislaine, Kriti, Mukesh, Pavish, Rajat, Sean
## Morning "hello"
- People are feeling good about our routine of saying "hello" in the morning in the internal channel.
- We'll continue this

## 2023 Cycle 2 project ideas brainstorming, part 2

### Pre-meeting prep
- **Discussion goal**: Have a final list of projects and their owners, so the owners can start writing them up.

Project ideas from previous meeting and follow up discussion on Matrix:

- Installation improvements
    - This is still a major barrier to Mathesar adoption
    - Implement the plan we've already decided on [here](https://wiki.mathesar.org/en/meeting-notes/2023-07/2023-07-28-installation-meeting.md)
- Make Mathesar work better with common existing Postgres setups
    - Major things we don't support that people have in their DBs
        - Views
            - Rudimentary support for DB views
        - Users/permissions
            - Better permission handling. We should try to work with existing pg permissions.
            - We need to do more research into this before committing to supporting Postgres users / permissions
        - Types
            - Better support for unknown types -- don't throw errors. We should allow editing wherever possible. We need to clarify our goals here. We should display the actual database type instead of "unknown"
        - Different pkey setups
            - Support tables without primary keys
            - Multi-column primary keys
        - Generated columns
            - Improved support for generated columns
        - Constraints
            - Display info for EXCLUDE and CHECK constraints 
- Improved UX for viewing all tables, e.g. hiding tables, showing ER diagram
- Testing Mathesar with other products that use Postgres
    - e.g. Supabase integration
- Product research for better definition of our niche
- Ideas from prior async brainstorming are [here](https://wiki.mathesar.org/en/meeting-notes/2023-08/2023-08-09-team-meeting.md#pre-meeting-notes-1)
### Pre-meeting notes
Additional thoughts from Kriti:

- Firefighting + backlog clearing team
    - Including stuff like moving wiki to MkDocs, automating internal deployment / `develop` Docker builds
- Do we also want to consider work that will let release more frequently? 
- We also need help with organizing our backlog
#### Brent's thoughts
- I think we should really try to do the project to fix up the column moving, or remove that feature, and wiring up to a preexisting DB makes this even more relevant. The current functionality lets you screw things up irreversibly, and it won't be obvious to a user when they're in danger from our current UI.
- Views:
    - We need 2 things IMO:
        - actually show the view in the UI (very easy; it's just a switch flag in the reflection calls, will reflect views as tables), and
        - flag the view as non-editable (for now). This is a bit harder, but still should be easy in the back end. Design work needed.
- I think "work with existing PG permissions" is too strong, or at least too general. We need only to be able to run as a reduced-permission user for the whole installation without throwing errors everywhere.
- Types:
    - Biggest problems are going to be composite types, and array types (which we're currently struggling with). SQLAlchemy makes working with unknown composite types extremely difficult, to the point that I'm not even sure where we'd start on that. It seems like if we drop SQLAlchemy and just use `psycopg`, things are a bit simpler, though still messy: https://www.psycopg.org/psycopg3/docs/basic/pgtypes.html
    - Scalar types should be relatively simple; we'd just treat them as strings, more-or-less.
- Generated columns:
    - I think the only support we need for this is to notice that they're essentially a dynamic default as far as the front end is concerned:
        - we shouldn't modify the default generator, or
        - allow input into those cells. 
    - We could also trivially show the generating expression (in fact this might already happen if we're showing dynamic defaults somehow), but I'd consider that a bonus.
    - We're already flagging these columns as a dynamic default in the back end, it's a matter of whether the front end is then handling that with enough fidelity.
- Supporting different                 setups: This may be the thing we need the most work on overall
    - Handling different types of primary key single columns:
        - Right now, we're flagging a column as a 'default' column (as in created by Mathesar). Then, we disallow any modification by the user of such a column through Mathesar.
        - I think we could pretty easily handle a dynamic-default primary key column by just flagging it as such, and disallow any modification of that column.
        - Multi-column: This will be tricky. We're assuming we have a single pkey column throughout our codebase. We could just filter these tables out of the ones we handle, or treat them as read-only.
- Constraints:
    - I consider this to be extremely optional, other than smoothly handling 'constraint violation' errors.

### Discussion
Are there projects that we need to continue?

- "Backend fixes"
- "Frontend fixes"
- Kriti: What is the status of i18n project?
    - Should be finished soon. But This is only the infrastructure around it -- not actually the translation. We'll be hiding the UI so that there are no user-facing changes until. 
    - Rajat will be working on workflow and documentation next week. Expecting to finish by the end of the cycle.
- Sean: concern about some tasks being too big for one cycle and some tasks being too small for the cycle
- We should have two people working on smaller tasks and backlog type things.
- How should we refer to these smaller tasks?
    - "on call"? -- no.
    - "Firefighting"? -- not great.
    - "cycle helpers"?
    - "Generalists"
    - "ad-hoc" -- (seconded)
    - This is still up for debate
- How/when should we rotate ad-hoc helpers?
    - We'll try to begin rotating next cycle
- Kriti: fixing things that are not working well seems to be higher priority than adding new features
    - Most agree
    - Brent: column-moving is not working "to a dangerous level". However, we should consider whether we want to get to a "beta" or "v1" sooner, or wether we want to scaffold out this sort of product so that people have a better idea of the features we'll have once we're more mature.
        - Kriti: would lean towards prioritizing stability of existing features before building new features.
- What bugs to we currently have?
    - We might want to do some research/testing to identify new bugs
    - Dom: we already have a lot of existing bugs that we could prioritize for this cycle
    - Kriti: there may be other bugs we'd uncover during testing that are higher priority than the bugs of which we're already aware
    - Pavish: we might want to identify some use-cases to help steer our testing to better identify issues.
        - Kriti: this would be good work for the person who owns this project.
- Pavish: Should we identify issues first, or fix them as we go?
    - Kriti: we should try to identify lots of them first so that we can prioritize them
- Pavish: talking to users would help us identify more issues and give us a better idea of how to address them
- Kriti: interested in integration with Supabase. This might give us visibility to Supabase users through the Supabase UI.
    - https://supabase.com/docs/guides/platform/marketplace
    - https://supabase.com/partners/integrations#data%20platform
    - https://supabase.com/partners/integrations#become-a-partner
    - https://supabase.com/docs/guides/platform/oauth-apps/build-a-supabase-integration#create-an-oauth-app (new integration workflow coming soon)
    - Also look at Directus Supabase integration since they're similar to us
    - [Rowy](https://www.rowy.io/) can be used as a reference. It provides a UI for firestore database
    - How much work would this be? Maybe a whole cycle if we also start on implementation.
    - This might be a good project for the ad-hoc team.
- Column moving problems
    - Read Brent's thoughts on this
    - Sean: seems like a lower priority, given our current focus on working with pre-existing databases
    - Maybe we could disable the feature?
    - Could we add a warning message?
- Ad-hoc team will not have a project page
- We'll need to discuss our process for organizing the backlog issues (future meeting)
### Conclusion
- Installation improvements
    - Mukesh (owner)
    - Anish (helper)
    - Rajat (helper)
- Product research to narrow our niche
    - Ghislaine (owner)
    - Brent (helper)
    - Pavish (helper)
- Ad-hoc helpers
    - Sean
    - Rajat
    - Dom
    - Ad-hoc tasks
        - Research Supabase integration/affiliation
    - Other ad-hoc ideas
        - Exporting tables as CSV
        - Duplicating a table
- Investigating compatibility with pre-existing databases
    - Brent (full-time, owner) 
    - Pavish (full-time)
    - Ghislaine (part-time)
    - Sean (part-time)
## Remove SQLAlchemy project update
- We're pausing work on this.
- Brent wants to "let it simmer" for this cycle. Much of the work is done, but we need to validate the tactic we're using "in the field". There is still more work to do to fully remove SQLA, but we'll pause work on it for a while.
- Brent was originally fearful that the refactoring would be disruptive. He's not as worried about that now, which is why he's okay with deferring it for a while.
## Future meetings

### Pre-meeting prep
- **Discussion goal**: Figure out when we're having the remaining discussions we need to have

Already covered at this meeting:

- Project planning for August 21 cycle

Things we need to discuss:

- How to prioritize the backlog
- RSQLA retrospective
- “Should we install things on the DB?” discussion
- Figuring out how to handle XY problem with user feedback
- Criteria for closing user-reported tickets
- Internationalization retrospective
- Installation plan details finalization
- Product level permissions discussion to account for related entities
- Approval of written up projects
- Delegating responsibilities for Kriti's time off 
### Conclusion
- How to prioritize the backlog
	- Rajat, Sean, Dom, Kriti will come up with a plan
	- Kriti will start Matrix DM to kickstart
- RSQLA retrospective
	- Brent will start email thread
- “Should we install things on the DB?” discussion
	- Brent will start email thread based on notes written in the meeting notes doc.
		- Pavish can send his notes as a reply.
- Figuring out how to handle XY problem with user feedback
	- Pavish will start an email thread
- Criteria for closing user-reported tickets
	- Everyone should respond to [this email thread](https://groups.google.com/a/mathesar.org/g/mathesar-developers/c/w9CskyV9r3s/m/jmbOkbC5BAAJ)
- Internationalization retrospective
	- Rajat will start an email thread
- Installation plan details finalization
	- We don't need any more discussion about permissions
	- Mukesh will start an email thread about finalizing where to store config
- Product level permissions discussion to account for related entities
	- Pavish will start an email thread
- Approval of written up projects
	- We'll do this at next Wednesday's weekly meeting
- Delegating responsibilities for Kriti's time off 
	- Kriti will start an email thread