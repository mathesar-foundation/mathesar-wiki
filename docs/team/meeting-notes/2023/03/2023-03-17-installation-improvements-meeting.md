# Installation Improvements Meeting

## Meeting Information
**Meeting Purpose:** Brainstorm Installation Improvements

**Attendees:** Brent, Kriti, Mukesh, Pavish

## Projects
We need to split "installation improvements" into smaller projects:

### Ideas
- Simplify Docker images - ideally one Docker image
    - Seems very important, will simplify all the other setups
    - Cannot do Watchtower
    - Can do DB + service
    - Ideally:
        - Single Docker image
        - Will come with DB for Django
        - User can create DB or 
- Provide a single Docker Compose file 
    - Ensure comments
- Set up configuration file for Mathesar installation
    - e.g. mathesar.conf (e.g. yaml file)
    - We could turn this into .env
    - Simplify how we configure environment variables (database URLs)
- Consider setting up a UI
- Consider removing interactive installer
    - Hard to maintain
    - Developers are used to config files
- Consider removing Caddy
    - Not useful for local infrastructure
    - Not useful for cloud providers
    - Should be add on, not the default
- Install Mathesar using Helm chart
    - depends on the single Docker image
- Use podman for Mathesar
    - Will "just work" if we have a Docker image
    - May not be necessary if we remove interactive installer
- Install Mathesar without Docker
- Provide minimal Docker setup without optional services like Caddy
- Figure out general upgrade infrastructure
    - Installation flexibility means less upgrade help
    - Remove Watchtower
- Create packages / add to repos
    - Arch User Repository
    - Set up .deb files
    - Set up Flatpak
    - Need automation for all this
    - yum (redhat/fedora)
    - homebrew?

### Discussion
- Why use Caddy?
    - Load balancing
    - DDoS attacks
    - Static files
    - SSL certificate

## Selected ideas and prioritization
*We ran out of time. Mukesh will follow up on using the new projects framework to create and prioritize installation related projects. Once he's done with the write up, we will review.*

1. Document how to run current docker image without docker compose
    a. Document configuration of this setup

## Assisting installs
- Brent will be taking the lead for now and keeping Mukesh informed.

## Inspiration
- https://docs.nocodb.com/getting-started/installation/
- https://baserow.io/docs/installation%2Finstall-with-docker-compose
- https://matrix-org.github.io/synapse/latest/setup/installation.html

## Mukesh's email
*Sent to the core team list prior to the meeting.*

During our Alpha release, we managed to release a one-line bash command for setting up Mathesar. But the installation process is opinionated and cannot be easily configured which is what the users expect based on the feedback we received from various sources.

Our Users want to:

- Install Mathesar on a Kubernetes or similar infrastructure
- Run Mathesar without administrative access which is required by our installation script.
- Install only the Mathesar web server without any additional services like Caddy, and Watchtower which are currently installed alongside the Mathesar webserver by our installation script.
- Run Mathesar without using Docker
- Directly modify the configuration variables/files instead of having to use the installation script.

Problems that are stopping the user from their goals:

- Our installation Documentation is incomplete
  - Only Docker-based installation is listed in our docs
  - There isn't much information about Mathesar services or about the configuration files
  - There isn't much information on what the installation script does which makes it hard for users to trust
- Configuration files don't have enough comments, preventing users from tinkering.
- The installation script is tightly coupled, preventing them from using it with their own setup. It sets up the configuration file, downloads the docker-compose file, sets up the Mathesar database, and so on. The user cannot use the script to do only certain tasks, for example, they cannot use the script to only create a configuration file and skip other steps.

Other problems:

- Our installation script does not allow for edits. Making the user start fresh if they made a mistake.
- Our upgrades are tightly coupled with the Watchtower upgrade service(?), so Mathesar might not work(?) if they install only certain services.

Based on the above feedback, we can understand that

- The users are technical enough and would like to tinker with the configuration
- They want to use Mathesar with their own setup
- Security conscious

Here is what is done to fix the above problems

- Kriti mentioned that she has a lot of thoughts on improving our installation process, so Brent, Kriti, Mukesh, and Pavish will be having a meeting today to get a brain dump from Kriti.
- I will be creating a list of issues based on the discussion from the meeting and update this email thread with the next set of actions items after the meeting
- I will be coordinating with Marius de Beer who is currently writing documentation for "Installing Mathesar on various Linux Distro with/without Docker" to make sure the documentation and improvements to the installation process are in sync. 

