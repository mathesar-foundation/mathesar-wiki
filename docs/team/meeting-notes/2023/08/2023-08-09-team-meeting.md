# 2023-08-09 team meeting

**Attendees**: Anish, Brent, Dom, Ghislaine, Kriti, Mukesh, Pavish, Rajat, Sean

## Product strategy & niche discussion

### Pre-meeting prep
- **Discussion prompt**:
    - Feedback from the team in 1:1s so far has been "just pick a niche!"
    - We'll be focusing on business users that already have a PostgreSQL database to connect to.
    - We do need to narrow this further, this is what our research will be focused on in the next cycle.
- **Discussion goal**: Buy-in from team, resolving concerns.
### Notes
- Team agrees that "focusing on business users that already have a PostgreSQL database" is a good idea.
	- Still need to decide how specific our niche is. We'll do this once we've done more research, planned for the next cycle.
- Please note that this _does not mean_ we're only supporting users with existing databases. We're just going to be focusing on making the experience better for those users first.
	- We should not be making any technical or architectural decisions that cut off our ability to support other users in the future.
- Side note: 1/1 discussions to gather feedback on product strategy were productive! 
	- Ghislaine will be scheduling discussions with remaining team members about product strategy.
	- We'll also use this discussion format more in the future.

## 2023 Cycle 1 retrospective

### Pre-meeting prep
- **Discussion prompt**:
    - Please write down your thoughts about the previous cycle, we'll discuss.
- **Discussion goal**: 
    - Analyze previous cycle
    - See what worked so we can keep it for the next cycle
    - See what didn't work so we can figure out how to tweak the next cycle

### Pre-meeting notes
#### What went well
- [Kriti] Signifcant progress on most projects
- [Kriti] We have a plan for installation finally
- [Brent] I felt like I was able to really focus on my work, and RSQLA1 in particular
- [Brent] We were able to capture information from the List project that will hopefully help us make future decisions
- [Sean] Qualitatively, it feels like our collective pace has really accelerated in this cycle
- [Ghislaine] My tasks were clear. Check-ins with Kriti felt very efficient and I think we managed to align around the same goals. I also enjoyed having more discussions with team members.
- [Rajat] I was personally able to deliver a lot more as compared to previous cycles.
- [Dom] Working on a mix of different issues was stimulating, and them not depending on each other was nice, because one of them getting blocked meant that I could just switch to the next one.
- [Pavish] I had a lot of focused time for coding/coding-related tasks during the cycle.
- [Pavish] Working on the backend has helped me understand some parts of the BE architecture, and has given me a sense of calculating effort when it comes to moving logic between FE and BE, and deciding the best place to implement said logic.
- [Pavish] Repeating a point made by almost everyone: Overall, I feel like we've gotten a significant amount of work done as a team.
- [Mukesh] We got a good amount of quality feedback from the community.
- [Mukesh] Figuring out the targeted persona (even if it is an assumption at this point) our app is aimed at, helped progress the Installation plan significantly.
#### What didn't go so well
- [Kriti] Most projects didn't get completed
- [Brent] People seemed to each be absorbed by their own projects (at least in the back end); cross-communication was weak.
- [Brent] No synergy between back end projects; time spent on one was time lost on another.
- [Sean] hard to know exactly how to deal with changes in plans mid-cycle. I spent almost the entire cycle on unplanned work because it was related to a user-reported bug.
- [Rajat] Sean had a lot of review items on him which contributed towards some of the delays. 
- [Ghislaine] There's room for improvement in how we facilitate more meaningful team discussions.
- [Dom] Underestimated how much time work outside my project will require, and that this work will mostly have to happen at the last 1-2 weeks of the cycle. 
- [Pavish] Task assignment planning before the cycle needs to be improved. Both i18n and Shareable links projects had a lot of code changes (and multiple PRs) to review, and Sean had to do both, which lead to inevitable delays.
- [Pavish] There was a part of me that wanted to avoid context switching and not do tasks that felt like they took my focus away from my project, and another part of me that wanted to do those tasks. I did subpar work juggling between the two.
  - I wanted to collect my thoughts and have a more focused discussion around 'Users who do not want anything installed on their DB', and resorted to chats over Matrix in the end. I could have taken a day or two to send a more meaningful mail instead.
  - I noticed a number of issues that we may want to focus on the next cycle which I discussed over chat, and am yet to create tickets for.
  - I did not attend the last Installation planning meeting to focus more on my project, though I was super interested in it.
