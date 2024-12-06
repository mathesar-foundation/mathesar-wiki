# 2024-07-24 permissions retrospective

**Attendees**: Mathesar maintainers

Let's talk about the product and design process for permissions - what went well, what didn't go so well, what can we learn from this process for future features?

## Notes written before the meeting

### Anish
- I'm happy that we finally came to a conclusion, it really felt like these discussions were never going to end.
- I really wish we had made incremental progress on permissions with each release rather than doing everything at once.
- Videos were super helpful for me to reduce the time required to understand the concepts clearly and concisely. I think we should do more of these for complex concepts.

### Pavish
* I'm happy with the final result.
* It took a lot of time to arrive at our result and often times it felt like I was not making any progress/working and that was frustrating. It felt like I was wasting a lot of time. It's hard to quantify product work.
* Balancing user friendly abstractions vs providing raw power vs representing things as they are, was a huge challenge. Not having direct user feedback & not knowing our user base meant we had to satisfy all of these for the broader set of possible users.
	- Once we reach the point after our beta and get that idea, I think our requirements would be clear for each feature.
* Initial group meetings were exhausting.
    - Explaining the entire thought process that went into a concept was quite hard and it wasn't possible in group calls.
    - Everyone approached the feature in a different mindset, which was great, but it also meant that I couldn't answer everyone in the way they approached the problem. 1:1s were more effective.
* Feedback that went in a different direction from what I had presented meant that I had to rethink a bunch of stuff to tie the user flow together and go through loop of presenting it to the team again. This is good. The problem was that, with the new concepts, I received completely opposite feedback from what everyone had communicated in the previous meetings. I had to keep going back to square 1 every time this happened.
* Documentation took a lot of time and did not yield the team understanding I expected out of it. In contrast, designs were way useful in getting the ideas across.
* 1:1s were way better than group calls, but this lead to people still having different ideas in their minds and the final group calls revealed issues and we had to rework on the concepts.
    - I still think this was better and way less time consuming than having group calls every time.
* I realized running meetings was a skill of its own and it's a hard skill to master.
* Discussing raw concepts was very hard since they were fluid and I wasn't entirely confident and opinionated on the raw concepts themselves and my only focus was on the user experience. It was the opposite of discussing code related work and it took a while to get used to.
* We encountered additional things we hadn't thought of in the design sessions, even after agreeing on the product spec. Often times in the design process with Ghislaine, we both felt pessimistic and had to pull back from feeling that.
* Shout out to Ghislaine for bearing with me in the entire set of initial design sessions and for coming up with great designs. The process was mentally draining.

### Kriti
- I think we ended up with a great result.
- Pavish did a great job driving the project forward - it's hugely complex and unique and creating a user-friendly AND Postgres-compatible permissions system is amazing - no one else is doing this.
- I also want to recognize Pavish for being so open to feedback without being defensive, what we started with was very different.
- We did take a long time and I know the process was opaque and frustrating at times – what can we learn from that?
- This process made me realize how much stuff goes into project / product / team / meeting management that I didn't know I knew.
    - Upcoming hire should increase capacity for this.
    - I'd like everyone to develop this experience with more support than I was able to give Pavish, but not sure if that's feasible at our stage.

### Ghislaine

- It was stressful to feel that design was the bottleneck, even though it depended on more people in the team. Sometimes there wasn’t much to do other than trying to push the ideas forward.
- Design sessions were extremely helpful. I was very happy to have a more participative process.
- I really like our current solution. It does a good job reflecting what’s really happening at the database level while bridging the gap with less technical users.
- Even though I understood the technical aspects of roles, many scenarios eluded me, and it was frustrating to run into them during the development of design ideas. I’m not sure how this could be improved. Maybe a more divergent process at the start without thinking about the design itself.
- Shout out to Pavish for his help in navigating through the messy part of the process.

### Brent

- Really excited about the end result
- I think we took a lot of time to get to the end result, though. 
    - We kept having "false agreement" where we (or some subset) thought things were decided, but then had to go back to that decision
    - I think I got pushed into starting from a back end perspective, but we seemed to get more agreement more quickly when we were going through actual UIs, then working back to models, etc.
    - I think we spent too much time overoptimizing with abstractions, straying from one of our core values, representing the DB state directly


## Discussion
*Much of the initial discussion reiterated the feedback above; that has been omitted from this section.*

- Permissions in Postgres are a difficult concept to grok, despite reading docs, nuances were not always obvious.
- The color coded specs were a good idea, neat and clever way to refer to ideas.
- Sean's work on user stories ultimately ended up not being helpful.
- We all agreed we took a lot more time than expected.
- The team had very different opinions on how to structure the work.
    - Sean wanted to start with database models.
    - Others wanted requirements, specs, UI.
