# 2023-11-08 Team meeting

## Progress check in

- No new updates on the 0.1.4 release, we're making progress
    - DB connections is now more clearly scoped
    - Sean would like remaining Installation work captured in tickets so that it's easier to manage the release
        - Brent will create the issues
- DB connections
    - Backend work is pending, Anish & Brent are working on it
        - Brent:
            - A proper remodel would take a lot of work, and would like a timeline of when we intend to release/get a clear idea of the scope
            - Long term, we're gonna get rid of this anyway, so it might make sense to not put a lot of effort into it
    - Design is complete. Frontend work is pending, blocked on backend
- Installation
    - Kriti would like to deprecate the guided script install
        - Brent agrees
    - Docker-compose deprecation needs to be addressed
        - Kriti doesn't want to deprecate this, Pavish agrees
            - Sean: We could remove it instead of deprecating
            - We'll be reorganizing this instead
            - Pavish: It'd be good to have a migration guide to inform the removal of MATHESAR_DATABASES env variable, and we could mention that guided install is no longer supported
        - Conversation tracked in email
    - Sean, Brent, & Anish will sync up on figuring out documentation work
        - Kriti might have some time to help too
- User research / help
    - Ghislaine is looking to adding a chat option on the website
    - Kriti will be taking a look at where everything's at during the upcoming week
    - Brent is working on figuring out infra stuff on AWS, to help users
    - Supporting Windows users?
        - We need to add a lot of documentation on it
- i18n
    - Pavish took over from Rajat last week
    - Needed to change the library since it didn't work with our translation service provider (Transifex)
    - Will take a few weeks to complete
    - Work is proceeding at a good pace
- Product / GTM strategy + hiring plan
    - Kriti hasn't worked on it this week, but she'll be focusing on it the upcoming week
- Beta
    - waiting until above items are done before focusing on this
    - use the document https://hackmd.io/xHWKXnMnRlyxYFt3XIzFQQ

## Product process

- **Added by**: Kriti 

In the last meeting, Sean brought up having a process to quickly move product work forward. When new work is proposed (either internally or externally):
- First we need to decide _if_ we want to do it
- Second we need to decide that we want to prioritize it, or do it _now_.

How should this work? Who should be involved?

### Pre-meeting thoughts From Sean

I mentioned two distinct processes that I want us to improve:

1. Our **"approval process"**: This is where we deicide _if_ we want to do something specified in a ticket. This process moves a ticket from `status: draft` to `status: ready`.

1. Our **"prioritization process"**: This is where we decide _when_ to do something. This process alters the milestone on a ticket, slating it to be completed for an upcoming release.

Generally, I think our prioritization process could use some honing, but I'd say it's actually working okay and might not warrant a team-wide discussion at this point.

**The approval process is what I want to discuss the most,** because our process here seems to be less specified than others.

Here are some examples of "draft" tickets which (as I see it) are currently blocked on this "approval" process. If we can figure out how to approve tickets like this, then in many cases we could open them up to community contributors to work on. Or, if we can figure out how to "reject" them, then we can reduce our queue while maintaining an archival log of our decision process.

