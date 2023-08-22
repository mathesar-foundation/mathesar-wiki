---
title: 2023-06-13 Installation Planning Meeting
description: 
published: true
date: 2023-07-19T23:34:49.257Z
tags: 
editor: markdown
dateCreated: 2023-06-15T18:52:57.263Z
---

Attending:
- Kriti
- Brent
- Mukesh
- Sean

Continued on 2023-06-14, Aritra and Anshuman also attended.

## Current install process

- Flowchart

    https://drive.google.com/file/d/1ZTVwCkGxv8jQMHH9IhsnMFd80P1HM5b9/view?usp=drive_link

## Examples of apps with nice installation
- [syncthing](https://github.com/syncthing/syncthing)
    - On Mac, drag and drop DMG
    - On Linux, available in package management repos
    - It's complicated – it's got a web server, electron app type GUI, web frontend, all sort of networking
    - You install it, it pops up a browser window or GUI
- [pgweb](https://github.com/sosedoff/pgweb) - single-file executable CLI to launch a webserver
- These are local though
- There's some unavoidable complexity with installations on servers
    - We need to make it safe to connect to the internet
- Brent: Would love to find good examples of python/django apps that have good installation flows
    - Baserow is an example
- Baserow's install seems simpler than ours, but less flexible
    - Does not need an external database by default

## Our needs
- Need "quick" install, just to try Mathesar, without lots of config
- Installation "personas":
    - Someone trying Mathesar out quickly (and can use Docker)
    - Someone trying Mathesar out quickly (and cannot use Docker)
    - Someone installing everything on localhost (no internet needed)
    - Someone installing server on localhost, but connecting to a remote DB
    - Someone installing server & DB on same remote system
        - DB created by Mathesar
        - DB already exists
    - Someone installing server & DB on separate remote systems
        - DB already exists
- Sean: do we want non-technical people to be able to install Mathesar any time soon?
    - Kriti: No. We can wait until post-alpha. Not a high priority now.

## Ideas

[Sean]
- Maybe Mathesar should not concern itself with supplying a Postgres server
- I'd really like to have a single-file executable someday

[Brent]
- All localhost, DB managed by Mathesar should be improved most (imo)
    - No config needed.
    - Should start things (maybe even in one container including DB) easily
    - Useful for real use cases, but also for 'trying it out'
- Trying Mathesar out ideas:
    - localhost/localhost, mathesar managed
    - improve demo, have separate users
    - PAAS
- Server and DB on separate systems (optimally with managed DB) is best for 'mission critical' prod right now. Consider emphasizing that.
- Segregate installation paths by use-case

[Kriti]
- Build static files before release
- Have a human readable config file that we do the work to convert (e.g. replace database url string with several different variables, we can convert it into a database URL)
- We need a single Docker command that just brings up a fully functioning Mathesar instance on localhost
- Users should not need to install git or check out our repo – we should release a downloadable version of our source code for a release on GitHub.
- PaaS options (e.g. "one click install on Dreamhost") would be helpful for trying out
- Helm charts / Kubernetes - make it easier to install Mathesar

[Mukesh]
- Build static files during release
- move config to UI
- move installing schemas to UI
- Build zipapps or binaries for Mathesar
- Generate secret key automatically
- Have a least resistance build without addons like Caddy
- One click installs
- Cpanel
- Debian Images, flatpak, native OS images

## Ideal installation flow by "persona"

### Someone trying Mathesar out quickly (and can use Docker)

- Kriti: This person is technical, since we're still in alpha. They're comfortable running a Docker command.
    - Brent: If they don't have Docker, then this is still a problem. People have more trouble installing Docker than they do installing Mathesar.
    - Mukesh: Maybe we should broaden our scope for "technical users"?
    - Kriti: people are technical but don't have time to tinker
- What is our ideal flow here?
    - Brent: `docker run`. Then it prints the URL to open Mathesar locally
    - Zero configuration, DB is automatically set up on the container
- Sean: Where would the user database live?
    - Within the container
- What if user wants to connect to pre-existing database outside the container?
    - We might be able to do this by passing more config into `docker run`
- Kriti: Can we have a config file to specify an external database?
    - This is hard with Docker
    - We could maybe do this with volumes
    - Mukesh: Why do we prefer config file vs env vars?
        - Something like YAML would be easier for users to edit
    - This would be **possible**, with some more thought/design
    - Kriti: Where would the config file live?
        - It would need to live in a volume. It would be accessed by both the host and the container
        - There could be some permissions issues
- Brent: There's also an `args` syntax for docker run that might be useful
- Mukesh: maybe we could stick with env vars but make improve the syntax so that it's easier for users to edit
- Brent: Env vars are not "durable". They don't persist after you restart your machine. This is harder for users. This is an argument for using a config file.

### Someone trying Mathesar out quickly (and cannot use Docker)
- PaaS "one click" is a way to do this
- Live demo
    - Why would people want to install Mathesar locally instead of using the demo?
        - Understand how Mathesar works with Postgres locally
        - Don't feel comfortable with uploading their data to the demo
- Ideas
    - Users should be able in:
        - Homebrew on Mac
        - Linux:
            - .deb repos
            - .aur for Arch
            - dpkg? 
    - Mac: DMG file / EXE files for Windows
        - e.g. OpenRefine, opens in a browser
- Where is the Postgres server?
    - Package manager installs would use Postgres
        - But user and database still need to be created
        - Seems like a non-starter for "trying Mathesar out"
    - Can we use SQLite as the Django database?
        - Worth considering, since it may not be that hard
    - Executable files
        - EXE files can have Postgres embedded, others cannot
        - https://github.com/garethflowers/postgresql-portable
- Should be one command
- Compile binary using pyinstaller
    - ships with Python interpreter
- Best we can hope for "someone trying this out quickly without Docker" is no Postgres server, but using SQLite for Django DB
    - We may need to require them to use an external Postgres server
    - Consider setting up server in the UI
        - Kriti: Where would we store pg passwords? It would be nice to avoid storing that along with our metadata.
            - Brent: Maybe it wouldn't be a problem. Maybe we could encrypt it.
            - Kriti: If we can find a way of storing it without putting it in plaintext (and with a good encryption algorithm), that would be fine.
            - Server could take API call and could also write it to a config file instead of storing in the DB
- Advantages of repo distribution over plain download (of an executable)
    - Fits into users' package management workflows
    - Better security peace of mind for users
    - easier to get in $PATH
    - easier to upgrade
    - smaller file size - no bundled dependencies
    - We can include postgres as a package dependency
- Advantages of plain download (of an executable) over repo distribution 
    - more up-to-date
    - simpler for us in the short term
- Additional args/flags that the CLI app could have
    - Option to disable auth, so that user can get to working Mathesar immediately
    - Option to permit the API/UI to edit the config file
- OS Dependencies
    - Minimum version of python
        - pyinstaller ships Python interpreter
    - Python dependencies
        - zipapp ships with dependencies
    - C build dependencies, unless we use the precompiled versions of psycopg
    - postgres server (minimum version)


## Ideal Flow
- Download the binaries from our release page
- Run the downloaded binary file using the cli or as a executable
- Mathesar will open in a browser window or an electron app
- Configuration dialog is shown inside the Mathesar app
- User creates a superuser account using the configuration dialog
- User is then shown a list of databases handled by Mathesar
- User proceeds to add the connection string details of the databases to be managed by Mathesar
- User then installs the necessary Schema based on the features he requires, for example, DML only schema


### Someone installing everything on localhost (not just trying it out)
- If you're using Docker setup:
    - May need to be a little different 
    - Docker volume needs to not be knocked out
        - Don't let Docker volumes be managed by Docker, use a directory
    - We should say this is NOT recommended for longer term Mathesar use
- If you're not using Docker:
    - This should be the recommended way to store Mathesar data persistently on localhost
    - "Ideal flow" should work well for this.
    - Config file being moved to the UI is the hard part of this.
- Should we even have the Docker version for this persona?
    - It will be easier for us, quicker to release

### Someone installing server on localhost, but connecting to a remote DB
- Theoretically easier if Django DB is on SQLite
- "Ideal flow" should also work well for this.
- Mathesar server is still on localhost, so security considerations with the remote DB are delegated to the user

### Someone installing server & DB on same remote system
- Mathesar needs to be accessible to the internet (also needed for collaboration)
- How do we handle security best practices?
    - Our own docs should be a reference
    - We can have step by step guides in a different section
        - This is an organizing principle 
        - We should not write a lot of guides, maybe just have one high quality one
        - We can link to community written guides as they emerge
    - e.g.
        - Synapse official docs: https://matrix-org.github.io/synapse/latest/setup/installation.html
        - Synapse guides: https://matrix.org/docs/guides/#installing-synapse
    - Docker lets us automate a lot of this - reverse proxy, port setup, etc.
- We should invest time into PaaS, this is a good way for people without time to install quickly
- Potential options:
    - Docker
    - From source
        - Use package managers
    - PaaS (Docker under the hood)
    - Ansible playbooks that the user can configure
        - Ansible would be automation of "from source"
- One Docker image that they run and have all the pieces in it
    - Comes with Postgres and Caddy
    - But domain and ports still need to be set up by the user
- We need to have a way for users to just get Mathesar up and runnng on a server with minimal steps
    - This will probably use Docker
    - PaaS fits here too
- We also need a way for users who want to customize Mathesar to have the information to do so.
    - This is probably the one high quality "from source" guide that we maintain
    - Would we want to use Docker Compose?
        - Brent: not really meant for prod container orchestration
- Not worth the time to build multiple Docker images with different configs (e.g. nginx and Caddy)
- Docker Compose is a third type of set up, probably not worth supporting since it's midway between "set and forget" and "configure everything", we shouldn't support this unless we have evidence that there's a whole bunch of users who need a middle option.

### Someone installing server & DB on separate remote systems
*Will be discussed at the next meeting*

### Someone installing Mathesar on a PaaS
- Options that our competitors support:
    - [NocoDB](https://docs.nocodb.com/getting-started/installation):
        - AWS ECS (Fargate)
        - GCP (Cloud Run)
        - DigitalOcean (App)
        - Cloudron
        - CapRover
        - Railway
    - [Baserow](https://baserow.io/docs/installation%2Finstall-with-docker)
        - Heroku
        - Render
        - Cloudron

*Will be discussed at the next meeting*

### Next steps and action items (2023-06-14)
- Should we wait until Kriti's back to have more meetings?
    - Yes
    - Kriti will schedule once she's back
- Next steps (for Mukesh) – in no particular order:
    - Research into shipping Mathesar as an executable
        - Write up summary
    - Research into supporting SQLite for Mathesar internal DB
        - Will be useful for multiple personas / installation types
    - Research feasibility of doing config through UI (from security perspective) 
        - How best to store config if we move DB config into UI
        - How to do this on a remote server (accessible to the internet) securely
            - maybe look at WordPress
    - Research how to make Mathesar work with different levels of DB user permissions
    - Building static files into release
- Note for Kriti: we need to also talk about upgrading Mathesar & Kubernetes / Helm charts (cloud based orchestration setups)