- [Pavish] There was no specific person assigned to deal with general issues that may arise during the cycle. It was hard to request help from any specific person since everyone had a lot of work.
  - I was met with test case failures due to 'too many clients' error, and I required help from the backend team members who had overall knowledge of the test suite so that I could proceed in the best possible direction. I wasn't sure whom to reach out to, and requested help from everyone. 
- [Mukesh] Context switching between researching and doing code related work in the same cycle was daunting.
- [Mukesh] There was no one assigned for firefighting issues that weren't related to any project.
#### Shout outs
- [Kriti] Pavish for great work on taking sharable links from conception to implementation
- [Brent] Anish did fantastic work and was crucial to the success of RSQLA1.
- [Brent] Dom for really pushing me to make sure the SQL code is as well-documented and easy to understand as possible.
- [Sean] echoing Kriti's praise for Pavish. Awesome to see a team member doing such extensive work across the entire stack!
- [Sean] Impressed with Rajat's sheer amount of code changes in a relatively short amount of time for the i18n work
- [Ghislaine] Kriti did an amazing job with Mathesar's presentation. Also Mukesh for being proactive in researching use cases for Mathesar and starting conversations with other people around this topic. I got a lot of insights from our conversations.
- [Rajat] Mukesh for helping me with the backend work and for faster PR reviews.
- [Dom] Brent for being a living encyclopedia of Postgres internals. Your insights saved me days and days of work!
- [Dom] Pavish on implementing a significant feature across the stack!
- [Pavish] Brent for stepping up and helping me handle the test case failures. It saved me a lot of time.
- [Pavish] Mukesh for taking the time for a long call on permissions, and reviewing permission related changes in my PRs. In hindsight, I should have mentioned him as a reviewer before the cycle but hadn't. This was additional work for him that he hadn't planned for.
- [Mukesh] Kriti for helping with putting together the installation plan
- [Mukesh] Brent for his honest feedback on the various discussions
#### Ideas
- [Kriti] Increase buffer times when you're estimating projects
- [Kriti/Sean] Designate a priority order for projects in the cycle so that we know what to cut ahead of time if we need to shift some responsibilities around
- [Brent] Fewer overall projects, more people per project
- [Brent] Try to choose projects that 'go together' to help encourage communication and working together
- [Brent] Think of ways to get FE and BE ways to work together on things.
    - [Dom] In reply to the common theme of above ideas, I'm skeptical of people working on the same thing at the same time being good for synergy, or, at least, I'd say this is nuanced. While I see some pros, such as everyone being engaged at the same time and thus being able to sanity-check others more promptly, I also see cons, such as people blocking each other when working too closely or stepping on each others' toes when working too loosely; we've not always gotten that balance right. I'd like to hear more about the envisioned benefits. That said, I'm not against experimenting with this.
### Notes
- Sean: which "fires" should we have "fought" during the cycle?
    - Mukesh: issues with tests cases that Pavish raised.
    - Dom: I would have been able to help with this, but I didn't know it was a problem.
    - Pavish: this ties into the questions about how to prioritize one team member's work over another's.
    - Kriti: prioritizing projects could help with this
- Kriti: we should either prioritize each project relative to others or delegate a smaller group of people to "firefighting".
- Pavish: lots of unknowns within the user-reported issue that Sean/Dom worked on. This "unknown" was challenging
    - Dom: maybe unavoidable?
