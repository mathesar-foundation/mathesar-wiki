# 2023-09-27 team meeting

**Attendees**: Anish, Brent, Dom, Ghislaine, Kriti, Mukesh, Pavish, Rajat, Sean

## Release 0.1.4 check in
**Discussion goal**: Figure out what we need to do to get 0.1.4 out and re-allocate responsibilities as needed.

### Discussion
* Rajat sent an email with open issues for 0.1.4
    * Needs to sorted into critical, nice-to-have
* Kriti: It's important to have Installation as part of 0.1.4
    * Important to release 0.1.4 before our public funding announcement
    * Mukesh on Installation:
        * Docker image with inbuilt PG and related documentation is complete
        * Debian package PR is blocked on DB credentials UI work, documentation is in works (needs to be reviewed)
    * Kriti: Installation work needs to be 'complete' i.e. close to original installation plan
        * We should treat 0.1.4 like a launch
        * Installation testing and smoke testing are both required for 0.1.4
        * We could hire people from Upwork for testing
        * We need to also review documentation in an overall holistic perspective
    * We need someone to co-ordinate the release, with tracking Installation work, testing, documentation reviews etc.,
        * Sean's doing it
        * Kriti can help Sean understand the Installation plan
        * Pavish and Brent can help with the 'release process'
    * Pavish: We need Node 18 to get merged for release
    * It would be good to have i18n work
        * It would take a while to get there
        * We would have to use translations throughout the app, and have JP translations additionally
        * We will not be blocking release for i18n
    * Kriti and Brent would like to be involved in reviewing all installation documentations

### Conclusion
New priorities for release have been established (getting installation as close to the orignal plan as we can, so people can install Mathesar easily). Sean will coordinate the release so Mukesh and Rajat can focus on implementation.

## Plan for cooldown + product direction

### Pre-meeting prep
**Discussion goal**: Convey the plan for the cooldown & next steps for determining product direction, answer questions from the team.

#### Cool down
- We will be extending the cooldown from 2 weeks to 3-4 weeks so that we can all be on the same page about product direction.
- During the cooldown, our priorities will be (in order):
    - Releasing 0.1.4
    - Announcing funding
    - Talking to users (see below)
    - Buy-in on product direction and needs
    - Plan for growing the team (based on product direction and needs)
    - Planning out the next cycle
- Kriti will also be working on:
    - New organizational structure

#### Product direction
- The PostgreSQL compatibility project has confirmed that Mathesar connecting to existing databases is viable – we need to solve some performance issues, but the outlook is optimistic.
- We have a lot of data on the market thanks to the niche research project, but we need to talk to users to get more concrete data on the problems Mathesar solves for them.
    - This is what we need to make decisions about product direction.
    - The entire team will be involved in this process.
- We are transitioning from an engineering team to a sustainable organization, and we need to be focused on providing value rather than just building software.


### Discussion
* Talking to users
    * High priority after release
    * We'll split conversations with users with everyone on the team
    * Ghislaine is writing up a plan
        * Right now, she's building a CRM
    * Would give us solid data to move forward and focus on a Niche
* Compatibility with existing PG db
    * Mostly good news, with some performance issues
    * Brent is poking through endpoints and their individual performances and trying to tune them
        * It wouldn't take months, perhaps a few weeks
        * If we can tune a few specific endpoints, we could improve performance greatly
* Niche research
    * Ghislaine's report had a lot of research around small businesses using Postgres
    * The outcome can be attained only after we talk to users 
* Moving from alpha to beta
    * We are ready to be used in production i.e we can openly recommend using Mathesar in production
    * We may not necessarily need more features, but if we get feedback from users on deal-breaking features, we can add them in
* Moving from beta to 1.0
    * There are people using Mathesar in production
* Beta and 1.0 are more about improving stability and being production-ready than having more features
* Architectural changes
    * Brent is working on a plan and we will discuss this during the cooldown
    * This will also include information on what would be a 'public' interface and what wouldn't
* Product direction
    * General plan is to talk to more users, understand their needs
    * Ghislaine: We need a fallback if users do not end up scheduling calls
    * Kriti: This should be part of the plan
        * eg., offering a gift card or some incentive for user interviews
    * Ghislaine, Sean, and Pavish will work on the plan, and Kriti will be reviewing it
* We have 134 subscribers in our mailing list
* Once we have more data, we will plan on more resources needed
* There's no specific date to begin the next cycle yet
* Pavish: We would need more conversations on E2E tests and avoiding regressions
    * Will reach out to Brent and figure it out

### Conclusion
* Sean will be coordinating the release
* Rajat and Mukesh will work on Installation
* Pavish will be helping Ghislaine and planning E2E testing
* Brent will be working on performance stuff
* Ghislaine will be working on talking to users
    * Sean and Pavish will help
* Dom has work from previous cycle, which he'll be focusing on
    * Sean will coordinate with Dom on tasks with higher priority
* Anish will help with bugs in Installation work
    * Sean will coordinate with Anish on tasks with high priority
* Kriti will be reviewing everything and work on new organizational structure

## Infrastructure as an ongoing responsibility pitch

### Pre-meeting prep
**Discussion goal**: Determine whether we want to add "Maintaining infrastructure" as a tracked ongoing responsibility, assign it if so.

This is motivated by the growing number of servers, etc. we have on GCP, and some balls which we (I) dropped w.r.t. those over the course of this cycle. I think we should track this as an ongoing responsibility, and probably dedicate a page to it on the wiki or some more private place (depending on how precise we want the docs to be). Further, I think we should occasionally rotate this responsibility to avoid bus factor (or maybe just have a team of 2 who know about it). Off the top of my head, things under this banner are:

- All Mathesar domains (renewal, certs, etc.)
- Servers/load balancers on GCP
    - bespoke installations using Ansible
    - demo (aaaaargh)
    - internal (uses docker compose)
- Networks on GCP
    - Associated with the above servers, some should probably be deleted
- Databases on GCP
    - only internal.mathesar.org for now

It may be necessary to incorporate some projects under this ongoing responsibility:

- Setting up monitoring for all managed services
- Consolidating deployments

### Discussion
* Kriti agrees that it needs to be an ongoing responsibility
* The highest priority is to document the current process
* Brent will hold the responsibility for now

## Coordinating with helpers during the cycle

### Pre-meeting prep
**Discussion goal**: Come up with suggestions to effectively coordinate with project helpers

The Installation Improvement 0.1.4 project got delayed as a crucial feature (Database credentials page) which other features depended upon got delayed. This problem happened as I didn't communicate the urgency of the work needed to be done and instead did a async check in with the helpers. I would like to hear some suggestions to avoid this problem in future. 

Suggestion:
- weekly sync check in with helpers to discuss their work load make sense or if we should reorganise their work

### Discussion
* Brent's idea: It would make sense if everyone working on a project should meet once a week
    * Whoever owns the project should setup the meetings
    * Kriti agrees

### Conclusion
It's now expected that all members of a project meet _at least_ weekly, more is fine depending on project needs.
