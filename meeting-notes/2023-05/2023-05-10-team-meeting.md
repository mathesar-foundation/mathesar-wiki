---
title: 2023-05-10 Team meeting
description: 
published: true
date: 2023-05-10T00:00:00.000Z
tags: 
editor: markdown
dateCreated: 2023-05-10T00:00:00.000Z
---



## GSoC proposal phase retrospective

- **Added by**: Dom
- **Summary**: During the proposal phase concerns came up and we postponed discussing them until now
- **Expected time**: 20mn
- **Priority**: Medium
- **Required participants:** Everyone who participated in the proposal phase
- **Additional participants:**: *Please replace this with your name if you're interested in participating*
- Goals:
  - Share whatever problems or ideas came up during the proposal phase;
  - Record that (including possible solutions to problems), so that they're available when/if organizing another GSoC.

```
Pavish
    - PR reviews
        - Not enough issues for contributors to work on
        - Allowing multiple contributors to work on the same issue
            - Too many PRs for the same issue
        - Especially a problem on the frontend
    - Sometimes would make changes to contributor's PR to get it mergeable
        - And so that our github repo would get contributor statistics
            - Github considers Mathesar to have another contributor
    - We need a better system for ranking/scoring candidates
    - Should rank also proposals that didn't have PRs

Brent
    - PR reviews
        - Problems stem from treating issues as try-outs that aren't actual work we need done
        - We should have agreement on when to cut off problematic PRs that require a lot of review/handholding
        - Too few issues for contributors
            - Main source of issues during proposal phase
    - GSoC motivates people to get into our codebase
        - People who aren't "scratching their own itch"
        - We don't get people that are "scratching their own itch"
        - Double edged sword
            - It's about managing the funnel
                - In GSoC, developers are the front-line for sorting out candidates
                    - Unnatural
                    - Normally, non-developers filter out 80% of candidates
                        - Then the remaining 20% is technical
                        - For us, 100% is technical
                            - Which is super noisy
    - Noise seems concentrated in the frontend
        - Even though projects we ended up getting good proposals for were for backend
        - Seems to happen all over open-source
    - Maybe have candidates find and solve a bug
    - Doesn't like the numerical scoring system
        - Different people grade on different scales
            - Hard to aggregate
        - Deceptively organized
        - Veto/neutral/sponsor is something to consider
        
Sean
    - PR reviews
    - We could do a retrospective of GSoC at the end of GSoC (end of summer)
    - Feels cynical
        - Example
            - 4 PRs for a single issue
                - 3 team members left 15 comments across them
                - at the end Sean submitted a PR himself
                    - took him 1 hour and Pavish didn't have critique
        - Hasn't seen the rewards of GSoC
        - Feels like a competitive classroom
            - As opposed to a community
        - GSoC sucks all of the good first issues
            - Makes them unavailable to contributors from outside GSoC
    - What are we open to considering changing (next year)?
    - Are there other ways we could evaluate candidates?
    - Ranking/scoring needs improvement, but went smoother than contributions
    
Kriti
    - Many ways to solve candidate evaluation
        - We could have a test that people have to take
    - Too much core team time spent on candidates that might not be interesting
        - Seen other projects not engage with people until they've done some work
    - At CC
        - Less noise
        - Maybe GSoC is different these days
    - A lot of people don't put in the minimum of effort
    - People wanting to put things on their resume is not bad
        - It's an exchange
            - Problem is if the candidate doesn't offer anything
        
Anish
    - Many people were trying to pump up number of PRs they had
        - A single person did 7 good-first-issues
            - Instead of doing more difficult issues
        - Or single person doing many issues simultaneously
        
Mukesh
    - Lack of documentation is a test for contributors
    - A lot of contributors seem to treat GSoC as competitive
        - GSoC is something you can put on your resume
    - There should be a progression from easy to hard issues
        - For each contributor
    - Maybe contributors should come up with suggestions or ideas
        - Kriti: we've had bad experiences with this
    - GSoC candidates are often on Windows
        - Causes many Windows-related issues
            - Distorts feedback space
            - Actual users might not be on Windows
        - Kriti: we should just take this into account when triaging issues
    - Unequal distribution of proposals for project ideas
        - Many strong proposals for the same project idea
            - But many project ideas didn't get almost any proposals
        
Ghislaine
    - Valuable contributors are those that actually want to add new features
        - They care
        - Sean:
            - 1 contributor on frontend that didn't come from GSoC
        
Survey
    - What percentage of time each of us spent on GSoC during the proposal phase?
        - Sean 60%
        - Pavish 50%
        - Kriti 20%
        - Mukesh 40%
        - Brent 20%
        - Anish 30%
        - Dom 100%
```

    
## General Q&A

- **Added by**: Kriti
- **Summary**: I'm around to answer questions about what I've been working on if anyone has any.
- **Expected time**: ??
- **Priority**: Low
- **Required participants:** No one


### Notes

- Mukesh: been talking to people doing "maptivism" (mapping + activism). They are interested in using Mathesar. They want to know our estimates for when/how we'll build more mapping features into Mathesar. They might be able to to help us get more funding. Met with three different people, three different projects. Marine life mapping, aggricultural mapping, etc.
    - Kriti: maybe introduce them to me? Location types would be a good thing to prioritize. Other people have said this. Lots of Postgres users because of PostGIS. Foundation of Public Code wants to use Mathesar for geospatial work.
    - Kriti: We don't have an estimate for when we'd have these features. We need to do more planning.
    - Mukesh: will follow up via email

- Mukesh: Any other ways we can help you, Kriti?
    - Kriti: most of my work right now is meetings and networking. Hard to parallelize. Talking to me about use-cases is helpful.


