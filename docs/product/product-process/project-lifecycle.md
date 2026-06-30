# Project Lifecycle

## Stages

- [Selection](#selection)
- [Ideas](#ideas)
- [Upcoming](#upcoming)
- [Planning](#planning)
- [In Progress](#in-progress)
- [Shipped](#shipped)

## Selection {#selection}

The "Selection" stage is where potential projects are explored for future development consideration. The objective of this stage is to add new projects to the "Ideas" stage.

Members of the product planning team can add potential projects to the "Ideas" column of the project board at any time, using their discretion. New ideas should be added to the bottom of the list, as draft items.

Ideas should *always* be informed by:

* User-submitted bug reports and feature requests
* Internally proposed ideas or experiments from maintainers
* Patterns in support conversations, user interviews, or analytics
* Competitor feature sets and market expectations

The product planning team will routinely review, prioritize or reject new projects from the "Ideas" list at the weekly planning meetings. We may also implement larger, dedicated sessions for product ideation at a quarterly or yearly cadence. When reviewing ideas the product planning team bundles different ideas into coherent projects based on how they map to user-facing value and existing product conventions.

## Ideas {#ideas}

Projects at this stage have been vetted by the product planning team as work we “should”, “probably will”, or “are likely” to do. They have not yet been prioritized, scoped, or formally assessed for feasibility. At this stage, the product planning team will prioritize ideas to be evaluated for requirements and feasibility. The goals of this stage are to:

* Ensure that the feature requests, bugs, and ideas grouped together during the “selection” stage form a coherent project that addresses specific use cases.
* Define those use cases through listed project requirements and user stories.
* Avoid being prescriptive about a specific implementation or solution, rather clearly define the problem and determine if it is worthwhile and feasible to solve.
* Provide succinct and sufficient context to allow someone to write a [project proposal](#guidelines-for-project-proposals) without having to read anything else.

### Guidelines for requirements documents

TBD. Will be informed by example requirements documents created by Zack and Kriti.

Review process
Requirements documents should be reviewed swiftly; either synchronously in a project planning team meeting or async within **3 business days of authoring**.

### After review

After approval, project requirements documents are merged into Mathesar’s Wiki and shared with the rest of Mathesar’s maintainers via an email to the “Developers” group. An update is provided on the project issue body linking to the requirements document. The issue body’s description is updated to provide a clearer definition of the problem being solved. Finally, the project issue is moved to the “Upcoming” stage.

If a requirements document is “rejected”, i.e., it leads us to believe a project can or should not be worked on, the project issue is closed. Depending on the rationale, linked issues and bug reports from users should be closed or moved to other projects. We can **not leave users without context** for why their problems were “rejected”, or worse, ignored.

## Upcoming {#upcoming}

This is our backlog of approved and vetted projects. This stage primarily serves as a community resource that lets users know what changes to expect in Mathesar. **This is extremely important.** Users use a project’s roadmap and upcoming features for many things:

* To decide if they can use a project *now* despite it lacking the features they use regularly
* To evaluate the health and longevity of a project
* To give feedback and input on the features they care about

As soon as the product planning team determines that we should start working on an Upcoming project, it is assigned to an engineer or designer for planning work and moved to the Planning stage.

In our regular Product Planning meetings, we will identify and assign projects to members of the product planning team and have a Mathesar maintainer write a [Project proposal](https://docs.google.com/document/d/1PWsKvO9TXolZc-9iEu-r6pLJMuXFgukiuNiHIILy08w/edit?pli=1&tab=t.gbwb7vmjjmm#heading=h.8wb2kb32b5pk).

Once a project proposal has been approved by its two reviewers (at least one reviewer must be a member of the product planning team), the author will update the project [issue body](https://docs.google.com/document/d/1PWsKvO9TXolZc-9iEu-r6pLJMuXFgukiuNiHIILy08w/edit?pli=1&tab=t.gbwb7vmjjmm#heading=h.ssgo7o8tmd1s) and move it to the “Upcoming” section, with the priority determined by the product planning team.

### Guidelines for project proposals {#guidelines-for-project-proposals}

The primary goals of this project proposals are that of discovery; uncovering assumptions we’ve made about the project’s goals and the proposed approach to meeting those goals. Depending on the project, this discovery process may weigh more heavily towards user behavior and desires; infrastructural and technical considerations; or towards team processes and execution strategy.

Project proposals must follow the [project proposal template](https://docs.google.com/document/d/1PWsKvO9TXolZc-9iEu-r6pLJMuXFgukiuNiHIILy08w/edit?pli=1&tab=t.gbwb7vmjjmm#heading=h.8wb2kb32b5pk) and should be delivered as Pull Requests to Mathesar’s Wiki. Proposal authors are not expected to *know everything* or have complete answers to all of a project’s questions; rather, they should ask questions directly in the document.

### Review process

Project proposals are open for a maximum two-week review period. In cases where relevant contributors are out or otherwise unavailable, or a proposal experiences low engagement (for a variety of reasons), proposal deadlines will be extended as necessary.

This process is meant to be rapid, intensive, and thorough. It is designed to catch blockers early and force maintainers to commit to solutions that meet the project criteria, even if there are speculative potential alternative solutions discovered later on. This doesn’t mean we can’t be adaptable to changing constraints; but it does encourage us to commit to a path without dwelling on other potential futures.

See more about the structure and guidelines for the [review process](https://docs.google.com/document/d/1PWsKvO9TXolZc-9iEu-r6pLJMuXFgukiuNiHIILy08w/edit?pli=1&tab=t.s84h49iau0op).

### After review

Finally, the project is merged and the project issue is given a substantial update. At this point, we should be able to fill in most project metadata and some additional details:

* Create GitHub issues for all of the necessary technical specs and link to them in the project issue body. This allows implementation plans to be assigned and scheduled properly alongside development work.
* Add the release number we are planning to include the project with. **This may not always be known, advisable, or possible.**

At this point, it may be relevant to share our intent to work on this project to a larger audience for feedback or to build excitement. It might *also* be a good time to connect with any existing users who have requested a feature and share the project details with them.

## Planning {#planning}

Projects in the planning stage are undergoing technical specifications or design mockups. Work *may* have started in *some* areas of the project, but if any part of the project is still under discussion it should remain in this stage.

Once a project has been fully planned and development can begin, it is moved to the In Progress stage.

### Guidelines for technical specifications

The goal of technical specs is to produce a discrete and ordered list of steps for implementing the project’s requirements. As much as possible, these steps should be organised into parallelizable work streams that *could be* distributed across multiple team members.

Technical specs share *some* philosophical goals with project proposals. They should seek to uncover and discover new or unforeseen details about a project.

Technical specs must follow the [technical spec template](https://docs.google.com/document/d/1PWsKvO9TXolZc-9iEu-r6pLJMuXFgukiuNiHIILy08w/edit?pli=1&tab=t.gbwb7vmjjmm#heading=h.kqil3wgeix05) and should be delivered as Pull Requests to Mathesar’s Wiki.

### Review Process

Technical specs will be open for a maximum two-week review period. In cases where relevant contributors are out or otherwise unavailable, or a technical spec experiences low engagement (for a variety of reasons), technical spec deadlines will be extended as necessary.

This process is meant to be rapid, intensive, and thorough. It is designed to catch blockers early and force maintainers to commit to solutions that meet the project criteria, even if there are speculative potential alternative solutions discovered later on. This doesn’t mean we can’t be adaptable to changing constraints; but it does encourage us to commit to a path without dwelling on other potential futures.

See more about the structure and guidelines for the [review process](?tab=t.s84h49iau0op).

### After review

Finally, the technical spec is merged into the wiki repo. Maintainers then create GitHub issues for all of the work identified in the spec. This process can be quite time-consuming for large projects. Generally, it makes sense to create issues in the order in which they must be completed; this allows work to begin if, for some reason, there is delay in creating issues for the work at the end of a project, or if earlier work *could* redefine later, dependent work.

It also, however, makes sense to prioritize issues that are “good first issues” and “help wanted” issues contributors outside of the core maintainers can help with.

Whenever possible, issues should be written so that an implementer can complete an atomic unit of work without needing to understand the full scope and technicalities of the project. The issue description should contain all necessary information to complete the issue. This should include linking to specific relevant sections of the existing technical spec(s).

## In Progress {#in-progress}

In progress projects are the ones we’re actively working on. Projects are likely to be in this stage longer than the other stages.

## Shipped {#shipped}

These are the projects we have shipped, in order of completion. After a project is completed the date it was launched should be added to the [issue body](?tab=t.gbwb7vmjjmm#heading=h.ssgo7o8tmd1s) and the project should be closed.

Finally, the team holds dedicated retrospective meetings \[TODO, add link to retro process doc when written\] after each release cycle. During those sessions we discuss any completed projects and reflect on this process with the goal of identifying improvements.