- Pavish: maybe more planning ahead of time could have helped with Sean/Dom's work
- Pavish: I could have done the import changes faster than Sean
    - Sean: Agree
- Brent: rotating "firefighters" helps everyone to see different parts of the codebase, and this is beneficial for the project as a whole
- Sean: need to be agile a bit with user-reported issues
    - Kriti: okay to embrace some chaos to an extent
- Kriti: proposal to prioritize all the projects in a cycle
    - All agree
- Dom: when someone needs someone from me, it's helpful for me to understand how soon they need it.
    - Kriti: When people need something from another team member, please ask clearly, assertively. Be clear about how soon you need it.
- Pavish: We should also be able to re-adjust timelines and priorities mid-cycle
- Pavish: backend team and frontend teams are too fractured. If each team had a better understanding of the other team's work, it would help us all
- Brent: would also be nice to find projects that can be assigned to one frontend engineer and one backend engineer
### Decisions
- We'll make sure projects have priorities relative to each other, and also reevaluate them during weekly meetings.
- Designated firefighters seem like a good idea, they can also work on issues from the backlog during downtime.
	- This will need some pre-work to "groom" the backlog and keep it up to date.
- When requesting help, be assertive and provide a timeline that you need help by.
- We'll figure out what work we need to do and assign teams accordingly, we're not going to have a rule that says each project needs multiple people.
## 2023 Cycle 2 project ideas brainstorming

### Pre-meeting prep
- **Discussion prompt**: We should brainstorm project ideas for the next cycle.
- **Discussion goal**: We should have a list of projects and their owners, so the owners can start writing them up.
### Pre-meeting notes
- Kriti's ideas based on niche & goals:
    - Testing how well we work with existing Postgres DBs, associated fixes
    - Figure out what it would take to get us to 1.0 and work on that
    - Product research for better definition of our niche
- Dom
    - Backend fixes project still has a few minor issues left, should be ale to cobble together a cycle-worth of work
    - Very basic support for setting dynamic column defaults (whitelist-based)
