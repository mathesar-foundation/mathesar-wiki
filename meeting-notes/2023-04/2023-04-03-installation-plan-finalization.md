---
title: 2023-04-03 Installation plan finalization
description: 
published: true
date: 2023-04-11T02:23:46.765Z
tags: 
editor: markdown
dateCreated: 2023-04-07T14:52:40.333Z
---

## Mukesh's reply to email:
* The documentation plan is same
* The install.py should be moved from startup script to the UI
* We need swiching databases

UI for switching database needs to be separate from installation.

## Configuring databases from UI:
* Kriti: What does it solve? How are we going to store credentials in DB with the security risks involved?
  - Mukesh: We require some plugin architecture to be solve the user requirement from the GH ticket. We should probably not store it in DB for now. For 0.1.2, it can be query string in each url, like a JWT with connection string, username and password.
  - Kriti: This doesn't seem related to installation but towards authentication.
* For installation, it's configuring databases and switching dbs.
  - We should do the switching databases.
  - Mukesh: We don't need UI for installing types. It is useful when adding a database without using the config file

## Plan for 0.1.2
* Documentation on setting up Mathesar with the Mathesar Service Docker Image
  - User will have to run install.py
* Documentation without using install.sh
  - Our own docker-compose services, without install script
* We're skipping UI for installing types
* Documenting our config files so user can manually edit them
* Documenting setting up Mathesar without Docker
* Documenting upgrades and changes in UI to add instructions for non-docker-compose environments
    - We'll repurpose https://github.com/centerofci/mathesar/issues/2646 for the UI instructions
* Consider removing interactive installer
  * We can defer removing it, but we'll document it's limitations i.e not able to support multiple DBs, is not flexible etc., Point users to documentations.
* Separate docker-compose file for production
  * User feedback from HN, not tracked at the moment.
  * We should separate dev docker-compose with prod.
  * We should probably have profiles for service+DB, and service+DB+watchtower+caddy
* UI for switching databases

## For 0.1.3 or later
* Helm chart
  * Kriti: Atleast we should test the initial version and maintain this, since a few people asked for this explicitly. Can't we automate this?
  * Mukesh: Automating & maintaining this is going to be extra work.
  * We'll try to check if we can hire someone from Upwork to do this.
* SSO related stuff
    - Fetching Db credentials from various source.
* Getting feedback from 0.1.2, and having a quick default way to install Mathesar.
  * We don't have enough information to do this for 0.1.2.
* Single Docker image for DB + webserver?
  * Kriti: Why are we deprioritizing this?
  * Mukesh: We could have two docker images, one with DB, one without DB.
- Create desktop packages / add to repos (.deb, flatpak, etc.)
* Consider simplifying config file - needs more discussion

## Testing
* We require people to test the installation options. We'd hire them from Upwork.
* We'll setup a channel in Matrix to do this.
  * Kriti will setup the channel.
  * Pavish will co-ordinate testing.
  * We'll perform testing after documentation is solid.
* We could have Marius take a second look at documentation.
  * Mukesh: This would be helpful.
  * Mukesh would provide a draft and Marius would look at it, detail and polish it.

## Release
* Mukesh will update the installation project
* Pavish will create a project for 0.1.2 and include switching dbs in the project
* We'll have the issues created, projects approved, 0.1.2 milestone cleaned up, and a deadline needs to be decided by the end of this week.
  * Time should include testing, post-test issues etc.,
