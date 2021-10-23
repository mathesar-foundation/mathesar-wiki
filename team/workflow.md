---
title: Mathesar Team Workflow
description: Description of Mathesar's product development workflow
published: true
date: 2021-10-23T19:12:46.622Z
tags: 
editor: markdown
dateCreated: 2021-10-23T18:29:01.610Z
---

Mathesar work happens on GitHub. We create GitHub issues to track everything we're working on for both design and code.

# Workflow

We track our tasks in the (private) [Mathesar GitHub project](https://github.com/orgs/centerofci/projects/1).
- The [Active view](https://github.com/orgs/centerofci/projects/1/views/1) lists everything that is currently in progress grouped by status.
- The [Backlog view](https://github.com/orgs/centerofci/projects/1/views/3) lists everything that is planned to be worked on by milestone.
- The [Future view](https://github.com/orgs/centerofci/projects/1/views/17) lists issues that we've created placeholders for to consider in the future. These issues are not actively planned to be worked on.

## Picking work

We do not pre-plan work. Team members are expected to pick up tasks as they have availability.

- Use the [Backlog view](https://github.com/orgs/centerofci/projects/1/views/3) to find tasks. Milestones are ordered and it's expected that we complete a milestone before going on the next one.
- See [Issue Assignment](/team/issue-assignment) for the processs of picking up an issue.
- Design work is usually a milestone or two ahead of backend work, which is usually a milestone or two ahead of frontend work.

# Resources

- [Mathesar repository](https://github.com/centerofci/mathesar)
  - [Mathesar GitHub Discussions](https://github.com/centerofci/mathesar/discussions): we discuss designs, code, and check in weekly here.
  - [Mathesar milestones](https://github.com/centerofci/mathesar/milestones?direction=asc&sort=due_date&state=open):  we track our roadmap using GitHub milestones
  - [Mathesar issues](https://github.com/centerofci/mathesar/issues)
  - [Mathesar pull requests](https://github.com/centerofci/mathesar/pulls)
- [Mathesar design prototype repository](https://github.com/centerofci/mathesar-design): The design team prototypes upcoming feature designs for Mathesar in this repository.
- We have forked [sqlalchemy-filters](https://github.com/centerofci/sqlalchemy-filters) to add some functionality.
- The [Mathesar Wiki](https://wiki.mathesar.org/) (this wiki) is our main knowledge base.

We try and keep our communication public. See:
- [Meeting Notes](/meeting-notes)
- [Community](/community)

## Private resources

These resources are only available to the Mathesar core or community team at the moment.

- [Mathesar GitHub project](https://github.com/orgs/centerofci/projects/1) that organizes our open issues
  - The project is only accessible to [Team](/team) members, but all relevant information (such as status, priority, and milestone) should be available on individual issues.
  - We will make this project public as soon as GitHub supports it.
- The [Mathesar Ansible repository](https://github.com/centerofci/mathesar-ansible) contains a playbook that deploys our staging server.
- The [Mathesar wiki repository](https://github.com/centerofci/mathesar-wiki) contains a copy of this wiki's content. Updates to the repo will reflect here.
- The [Mathesar "staging" server](https://staging.mathesar.org/) is a deployed version of the latest `master`. The username and password to access it are located in 1Password.