- Pavish's ideas:
    - Start research and discussions on how to handle permissions between related entities.
      - Eg., If a user has access to only one table, how to they interact with FK columns?
    - Feature to allow users copy tables and schemas (Similar idea proposed by Brent on mail thread).
      - I think this would be a more useful and immediate feature to provide to users coming from a 'spreadsheet' background, than attempting to implementing versioning.
    - Add additional endpoints to provide custom (non-REST compliant) responses to help improve stability and performance of the frontend.
      - This would be a refactor and reduce our focus on building new features, but this would definitely improve the frontend codebase.
      - For eg., Adding a single GET endpoint that provides all the structural details of a table (table's properties, columns with their Mathesar types, constraints) would reduce so much state management on the frontend and enable us delete a chunk of code, improving FE stability, maintainability, and performance.
      - I think it is worth it to research parts of FE that can be improved this way, and take the time to implement it.
- Mukesh idea's:
    - Mathesar error reporting and troubleshooting plan


Fixing backend tests
    Right now, we have a somewhat ad-hoc testing suite for the back end code.  It's slow, and doesn't have a coherent strategy. I'm not confident that any breakages will be caught (in fact, I'm confident they won't all be caught), and I think a number of things are tested repeatedly in the course of testing some other behavior. We should try to fix this. The goals should be to have a strategy with 'buy-in' from the back end core team members, and then make steps to implement that strategy.

Researching FDWs
    We've discussed this through a few channels, but I think we should research how painful it would be to support FDWs in Mathesar. Already, if there are foreign tables in the DB (that Mathesar has access to) then we'll show them, and then probably throw some inscrutable low-level errors if you try to modify them via DDL operations. It would be good to start by simply handling any errors gracefully. It might also be nice to support adding external data sources to your Mathesar DB as a feature. We could support wiring up MariaDB, or Redis caches, or even arbitrary RSS feeds through this (maybe). However, this is a massive undertaking with product, design, and technical challenges. Thus, I think we should start with a cycle's worth of doing the design and product work (if we want this), and doing some technical prototyping.

Rudimentary support for DB views
    I think this might be low-hanging fruit. The main challenge would be design so that a user understands that they can't edit (for now) in a view, but have to edit underlying tables. I don't even think we'd really need to allow users to *create* views through Mathesar at this juncture, just view them. The reason this would be useful is that we've already had a user or two (or, honestly, maybe only the one) mention that they could set up views for their less-privileged users and give Mathesar access to those. The 'views for less-privileged users' strategy is super common, and if we have any support for that, it might help some admins choose us over competitors.

Researching table versioning (part 27/n)
    We've received more requests for table versioning/undo. One idea that a user mentioned was keeping a long-running transaction open so the user can play around before committing. Might be worth thinking about. The use case for that one was wanting to give less-privileged users the ability to play around and model the data, without necessarily corrupting the 'real data'. I think we should start from that use case, and try to determine how we could best support that. It could be as simple as 'copy schema' or something, though that wouldn't really allow merging it back into the root schema afterwards.

Further permissions management
    We're currently going back-and-forth on a PR to remove the superuser requirement when installing Mathesar. Suffice to say, I think we need to consider this from a product direction, determine what we're trying to achieve, and then go for a coherent implementation. As mentioned above, it might make sense to split Mathesar requests (to the DB) into two privilege levels; one for daily driving, the other for user modification and so on. This could be an intermediate step between only having a root level Mathesar user for connecting to the DB, and having a DB user for each Mathesar user.

Finish column moving features, improve logic
    It came to my attention during RSQLA1 that this feature isn't complete, and the current state is sort of dangerous. You can only move columns in one direction along a foreign key link, and I expect that asymmetry won't be obvious to users. Also, the moving logic could cause data loss under some edge-case circumstances. So, they could be tinkering around, move some columns, and then find out they can't move them back, or extract some columns only to find out they can't be put back together with the original table. Worse, when moving columns, they might find that some other, as far as they understand uninvolved, table might be missing rows afterwards. I think the current state of column extraction and moving is therefore a ragequit-inducing antifeature. We should either take out that functionality entirely (I don't like this except as a stopgap), or make it work as users would expect. I'll put more detail into a proper project proposal; here I'll just note that we need product work before we start to think too much about implementation on this.

Mathesar update capability analysis, determine plan
    As we add more installation methods and move away from the docker compose setup, we need to make sure that we have proper instructions for updating Mathesar, and recovering if an update doesn't work for each installation type we do. This could be rolled into the installation project(s), but I'm worried that so far we haven't thought about it at all for any of the non-docker-compose installations (I could be wrong here; that would be great!)
### Notes
- Kriti: Let's ignore the above list for a bit. If we're trying to support existing databases, what is some of the most important work for us to do?
- better permission handling. We should try to work with existing pg permissions.
- better support for unknown types -- don't throw errors. We should allow editing wherever possible. We need to clarify our goals here. We should display the actual database type instead of "unknown"
- Support tables without primary keys
- Multi-column primary keys
- Testing Mathesar with other products that use Postgres
- Improved support for views
- Improved support for generated columns
- Display info for EXCLUDE and CHECK constraints
- Improved UX for viewing all tables, e.g. hiding tables, showing ER diagram
#### Brent side-notes preexisting Posgres
Major things we don't support that people have in their DBs
- Views
- Users/permissions
- Types
- Different pkey setups
### Conclusions
- Ran out of time, will continue discussion at the next meeting.

## Scheduling the next meeting

### Pre-meeting prep
- **Discussion goal**: Figure out when we should have our next meeting given that we have a lot to talk about
### Decision
- Next meeting will be tomorrow


