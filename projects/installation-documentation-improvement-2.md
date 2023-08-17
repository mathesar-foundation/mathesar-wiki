---
title: Installation Improvement Part 2
description: 
published: true
date: 2023-08-17T09:46:04.548Z
tags: 
editor: markdown
dateCreated: 2023-08-17T09:41:23.712Z
---

**Status**: Draft

## Team
| Role | Assignee |
|-|-|-|
| **Owner** | Mukesh |
| **Backend Helpers** | TBD |
| **Frontend Helpers** | TBD |
| **Design Helper** | TBD |
| **Design Reviewer** | TBD |
| **Backend Reviewer** | TBD |
| **Frontend Reviewer** | TBD |

## Problem

Our current documentation includes a lot of unnecessary information and does not align with the proposed Installation flow


## Solution

Reorganise our current documentation based on [agreed outline](https://wiki.mathesar.org/en/meeting-notes/2023-07/2023-07-28-installation-meeting.md#table-of-contents) targeting [these](https://wiki.mathesar.org/en/meeting-notes/2023-07/2023-07-28-installation-meeting.md#do-the-personas-make-sense-do-we-need-any-additional-narrowing-down-or-clarification) personas

### Homepage
- Introduction & Overview 
    - Content: homepage of docs.mathesar.org
    - Remains the same
- Installation 
    - We will be replacing the current Installation section in the homepage of docs.mathesar.org and the related navigation section with the following installation options. Each installation option will point to the content page
    - Install with Docker
        - Content: [Single image Docker](#install-with-docker)
        - Note: We will provide a single Docker image which comes in-built with Postgres server. The Postgres server won't be started if the user configures Mathesar to use an existing database as its internal database
        - Persona: Try it out quickly locally [TOP]
        - Persona: Someone installing on a remote system [TOP]
    - Install on [PaaS name]
        - Content: [Instructions for specific PaaS](#install-with-paas)
        - Note: By default, configured to be production ready.
        - Persona: Try it out quickly on a PaaS [TOP]
    - Install on Debian
        - Content: [Non-Docker install](#install-on-debian)
        - Persona: Someone installing on a remote system (Debian) [TOP]
    - Install as Python module from PyPI
        - Content: [Instructions for installing from PyPI](#install-as-python-module-from-pypi)
        - Persona: Someone installing on a remote system (non-Debian Linux) [TOP]
        - Persona: Someone installing server on localhost, but connecting to a remote DB [MEDIUM]
    - Install with Helm
        - Content: [Instructions for using Helm Chart](#install-with-helm)
        - Persona: Install on existing infrastructure [MEDIUM]
- Configuration
    - Environment (common for all installation options)
    - Connecting to DBs on localhost

##### Pattern for the content page (for the reader; not part of outline)
We will follow the below pattern to keep the documentation consistent and easier to maintain. We will be using the terminology introduced in 
- Pre-requisites
- Installation
  - Install steps 
  - Pre-install config options will be shown as a tip or a warning.
    - As these steps should be done before starting Mathesar, we need to make sure the user knows about these steps and takes an informed decision before proceeding further.
    - The description is meant to be brief and will point to the actual content which will be under the "Next steps to take" Mathesar section
  - Setup steps
- Next steps to take
    - Post install non-mathesar config options
      - Only the information on why and how to configure using the UI
    - Use case based configurations
      - Groups multiple configurations to fit into a use case which helps the user take an informed decision
        - Use case (ex: Setting up for production, automatic updates)
          - Description on why it is needed
          - Points to the relevant section in the Configuring Mathesar. Can point to multiple configuration options (use env variables, access Mathesar using a domain name)
- Administration
  - Update process
  - Configuring Mathesar
    - Post install Mathesar config options
      - Inform users to restart Mathesar after making changes
    - Pre-install config options
      - Inform users of data loss or unexpected state if these configurations are changed after using Mathesar
  - Uninstall process

### Content Page
##### Install with Docker
- Pre-requisites:
    - Install Docker
    - Root access if you're on Linux
- Steps:
    - Single docker run command (Install)
        - Mount a volume to store information in the default location used by Docker
        - Tip where we explain how to configure for production use (Pre-install config)
            - Set secret key as environment variable 
            - Use a separate database for storing mathesar metadata etc
    - Set up superuser through UI (Setup)
- Next steps to take (Post install config)
  - Set up additional DBs through UI
  - Set up a update server
  - Set up for production server
    - Use environment variables. Point to "Configuring Mathesar" section
- Administration
  - Configuring Mathesar
    - Platform specific configuration instructions
    - Point to "Environment variables" page
  - Uninstall process
- Implementation details (for the reader; not part of outline)
  - The docker image will come with an in-built Postgres server, where the internal and user database will be created by default unless the user configures Mathesar to use a remote database
  - The in-built Postgres server won't be started to save resources if the user has configured Mathesar to use a remote database


##### Install with PaaS
- Pre-requisites:
    - Have an account on the PaaS platform (Depends on the platform, some platforms **might** allow you to set up without an account)
- Steps:
    - Click the one click deploy button or click on the Mathesar app on the app store which will install Postgres server along with Mathesar server (Varies based on the platform)
    - Set up superuser through UI
- Next steps to take
  - Set up an automatic update process
- Administration
  - Configuring Mathesar
    - Platform specific configuration instructions
    - Point to "Environment variables" page
  - Uninstall process

##### Install on Debian
- Pre-requisites:
    - Postgres server
- Steps:
    - Add Mathesar repo to apt
    - Run `apt install` to install Mathesar
    - Run command to start the Mathesar executable
    - Set up superuser through UI
    - Set up user DBs through UI
- Next steps to take
  - Set up for production server
    - Use environment variables. Point to "Configuring Mathesar" section
    - Use Postgres server as the internal database
- Administration
  - Steps for updating
  - Configuring Mathesar
    - Platform specific configuration instructions
    - Point to "Environment variables" page
  - Uninstall process

##### Install as Python module from PyPI
- Pre-requisites:
    - Python Interpreter
    - Postgres server
- Steps:
    - Set up a virtualenv
    - Install using pip
    - Run command to start the Mathesar executable
    - Set up superuser through UI
    - Set up user DBs through UI
- Next steps to take
  - Set up for production server
    - Use environment variables. Point to "Configuring Mathesar" section
    - Use Postgres server as internal database
- Administration
  - Steps for updating
  - Configuring Mathesar
    - Platform specific configuration instructions
    - Point to "Environment variables" page
  - Uninstall process

##### Install with Helm
- Pre-requisites:
    - Kubernetes
    - Helm
    - Postgres server
- Steps:
    - Add Mathesar repo to helm repo
    - Run `helm install` to install Mathesar
    - Set up superuser through UI
    - Set up user DBs through UI
- Next steps to take
  - Set up for production server
    - Use environment variables
    - Enable ingress
- Administration
  - Steps for updating
  - Configuring Mathesar
    - Platform specific configuration instructions
    - Point to "Environment variables" page
  - Uninstall process