---
title: Installation Improvements 0.1.4
description: 
published: true
date: 2023-08-17T09:45:43.722Z
tags: 
editor: markdown
dateCreated: 2023-08-17T09:42:41.660Z
---

**Status**: In Progress
**Review status**: In Review

## Team
| Role                                | Assignee  |
|-------------------------------------|-----------|
| **Owner**                           | Mukesh    |
| **Backend**                         | Anish     |
| **Backend Helper**                  | Mukesh    |
| **Infrastructure Work**             | Mukesh    |
| **Infrastructure Helper**           | Anish     |
| **Frontend**                        | Rajat     |
| **Design Helper**                   | Ghislaine |
| **Design Reviewer**                 | Pavish    |
| **Documentation**                   | Mukesh    |
| **Discussion**                      | Mukesh    |
| **Documentation Helper & Reviewer** | Sean      |
| **Infrastructure Reviewer**         | Brent     |
| **Frontend Reviewer**               | Pavish    |


## Problem
Our current installation process is not aligned with the proposed [Installation Plan](/engineering/specs/installation-improvements-plan-0_1_4) for improving our installation flow. 

## Solution
We will be focusing on Top Priority Personas in this project. Please read through the [Installation Plan](/engineering/specs/installation-improvements-plan-0_1_4) and [this discussion](/team/meeting-notes/2023/07/2023-07-28-installation-meeting/#what-work-do-we-need-to-do-to-enable-this-outline) to get a better idea of the proposed solutions

- Add Postgres to our docker image (Carried over from the [previous cycle](/projects/2023/07/installation-improvements-0_1_3), needs testing before it can be merged)
- Create a Debian package (Partially complete, carried over from the [previous cycle](/projects/2023/07/installation-improvements-0_1_3)
- User database configuration moved to the Mathesar UI
    - Only superuser can add a Database
    - The user database credentials set using the environment variable (in case of PaaS) will be read only. It cannot be modified using the UI 
- Remove the docker compose installation section and the related scripts
- Remove Build from the source installation section
- Add Install on Debian to our documentation

## Outcome
- Database credentials for user database can be managed using the UI instead of using env variables. This provides better feedback, decouples from Mathesar installation and lets the user configure without restarting the server
- Simplified installation which lets the user install Mathesar in a few steps. This also makes the installation documentation easier to parse for the user.
- We won't be bombarding the user with addon services or unnecessary configuration options

### Github issue
- [Meta issue](https://github.com/mathesar-foundation/mathesar/issues/3172)

### Discussion work
- Figure out where to host the Debian package on a server until we can get into the Debian official package repo. Possible options
    - [LaunchpadPPA](https://launchpad.net/ubuntu/+ppas) - Familiar to most linux uses. Dependencies are prioritized to use the same launchpad PPA and ubuntu repository, so there could be compatibility issues with Debian. We would need to test it on multiple distro
    - [Open Build Service](https://openbuildservice.org/) - Supports building for multiple distro (we don't need this because we are using docker to build our packages).
    - [Gitlab's repository](https://docs.gitlab.com/ee/user/packages/debian_repository/)
- Figure out as a team how we want to manage our DockerHub repo and tags - Some users want to use our features as soon as they are pushed into develop branch. Maybe we could set up a nightly build for such users
- Reassess Docker version requirements once we do a single Docker image


## Timeline

| Date | Outcome |
|-|-|
| **2023-08-21** | Backend and Design work for adding user database credentials using the UI starts |
| **2023-08-21** | Infrastructure work starts |
| **2023-08-21** | Start sending discussion related emails |
| **2023-08-28** | Debian package and Postgres docker image review starts |
| **2023-08-28** | Documentation work starts |
| **2023-08-31** | Backend and Design work for adding user database credentials using the UI will be completed |
| **2023-09-01** | Frontend work for adding user database credentials using the UI starts |
| **2023-09-08** | Github Action to build static files and hosting the debian package is complete |
| **2023-09-15** | Documentation is up for review |
| **2023-09-15** | Frontend work for adding user database credentials is complete |
| **2023-09-15** | Buffer of 1 week |

## Resources

- [Previous cycle project](/projects/2023/07/installation-improvements-0_1_3)
- [Installation Plan](/engineering/specs/installation-improvements-plan-0_1_4)
- [Project Feedback and Approval Thread](https://groups.google.com/a/mathesar.org/g/mathesar-developers/c/afuDFJAiK1Q)
