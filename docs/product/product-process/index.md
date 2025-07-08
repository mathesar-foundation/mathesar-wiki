# Product Process

This document outlines the workflow for managing Mathesar’s product process--including [releases](#managing-releases) and [projects](#what-is-a-project)--guided by user needs, team expertise, and organizational goals.

## Key aims of this process

- Introduce a "minimum viable process" to enable faster feature implementation and meaningful impact to users.
- Reduce planning time lost to unclear goals and ownership without introducing bureaucracy or excessive process.
- Keep the effective parts of our current workflow. Discard what isn’t helping.
- Avoid writing code, automations, or introducing dependencies that make this process difficult to revert or revise.

### How do we know this process is working?

This process is viable if it helps us ship impactful work faster and with less friction. We’ll test it over a few release cycles and adapt quickly if it’s not delivering clear improvements. If it merely preserves the status quo, then it has failed.

---

## Managing Releases

Mathesar follows a monthly release cadence.

### Versioning

Mathesar follows a `MAJOR.MINOR.PATCH` versioning convention:

1. `MAJOR` version changes with a significant overhaul of the product
2. `MINOR` version changes with our standard monthly releases
3. `PATCH` version changes with big fixes

## Managing projects

Projects will *ultimately* live in a public roadmap powered by an internal Mathesar instance. Until we have the features to support such a workflow--shared views and comments, in particular--we use a [GitHub project board][project-board], aka the **Public Roadmap**, to track projects.

Each project is represented by a GitHub issue with a `type: project` label and added to the project board.

### What _is_ a project?

Projects help us organize meaningful improvements to Mathesar. A project is **any Mathesar initiative that benefits from the structured planning and collaboration of the project process**.

The product planning team is responsible for bundling app features and non-code work into projects. The project planning team factors in Go To Market goals, user feedback, and input from Mathesar maintainers into the scope and prioritization of projects.

Projects often span code, design, documentation, marketing, and community outreach, and typically involve collaboration across roles. They do not *exclusively* refer to features within the Mathesar application.

Projects should be trackable over time (generally longer than a week) and often involve multiple contributors.

### Project Lifecycle

Please see the [full project lifecycle here](./project-lifecycle.md). For convenience, here’s a one-line description of each phase:

* [Selection](./project-lifecycle.md#selection) \- How we determine potential projects
* [Ideas](./project-lifecycle.md#ideas) \- Likely projects that haven't been evaluated for feasibility or impact.
* [Upcoming](./project-lifecycle.md#upcoming) \- Projects we will do, approved for feasibility and impact.
* [Planning](./project-lifecycle.md#planning) \- Projects being specified for implementation.
* [In Progress](./project-lifecycle.md#in-progress) \- Projects under active development.
* [Shipped](./project-lifecycle.md#shipped) \- Projects that are completed.

## Process summary

The product planning team vets projects and writes project proposals to determine feasibility, scope, and goals. After a [review period](?tab=t.s84h49iau0op) project proposals are approved and projects are added to our backlog.

Each release cycle, the product planning team pulls projects from the backlog, and assigns a maintainer(s) to write necessary technical specifications. After a [review](?tab=t.s84h49iau0op) period technical specs are approved and projects are added to our “In Progress” list. Work begins.


### Public Roadmap

Mathesar’s public roadmap is maintained by the Product Lead, who checks daily for community input and updates (or lack of) from Mathesar maintainers.

The Product Lead monitors the [public roadmap][project-board] at the start, midpoint, and end of each release cycle as as a “dashboard” to inform some critical questions:

* Are we making progress on our current open projects?
* Are there any projects we need to put on hold, or expedite?
* Are any projects blocked or in need of major intervention?
* Are there any projects we need to start now, or soon, in order to meet our goals for the year?
* Are there any critical projects we are missing?

### Project Issues

Project issues are issues in the main Mathesar repository with special characteristics:

* The issue follows the [project issue template](?tab=t.gbwb7vmjjmm#heading=h.ssgo7o8tmd1s)
* The project label is applied to the issue
* A status is applied to the issue within our [Public Roadmap][project-board]

Think of these issues as "meta meta" issues that sit behind (or replace) the kind of meta issues we usually write ([example](https://github.com/mathesar-foundation/mathesar/issues/4509) and [example](https://github.com/mathesar-foundation/mathesar/issues/4303)). These project issues will serve as a central location where users and contributors can follow progress and share feedback.

[project-board]: https://github.com/orgs/mathesar-foundation/projects/2?query=sort%3Aupdated-desc+is%3Aopen
