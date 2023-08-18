---
title: Installation Improvement Plan 
description: 
published: true
date: 2023-08-17T11:50:00.303Z
tags: 
editor: markdown
dateCreated: 2023-08-17T09:41:30.671Z
---

**Status**: In review

## Team
| Role | Assignee |
|-|-|-|
| **Owner** | Mukesh |
| **Helpers** | Kriti |


This project contains the summarized plan to improve the installation, mostly based on the [ previous discussions](https://wiki.mathesar.org/en/meeting-notes/2023-07/2023-07-28-installation-meeting).
Implementing the planned changes will be done in separate projects
- [Installation Improvement 0.1.4](/en/projects/installation-improvements-0_1_4)

### Problems
1. Many users have found our installation process to be complicated, [this great feedback](https://github.com/centerofci/mathesar/discussions/3108) summarizes a lot of pain points.

### Reasons
1. We are targeting too many different use cases for Mathesar in our current documentation, which makes the documentation overwhelming for the user, and we need to simplify things.
2. Installing Mathesar involves many steps without any feedback or preventive checks in place, which makes the process brittle and introduces failure points that we can avoid. he user might miss out some steps and will be able to only notice it after completing all the installation steps.
3. There is too much configuration needed before Mathesar can be started, which makes it difficult to try Mathesar out quickly.
4. Configuration is done through scripts specific to certain installation methods, and not in the product itself, which makes some installation methods much more difficult, hard to give feedback. This also makes it hard to explain in the documentation in an intuitive manner.


### Targeted Personas

We discussed and agreed upon a [set of personas to target initially](https://wiki.mathesar.org/en/meeting-notes/2023-07/2023-07-28-installation-meeting#do-the-personas-make-sense-do-we-need-any-additional-narrowing-down-or-clarification)

Top
- Someone trying Mathesar out quickly (and can use Docker)
  - We assume this user is just evaluating Mathesar and will move to a different installation setup after evaluating.
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

### Limitations of the Project
- We won't be making any changes to other areas of the product like database permissions, updating packages. We will only be organizing our existing Installation process. The user need to be a `SUPERUSER` or be the `OWNER` of the database if they wish Mathesar to manage that database

### Terminology
- Internal database - Mathesar stores its metadata like `Exploration`, `Admin user` registration details in this database. 
- User database - These databases contain the data which the user wants to manage using Mathesar. Mathesar can manage more than one database at a time.
- Installing Mathesar Schema - Mathesar needs to install some SQL functions in the user database for it to function correctly. When the user does some operation using the Mathesar UI these functions are called by Mathesar to perform operations on the database. Additionally Mathesar offers custom types that don't exists on Postgres like `EMAIL` which can be used by the user.


### Possible lifecycle of Mathesar
1. Installing and setting up Mathesar App - User installs and sets up Mathesar as a functionally incomplete app (like hardware without software). It has no uses as of now as there won't be any databases managed by Mathesar at this point. We expect the user to perform these steps only once in the installation lifecycle. This happens only **once**
2. Configuring Mathesar - The user might want to make some additional configuration like connecting to an additional database, pointing a domain at the Mathesar server. The user might want to configure **more than once** and might not do it right after installation
3. Updating Mathesar - When we make a new release, the user will need to update Mathesar to use the new features. This can happen **more than once**
4. Uninstalling Mathesar - In some unfortunate circumstances, the user might uninstall Mathesar. This happens only **once**


***The installation plan is based on the assumption above. So please comment if you are not okay with the above assumption***

### Outline of the steps after the installation overhaul project
Please note, these steps don't directly correlate 1:1 with our installation documentation structure, rather the intent is to categorize based on the behavior of the steps and give an overview of the steps for easier understanding of how they affect the installation process. The documentation outline will provide detailed information of the steps involved with a particular installation type 

#### Installing Mathesar
The installation steps are grouped into three categories (ordered sequentially)
1. Install
   - This category includes steps for setting up the download source, fetching the necessary files (docker image, binary) and commands for installing and starting Mathesar.
   - Once these steps are complete, Mathesar will be running locally, and the user can open Mathesar by visiting a particular URL (defaults to http://localhost:8000)
   - The following defaults apply to all the installation type
     - A `SECRET_KEY` will be automatically generated and stored in the config file
     - An SQLite database file will be created and will be used as the internal database for storing the Mathesar metadata
   - For certain installation types, we might override the above defaults to provide a better default suited for that installation type. These will be mentioned in the [documentation outline](#outline-of-the-documentation)
2. Pre-install config
   - The defaults Mathesar come with might not suit every use-case. These are the **optional** steps that the user may need to perform to adapt Mathesar to their environment.
   - These settings are targeted towards technical users, mostly done using the command line, and it is assumed the user knows what he is doing
   - Note: They need to be **performed before starting and using** Mathesar.
   - Mathesar related is tightly tied to configurations in this step. The user should not expect to retain Mathesar data magically if he is pointing the internal database URL to a different database.
   - The following configuration steps fall into this category
     - Passing in their own secret key as an environment variable. 
     - Passing in the credentials of the database to be used as the internal database.
3. Setup
   - Once Mathesar is installed and running, the user needs to set up few things before Mathesar can be used.
   - These will be done using the Mathesar UI
   - The following configuration steps fall into this category
     - Setting up a Mathesar admin user

#### Post Install Configuring Mathesar
The installation steps are grouped into two
1. Post-install non-mathesar config 
   - These are optional steps that the user may need to perform to actually make Mathesar functionally complete.
   - These steps will be done using the Mathesar UI
   - Internal database will be used for storing the information (if any)
   - The following configuration steps fall into this category
     - Adding an external database credentials into Mathesar using the Mathesar UI. The schemas are automatically installed into the database when the credentials are added
2. Post-install mathesar config
   - These are optional steps that the user may perform to configure Mathesar.
   - Unlike the "Pre-install config" these are optional and can be configured even after using Mathesar after sometime
   - Unlike the "Post-install non-mathesar config", they cannot be configured on the fly instead the user will need to restart the Mathesar server for the effect to take place
   - The following configuration steps fall into this category
     - Whitelisting domains from which Mathesar can accept API requests.

#### Update process
- Update will most likely be a one or two-step process and will be quite similar to the steps in "Installing Mathesar". For example, if you had used `apt install mathesar` when installing, you would do `apt update mathesar`
- For certain installation types, optionally, we will offer a convenient way UI to let the user update from within the Mathesar app.
- We will automatically run the necessary database migrations, update Mathesar schema for the user databases managed by Mathesar without any user intervention

#### Uninstall process
- Remove the installed schema from a specific database - Removing the database from Mathesar will uninstall all the installed types from the user database
- Completely remove Mathesar - Remove databases first using the above step and then perform one or two steps specific to the installation type for uninstalling Mathesar completely 



### Outline of the documentation

## Proposed Outline
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
We will follow the below pattern to keep the documentation consistent and easier to maintain.

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
      - Warn users of data loss or unexpected state if these configurations are changed after using Mathesar
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
  
  
### Environment Variables
List of environment variables and descriptions

### Connecting to DBs on localhost
This will explain how to connect to localhost DBs if you're using Docker (content is already on docs.mathesar.org)

### Stuff we're removing from current docs (not part of outline)
- Guided script installation
    - plus appendices
- Docker compose installation
    - plus "customizing docker compose" page
- Install from scratch
- Administration section (uninstall & upgrade Mathesar)
    - It Will be folded into individual installation types