- We need to ensure that the process has enough information for each team member to be able to understand and provide feedback on the idea.
    - We need to have a product process that supports this.
    - We need to have smaller phases that are more predictable.
    - We will discuss this further when we are building the next feature.
- It would've been helpful to provide more context on what was going on at the DB layer during meetings.

### Why did it take so long?
- Pavish's perspective
    - No clear requirements for the feature ahead of time.
    - A lot of information for one person to digest and propose ideas for.
    - Explaining concepts took longer than expected.
    - Team disagreed about more things than originally anticipated.
    - Feedback cycles were long - small amounts of feedback led to an additional week of work.
    - Contradictory feedback on the same decision at different points.
    - Group calls were not helpful, once we got to 1:1s, process went better.
- Brent's perspective
    - We are weak when it comes to making confident decisions
    - Not enough user feedback to rely on.
    - Not enough material at the top of the funnel.
    - Solving theoretical For future projects of this level of complexity, we should start with someone having a deep understanding and imparting it to others
    - problems, with different team members with different views on what the most important hypotheticals are.
    - All this makes decision making hard.
    - Having Pavish working on product model and Brent working on data model in parallel was difficult, conflicting ideas to resolve.
- Ghislaine's perspective:
    - Seconding Brent's perspective.
    - Our product has very different concepts, can't rely on existing UX from SaaS products
        - e.g. role groups
    - Hypothetical user needs complicated things, design was simplified by removing some of this.
        - e.g. nicknames for databases
    - Was surprised by the complexity of the work.
    - Moving parts were not anticipated ahead of time.
    - Would have been better to start with drawing UI based on Pavish and Brent's iddeas, would've given everyone more context.
- Sean's perspective:
    - Permissions has intrinsic complexity because of PostgreSQL, not in our control.
    - Would've helped to have a workshop on how Postgres permissions worked before reviewing any proposals.
        - Originally thought reading docs was unnecessary.
    - For future projects of this level of complexity, we should start with someone having a deep understanding and imparting it to others
    - We also had some "accidental" complexity based on features assumed early on
    - Start with a higher priority on simplification in the future, we simplified only at the end
    - Order of operations is a different ball of wax
        - Objectively, this slowed us down because we all had different ideas about the order in which we should do different things
    - We made a number of agreements which got subsequently unmade.
        - Different team members had different ideas about what had been agreed upon
        - This meant later we'd realize that we didn't actually agree on a given point
    - Didn't focus enough on resolving fundamental alignment issues at various stages.
        - e.g. Pavish and Brent not aligned on encapsulation around Feb/Mar
        - e.g. unique constraint debate when reviewing database models
    - We were not synced up on are understanding of agreements and this was a big reason for our delays.
- Kriti's perspective:
    - Team members approaching it from different focus.
        - Pavish: product concept first
        - Sean: data model first
        - Brent: needs to see the UI
        - Ghislaine: UX and usability concerns

### What do people need from the product process?

- Pavish:
    - Would like to see how the user is going to use the product on a daily basis and what features they will be using.
    - Important to agree on this first before worrying about the rest.
    - Would like clear target users to help make design decisions.
        - e.g. Some users understand roles and some don't
- Brent:
    - Seconding Pavish.
    - Even if we start with a hypothetical user, its important to start a process without thinking of what page they are on, or what features they will use, even if this is lower level.
        - As an engineering team we have a tendency to start product and design process at low level. Users don't want to create roles, they want to create and store data and retrieve, use and analyse it.
    - Having user stories should be a crucial part of the design process.
        - We had user stories for permissions, but too late in the process.
- Ghislaine:
    - Conversations about user perspective did happen, but late in the process (with Pavish and Kriti)
- Sean:
    - Generally has a clear process when designing a product feature on his owm, follows 5 steps:
        - Problem the user has
        - Product design (what can a user do with the product to solve the problem)
        - Data model
        - UX (Answering the 'how' question)
        - Graphic design (color, icons)
    - See Sean's designs specs on the wiki for examples.
- Anish:
    - We should prioritize dogfooding so that we can get user feedback from ourselves
    - (Team agreed this should be a priority once develop branch is working.)
- Ghislaine:
    - Agreed with Sean's separation of steps and the data model focused approach.
- Brent:
    - Going through the process via 'what can the product do" is a good approach. 
        - Has implications for the data model.
    - Doesn't make sense for one person to spec the data model on their own.
        - Data model and the product need to work together.
        - The same person should work on both.
    - We need to make sure we're collaborating in a way that makes sense.
- Pavish:
    - We should have discussions after implementation / release when we don't have clear requirements, see how users are actually using it.
