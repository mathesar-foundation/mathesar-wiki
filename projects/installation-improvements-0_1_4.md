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
**Review status**: In Review

## Team
| Role | Assignee |
|-|-|-|
| **Owner** | Mukesh |
| **Backend** | Anish |
| **Backend Helper** | Mukesh |
| **Infrastructure Work** | Mukesh |
| **Infrastructure Helper** | Anish |
| **Frontend** | Rajat |
| **Design Helper** | Ghislaine |
| **Design Reviewer** | Pavish |
| **Documentation** | Mukesh |
| **Documentation Helper & Reviewer** | Sean |
| **Infrastructure Reviewer** | Brent |
| **Frontend Reviewer** | Pavish |


## Problem
Our current installation process is vastly aligned with the proposed [Installation Plan](https://wiki.mathesar.org/en/projects/installation-improvements-plan-0_1_4) for improving our installation flow. 

## Solution
We will be focusing on Top Priority Personas in this project. Please read through the [Installation Plan](https://wiki.mathesar.org/en/projects/installation-improvements-plan-0_1_4) and [this discussion](https://wiki.mathesar.org/en/meeting-notes/2023-07/2023-07-28-installation-meeting.md#what-work-do-we-need-to-do-to-enable-this-outline) to get a better idea of the proposed solutions

- Add Postgres to our docker image (Carried over from the [previous cycle](https://wiki.mathesar.org/en/projects/installation-improvements-0_1_3.md), needs testing before it can be merged)
- Create a Debian package (Partially complete, carried over from the [previous cycle](https://wiki.mathesar.org/en/projects/installation-improvements-0_1_3.md)
- User database configuration moved to the Mathesar UI
  - Only superuser can add a Database
  - The user database credentials set using the environment variable (in case of PaaS) will be read only. It cannot be modified using the UI 
- Remove the docker compose installation section and the related scripts
- Remove Build from the source installation section
- Add Install on Debian to our documentation

## Outcome
- 

### Tasks

### Backend Work (Anish)
- Create API to store the user database credentials in the internal Django database
  - The following information will be sent from the client
    - Unique name for the database
    - Database name
    - Database username
    - Database password
  - The database credentials other than the unique name should be encrypted using the `SECRET_KEY`
  - Mathesar schema (containing Mathesar types and schema) should be automatically installed into the user database when it is added to Mathesar
  - Can be added only by the superuser
- Create API to edit the user database credentials in the internal Django database
  - The following information can be edited
    - Database name
    - Database username
    - Database password
  - Can be edited only by the superuser
  - Database object from `MATHESAR_DATABASES` env variable should not be editable
- Create API to remove the user database credentials
  - Optionally, accept boolean to remove Mathesar Schema when the user database credential is removed from Mathesar
  - If the boolean to remove Mathesar schema is `True`, we should remove Mathesar schema first before removing the credentials from Mathesar
- Database credentials in the environment variable `MATHESAR_DATABASES` should be read and created when mathesar is started
  - These databases should be marked as readonly and cannot be edited using the UI
- Redirect the user to the database create page if no user database exists
- Remove the usage of `django.contrib.postgres.fields.ArrayField` so that we can use `SQLite` for the internal Mathesar database.
- Remove type annotations to get Mathesar working with a wide band of Python


### Design and Frontend Work (Ghislaine & Rajat)
- UI for getting the user database credentials from the user
  - This page falls into "Post-install non-mathesar config" will be initially visited i most cases after a superuser is created.
  - The page will be shown initially only if no database exists. The user won't be redirected to this page if a default user database exists (happens with Docker image, Paas installation method)
  - Only superuser can add database credentials
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
    - Database added using environment variables should not be editable and cannot be deleted
  - Success state: 
    - The database credentials are removed from the Mathesar
    - Mathesar schema is removed if the checkbox was ticked
  - Failure state:
    - We were unable to remove the Mathesar schema
- UI for listing the user database credentials from the user
  - List of all the user databases added to Mathesar
- UI for editing the user database credentials from the user
  - Database added using environment variables should not be editable and cannot be deleted

### Infrastructure Work (Mostly Mukesh unless specified)
- Add Postgres to our docker image ([Carried over from the previous cycle](https://github.com/centerofci/mathesar/pull/3121), needs testing before it can be merged)
- [Create a Debian package](https://github.com/centerofci/mathesar/issues/2765) (Partially complete, carried over from the previous cycle)
- Remove docker compose scripts
- Github Action to build static files during release (Anish)
- Host the Debian package on a server or consider using a Package repository like [Gitlab's repository](https://docs.gitlab.com/ee/user/packages/debian_repository/)


### Documentation Work
- Remove the docker-compose Installation section
- Update the Docker Installation section to not require Postgres server as a pre-requisite
- Remove Guided script installation
    - plus appendices
    - Point the user to use the deprecated docker-compose commands
- Deprecate Docker compose installation
    - plus "customizing docker compose" page
    - We will work on adding a migration script in later cycles to migrate the users to a different installation (most likely docker), for now the focus is not to have a new user look at this documentation.
- Deprecate Install from scratch. Add a note to redirect the user to use debian package (which is similar without information on compiling or setting up a reverse proxy, database, etc)
- Remove Administration section (uninstall & upgrade Mathesar)
- Add instructions for installing on Debian

### Discussion work
- Figure out where to host the Debian package on a server until we can get into the Debian official package repo. Possible options
  - [LaunchpadPPA](https://launchpad.net/ubuntu/+ppas) - Familiar to most linux uses. Dependencies are prioritized to use the same launchpad PPA and ubuntu repository, so there could be compatibility issues with Debian. We would need to test it on multiple distro
  - [Open Build Service](https://openbuildservice.org/) - Supports building for multiple distro (we don't need this because we are using docker to build our packages).
  - [Gitlab's repository](https://docs.gitlab.com/ee/user/packages/debian_repository/)
- Figure out as a team how we want to manage our DockerHub repo and tags - Some users want to use our features as soon as they are pushed into develop branch. Maybe we could set up a nightly build for such users
- Reassess Docker version requirements once we do a single Docker image

### Research Work
- Come up with a list of PaaS to support and get approval from the team

## Timeline

| Date | Outcome |
|-|-|-|-|-|
| **2023-08-21** | Backend and Design work for adding user database credentials using the UI starts |
| **2023-08-21** | Infrastructure work starts |
| **2023-08-21** | Send email for all the discussion work |
| **2023-08-25** | Debian package and Postgres docker image review starts |
| **2023-08-28** | Documentation work starts |
| **2023-08-31** | Backend and Design work for adding user database credentials using the UI will be completed |
| **2023-09-01** | Frontend work for adding user database credentials using the UI starts |
| **2023-09-08** | Github Action to build static files and hosting the debian package is complete |
| **2023-09-015** | Documentation is up for review |
| **2023-09-15** | Frontend work for adding user database credentials is complete |
| **2023-09-15** | Buffer of 1 week |

## Resources

- [Previous cycle project](https://wiki.mathesar.org/en/projects/installation-improvements-0_1_3.md)
- [Installation Plan](https://wiki.mathesar.org/en/projects/installation-improvements-plan-0_1_4)