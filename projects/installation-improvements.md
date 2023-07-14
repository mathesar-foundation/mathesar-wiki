---
title: Installation Improvements Project
description: 
published: true
date: 2023-07-14T13:09:58.235Z
tags: 
editor: markdown
dateCreated: 2023-03-15T20:52:47.673Z
---


**Name**: Simplifying Installation - Part I (2023-17-10)
**Status**: In review
**Previous Discussion references**: https://hackmd.io/i1hi188ETdq7AKeqD7-OKw

## Team
| Role | Assignee |
|-|-|-|
| **Owner** | Mukesh |
| **Backend Helpers**| Dominkyas |
| **Frontend Helpers**| Pavish |
| **Design Helper**| Ghislaine |
| **Backend Reviewer**| Brent |
| **Frontend Reviewer**| Rajat |
| **Contributors (ideation)**| Brent, Kriti, Mukesh, Pavish| Anyone else interested can join

## Targeted Persona
- Someone trying Mathesar out quickly (and can use Docker)
- Someone installing Mathesar on a PaaS
- Someone installing server & DB on same remote system
- Someone installing server & DB on separate remote systems

## Problem: 
  - There are too many steps involved in installing Mathesar
  - There are too many steps involved before Mathesar can be started
  - Some steps differ based on the installation method which makes it hard to provide a consistent experience
  - [Existing steps involved](#current-steps)

## Outcome: 
  - The number of steps involved in installing and starting Mathesar will be reduced
  - Some steps involved in setting up Mathesar will be moved to the UI so that they will be the same across all the installation methods. It also has the benefit of reducing the steps involved before starting Mathesar instead of having the user fiddle around with some command.
  - Configuration Steps which are blocked from being moved to the UI due to pending discussions will have a solution ready to be implemented in the next cycle
  - [Steps involved after this project](#expected-steps-after-this-project)

## Solution: 
  - Prompt the user to create a Superuser creation when starting Mathesar for the first time (Moves a configuration step to the Mathesar UI)
  - Build Mathesar + Postgres docker image (Reduces installation steps)
  - Build debian package (Reduces installation steps for non-docker)
  - Specify the correct permissions to use instead of asking for superuser privileges in our documentation([user reported fix](https://github.com/centerofci/mathesar/issues/2990))
  - Have meetings to figure out a plan for moving configuration to UI (Moves a configuration step to the Mathesar UI)
  - Research and have meetings for PaaS to support (Reduces installation steps)
  - Have meetings to figure out a plan for making Installation easier for all the targeted Personas

- **Lower Impact Solutions**: 

  **If there is more time left, we will focus on implementing these solutions**
    - Build helm charts (Reduces steps for Kubernetes)
    - Move documentation on auxiliary services(caddy, watchtower) to different docs (will be called as best practice guide)
    - Build zipapps(Reduces steps for non-docker non-linux installs)
    - Support SQLite as an additional datasource for the internal database (Makes it easier to start Mathesar for users without an inbuilt Postgres server package)


## Timeline:
Some work is done in parallel by different contributors. So I added the work that deals with multiple contributors (Superuser creation screen, meetings) on the left-hand side and the work done mostly my Mukesh (on the right hand sided). The meeting dates are tentative as it depends on everyone's availability

| Date | Outcome | Parallel work Date | Outcome |
|-|-|-|-|-|
| **20203-7-17** | Design work for superuser creation page begins|
| **20203-7-17** | Backend work for superuser creation page begins |
| **20203-7-18** | Meeting to discuss the location and workflow for storing  |
| **20203-7-20**| Superuser creation screen UI handoff |
| | | **20203-7-19**| Work for Mathesar .deb file begins |
| **20203-7-24** | Research on Paas solutions to support  |
| | | **20203-7-25**| Work for adding Mathesar + Postgres docker image begins |
| **20203-7-25** | Meeting to discuss Paas offering to support  |
| **20203-7-24** | Backend work for superuser creation page is completed  |
| | | **20203-7-26**| Script for generating Mathesar .deb file is completed |
| | | **20203-7-27**| Refactor the "Build from source" documentation to use the debian package instead of compiling Mathesar image|
| | | **20203-7-27**| Add Mathesar + Postgres docker image install instructions to our documentation|
| **20203-7-01** | Meeting to discuss Paas offering to support  |
| **20203-7-28**| Work on Django templates for superuser creation screen begins|
| | | **20203-7-31**| Work for Mathesar + Postgres docker image completed |
| **20203-8-03**| Django templates for superuser creation is completed  |
| | | **20203-7-02**| Time for the implementing lower impact solutions |


## High-level view of implementation details:
  - Superuser creation page - We will be using middleware to check for the non-existence of a superuser and redirect them to the superuser creation page which will be based on Django templates
  - Debian package will be created using [dh-virtualenv](https://github.com/spotify/dh-virtualenv). The script will build a python virtual environment for mathesar and will link to the system python. The implementation will closely follow [Synapse deb file build script](https://github.com/matrix-org/synapse/blob/develop/scripts-dev/build_debian_packages.py)
  - Mathesar + Postgres image will use our existing Mathesar docker image as a base and add PostgreSQL to the Mathesar + Postgres docker image
  - Zipapps will be built using [shiv](https://shiv.readthedocs.io/en/latest/)
  - SQLite codebase refactor is quite small as Mathesar uses a Postgres related field in only one place (for storing column order)

## User reported Issues which will be fixed in this cycle: 
- The Need for a debian package was reported on Hackernews
- [The requirement of superuser postgresql access is problematic](https://github.com/centerofci/mathesar/issues/2990)

## User reported Issues which maybe be fixed in this cycle: 
- [Helm Charts](https://github.com/centerofci/mathesar/issues/2633]
- [Kubernetes Manifests](https://github.com/centerofci/mathesar/issues/2707#top)
- [Consider merging `config` into `mathesar` package](https://github.com/centerofci/mathesar/issues/2712#top)

## Additional issues: 
It will be created once the project is reviewed




## References

### Current steps:
1. Pre-requisites before installing Mathesar
    <details>
      <summary>Docker Compose(1 step)</summary>
        - Install Docker
    </details>
    <details>
      <summary>Docker Image(3 steps)</summary>
        - Install Docker
        - Setup a database
        - Create a database superuser
    </details>
    <details>
      <summary>Building from source(3 steps)</summary>
        - Install Postgres
        - Setup mathesar database
        - Create a database superuser
    </details>


1. Downloading and set up Mathesar 
    <details>
      <summary>Docker Compose(2 steps)</summary>
        - Download docker compose script
        - Run docker compose command to download
    </details>
    <details>
      <summary>Docker Image(0 steps)</summary>
    </details>
    <details>
      <summary>Building from source(6 steps)</summary>
        - Clone git repo
        - Install python
        - Create virtualenv for python
        - Install python dependencies
        - Install nodejs
        - Build static files
    </details>

1. Configuring Mathesar
    <details>
      <summary>Docker Compose(6 steps)</summary>
            - Generate secret key
            - Add secret key to env file
            - Add internal database credentials to env file
            - Add user database credentials to env file
            - Create superuser
            - Run install script(migrations and install database types)
    </details>
    <details>
      <summary>Mathesar docker Image(6 steps)</summary>
            - Generate secret key
            - Add secret key to env file
            - Add internal database credentials to env file
            - Add user database credentials to env file
            - Create superuser
            - Run install script(migrations and install database types)
    </details>
    <details>
      <summary>Building from source(7 steps)</summary>
            - Add internal database credentials to env file
            - Add user database credentials to env file
            - Generate secret key
            - Add secret key to env file
            - Export environment variables
            - Create superuser
            - Run install script(migrations and install database types)
    </details>

1. Starting Mathesar

    <details>
      <summary>Docker Compose(1 step)</summary>
            - Run docker command
    </details>
    <details>
      <summary>Docker Image(1 step)</summary>
            - Run docker command
    </details>
    <details>
      <summary>Building from source(2 steps)</summary>
            - Create gunicorn systemctl script
            - Run the script
    </details>



### Expected Steps after this project:

1. Pre-requisites before installing Mathesar
    <details>
      <summary>Docker Compose(1 step)</summary>
        - Install Docker
    </details>
    <details>
      <summary>Mathesar docker Image(3 steps)</summary>
        - Install Docker
        - Setup a database
        - Create a database superuser
    </details>
   <details>
      <summary>Mathesar + Postgres docker Image(1 step)</summary>
        - Install Docker
    </details>
    <details>
      <summary>Building from source(3 steps)</summary>
        - Install Postgres
        - Setup mathesar database
        - Create a database superuser
    </details>


1. Downloading and set up Mathesar 
    <details>
      <summary>Docker Compose(2 steps)</summary>
  
        - Download docker compose script
        - Run docker compose command to download
    </details>
    <details>
      <summary>Both Docker Image(0 steps)</summary>
    </details>
    <details>
      <summary>Building from source-Debian(1 step)</summary>
  
        - Run apt install
    </details>
    <details>
      <summary>Building from source-Non-debian(1 step)</summary>
  
        - Install Python
        - Download zipapps
    </details>
   
1. Configuring Mathesar
    <details>
      <summary>Docker Compose(5 steps)</summary>
  
            - Generate secret key
            - Add secret key to env file
            - Add internal database credentials to env file
            - Add user database credentials to env file
            - Run install script(migrations and install database types)
    </details>
    <details>
      <summary>Mathesar docker Image(5 steps)</summary>
  
            - Generate secret key
            - Add secret key to env file
            - Add internal database credentials to env file
            - Add user database credentials to env file
            - Run install script(migrations and install database types)
    </details>
         <summary>Mathesar + PG docker Image(5 steps)</summary>
         
            - Generate secret key
            - Add secret key to env file
            - Run install script(migrations and install database types)
    </details>
    <details>
      <summary>Building from source(6 steps)</summary>
  
            - Add internal database credentials to env file
            - Add user database credentials to env file
            - Generate secret key
            - Add secret key to env file
            - Export environment variables
            - Run install script(migrations and install database types)
    </details>
   
1. Starting Mathesar

    <details>
      <summary>Docker Compose(1 step)</summary>
  
            - Run docker command
    </details>
    <details>
      <summary>Docker Image(1 step)</summary>
  
            - Run docker command
    </details>
    <details>
      <summary>Building from source(1 step)</summary>
  
            - Run the Mathesar executable
    </details>