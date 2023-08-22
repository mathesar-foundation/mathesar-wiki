# 2023-07-06 installation planning meeting

> See [this page](/meeting-notes/2023-06/2023-06-13-installation-planning-meeting.md) for notes on parts I and II of this meeting. 
{.is-info}

**Attendees**: Kriti, Brent, Mukesh, Sean, Pavish

## Links
- [Mukesh's installation research](https://hackmd.io/SFWrMLWMR72P-iQ_M30JFA) (private)

## Ideal installation flows by "persona"

### Someone trying Mathesar out quickly (and can use Docker)
- Discussed in previous meetings. Summary:
    - Ideal flow is single `docker run` command
    - New DB automatically set up on container
    - Provide option to change DB to remote
    - Some disagreement about where to provide the option to change
        - Env vars vs. config file vs. UI
        - What should be the source of truth?
- Notes:
    - Make it really clear what URL to use it.
    - Make it really easy to log in 
        - No solution presumed, could be token to set up first user, or automatically creating a user, or whatever.
    - Aside: token based auth will help with E2E tests later

### Someone trying Mathesar out quickly locally (and cannot use Docker)
- Summary of discussion last time:
    - PaaS could serve users here
    - Can potentially do Python zipapp, but Postgres is a problem
    - We'll need to ask them to use a remote Postgres server for a one click option
    - Ideal flow:
        - Download the binaries from our release page
        - Run the downloaded binary file using the cli or as a executable
        - Mathesar will open in a browser window or an electron app
        - Configuration dialog is shown inside the Mathesar app
        - User creates a superuser account using the configuration dialog
        - User is then shown a list of databases handled by Mathesar
        - User proceeds to add the connection string details of the databases to be managed by Mathesar
        - User then installs the necessary Schema based on the features he requires, for example, DML only schema
- From Mukesh's research:
    - Windows & Mac - it's possible to install Postgres, but it's not ideal because it's a background service
        - People complain about running background services
- We should find a way to run it on local Python intepreter 
    - Zipapp doesn't bundle intepreter, it just bundles dependencies
- Pyinstaller does bundle interpreter, but it does a lot of magic and is hard to get working
    - But Mukesh got Pyoxidizer and cx_freeze working
- People installing Python is a problem – lots of ways to install Python and many problems can arrive
- But Mukesh got the zipapp working
- Can enable a larger percentage of people using Mathesar if we can broaden what versions of Python we can work with

### Someone installing everything on localhost (not just trying it out)
- Summary from last time:
    - Docker: We should say this is NOT recommended for longer term Mathesar use because we cannot guarantee volume persistence and backups are hard
    - Not Docker:
        - Same as "ideal flow" above
- Ideal flow is the same, but we can assume they're willing to do more wrangling since they're not "trying it out quickly"
- Security considerations are lower - we may be able to skip some steps

### Someone installing server on localhost, but connecting to a remote DB
- Summary:
    - Theoretically easier if Django DB is on SQLite
    - "Ideal flow" should also work well for this.
    - Mathesar server is still on localhost, so security considerations with the remote DB are delegated to the user
- Security considerations are lower - we may be able to skip some steps
- Where do we store DB credentials for remote systems?

### Someone installing server & DB on same remote system
- Summary:
    - Mathesar needs to be accessible to the internet (also needed for collaboration)
    - Security is more important
        - Our docs should only document our options
        - Separate section for step-by-step guides about how to harden Mathesar overall
            - e.g., reverse proxies
    - Things start to get more complicated
    - Many more options
        - docker,
        - from source,
        - PAAS
        - Ansible
    - Production persona: minimal configuration
    - Customized production persona
    - One from-source guide with all information that they can modify if wanted
    - Not worth the time to build multiple docker images and run minimal containers
    - Docker compose: third way; some customization, but not all; not worth prioritizing
- Ansible & PaaS – zipapps are much better than cloning repo & install dependencies
    - You can do `pip install mathesar` and then run Mathesar
- Shipping static files along with release seems unnecessary for "build from source"
- We should not conflate people who want to install stable Mathesar without Docker with people who want to modify Mathesar's code – we're calling these both "build from source"
    - non-Docker: people who want to install stable Mathesar without Docker
    - build from source: people who want to modify Mathesar's code
- Options for non-Docker:
    - Zipapps, OS specific binaries like .deb files, .exe files etc
- Considerations:
    - DB connection and access
    - Do we "own" the DB, does uninstalling Mathesar delete the database?
- We need to make a distinction between:
    - DBs that Mathesar "owns"
    - DBs that Mathesar is used as an interface to.
- Maybe we can say Mathesar always has a DB it owns
    - DBs that Mathesar is used as an interface to can be done using Postgres Foreign Data Wrappers
    - This means DDL would be impossible for those DBs
    - But we can support a lot more DB software - Oracle, Redis, etc.
- It seems like users who want to use the data modeling features are pretty much XOR with users who want to connect to existing DBs
- FDWs use the wire, but you could end up in stale states
    - Parking lot
- Environment variables seem more secure than config files
    - How do we add more DBs when we use environment variables

### Someone installing server & DB on separate remote systems
- Similar to previous persona.
- We need to provide documentation on how to do this.
- Depends on:
    - DB connection and access
    - Managed vs. installed DBs
- Where do we store DB credentials for remote systems?
    - Maybe encrypt with secret key and store it in the DB

### Someone installing Mathesar on a PaaS
- Probably use Docker image for this
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
- Use single Docker image that includes the DB
    - Unless the PaaS has a managed DB, we'll use that then
- SQLite doesn't work with load balancers - we'll need a Postgres database
    - This applies to all server installations
    - Docs should strongly recommend Postgres for internal
- Where do we store DB credentials for remote systems?

### Someone installing Mathesar on existing DevOps infrastructure
- e.g. Kubernetes, Helm
- How much help do we want to give them?
- PaaS should work for any DevOps infrastructure
- We could provide a Helm Chart (https://helm.sh/)

### Someone who wants to build Mathesar from source
- Probably a developer, existing docs should be enough
- Our existing docs are currently "build from source", but we don't want them to be
- Checking out git repo
- Doesn't seem like an important persona

## Prioritization

General strategy:
- Until we get to 1.0, we are going to assume installation will be done by technical users.
- UI should be friendly to non-technical users
- You need to be technical to install Mathesar, or learn something

Discussion:
- But what about users who have contacted us who are running on localhost?
    - SaaS could serve their need
    - Or a detailed server setup guide (e.g. "how to set up on GCP" that includes all their settings)
    - Or PaaS
- No need to work on Mac or Windows servers
- We're assuming servers are Linux (not FreeBSD etc. – at least not yet)

### Top
- Someone trying Mathesar out quickly (and can use Docker)
- Someone installing Mathesar on a PaaS
- Someone installing server & DB on same remote system
- Someone installing server & DB on separate remote systems

### Medium
- Someone installing server on localhost, but connecting to a remote DB
- Someone installing Mathesar on existing DevOps infrastructure

### Not prioritizing at all / discourage
- Someone trying Mathesar out quickly locally (and cannot use Docker)
- Someone who wants to build Mathesar from source
- Someone installing everything on localhost (not just trying it out)

## Next steps
Mukesh will come up with a project plan based on our priorities discussed here – we've already identified the major problems, and he's already done some research.

We'll discuss Mukesh's proposal / solutions at part 4 of this meeting next week.