---
title: Installation Improvement Plan 
description: 
published: true
date: 2023-08-17T10:23:14.431Z
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

### Problems
1. Users are finding our Installation complicated

### Reasons
1. We are targeting too many different use cases for Mathesar in our current documentation, and we need to simplify things.
2. Installing Mathesar involves many steps without any feedback or preventive checks in place, which makes the process brittle and introduces failure points that we can avoid. Moreover the user might miss out some steps and will be able to only notice it after completing all the installation steps.
3. There is too much configuration needed before Mathesar can be started, which makes it difficult to try Mathesar out quickly.
4. Configuration is done through scripts specific to certain installation methods, and not in the product itself, which makes some installation methods much more difficult, hard to give a feedback and inconsistent.
5. This also makes the documentation harder to maintain since each installation method has very different steps.

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



### Possible lifecycle of Mathesar
These are the possible lifecycle
1. Installing and setting up Mathesar App - User installs and sets up Mathesar as a functionally incomplete app (like hardware without software). It has no uses as of now as there won't be any databases managed by Mathesar at this point. We expect the user to perform these steps only once in the installation lifecycle
2. Configuring Mathesar - The user might want to make some additional configuration like connecting to an additional database, pointing a domain at the Mathesar server. The user might want to configure more than once and might not do it right after installation
3. Updating Mathesar - When we make a new release, the user will need to update Mathesar to use the new features. This can happen more than once
4. Uninstalling Mathesar - In some unfortunate circumstances, the user might uninstall Mathesar. This happens only once

### Outline of the steps after the installation overhaul project
Please note, these steps don't directly correlate 1:1 with our installation documentation structure, rather the intent is to categorize based on the behavior of the steps and give an overview of the steps for easier understanding of how they affect the installation process. The documentation outline will provide detailed information of the steps involved with a particular installation type 

#### Installing Mathesar
The installation steps are grouped into three categories
1. Install
   - This category includes steps for setting up the download source, fetching the necessary files (docker image, binary) and commands for installing and starting Mathesar.
   - Once these steps are complete, Mathesar will be running locally, and the user can open Mathesar by visiting a particular URL (defaults to http://localhost:8000)
   - The following defaults apply to all the installation type
     - A `SECRET_KEY` will be automatically generated and stored in the config file
     - An SQLite database file will be created and will be used as the internal database for storing the Mathesar metadata
   - For certain installation types, we might override the above defaults to provide a better default suited for that installation type. These will be mentioned in the [documentation outline](https://wiki.mathesar.org/e/en/projects/installation-documentation-improvement-2)
   
2. Pre-install config
   - The defaults Mathesar come with might not suit every use-case. These are the **optional** steps that the user may need to perform to adapt Mathesar to their environment.
   - These settings are targeted towards technical users, and it is assumed the user knows what he is doing
   - Note: They need to be **performed before starting and using** Mathesar. Revisiting this step after using Mathesar for some time will lead to some unexpected state. For example, if the internal database URL is changed, the new database won't contain the old metadata information like `Column order` or `Explorations`.
   - The following configuration steps fall into this category
     - Passing in their own secret key as an environment variable. 
     - Passing in the credentials of the database to be used as the internal database.
3. Setup
   - Once Mathesar is installed and running, the user needs to set up few things before Mathesar can be used.
   - These will be done using the Mathesar UI-
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
     - Whitelisting domains from which Mathesar can accept API requests. Needed if Mathesar is exposed to the internet

#### Update process
- Update will most likely be a one or two-step process and will be quite similar to the steps in "Installing Mathesar". For example, if you had used `apt install mathesar` when installing, you would do `apt update mathesar`
- For certain installation types, optionally, we will offer a convenient way UI to let the user update from within the Mathesar app.
- We will automatically run the necessary database migrations, update Mathesar schema for the user databases managed by Mathesar without any user intervention


#### Uninstall process
- Remove the installed schema from a specific database - Removing the database from Mathesar will uninstall all the installed types from the user database
- Completely remove Mathesar - Remove databases first using the above step and then perform one or two steps specific to the installation type for uninstalling Mathesar completely 




In order to make the following changes, we will be making some changes to the codebase and updating our documentation. I have created two projects to track the necessary work
1. [Laying the groundwork for improving our installation process](/en/projects/installation-improvements-0_1_4) - This project involves all the code related changes. We won't be overhauling the documentation in this project, instead we will make enough changes just to keep the documentation updated based on the new features.
2. [Overhaul of the Installation documentation](/en/projects/installation-documentation-improvement-2) - We will be removing deprecated installation types, removing unnecessary information and reorganizing documentation in this project.


