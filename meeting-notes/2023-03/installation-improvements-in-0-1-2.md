---
title: Installation improvements planned for 0.1.2
description: 
published: true
date: 2023-03-27T15:25:03.541Z
tags: 
editor: markdown
dateCreated: 2023-03-27T15:25:03.541Z
---

# Installation improvements for 0.1.2

Attendees: Mukesh, Pavish

## Priority
- Documentation for setting up Mathesar using a Mathesar Service Docker Image
- Documentation for setting up Mathesar without using the install.sh script for docker-compose
- Documentation for setting up Mathesar without Docker
- UI for setting up/connection to user DB
    - Show in the UI for using the same django DB server to create new db if user wants to
    - Show an option to connect to different server 
- Mention in UI that we add custom types (optional) and casting functions (mandatory) in the user DB
- Update upgrade UI to mention instructions on how to perform an update in non-docker (docker-compose) environments
- Make our config file easier to for users to understand
    - This should no longer be a concern once we have the UI for installation

## Requires discussion
- Discuss storing connection string
    1. Stored encrypted and decrypted while making connection, or
    2. Connection through encrypted channel?
        - Setup is complicated
        - Requires changes to user db
- Create desktop packages / add to repos
    - Requires a lot of work and attention
    - Should we prioritize this anytime soon?
    - For 0.1.2, it's not possible
- Do we need an image for DB + webserver?
- Consider removing the interactive installer
    - Removing this would not a priority once documentation is updated for all setup options
- Use podman for Mathesar
    - Having a single Docker image should solve this. We can add documentation saying users can use either Docker or Podman
- Helm chart, Kubernetes manifest
    - Not possible for 0.1.2
    - Maybe as a community specified installation option

## Notes
- Marius Documentation https://github.com/mariusdebeer/mathesar/blob/master/docs/docs/installation/ubuntu-manual.md
- Add agenda to Wednesday meeting
