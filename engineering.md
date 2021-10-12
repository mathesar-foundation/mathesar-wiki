---
title: Engineering
description: Resources and notes for Mathesar developers
published: true
date: 2021-10-12T22:05:02.266Z
tags: 
editor: markdown
dateCreated: 2021-04-20T16:15:59.765Z
---

Mathesar engineering work happens on GitHub. We create GitHub issues to track everything we're working on.

- [Mathesar code](https://github.com/centerofci/mathesar)
- [Mathesar GitHub Discussions](https://github.com/centerofci/mathesar/discussions): we discuss and document architectural decisions here.
- [Mathesar GitHub project](https://github.com/orgs/centerofci/projects/1) that organizes our open issues
  - The project is only accessible to [Team](/team) members, but all relevant information (such as status, priority, and milestone) should be available on individual issues.
  - We will make this project public as soon as GitHub supports it.

We try and keep our communication public. See:
- [Meeting Notes](/meeting-notes)
- [Community](/community)

We welcome new contributors! Please see [Contributing to Mathesar](/community/contributing) for more information.

# Process
- [:white_check_mark: Code Review *Code review guidelines*](/engineering/code-review)
- [:hospital: Issue Triage *How to triage new issues*](/engineering/issue-triage)
- [:bangbang: Common Issues *How to fix common issues in the code*](/engineering/common-issues)
{.links-list}

# Notes
- [:balance_scale: Engineering Decisions *Summary of major engineering decisions*](/engineering/decisions)
- [:classical_building: Architecture *Notes on Mathesar's technical design*](/engineering/architecture)
- [:books: Resources *Links to potentially interesting resources.*](/engineering/resources)
{.links-list}

# Stack
Mathesar is built using:
- [PostgreSQL](https://www.postgresql.org/) for the data storage
- [Python](https://www.python.org/) for the backend
- [SQLAlchemy](https://www.sqlalchemy.org/) to talk to the database
- [Django](https://www.djangoproject.com/) for the web application
- [Django REST Framework](https://www.django-rest-framework.org/) for the API 
- [Svelte](https://svelte.dev/) for the frontend
