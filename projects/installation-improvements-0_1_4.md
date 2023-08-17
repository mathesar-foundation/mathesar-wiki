---
title: Installation Improvements 0.1.4
description: 
published: true
date: 2023-08-17T09:45:43.722Z
tags: 
editor: markdown
dateCreated: 2023-08-17T09:42:41.660Z
---

**Status**: Draft
**Review status**: Review

## Team
| Role | Assignee |
|-|-|-|
| **Owner** | Mukesh |
| **Backend** | Anish |
| **Backend Helper** | Mukesh |
| **Infrastructure Work** | Mukesh |
| **Frontend Helpers** | Rajat |
| **Design Helper** | Ghislaine |
| **Design Reviewer** | Kriti |
| **Infrastructure Reviewer** | Brent |
| **Frontend Reviewer** | Pavish |


## Problem
Our current installation process is vastly aligned with the proposed [Installation Plan](https://wiki.mathesar.org/en/projects/installation-improvements-plan-0_1_4) for improving our installation flow. Please read through the [Installation Plan](https://wiki.mathesar.org/en/projects/installation-improvements-plan-0_1_4) to get a better idea of the installation flow before continuing further

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
- Remove type annotations to get Mathesar working with a wide band of Python

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
- Add Postgres to our docker image (Carried over from the previous cycle, needs testing before it can be merged)
- Create a Debian package (Partially complete, carried over from the previous cycle)
- Create a PyPI package
- Create a helm chart
- Github Action to build static files during release
- Host the Debian package on a server or consider using a Package repository like [Gitlab's repository](https://docs.gitlab.com/ee/user/packages/debian_repository/)


### Discussion work
- Figure out as a team how we want to manage our DockerHub repo and tags - Some users want to use our features as soon as they are pushed into develop branch. Maybe we could set up a nightly build for such users
- Reassess Docker version requirements once we do a single Docker image
- Figure out where to host the Debian package on a server 
  - Consider using a Package repository like [Gitlab's repository](https://docs.gitlab.com/ee/user/packages/debian_repository/)

### Research Work
- Come up with a list of PaaS to support and get approval from the team


## Timeline

| Date | Outcome |
|-|-|-|-|-|
| **2023-08-21** | Backend and Design work for adding user database credentials using the UI starts |
| **2023-08-21** | Infrastructure work starts |
| **2023-08-25** | Debian package and Postgres docker image review starts |
| **2023-08-31** | Backend and Design work for adding user database credentials using the UI will be completed |
| **2023-09-01** | Frontend work for adding user database credentials using the UI starts |
| **2023-09-01** | Helm chart and PyPI package review starts |
| **2023-09-08** | Github Action to build static files and hosting the debian package is complete |
| **2023-09-15** | Frontend work for adding user database credentials is complete |
| **2023-09-15** | Buffer of 1 week for fixing any infrastructure or backend related work |

## Resources

- [Previous cycle project](https://wiki.mathesar.org/en/projects/installation-improvements-0_1_3.md)
- [Installation Plan](https://wiki.mathesar.org/en/projects/installation-improvements-plan-0_1_4)