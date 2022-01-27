---
title: Mathesar Team Workflow
description: Description of Mathesar's product development workflow
published: true
date: 2022-01-26T00:57:59.122Z
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

We do not pre-plan sprints. Team members are expected to pick up tasks as they have availability.

- Use the [Backlog view](https://github.com/orgs/centerofci/projects/1/views/3) to find tasks. Milestones are ordered and it's expected that we complete a milestone before going on the next one.
- See [Issue Assignment](/team/guide/issue-assignment) for the processs of picking up an issue.
- Design work is usually a milestone or two ahead of backend work, which is usually a milestone or two ahead of frontend work.

## Creating pull requests

- All pull requests should follow the [code review rules](https://wiki.mathesar.org/engineering/code-review).
- All external contributors need to open an issue first before creating a pull request.
- Team members are allowed to create PRs for minor changes without a related issue.

## In case of breaking API changes
This process is only valid until we have a first user.  Then, it should be reviewed.
- Try to implement API changes in ways that do not cause breakage.

In case that's unavoidable:

1. Finish the changes to the API, and open a PR.  This should be well documented, with a clear description of what the breaking changes are.
2. Contact a front end dev directly, and ask them to look at the PR.  At this point, they should just assess whether the needed front end changes are quick, easy, and feasible with a short turnaround time.
3. Go through the normal review process for the back end code and API form to the point where all are happy with the API response format.
4. If the front end devs are able to make appropriate front end changes easily and quickly, they should do so in the same PR.
5. If not (i.e., if front end devs are busy, if it's too complicated, or if the back end PR's unmerged state starts to block too many things): merge the PR with a big warning (i.e., a comment @'ing multiple people).
6. File an urgent bug describing the changes to the back end, and the needed changes to the front end.


# Resources
For a list of public repos and other resources, see [GitHub](/en/community/github).

## Private resources

These resources are only available to the Mathesar core or community team at the moment.

- [Mathesar GitHub project](https://github.com/orgs/centerofci/projects/1) that organizes our open issues
  - The project is only accessible to [Team](/team) members, but all relevant information (such as status, priority, and milestone) should be available on individual issues.
  - We will make this project public as soon as GitHub supports it.
- The [Mathesar Ansible repository](https://github.com/centerofci/mathesar-ansible) contains a playbook that deploys our staging server.
- The [Mathesar "staging" server](https://staging.mathesar.org/) is a deployed version of the latest `master`. The username and password to access it are located in 1Password.
- The [Mathesar private notes repository](https://github.com/centerofci/mathesar-private-notes) contains notes that are private to the core team.
- The [Mathesar scripts repository](https://github.com/centerofci/mathesar-scripts) contains a bunch of random scripts useful for Mathesar workflows.
