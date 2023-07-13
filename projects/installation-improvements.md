---
title: Installation Improvements Project
description: 
published: true
date: 2023-07-13T13:13:48.818Z
tags: 
editor: markdown
dateCreated: 2023-03-15T20:52:47.673Z
---

**(WIP)**

- **Roles**:

| Role | Assignee |
|-|-|-|
| **Owner** | Mukesh |
| **Helpers**| Dominkyas, Sean

 
- **Status**: Draft
- **Problem**: 
  - There are too many steps involved in installing Mathesar
  - There are too many steps involved in starting Mathesar
  - Some steps differ based on the installation method
  - We are also adding a lot of production addons to our Mathesar installation process instead of recommending it

- **Outcome**: 
  - The number of steps involved in installing and starting Mathesar will be reduced
  - Steps involved in configuring Mathesar will be same across all the installation methods
  - Code examples for integrating Mathesar with other tools like a reverse proxy, auto updater will be moved to the examples folder
  - Documentation which is not related to installing Mathesar will be moved to Best practices docs directory

- **Solution**: 
  - Prompt the user to create a Superuser creation when starting Mathesar for the first time (or until a superuser is created)
  - Build Mathesar + Postgres docker image (Reduces steps)
  - Build debian package (Reduces steps for non-docker)
  - Build helm charts (Reduces steps for Kubernetes)
  - Specify the correct permissions to use instead of asking for superuser privileges
  - Move documentation on auxiliary  services to different docs

  If there is more time left we can focus on implementing these solutions
    1. Build zipapps(Reduces steps for non-docker non-linux installs)
    1. Build static files and upload to release page (For users who wish to serve static files using a different service)
    1. SQLite support (For users without inbuilt Postgres server package)

- **Timeline**: TODO
- **Issues**: 
- **Themes**: User Experience and growth

