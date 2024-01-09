# 2023-07-11 installation meeting

## Links
- [Meeting notes: Parts I & II](/meeting-notes/2023-06/2023-06-13-installation-planning-meeting.md)
- [Meeting notes: Part III](/meeting-notes/2023-07/2023-07-06-installation-meeting.md)
- [Mukesh's installation research](https://hackmd.io/SFWrMLWMR72P-iQ_M30JFA) (private)

## Notes

### Terminology

- **User database** - Database containing user data (shows up in UI)
- **Internal database** - Database containing metadata used internally by the software (doesn't show up in UI)

### 1st Persona: Someone Trying out Mathesar quickly, with Docker

Assumptions:

- They have docker
- Want to try things out locally
- Won't keep this installation long-term

Solutions:

- Single Docker image
    - Postgres inside
    - Secret key generated with no interaction
    - Side benefit: support older Docker versions (since our compatibility issues are with docker compose)
- Should we have a second Docker image without Postgres?
    - For connecting to remote DBs
    - This seems for a different persona
    - Also, connecting to local DBs (vs. remote DBs) from a Docker container is much harder for Linux
- Config files vs. environment variables
    - Research into similar products indicates users wants config files that can be overridden by environment variables
    - Config files can be put into protected locations (e.g. not readable by other users on the system)
    - Config file will live in the container, not the host system
    - Environment variables doesn't make sense for this persona
    - We can pass environment variables when running the image if needed, and they would persist in the config file in the Docker filesystem 
- What do we need environment variables for?
    - Binding volumes?
        - Not needed for this persona
        - If they want to transition installation to long term solution, that would be different, but we're not recommending that anyway 
        - We could have docs for "you lost your container, how to get your data"
    - Using different ports?
- For this persona, it's about speed to get Mathesar running
- What about users who want to try it out quickly by connecting to an existing DB? 
    - Pass config via environment variables
    - Write config file via UI, persist to disk.

### Installing Mathesar on PaaS (one-click, frictionless)
- Need a lean image without a DB for this
- We want to wire Mathesar up to managed DB services
- We need to decide what PaaS to target
    - Should be frictionless
    - Managed Postgres would be helpful
- Additional work we might need to do, on a per-platform basis:
    - Add Mathesar to their installer system
    - Add platform-specific details to our documentation
- Which platforms should we target?
    - Mukesh has not yet done research into this
- Pavish: We should consider the possibilty that users might want multiple instances of Mathsar running on the same PaaS. How will we acheive this if we use a config file?
    - Kriti: "I'm sure this is a solved problem"
    - Pavish: Mathesar might be unique in that we are planning to allow the application to modify the config file
- Pavish: What are we storing in the config file?
    - Mukesh: it would be the same as all the ENV vars
- Pavish: Do we even need the config file?
    - Mukesh: it's important for persistance. It's important in the case when you have Mathesar running behind a load balancer. Config file is meant only for running one instance of Mathesar
- Brent: I'm not convinced that horizontal scaling is a huge priority right now. In that case, the stuff that you's want to persist would be in the database anyway.
- Kriti: PaaS platforms often have their own systems for persisting private data like "secret key" and similar.
- Where do we store the database connection credentials?
    - PaaS service doesn't necessarily have access to modify files on disk, so we would need to store the user DB credentials in the internal DB.
    - How do we secure the credentials that we're storing in the Django DB?
- We either:
    - Need to store connection credentials in the internal DB
    - OR: we need to give up support for editing DB connections through the UI.
- We need to do more research on how to store connection credentials
- Brent: If we can solve the problem of securely storing the connection credentials in the internal DB, then we solve a huge class of problems that apply to many different personas

### Next steps
- What does Mukesh need in order to write up a project?
- Sean: concerned that we're not looking at the high level of "reducing total number of personas"
- Kriti: we've reduced the number of personas through prioritization
- Solving PaaS well could help solve other personas too
- Kriti reccomends:
    - Work towards implementing the "Single Docker Image" approach
    - Continue research on other approaches
    - Fine to focus on other research and implementation that would seem to improve other personas too, e.g. Zipapps, etc.
    - By the end of the cycle, we should have a plan for what personas we're doing and the implementation plan for them
- Mukesh will write up project
- Kriti & Mukesh will discuss next steps and schedule another call
