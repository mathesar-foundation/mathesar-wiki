# 2023-12-11 Team Meeting

## Team check in

### Adam

- mired in admin land
- 2024 budget
- Finalizing things with Insperity
- Vetting Remote.com and other options for contractors — should start new in Jan
    - Some people will need to do some paperwork to get set up. Will follow up as needed

### Anish

- Working on installation documentation for the upcoming release
- Waiting on review from Brent for Docker compose PR
- Reviewing some contributor PRs
- Don't have any thing immediate to work on
- Probably going to work on [Modify schemas API to accept connection IDs instead of connection nicknames](https://github.com/mathesar-foundation/mathesar/issues/3342) ()

### Brent

- DB Connections RPC work nearly done (top priority)
    - Finishing up demo data sets and testing
    - Slower than expected
    - New features requested had to be hacked together in a hurry
        - Installing demo data outside of demo environment
        - Adding users
    - I should have flagged those more urgently earlier, but I wasn't sure what had been agreed to or discussed before I was working on that part of things
    - Kriti: rough ETA?
        - Brent: by tomorrow
- Dent in productivity due to family sickness
- Installation work progressing, thanks to Anish's hard work
    - Going through the new (very well documented) docker compose setup
    - Looking at installation docs "globally" to see what makes most sense
- Reviewed demo site setup so we can move more quickly once we release
    - We should really improve this setup
    - This is relevant because we'll need to deploy 0.1.4 to the demo server after the release. We want to be prepared to do this quickly
    - "hostile" architecture — feels like you're working against it. Lots of room for improvement here.
- Still going through backend redesign plans when I have time
- I'm trying to regather some lost "institutional knowledge" that was particularly relevant to connections and installation
    - Most recent connection and database model work had recently been done by Dom
    - Most recent installation work had been planned/led by Mukesh
    - Keep finding holes where it takes me a while to figure out how some crucial bit works.

### Ghislaine

- I was away for most of last week.
- Design spec for "Unified Tables" feature, which integrates tables with explorations. This is almost ready for review by team.
- Organizing the next session which will focus on the linking of bulk records. This includes reviewing different solutions proposed by the team.
- Writing a spec for the navigation consistency updates, including how to incorporate links for import, data explorer.

### Kriti

- Working on admin stuff
    - Inspirity
    - Benefits, 401K, DCFSA
    - Budget
    - Basecamp
    - Name change, govt forms, etc.
    - very boring stuff!
- Everything I'm doing is tracked in Basecamp

### Pavish

- i18n work is progressing well.
	- I've moved about ~75% of the raw strings to translation dictionary
	- I expect to move upto 95% before the end of this week, and then plan next steps.
	- I don't think we can move 100% into the app very easily
	- Will plan for new patterns for devs to follow
	- Sean: Did you consider handing some work off to Anniket?
        - Would have been too hard to hand off
- I'm preparing to organize the product "big picture" meeting this thursday.

### Sean

- Main work: still DB connections for 0.1.4
    - Coming along nicely, couple things blocked on Brent
        - the API
        - Question about connection nicknames being editable
            - Has frontend architecture and API implications
            - Connection nicknames vs. IDs at the API level
    - Pretty close to getting this squared away
- Review of i18n, coming along well, Pavish is working hard, lots of tedious work
- Repo admin - cleaning up labels, new workflow to replace the GitHub project, excited about this
    - Will be documented once the dust settles
- Comimg up: will depend on when things are unblocked by Brent, repo admin stuff
- Pavish: Can we skip making connection names editable for 0.1.4?
    - Kriti agrees it's not a blocker

## Basecamp

We will be using Basecamp for general task management.

- Tour of current projects
- Tour of features
    - Activity
    - Lineup
    - Todos + hill charts
    - Schedule / events
    - Files
    - Team check-ins
    - Email forwards
    - Discussion board
    - Features we're not using:
        - Chat
- Tour of product development workflow
- Tour of team management
- More visibility into operations and admin tasks

Items to discuss:

- How to track design work
- How often should we do team check-ins?
- What other projects do we need?
- Should we track remaining ongoing responsibilities here?
    - e.g. Syften, repo admin
- When to use Basecamp vs. GitHub
- Should we set up automations?
    - e.g. survey response on Google Forms
        - can create task to send email out to user
    - e.g. installation request response
        - can create task to follow up with user

Next steps:

- Please start checking Basecamp daily
- Please track non-code related tasks in Basecamp
- Stop using work logs

### Pre-meeting notes

#### Thoughts on Basecamp from Pavish

* I like daily work logs on the wiki better than Basecamp
    * Work logs on wiki are faster to update since my code editor is open all the time
    * Daily work logs are easier for me to maintain, I just have to remember what I did during the day and update it. We seem to have set Basecamp to track work across Tuesdays and Thursdays and I have to try and remember everything I did or note it down separately, which adds overhead.
    * We already have a weekly meeting where we do a general task check-in. Do we need to do the same in Basecamp?
* I do not like Basecamp for Team management. I would prefer we only use it for internal Project management and nothing else.
    * The main problem we wanted to solve was separating external GH issues with internal project tasks, and non-code related tasks. I'd like for us to use Basecamp to explore that.
    * Do we want to bring team management into Basecamp as well? What problem does it solve?

#### Kriti's notes (mainly response to Pavish's notes)

* I don't think our work logs should be public. They're only of interest to the team, and I often find myself redacting information because they're public.
* It is difficult for me to maintain and sync todo lists in multiple locations. I moved all my todos to Basecamp and have stopped updating my work log.
* Problems I'm trying to solve
    * I'm the primary "user" of work logs. It's helpful for me to know what people are working on and try and anticipate issues and blockers.
    * Having them be in the same place as my tasks helps me since I don't have to check multiple locations.
* I don't think the wiki is more convenient for everybody. We have at least 3 team members (Kriti, Adam, Ghislaine) who don't have code editors open all day, and I expect that to grow. 
    * I'd like a unified management workflow for everyone.
* If everyone tracks their tasks in Basecamp, I'm not sure if we need work logs at all, given the "Activity" view in Basecamp.
    * Work on GitHub and meetings won't be covered, but I'm not sure if that matters.
* We could also change the check-in questions to be shorter, and not require a big list of work as an answer. Example questions:
    * Is there anything slowing you down or blocking you?
    * What's your top priority right now?

#### Sean's thoughts

I spent some time fiddling with Basecamp yesterday. At a high-level, my impression is lukewarm. I’m very curious to hear more (at the upcoming) about Kriti’s vision for how we would use it — and specifically what problems we’d like it to solve. While I imagine that much of my skepticism towards it would eventually be resolved after I understand it better, I do want to highlight one concern up front that I would consider a complete show-stopper when choosing a tool for any software engineering team in 2023: it does not appear to support markdown at all.

Personally, if I need to use a tool without markdown support for anything other than trivially simple tasks, then I’ll be very grumpy about it. I rely on markdown basically everywhere, including my work log. I did a little digging to see if there is some way to enable markdown and was baffled to find the Basecamp team [insisting](https://github.com/basecamp/trix/issues/626#issuecomment-800338265) on WYSIWYG editing.

I think it’s important for us to take this limitation into account as we consider how we might use Basecamp. If our usage of Basecamp is confined to simple to-do lists with plain-text titles, then the lack of markdown support might be acceptable. But at that point, I’m having trouble envisioning how Basecamp would be worth adopting. If we want to use Basecamp for any sort of discussions, then I would argue for considering other tools before continuing to evaluate it.

### Discussion

- Kriti: we need a tool to track non-code stuff. User research, admin, operations, infrastructure, demo server, etc.
- Kriti: Ideally our work would be transparent enough that we would not need the work check-ins at the beginning of team meetings
- Kriti: I'd like to use Basecamp to track any work that we can't track on GitHub
    - It moves into GitHub when it's ready for implementation
- Ghislaine: Could/should the "Doocuments" feature replace HackMD?
    - Kriti: I think HackMD will be better. We can link HackMD docs, wiki pages, and google docs to the projects.
    - Adam: it's been working well for us to use other tools (e.g. Google docs) for ephemeral notes and to-do items, and then move those into Basecamp later
- Pavish: should we make a project per meeting?
    - Kriti: no, projects should be bigger than than
    - In general, we should avoid having projects for really long-running things. For product things, I'd like to have projects that we can close
        - There are a few exceptsion though, e.g. "Product Ideas"
- Once we pay for Basecamp we should be able so share certain things publicly, e.g. for our roadmap
- Work logs
    - Kriti: I don't want to use the wiki because it's public. I want our work logs to be private
    - Kriti: if people are willing to maintain a more detailed to-do list, then we don't necessarily need the work logs at all
        - Dividing things into projects and keeping things fairly detailed would sufice
        - We don't need to utilize the "Question prompts" feature
- Kriti will discuss 1:1 with people to work out some of the details about how we'll use Basecamp. We'll talk more next week

