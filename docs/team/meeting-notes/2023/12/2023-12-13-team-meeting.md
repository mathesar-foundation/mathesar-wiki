# 2023-12-13 staff meeting

## GSoC 2024 participation

GSoC is Google Summer of Code. We did it last year, but it was lots of work.

- Should we participate in GSoC 2024?
    - Adam asks: Was it lots of busy work preparing?
        - Lots of resumes?
    - Last year we had lots of low-effort applicants who wanted to make an initial submission
    - More effort to get through application process
    - Once we actually had contributors selected, it worked really well.
    - We were using the same process as we had at Creative Commons
    - Adam wonders if we can automate any parts of the process using AI tools
        - Maybe reviewing resumes
    - Ghislaine thinks the applicants will use AI tools to improve their chances
    - Kriti thinks GSoC has been valuable for Mathesar
        - drives interest in the project
        - gets contributors interacting with the project
        - gets contributors interacting with the docs
        - We've had some contributors over the recent months who might not check out our project otherwise
        - benefits the ecosystem by getting people into open source
    - OTOH
        - We're at a crucial time getting the beta out
        - We need to make sure it's less distracting
        - Maybe we need a more "closed" initial filter
    - Sean doesn't want to do it
        - Doesn't seem like it works out from a cost-benefit perspective
        - Doesn't see how to run without enormous costs
    - Ghislaine wonders if we've tried to measure the benefits
        - Code contributed is a benefit
        - Hiring funnel
    - Sean asked the mentors
        - 2/3 would have saved time by doing it themselves
    - Brent wonders if we could try to increase the difficulty of the projects to reduce volume
    - Pavish is on "team GSoC", but mixed-feelings this year
        - Initial phase takes too much effort, though
        - Lots of tiny contributions
        - What if we contact contributors who are already active
    - Pavish rethinking:
        - We aren't equipped to handle the initial rush right now
        - If the projects are crucial, we shouldn't hand it off to new contributors
        - If they're not crucial, we shouldn't spend time guiding the contributors on it
    - Sean's ideas for making application phase lower-effort
        - Tell people "don't contribute"
        - Look at project idea list
            - Tell people to apply using that list
            - Interview applicants on a call instead of using code contribution
    - Brent - we should figure out a way to require more of contributors. Be more harsh about rejecting people's contributions.
- If we do participate:
    - What kinds of projects should we do?
    - How do we make the proposal period less work for us?
    - What are our next steps to writing up projects?
- We brainstormed for a bit about potential project ideas and ideas for reducing burden on maintainers during the applicant phase, and couldn't come up with any ideas that would be in the spirit of GSoC.

### Conclusion
Unanimous: We're not doing GSoC 2024.


## Community building
- Should we do other community building activities?
    - Ideas
        - Community update call (rather than or in addition to social events)
            - talk about plans and so on
            - less social than community event
        - Office hours for contributors
        - 1:1s with promising contributors
            - Sean thinks this is super valuable
        - Could reach out to contributors in a more organic fashion
    - Timeline?
        - After beta
- Community team
    - Current situation for community team
        - Contributor room
        - Write permissions on GH
        - Community Mailing list
    - Kriti proposes removing the GH permissions
    - Most people on our community team have write permissions but haven't been involved
        - We should clean that up
    - Idea: split into "supporters" and "contributors" teams
        - Reduce / remove permissions for supporters team on GitHub, leave them in mailing list and private Matrix channel
    - Invite promising contributors to our contributors team proactively
    - Sean thinks we should treat people on a case-by-case basis, avoid systems/processes
- We should probably also eventually organize the wiki a little better for contributors, maybe once we've settled into the Basecamp workflow for internal use.

### Conclusion
- We won't be focusing on community building activities until after the beta.
- We should all be proactive about mentoring promising contributors when they appear
- Kriti will proceed with community team changes

## Decision making process

Follow up on an internal email thread.

Problem we're solving is having too many people involved in given decisions. Maybe we could have owners for different responsibilities that are involved in decisions?

Initial list:

- Backend architecture: Brent
- Community building: Kriti
- Documentation: Kriti, Sean
- Frontend architecture: Pavish, Sean
- Installation: Brent, Pavish
- Prioritization: Kriti
- Product: Kriti
- UI and UX: Ghislaine, Kriti

Proposed changes:

- Add Sean and Pavish to UI and UX
- Clarify UI and UX further
- Add Sean to community building
- Remove community building as an area entirely
- Add infrastructure with Kriti / Brent as owners
- Consider adding:
    - Marketing
    - Graphic design
    - User feedback
    - Repo admin
    - User help
    - Testing strategy

Other ongoing responsibilities for completeness (not suggested in email, but just putting here for reference since most are covered above)

- Release management
- Fundraising
- Team management
- Go to market

### Conclusion
We're trying to solve problems we had with a larger team, let's not implement this process right now and see how things go with some of the new meetings and workflows we're otherwise adopting. If too many people being involved in decisions or decisions not being clear becomes a problem in the future, we will address it then.
