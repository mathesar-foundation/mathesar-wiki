---
title: Installation Improvements Project
description: 
published: true
date: 2023-07-13T16:47:12.703Z
tags: 
editor: markdown
dateCreated: 2023-03-15T20:52:47.673Z
---

**(WIP)**

- **Roles**:

| Role | Assignee |
|-|-|-|
| **Owner** | Mukesh |
| **Backend Helpers**| Dominkyas |
| **Frontend Helpers**| Pavish |
| **Design Helper**| Ghislaine |
| **Backend Reviewer**| Brent |
| **Frontend Reviewer**| Rajat |
| **Contributors (ideation)**| Brent, Kriti, Mukesh, Pavish| Anyone else interested can join
 
- **Status**: Draft


- **Problem**: 
  - There are too many steps involved in installing Mathesar
  - There are too many steps involved in starting Mathesar
  - Some steps differ based on the installation method


- **Outcome**: 
  - The number of steps involved in installing and starting Mathesar will be reduced
  - Some of the steps involved in configuring Mathesar will be same across all the installation methods
  - Code examples for integrating Mathesar with other tools ike a reverse proxy, auto updater will be moved to the examples folder


- **Solution**: 
  - Prompt the user to create a Superuser creation when starting Mathesar for the first time (or until a superuser is created)
  - Build Mathesar + Postgres docker image (Reduces steps)
  - Build debian package (Reduces steps for non-docker)
  - Specify the correct permissions to use instead of asking for superuser privileges in our documentation


- **Lower Impact Solutions**: 

  **If there is more time left we can focus on implementing these solutions**
    - Build helm charts (Reduces steps for Kubernetes)
    - Move documentation on auxiliary services to different docs
    - Build zipapps(Reduces steps for non-docker non-linux installs)
    - SQLite support (For users without inbuilt Postgres server package)


- **Timeline**:

| Date | Outcome | Parallel work Date | Outcome |
|-|-|-|-|
| **20203-7-17** | Design work for superuser creation page begins|
| **20203-7-17** | Backend work for superuser creation page begins |
| **20203-7-20**| Superuser creation screen UI handoff |
| | | **20203-7-19**| Work for Mathesar .deb file begins |
| | | **20203-7-25**| Work for adding Mathesar + Postgres docker image begins |
| **20203-7-24** | Backend work for superuser creation page is completed  |
| | | **20203-7-26**| Script for generating Mathesar .deb file is completed |
| | | **20203-7-27**| Refactor the "Build from source" documentation to use the debian package instead of compiling Mathesar image|
| | | **20203-7-27**| Add Mathesar + Postgres docker image install instructions to our documentation|
| **20203-7-28**| Work on Django templates for superuser creation screen begins|
| | | **20203-7-31**| Work for Mathesar + Postgres docker image completed |
| **20203-8-03**| Django templates for superuser creation is completed  |
| | | **20203-7-02**| Time for the implementing lower impact solutions |

- **High level view of implementation details**
	- Superuser creation page - We will be using a middleware to check for the non-existence of a superuser and redirect them to the superuser creation page which will be based on Django templates
  - Debian package will be created using [dh-virtualenv](https://github.com/spotify/dh-virtualenv). The script will build a python virtual environment for mathesar and will link to the system python. The implementation will closely follow [Synapse deb file build script](https://github.com/matrix-org/synapse/blob/develop/scripts-dev/build_debian_packages.py)
  - Mathesar + Postgres image will use our existing Mathesar docker image as a base and add PostgreSQL to the Mathesar + Postgres docker image
  - Zipapps will be built using [shiv](https://shiv.readthedocs.io/en/latest/)
	- SQLite codebase refactor is quite small as Mathesar uses a Postgres related field in only one place(for storing column order)

- **Issues**: 