- [Allow Typing Into Cells Once Highlighted](https://github.com/centerofci/mathesar/issues/3236)
- [Make navigation header behave more consistently](https://github.com/centerofci/mathesar/issues/3287)
- [Remove "Records will be repositioned on refresh" message](https://github.com/centerofci/mathesar/issues/3288)
- [Be explicit when displaying empty strings as cell values](https://github.com/centerofci/mathesar/issues/1373)

This is my main question:

- How do I determine which team members need to approve a ticket in order for the ticket as a whole to be considered approved?

Ideally we'd be able to codify a rubric that allows all team members to reliably and independently draw the same conclusions to that question. But I'm not seeing a simple path to such a rubric. For efficiency's sake, we ought to avoid requiring every team member to approve every ticket. But identifying a subset of our team to approve all such tickets risks omitting members who hold strong opinions or background knowledge on particular areas of the product.

This conundrum reminds me of this HN thread from last week: [The product manager role is a mistake](https://news.ycombinator.com/item?id=38058638). The article is, in my opinion, not very good. It makes some interesting points, but mostly seems to lament a dysfunctional dynamic present on some teams while failing to give pragmatic advice for better alternatives. I came away from the article perplexed. But after reading the HN _comments_, I began to reflect on the challenges we have in _our_ team making product decisions, and many of the comments refuting the article really began to resonate with me. This is all to say: I think we need some clarity within our team about who is responsible for these ticket "approval" decisions. For example, hypothetically our answer could be: _"Kriti (and only Kriti) is responsible for approving draft tickets"_. That would be fine with me. If we had that kind of clarity, then I would assign these "draft" tickets to her for her to review and approve. Then we could move them forward by approving (or closing) them. What's difficult for me currently is our lack of clarity on the process. Interestingly, I see that difficulty reflected in many of those HN comments arguing (against the article) that a "product manager" role is crucial for their teams.

### Discussion

- Kriti: for the approval process, I agree that having the entire team approve it is too much. And having only Kriti approve it is too limited. Maybe different "areas" of the product have different people responsible for approving tickets
- Brent: we might have "cracks" between different areas
- Brent: What's the problem with Kriti being the sole approver?
    - Kriti: I want to be able to go on vacation. Maybe I could delegate during vacation. Need to have a person with a lot of context. If we could try to document all that context, that would help. Maybe I'm responsible for everything and I try to document as I go.
    - Kriti: "context" here means that I know which team members will have opinions and experience to weigh in on specific tickets
    - Ghislaine: Maybe what we're calling context here is what people call an "epic" in the scrum model.
        - Kriti: worried that model might require too much bureaucracy for a team as small as ours.
- Pavish: just to be clear, anyone can weigh in on a ticket, right? Kriti: yes.
- Kriti: we might need to have some system of a "deadline" for weighing in
- Pavish: important for the implementer to have a stake in the approval process
    - Kriti: Tricky when community contributors are implementers
    - Kriti: somebody from engineering should be involved in approving all ticket
- Brent: somtimes the asynchronous nature of these decisions can make them drag on
- Sean: maybe a once per month meeting. 1hr max. Sean can curate a list of and send the list out ahead of time for people to  understand context and form opinions.
- Kriti: we could also use this meeting to close old tickets

### Conclusion

- **Decision:** Sean will coordinate meetings

## GitHub issues workflow

- **Allocated time**: 
- **Added by**: Sean

Potential questions (written by Kriti)

- What "jobs" are issues doing for us currently?
    - Tracking code-related work
    - Tracking non-code related work (design, product, infrastructure etc.)
    - A place for community members to leave feedback
    - Public product roadmap?
    - A place for contributors to find issues
- Issues vs. discussions
    - Should we use both?
- How should we track design issues in GitHub? 
    - What about frontend issues that include design spec?
- GitHub project
    - Should we be using this to track work?
    - What should our workflow be?
    - Who should be responsible for keeping it up to date?
- Repo admin priorities:
    - Respond to users ASAP
    - Keep the backlog "groomed"
- Cleaning up old issues
    - Should we do this now?

### Notes

Go-around style brain dump

Kriti:

- We're trying to do too muuh with issue. We should use issues only for code-related tasks. We shouldn't track workflow-related tasks in there (e.g. "shut down wiki serever")
- We should try to avoid placeholder issues. Users should be able to find issues easily. The more keywords the better.
- Hard for new contributors to find issues and have enough info to work on them.
- Nobody is really using the GH "project". We might have some opportunity to use it better
    - It could also help with prioritization
- Want to clean up old issues and good backlog.

Anish:

- Use issues for tracking code-related stuff
- If I don't know if it's viable, then I'll mention people in the comments and ask questions
- Other than code related issues, I don't know how useful GH issues are.

Brent:

- Agree with a lot of stuff Kriti said
- We're using GH issues for multiple things. I don't just mean code/non-code. The nature of the UI (and the fact that they can be submitted by anyone) mean that we get a lot of other disucussion in tickets. We have a process that assumes that issues are going to be a task to be done. Maybe we have other options like discussions, email messages.
    - Inadequate to just split into "feature"/"bug" dichotomy or "work"/"no work" dichotomy
- Should we be helping users find a different spot to submit questions and discussions? Or should we broaden our understanding of tickets to include discussions?
- We're using tickets for a lot of non-task things.

Ghislaine:

- Agreed with Kriti about design work maybe not having a place in GitHub
- Always feels kind of weird
- We used to have wiki spec added as a PR and have conversations there
- But email is better
- Figma comments are also good
- Design issues just stay blank
- But we don't have a project management / task management tool, this might fill that gap
- Ghislaine doesn't want to be out of the loop, she wants her work to be visible

Pavish:

- Pavish thinks most of his points are covered already
- Pavish hates the following:
    - Decision making issues: "Do we need this record re-positioning issues?"
        - Pavish doesn't know if he should ignore it or prioritize commenting on it, or do we even want to pick it up?
        - Also random people comment on it and say "I want to work on this"
        - Pavish may want to be involved, but it seems like a low priority
    - Long discussions in draft issues
        - If it's technical, it's fine
        - If it's fuzzy, e.g. "do we want to do this?"
        - Emails are better for this
- The above is not applicable to user-reported issues
- Pavish finds opening PRs way easier than creating issues
    - Unless issue needs to be visible to someone else
    - e.g. PRs for i18n, docker file
    - Stakeholders know about changes, why do we need an issue
- GitHub issues doesn't work for project tracking at all
- We need a different project / work tracking solution, not GitHub issues
- e.g. 1 meta ticket for i18n
- If there's only one reviewer, then it's more efficient to work 1:1
- For work visibility internally, we should use a project tracking solution
- Pavish only creates issues for things that we've already decided to do but can't do now

Sean:

- Likes GH issues
- inclined to use them for more things
- We should consolidate our workflow around that system
    - difficult to have mutually exclusive scope between different issues
- If we have things we _don't_ want to use issues for, we need to think about the scope of those other tools.
- GitHub Discussions is awfully implemented, really hard to use
    - real UX problems
- Discussions shine for Q&A for users
    - stack overflow model
    - we don't have a need for that kind of tool right now
    - we're using them as roadmap items, but those are tasks and make more sense as issues
    - questions, etc. are fine to be issues
    - maybe remove issue templates – barrier to create issue is very minimal, terribly worded, etc. is fine - good for our stage - we want people to interact with us
- Sean has specific things to change about how we do labels
    - That conversation isn't relevant now until we agree on the purpose of issues

Further discussion:

- Brent is also not of the opinion that we should use _only_ use issues for work tickets
    – just that we have set up processes around issues that assume they're work tickets
    - We should have a set of different process flows based on the nature of the issue (to keep us from trying to treat non-work-ticket issues as work tickets)
- Kriti: Seems like we have a dichotomy between two scopes: "external-facing" and "internal-facing". There are two separte things. Different granularity. We need more granular tracking for internal stuff than we do for external stuff. Maybe using project tracking software for internal stuff and use GH issues for external stuff.
- Kriti: slows us down to spec out tickets in detail sometimes.
- Pavish: seems like GH issues is designed for "extenal" use caess much more so than "internal" use cases


## DB connections implementation priorities

- Brent: right now have a `deleted` attribute. The front end uses this attribute to "hide" databases.
- Brent: Connections get marked as deleted after we're unable to connect to them one time. We don't have a way to "undelete" them. We need to remove this. It's going to be difficult to remove though. It's tangled up in huge swaths of the reflection code.
- Sean: can you put `deleted` on the new model and just have it always be false? Brent: no because this will have some perf drawbacks.
- Sean: mostly we don't want to _persist_ info about DB connection errors.
- We don't have a convincing use case for caching DB connection errors.
- Kriti: how many days to implement the "spackle"?
    - Brent: probably something we could get done early next week
    - Brent: we'll still have some spaghetti code that we'll need to remove eventually
- Anish: "deleted" has a lot to do with reflection, especially with regard to perf improvements within the context of needing to run reflection
- Kriti: we should decouple the frontend-blocking work from the larger architectural backend work. This way we can get the release out and deliver new features to users who are waiting on them.
