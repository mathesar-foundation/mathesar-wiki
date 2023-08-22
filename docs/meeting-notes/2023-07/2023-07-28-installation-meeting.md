---
title: 2023-07-28 installation meeting
description: 
published: true
date: 2023-07-28T15:15:16.432Z
tags: 
editor: markdown
dateCreated: 2023-07-28T15:15:16.432Z
---

# Links
- [Meeting notes: Parts I & II](https://wiki.mathesar.org/en/meeting-notes/2023-06/2023-06-13-installation-planning-meeting.md)
- [Meeting notes: Part III](https://wiki.mathesar.org/en/meeting-notes/2023-07/2023-07-06-installation-meeting.md)
- [Meeting notes: Part IV](https://wiki.mathesar.org/en/meeting-notes/2023-07/2023-07-11-installation-meeting)
- [2023-07 installation improvements project page](https://wiki.mathesar.org/en/projects/installation-improvements-0_1_3.md)
- [Mukesh's installation research](https://hackmd.io/SFWrMLWMR72P-iQ_M30JFA) (private)

# Pre-meeting prep
Please read the following proposed outline for the documentation

## Assumptions (for the reader; not part of outline)
- Users are comfortable with self-hosting, we do not need to educate them on self-hosting basics
- For PaaS
  - Considered to be used for production, so all best practices like using Postgres as internal db, env variables are used by default

## Table of contents
- Introduction & Overview 
    - Content: homepage of docs.mathesar.org
- Installation
    - Install with Docker
        - Content: Single image Docker
        - Note: We will no longer be offering a multi-container setup
        - Persona: Try it out quickly locally [TOP]
        - Persona: Someone installing on a remote system [TOP]
    - Install on [PaaS name]
        - Content: Instructions for specific PaaS, repeat this ToC item as needed for more PaaS
        - Persona: Try it out quickly on a PaaS [TOP]
    - Install on Debian
        - Content: Non-Docker install
        - Persona: Someone installing on a remote system (Debian) [TOP]
    - Install using Python binary
        - Content: `python mathesar.pyz`
            - We'll need to tell them how to connect to Postgres or install a Postgres server
        - Persona: Someone installing on a remote system (non-Debian Linux) [TOP]
        - Persona: Someone installing server on localhost, but connecting to a remote DB [MEDIUM]
    - Install with Helm
        - Content: Instructions for using Helm Chart
        - Persona: Install on existing infrastructure [MEDIUM]
    - [...same pattern will apply for future installs] 
- Configuration
    - Environment variables
    - Connecting to DBs on localhost

## Install with Docker
- Pre-requisites:
    - Install Docker
    - Root access if you're on Linux
- Steps:
    - Single docker run command
        - Mount a volume to store information in the default location used by Docker
        - Tip where we explain how to configure for production use
            - Set secret key as environment variable
    - Set up superuser through UI
- Next steps to take
  - Set up additional DBs through UI
  - Set up a update server
  - Set up for production server
    - Use environment variables. Point to "Configuring Mathesar" section
- Administration
  - Configuring Mathesar
    - Platform specific configuration instructions
    - Point to "Environment variables" page
  - Uninstall process

## Install with PaaS
- Pre-requisites:
    - Have an account on the PaaS platform (Depends on the platform, some platforms **might** allow you to set up without an account)
- Steps:
    - Click the one click deploy button or click on the Mathesar app on the app store which will install Postgres server along with Mathesar server (Varies based on the platform)
    - Set up superuser through UI
- Next steps to take
  - Set up an automatic update process
  - Set up for production server
    - Use environment variables. Point to "Configuring Mathesar" section
- Administration
  - Configuring Mathesar
    - Platform specific configuration instructions
    - Point to "Environment variables" page
  - Uninstall process

## Install on Debian
- Pre-requisites:
    - Postgres server
- Steps:
    - Add Mathesar repo to apt
    - Run `apt install` to install Mathesar
    - Run command to start the Mathesar executable
    - Set up superuser through UI
    - Set up user DBs through UI
- Next steps to take
  - Steps for updating
  - Set up for production server
    - Use environment variables. Point to "Configuring Mathesar" section
    - Use Postgres server as the internal database
- Administration
  - Configuring Mathesar
    - Platform specific configuration instructions
    - Point to "Environment variables" page
  - Uninstall process

## Install using Python binary
- Pre-requisites:
    - Python Interpreter
    - Postgres server
- Steps:
    - Download zipapp from our release page
    - Run command to start the Mathesar executable
    - Set up superuser through UI
    - Set up user DBs through UI
- Next steps to take
  - Steps for updating
  - Set up for production server
    - Use environment variables. Point to "Configuring Mathesar" section
    - Use Postgres server as internal database
- Administration
  - Configuring Mathesar
    - Platform specific configuration instructions
    - Point to "Environment variables" page
  - Uninstall process

## Install with Helm
- Pre-requisites:
    - Kubernetes
    - Helm
    - Postgres server
- Steps:
    - Add Mathesar repo to helm repo
    - Provide some adequate defaults such as enable ingress, internal postgres server to add to values.yml. This is similar to our existing docker compose `.env` file
      - Tip: Point to "Configuring Mathesar" section
    - Run `helm install` to install Mathesar
    - Set up superuser through UI
- Next steps to take
  - Steps for updating
  - Set up for production server
    - Use environment variables
- Administration
  - Configuring Mathesar
    - Platform specific configuration instructions
    - Point to "Environment variables" page
  - Uninstall process

## Environment Variables
List of environment variables and descriptions

## Connecting to DBs on localhost
This will explain how to connect to localhost DBs if you're using Docker (content is already on docs.mathesar.org)

## Stuff we're removing from current docs (not part of outline)
- Guided script installation
    - plus appendices
- Docker compose installation
    - plus "customizing docker compose" page
- Install from scratch --> renamed to "Install on Debian"
- Administration section (uninstall & upgrade Mathesar)
    - Will be folded into individual installation types

# Agenda

## Do the personas make sense? Do we need any additional narrowing down or clarification?

Top
- Someone trying Mathesar out quickly (and can use Docker)
- Someone installing Mathesar on a PaaS
- Someone installing server & DB on same remote system
    - Using Docker
    - Using Debian, but not Docker
    - Using some other flavor of Linux
- Someone installing server & DB on separate remote systems
    - same as above

Medium
- Someone installing server on localhost, but connecting to a remote DB
- Someone installing Mathesar on existing DevOps infrastructure
    - Helm, Kubernetes goes here

Not prioritizing at all - until more than one person asks
- Ansible / other automation guides
- Someone installing Mathesar on a remote system that's not Linux
- Someone who wants to build Mathesar from source
- Someone trying Mathesar out quickly locally (and cannot use Docker)

Discourage
- Someone installing everything on localhost (not just trying it out)

### Additional discussion
- What about people using load balancers?
    - This is outside Mathesar's purview, doesn't matter
    - PaaS probably covers load balancers anyway

### Conclusion
Personas are fine, see additional detail added above.

## Does the proposed outline make sense?

### Discussion
- "Install with Python binary" is a confusing header.
    - Maybe use "Install from binary"?
    - Maybe replace with PyPI installation?
        - This could lead to Python installation issues
        - Virtualenv needs to be set up
    - The persona we're trying to serve here is "someone installing on remote Linux server, non-Debian, non-Docker"
    - Are zipapps the best solution for this persona?
    - Brent & Kriti agree that they would probably ignore zipapps when consuming installation docs because they're not familiar
    - Lots of FUD about broken Python installs
    - We need to support a wider band of Python, `pip install` will work better
    - Synapse PyPI instructions: https://matrix-org.github.io/synapse/latest/setup/installation.html#installing-as-a-python-module-from-pypi
    - Conclusion: We'll replace this with "Install using PyPI"
    - We'll no longer be working on zipapps unless there's demonstrable user need in the future
- What we're removing:
    - Fine with removing Docker Compose & guided script
    - Might be useful to keep uninstallation & update in the sidebar
        - We'll keep the uninstall and update pages


## What work do we need to do to enable this outline?
- Get Mathesar working with a wide band of Python
- Create a Debian package
- Create a PyPI package
- We need to know what Postgres we support
- Move user DB management to the database, encrypted by secret key
    - Design work, UI work
- Helm chart work
- Superuser creation moved to the UI – already underway
- Make complete Docker image
- Figure out as a team how we want to manage our DockerHub repo and tags
    - There are a bunch of different strategies
- Reassess Docker version requirements once we do a single Docker image
    - We only have a stringent version requirement because of Docker Compose, which we don't plan to use 
- Building static files
    - If it's possible to build static files as part of the release assets in e.g. https://github.com/centerofci/mathesar/releases/tag/0.1.2, we should do that
    - Single source of truth for release assets
    - Debian package and PyPI can use this single source of truth
- Secret key generation
    - Docker should do this
    - Debian - post install script
    - Where should it live?
- Storing configuration
    - Do we want to even provide a Django settings file in our repo?
    - We ran out of time at this point
- Permissions
    - Should we create a DB automatically?
    - No time to discuss now

Mukesh will start separate email threads to discuss:
- Configuration
- Permissions

We'll try to get to a decision async and if we reach an impasse, we can set up another meeting.
