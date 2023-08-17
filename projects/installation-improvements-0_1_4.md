---
title: Installation Improvements 0.1.4
description: 
published: true
date: 2023-08-17T09:42:41.660Z
tags: 
editor: markdown
dateCreated: 2023-08-17T09:42:41.660Z
---

**Status**: In progress
**Review status**: Approved

## Team
| Role | Assignee |
|-|-|-|
| **Owner** | Mukesh |
| **Backend Helpers** | Anish |
| **Frontend Helpers** | Rajat |
| **Design Helper** | Ghislaine |
| **Design Reviewer** | Kriti |
| **Backend Reviewer** | Brent |
| **Frontend Reviewer** | Pavish |


## Problem
Our current installation process is vastly aligned with the proposed plan for improving our installation flow.

## Solution

We need to make the following changes to our current installation process to keep it aligned with the proposed installation flow
### Backend Work
- Create API to store the user database credentials in the internal Django database
  - The database credentials should be encrypted using the `SECRET_KEY`
  - Mathesar types and functions should be automatically installed into the user database when it is added to Mathesar
- Create API to remove the user database credentials
  - Optionally, accept boolean to remove Mathesar Schema when the user database credential is removed from Mathesar
  - If the boolean to remove Mathesar schema is `True`, we should remove Mathesar schema first before removing the credentials from Mathesar
- Remove the usage of `django.contrib.postgres.fields.ArrayField` so that we can use `SQLite` for the internal Mathesar database.

### Design and Frontend Work
- UI for getting the user database credentials from the user
  - This page falls into "Post-install non-mathesar config" will be initially visited after a superuser is created
  - Help Text
    - Inform the user to provide a DB user with correct privilege(`SUPERUSER` or DB `OWNER`)
    - Inform the user that we will be installing Mathesar schema on the given database
  - The following information is needed
    - Unique name for the database
    - Database name
    - Database username
    - Database password
  - Success state: 
    - We were able to connect to the database and install Mathesar schema using the provided credentials
  - Failure state:
    - We were unable to connect to the database
    - The provided DB user does not have a privilege to install Mathesar schema in the database
- UI for removing the user database credentials from the user
   - The following information is needed
    - Checkbox asking if the user wishes to remove Mathesar schema
    - Help Text: Warn the user of potential data loss if the Mathesar custom types are used
      - "Deleting this schema will also delete any database objects that depend on it. This should not be an issue if you don’t have any data using Mathesar’s custom data types."
  - Success state: 
    - The database credentials are removed from the Mathesar
    - Mathesar schema is removed if the checkbox was ticked
  - Failure state:
    - We were unable to remove the Mathesar schema


### Infrastructure Work
- Get Mathesar working with a wide band of Python
- Create a Debian package (Partially complete)
- Create a PyPI package
- Create a helm chart
- Host the Debian package on a server or consider using a Package repository like [Gitlab's repository](https://docs.gitlab.com/ee/user/packages/debian_repository/)
- Github Action to build static files during release


### Research work
- Figure out as a team how we want to manage our DockerHub repo and tags
    - There are a bunch of different strategies
- Reassess Docker version requirements once we do a single Docker image
    - We only have a stringent version requirement because of Docker Compose, which we don't plan to use 
- Come up with a list of PaaS to support
