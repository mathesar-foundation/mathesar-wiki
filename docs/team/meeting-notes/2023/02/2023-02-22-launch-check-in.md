# 2023-02-22 launch check-in

## General check in

#### Users & Permissions
- Frontend work mostly merged
- PR is open for UX change
    - Should be merged soon, pending review
    - Should be reviewed after the upgrades stuff
- For QA and documentation, Kriti has a spreadsheet set up
- Should have the documentation before tomorrow's meeting
- Pavish wants to add some tootips to help users understand what permissions do

### Installation & Deployment
- Everything is working for Type 1
- SSL is working, tested on GCP. Turned off in localhost.
- Brent's working on Type 2
- Deployment usability testing can be restarted
- Kriti talked with Mukesh about deployment type 3
    - We havea temp working on documenting the steps Ansible goes through for type 3

### Live demo
- We narrowed the problems down to reflection being very inefficient.
- Demo analytics has been merged
    - If time, add more analytics events

### Website
- Kriti posted new 404 in matrix yesterday
- PR is submitted (draft) for integrating docs into the website.
    - Should be merged after the docs look nicer
- Draft PR for social proof section.

### Documentation
- Wiki is now styled with our colors, etc.

### Usability improvements
- "Use 404 page in app" is in progress

### Upgrades
- Sean is addressing review feedback
- Kriti will figure out QA plan once merged.

### Release
- Document release process

### Publicity
- No update

### Priorities per person

#### Anish
- Completing QA spreadsheet
- Getting #2520 merged in
- Community work

#### Brent
- Deployment type 2
- Propose/document release process
- Deployment usability test fixes
- Website bio

#### Dom
- Find and fix demo server bottlenecks
- Figure out how to make demo server unlikely to break (reliable)

#### Ghislaine
- Update docs styling
- Alternative CTA design

#### Kriti
- Keep people unblocked
- Deployment usability testing
- Deployment Type 3
- Testing upgrades
- Update README, HN post, etc.

#### Mukesh
- Help Dom with live demo throughput issue
- Deployment Type 3 
    - install.sh improvements

#### Pavish
- Make changes based on outcome of permissions agenda item
- Re-review and merge Upgrades PR
- Ensure schema access control modal UX PR is merged (address review feedback if any)
- Add more analytics events
- Add in-app help tooltips for permissions, if time permits

#### Rajat
 - Get consistent 404 page PR merged - Usability testing.
 - Documentation for users and permissions.
 - QA user and permissions.
 - QA the platform in general. 

#### Sean
- Review [Update schema access control modal UX](https://github.com/centerofci/mathesar/pull/2540)
- Live demo UX improvements
- Review [Consistent 404 pages across client and server](https://github.com/centerofci/mathesar/pull/2529)
- Review [Add Deployment docs](https://github.com/centerofci/mathesar/pull/2497)

## Permissions - clarifications
- **Summary**: 
    1. Can a schema manager edit schema name & description?
        - We have options to do this at both the schema page & db page.
        - Currently, the UI allows schema managers to do this at the schema page, but not at the DB page. We need to make this consistent.
        - The product spec does not provide clarification into names and descriptions. This is a DDL operation on the schema itself, and based on the spec it should only be allowed if the user has manager access on the DB. However, the backend allows this.
    2. If we allow editing, should we allow delete? The backend allows this, the frontend doesn't. The spec says we shouldn't allow this.
- It's okay if the schema manager can edit/delete the schema.
    - Requires a quick change on frontend work

We also discussed https://github.com/centerofci/mathesar/issues/2537 - conclusion was that the backend behavior/product spec makes sense but we need a better UX. We won't worry about it for launch - users and permissions just needs to be working; not necessarily really smooth.

## Demo server readiness
- **Summary**: What steps do we need to take to make demo work during launch?
- **Participants:** Dom, Brent, Kriti, Mukesh, Pavish, Sean (partial)

### Problems
- Performance is a problem:
    - Request timeouts due to reflection
    - bogging down on reflection
    - Multiple servers hooked up to same DB doesn't help
- Too many connections
    - Increase connection limit?
    - Optimize connection management in the code
    - Reduce timeout of Postgres sessions
        - Slow down demo server, but won't crash it.
- Figure out how to set up load balancer if we need it.
- Note: ensure the ArXiv data loader doesn't write to the template

### Load tests
- https://github.com/centerofci/mathesar-scripts/tree/master/demo-loadtest

### Process
- Getting the demo server 100% reliable before Monday is not a reasonable goal.
- We shouldn't be trying to identify all issues at once.
- We need to rapidly iterate on fixes and load testing.

### Tasks
1. Figure out setting up (sticky sessions) load balancer and additional servers in GCP - Mukesh
2. Optimize Postgres settings - session timeout, connection limit, etc. - Dom
    - Connections may be memory intensive, pay attention to that.
    - Postgres connections according to docs, 128 MB
        - Not seeing that in production, 0.3% of 8 GB
        - 300 connections will use ALL the memory
3. Optimize reflection in the Mathesar codebase - Dom
4. Optimize connection management in the Mathesar codebase - Mukesh
5. Load test more and find other problems - Dom