- Kriti:
    - Commonalities that everyone is pointing out:
        - Lack of requirements, e.g. we didn't come up with the concept of ownership until late in the process.
        - "What can the product do" is a discussion we need to have at the beginning of future projects.
        - User stories need to be integrated into our process.

### Wrap up
- We will circle back to this conversation closer to beta / after beta, when we are planning our next big feature.
- Foreign data wrappers and worksheets are potemtoal big upcoming projects (although not as complex as permissions)
- Meeting was useful to surface a bunch of things to help better our process, we will use the feedback to improve our process. 

## Retrospective summary

### What went well?
- Everyone is happy with design
- Lots of shoutouts to Pavish
- Shoutout to Ghislaine
- Color coded named specs were helpful to distinguish ideas

### What did we learn?
- Took too long.
- Process was frustrating, progress was hard to see.
- We didn't have a clear context of requirements or user audience.
- Let's not write up a bunch of documentation - spec didn't get the idea across effectively.
- Technical nuances are hard to learn while designing.
- 1:1s were better than group calls, still faster despite people not being in agreement.
- Feeling pessimistic can be part of the process.
- User stories were not useful for this process, despite initial thoughts / effort.
- We all had different opinions about how to structure the work. Strong opinions about how to approach the work.
- Videos were helpful for complex concepts
- Holding all of permissions in your head was hard, it was hard to weigh in when not everything was understandable.
    - Roles and permissions have less documentation at the DB layer too.
    - Providing concepts within our meetings would have been helpful.
    
### Why did it take so long?
- No requirements for the project.
- No target user in mind.
- We needed to come up with a bunch of concepts and problem and solutions that those concepts were needed for.
    - Problems were not always something the team agreed on.
- Getting the team to share a mental model took a while.
- Presenting concepts - feedback meant that Pavish needed a whole week to rework it into a new concept.
- We kept going back to ideas from previous concepts after they were rejected.
- Group calls were not helpful.
- We don't have a large number of users telling us what pains them, so we're in a weak position to make confident decisions, usually requirements are driven by user feedback.
    - Theoretical users with theoretical problems - everyone has a different view of this, and everyone is pretty experienced and opinionated.
    - Everyone has different hypotheticals based on past experience.
    - This seems likely to be a problem for future features e.g. merging table and exploration view.
- Getting elements from other SaaS products was not helpful since our product is not similar.
- Projects idea for UX was mainly to address Brent's idea of encapsulation.
    - Editing the password applies to all DBs - took two months to get there.
    - Not synced up on understandings of agreements.
- Product work vs. data model being developed separately was a big issue.
- All the moving parts were not anticipated ahead of time. Ghislaine being more involved in the beginning with visualizing things Pavish / Brent were discussing would have been helpful.

### What do people need from product / design process?
Product design vs. UX design - blurry lines, everyone is not on the same page. Different people need different things from the process to provide good input.

- Pavish
    - Have a good understanding of users
    - Understand user problems, solve problem in this particular way.
    - This is the way we direct the user to do it.
    - Think about UI problems from a user perspective.
    - We talk a lot, we could've just implemented something and waited for user feedback, pick up quick solution instead of before implementing it.
- Brent
    - Good understanding of users
    - As engineers, We think too low level, features, specific flows, what page they are when. What's possible on the DB, how they fit into what page into they're on.
    - Users don't want to create roles or create tables or read tables, they want to manage their sales process (e.g.) and protect their data.
    - User stories should be a crucial part of a healthy design process.
    - Personas. Sally wants to do X.
    - Person working on product spec should also do data model.
- Sean
    - Very clear process for Sean's brain.
    - Problem that the user has - can be user stories, can be inside the head.
    - Product design - what can the user do with the product to solve the problem.
        - e.g. Users can set Postgres roles to be owners.
        - People can associate Mathesar users with PostgreSQL roles.
    - Product design tightly integrated with data model.
        - That's why the focus was on encapsulation.
        - What question, not a how question.
    - UX - answering the "how" question.
        - UX questions fall into place more clearly once product design is done.
        - Modal, save button, etc.
    - Graphic design - colors, icons, etc.
    - New DB connection form spec followed this pattern.
        - Had a data model, the first thing presented in the spec. Problem and product design was not really specified since there was precedent. Then mockups with UX and graphic design.
- Anish
    - Seems like we want opinions from real users rather than hypothetical users.
    - We could use Mathesar in our team. Set up some kind of project that we can all use Mathesar for.
    - Coming up with concepts - help us with workflow.
- Ghislaine
    - Separation of steps like Sean mentioned.
    - Data model would have helped Ghislaine understand technical issues.
    - Boundary sounds useful.

### How do we structure future projects?
- We need to focus on requirements - how to get to clear requirements from nebulous ideas.
- We'll continue this closer to / after beta.
