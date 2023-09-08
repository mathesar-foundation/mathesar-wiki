# 2023-09-06 team meeting

## Poll: Do we still want to give weekly project updates?

- **Allocated time**:  5 minutes
- **Added by**:  Sean

During the previous cycle, we agreed that project owners would send emails every Friday to update the developer list about project status. Do we want to continue that process this cycle, or abandon it?

Options:

- 📣 = Resume weekly project updates
- 🚫 = Abandon weekly project updates
- 💬 = Discuss it further

Votes:

- Anish -- ???
- Brent -- 📣
    - It's for the community, not really for us. I think we should do it in the interest of developing that community.
- Dom -- 💬
    - Ambivalent: Doesn't take much time, but doesn't derive benefit
- Ghislaine -- 🚫
- Mukesh -- 💬
    - Didn't find any reason to send an email in the initial weeks
    - Wants to send updates on his own cadence
- Pavish -- 💬
    - Doesn't think it makes sense for research projects,
    - Does think we should do it for development projects.
- Rajat -- 📣
- Sean -- 🚫

Decision: move updates to weekly on Monday


## Check in on progress for the cycle

- **Allocated time**:  15 minutes
- **Added by**: Sean

### Mukesh
- First week and half went well
- Got caught up with release deployment
- Lost few days trying to re-organize and catching up with others
- Back on track though with a delay of a two working days than what was initially planned
- Half way through the project. Documentation and frontend work is yet to be started. Design, Infrastructure and backend tasks are waiting for a review

### Anish
- Backend work mostly completed for installation improvements 0.1.4 just waiting for a review from Mukesh.
- GitHub action for adding static files to release also completed and waiting for a review from Mukesh.
- Currently working on migrating our internal db to SQLite.

### Brent
- Project started fine on W1, but then on W2
- I Got side tracked into Release, and then
- I Fell into a deployment vortex that went on and on.
- Regardless, progress is occurring on Pre-existing DB stuff; I'm currently still working on organizing the meta issue.
- We did manage to test some PostgreSQL versions. Results were comically bad.

### Ghislaine
- Completed design tasks that were needed for other projects. Did not follow up yet so not sure on completion status.
- Had niche research discussions but it feels like I won't be able to narrow down just by gathering information. Making a decision will require more team involvement.
- At this point I see no need for some originally planned niche research tasks. Like the collection of use cases outside of what we decide the scope will be.
- I'm blocked on publishing the survey.

### Dom
- Way behind, family life interfered
- No particular adaptation necessary, I'll just end up having done fewer backend "fixes"

### Pavish
- I felt like I didn't have enough to work on, for the first couple weeks.
- I'm mainly assiting with Postgres compatibility and Niche research projects. I still feel like I don't have concrete tasks to work on.
- Working on general stuff when I don't have specific project tasks.
    - Thinking on a bunch of stuff
    - Helped with some release work
    - Took some ad-hoc tasks
    - I'll also be upgrading packages and Node
    - A few reviews

### Rajat

- Was out for most of the time until this week.
- Positive for i18n & installations work. 
- Will start release work, early next week. 

### Sean

- I'm assigned to ad-hoc tasks
- Team management has taken more time than I planned for, so I haven't made much progress on ad-hoc tasks
- I didn't set clear goals for the ad-hoc tasks though, so I don't think I'm in danger of falling short of any goals. Rather, I just queued up a number of tasks in a priority order, and I'm continuing to work through them.


## Check in on longer email threads

- **Allocated time**:  10 minutes
- **Added by**: Sean

### Avoiding regressions, validating overall behavior (Brent)

- Seems to be some agreement, but no action plan
- Brent will write up a stub project, link to thread


### Quick User Check-in (Ghislaine)

- https://groups.google.com/a/mathesar.org/g/core-team/c/vbOS4LX4h94/m/QJjV2-nbBAAJ
- Sean has had lots of feedback, wonders if others have any
- Ghislaine is hoping Pavish will take a look at the PR
- Pavish agrees that the thred is not yet closed

### Product level permissions to account for related entities (Pavish)

- https://groups.google.com/a/mathesar.org/g/mathesar-developers/c/lhjFFGufbrI/m/4jSTD3BfAAAJ
- Thread has gotten into the weeds a bit. Do we want to continue in the weeds
- Brent/Pavish/Dom -- yes, let's continue the thread "in the weeds".
- We're viewing this as a "long running discussion in the background" and embracing continuing the discussion before formulating a project.
- Mukesh: Maybe we need "owners" for threads like this.
    - Pavish: sometimes it's tricky to assign an owner at the outset of a thread because the topic is so open-ended.

### RSQLA1 Retrospective

- https://groups.google.com/a/mathesar.org/g/mathesar-developers/c/nX6e-JhJPi8/m/kcQ9GvdVAAAJ
- Nobody has replied
- Brent would really like replies from Anish, Mukesh, Dom and anyone else who is interested
- Brent would like to continue with the next phases of the larger project. Feedback on this thread will inform future work.
- Brent would like feedback by 2023-09-15

## Niche Research Update

- **Allocated time**:  30 minutes
- **Added by**:  Ghislaine
- Participants: everyone

### Discussion Points

1. **Presentation of the Progression Model**
    - Presentation of the [progression model](https://hackmd.io/@mathesar/rk4qAhBRn) and its potential role in shaping our product strategy.
    - Sharing the rationale behind the model.

2. **Team Dialogue**
   - Team discussion on the model's viability in guiding our product strategy.


### Notes

- Each unique path is quite restrictive
- Looking at targeting specific industries where the need is greatest
- Started to focus on how small businesses are using data across industries
    - Mostly using actual DBs for storing transactions
    - Not using DB for reporting tasks
- Small businesses have accelerated growth
- Have need for ad-hoc data modelling and querying
- Ghislaine thinks we should narrow to start ups with less-defined processes
    - Ad-hoc attitude towards modelling 
    - Ad-hoc attitude towards security
- Input will probably be in a denormalized format
    - how to work with modelled data?
- Rather than focusing on a niche as an industry, we ought to focus on a niche as a "stage of development" for a business
