# Expanded Deployments

| **Role** | **Person** | **Status** |
|-|-|-|
| **Author** | Kriti Godey | 🟢 Done |
| **Reviewer** | Brent Moran | 🔵 In review |
| **Reviewer** | Zack Krida | 🔵 In review |

## Solution

### Supabase

*Why?*: Postgres-specificity + reach + potential for discoverability.

- The [Supabase partner integration page](https://supabase.com/partners/integrations) should include Mathesar. 
- Our documentation should link to the Supabase integration and an accompanying guide about how to use Supabase with Mathesar.
	- Also review docs for how well it explains RLS, how to set up a DB without allowing DDL changes, and how to set up roles and permissions.
- We should publish a blog post about how to set up RLS in Supabase / Postgres generally and use it with Mathesar.
- We should track analytics of how much traffic and clicks all this is generating, both for the Supabase specific items as well as generally.

Example: [Directus's Supabase integration](https://supabase.com/partners/integrations/directus) shows how to demonstrate integration with a self-hosted project.

*Maps to use case: Frances*  
*Maps to category: Hosted Postgres / backend services*

### Helm chart

*Why?*: Integrates into existing infrastructure, user requests.

- Users should be able to install Mathesar via a Helm chart. available in a repo.  
	- Potentially multiple types of helm charts based on structure. 
- Our documentation should link to those charts as a first class citizen in the installation section, with accompanying documentation on how to use them.
- We should track analytics of how much traffic and clicks all this is generating, both for the Helm specific items as well as generally.

*Maps to use case: Frances*  
*Maps to category: DevOps tools*

### DigitalOcean

*Why?*: Quick implementation time, helps people evaluate, makes Mathesar deployment accessible without CLI.

- Users should be able to find and install Mathesar in the [DigitalOcean Marketplace](https://marketplace.digitalocean.com/) as a [one-click app](https://docs.digitalocean.com/products/marketplace/droplet-1-click-apps/). 
- Our documentation should include deploying with Digital Ocean as a first class citizen in the installation section, with accompanying documentation on how to work with it.
	- The user should be able to complete the setup without ever using the command line or having to make any decisions about database size, SSL, etc.
	- The setup should take less than 15 minutes and produce a working HTTPS endpoint with a login screen.
	- We need to be able to help non-technical users find their organization’s existing DB and connect it to Mathesar in the UI or docs. We can’t assume as much technical familiarity when they’re doing a one-click deploy.
- Our README and documentation should include a [one-click deploy button](https://www.digitalocean.com/community/tutorials/one-click-deploy-button).
- We should track analytics of how much traffic and clicks all this is generating, both for the Digital Ocean specific items as well as generally.

*Maps to use case: Blair*  
*Maps to category: Simple platforms*

### Railway

*Why?*: Quick implementation time, helps people evaluate, makes Mathesar deployment accessible without CLI.

- Users should be able to find and install Mathesar on [Railway](https://railway.com/) as a [one-click app](https://railway.com/deploy). 
- Our documentation should include deploying with Railway as a first class citizen in the installation section, with accompanying documentation on how to work with it.
- Our README and documentation should include a [one-click deploy button](https://www.digitalocean.com/community/tutorials/one-click-deploy-button).
	- We need to be able to help non-technical users find their organization’s existing DB and connect it to Mathesar in the UI or docs. We can’t assume as much technical familiarity when they’re doing a one-click deploy.
- We should track analytics of how much traffic and clicks all this is generating, both for the Railway specific items as well as generally.

*Maps to use case: Drew*  
*Maps to category: Simple platforms, Developer-focused PaaS*

### Cloudron

*Why?*: Works for self-hosters, expanding platform diversity.

- Users should be able to find and install Mathesar through [Cloudron](https://www.cloudron.io/).
- Our documentation should include deploying with Cloudron as a first class citizen in the installation section, with accompanying documentation on how to work with it.
- We should track analytics of how much traffic and clicks all this is generating, both for the Cloudron specific items as well as generally.

*Maps to use case: Isa*  
*Maps to category: Self-hosted PaaS*

### Fly.io

*Why?*: Expands platform diversity to more developer-focused tooling.

- Our documentation should include a guide to deploying with fly.io as a first class citizen in the installation section, with accompanying documentation on how to work with it.
- We should track analytics of how much traffic and clicks all this is generating, both for the fly.io specific items as well as generally.

*Maps to use case: Casey*  
*Maps to category: Developer-focused PaaS*

### Google Cloud Platform

*Why?*: Big Three cloud infrastructure platform, expands platform diversity.

- Users should be able to find and install Mathesar through the [Google Cloud Marketplace](https://cloud.google.com/marketplace?hl=en).
- We should write guides for how to set up Mathesar with GCP, such that they are foolproof to follow and follow GCP best practices and networking.
	- Using CloudSQL
	- Using Helm + GKE
	- Using a VM

*Maps to use case: Gray*  
*Maps to category: Cloud IaaS*

---

*We will evaluate what’s next for this project after we complete implementation of the above, based on our current user base and the efficacy of all the things we've already done.* 

## Tradeoffs

These issues came up in the user stories below, but we're not prioritizing them.

* Updating UI documentation with screenshots for people to use to train other people.
	* Too much work; too unrelated to this project.
* AWS *and* GCP
	* We should only start with one here since it’ll be a lot of work.
	* Depends on what our users use more.
* Anything to do with the use cases of:
	* Harper, on-premise engineer.
	* John, Mac user.
	* Elliot: AWS user (unless we substitute him for Gray and do AWS instead of GCP).

Things to watch out for while implementing:

* Not making installation methods easily discoverable in our documentation. See [Self-hosting](https://nocodb.com/docs/self-hosting) (NocoDB) and [Install with Docker](https://baserow.io/docs/installation%2Finstall-with-docker) (Baserow, see sidebar) for positive examples.
* Trying to make our documentation too preemptively perfect – let’s just put it out there.
* Not implementing things because of prioritizing hypothetical maintainability concerns, or not imagining that something might be useful, or worrying about cluttering the documentation (these have all come up in the past).
* Spending a lot of time stuck on one installation method without raising it / figuring out if we should keep going.


## High-Level Implementation Plan

**Work needed**: Backend & documentation work, primarily.

**Implementers and reviewers**:

Brent & Anish to implement, Kriti reviews user-facing or admin-facing changes as they are merged.

**Rough timeline:** 1 type completed per week.

## Research

### Comparison of hosting platforms

| 🏁Targets to prioritize | **🏋️Effort**  | **🚨Urgency** | **⚠️Importance** | 🚧Evaluating Mathesar for production use | ⚒️ Integrating into their own infra | 🚢 Discovering Mathesar through a tool they use| 🧱Aiming to make prod. deployment easier |
|---|---|---|---|---|---|---|---|
| | | | | 🧑‍💻Semi-technical users deploying Mathesar | 🧪 Test with their own secure data | ⭐ Social-proof validation through integrations | 📡 Real-world signal from reproducible methods  |
| **As many as possible** (meta) | N/A |  | *N/A* | ❌ We only need a couple simple ones for this cohort | ✅ We need to integrate with as many platforms as people use. | ✅ More people will discover us if we’re more places | 🟨 We’re likely to get most benefits with this cohort with a few well chosen platforms. |
| **Simpler PaaS**<br>Digital Ocean<br>Heroku<br>Railway<br>etc. |  | **Medium**<br>Not blocking anything | **High**<br>Removes adoption barrier | ✅ People don’t want to spend time deploying to evaluate or if they’re non-technical | ❌ People who’ve invested in infrastructure usually end up at a bigger cloud marketplace. | 🟨 Some people will discover us here, but people who tend to be discovering things through platforms are likely bigger.  | ✅ People who just want to deploy Mathesar will appreciate easy deployment options.   |
| **Cheaper hosts**<br>Dreamhost, etc. | **Medium**<br>Don’t usually support Docker out of the box | **Low**<br>No one asked for this | **Low**<br>There are other ways to solve low-cost evaluation | ✅ People don’t want to pay much to evaluate | ❌ See above. | ❌ See above. | 🟨 Easy deployment doesn’t usually mean cheap. |
| **Cloud IaaS**<br>GCP, AWS, Azure, IBM etc. | **Medium**<br>May need approval & learning platform specifics | **Medium**<br>Not blocking anything, although people have asked. | **High**<br>We have often seen people deploy on these, people have asked us for an AMI. | ❌ Not always likely to have AWS etc. accounts | ✅ Definitely the place to be for integrating into existing infrastructure. | 🟨 People do discover things on AWS and GCP, but may be better on smaller platforms. | 🟨 Cloud infrastructure is sometimes hard to deploy. |
| **DevOps tools**<br>Helm chart<br>Terraform modules<br>Ansible playbook<br>Kubernetes operator<br>Packer template<br>etc. | **Medium**<br>This needs some learning | **Medium**<br>Not blocking anything, although people have asked. | **High**<br>People have also asked us repeatedly for a helm chart. | ❌ Too technical | ✅ Often necessary | ✅ Often necessary | 🟨 Sometimes too technical, sometimes helpful. |
| **Postgres-like DBs**<br>Citus<br>TimescaleDB (TigerData)<br>Yugabyte<br>CockroachDB<br>Babelfish<br>AWS Aurora<br>Materialize<br>etc. | **High**<br> Often don’t support Postgres features we depend on. | **Low**<br>Not many asks for it. | **Low**<br>No use case we know of. | ❌ Too technical | 🟨 Sometimes a key part of their stack, sometimes too specialized to need Mathesar. | 🟨 Could be a source of growth if we find one that works well. | ❌ Not likely to be helpful here. |
| **Frontend platforms**<br>Vercel, Netlify, etc. | **Medium**<br>This needs us to figure out the platform. | **Medium**<br>Seems like they would be a good place for discovery. | **Medium**<br>This is expansive rather than unblocking. | 🟨 People are more likely to be looking for DBs if they’re users of these platforms. | 🟨 Depending on the team, they may rely more on these platforms. | ✅ This seems like a good place for discovery. | ✅ People who use these platforms are likely looking for a quick deployment. |
| **Backend platforms**<br>Supabase, etc. | **Low**<br>They use Postgres, we just need a guide on how to connect to it. | **High**<br>Postgres-specific platform with high reach. | **High**<br>Likely strong overlap in users. | 🟨 Potentially, people who have a Supabase DB are likely to want quick evaluation. | 🟨 Supabase is definitely a popular tool. | ✅ This seems like a good place for discovery. | ✅ People who use these platforms are likely looking for a quick deployment. |
| **Developer-focused PaaS** <br>fly.io<br>Railway<br>Koyeb<br>Render<br>etc. | **Medium**<br>This needs us to figure out the platform. | **Medium**<br>Seems important to our user base. | **Medium**<br>Seems like a good platform to be on eventually. | ❌ Too focused on high-performance and serverless. | 🟨 *Maybe*. Seems a bit specialized.  | 🟨 *Maybe* – seems a bit specialized. | ✅ People who use these platforms are likely looking for a quick deployment. |
| **Self-hosted PaaS**<br>Coolify<br>Cloudron<br>Caprover<br>etc. | **Medium**<br>This needs us to figure out the platform. | **Medium**<br>Seems important to our user base. | **Medium**<br>Seems like a good platform to be on eventually. | ❌ Definitely not self-hosters | 🟨 Seems less likely for orgs, but people who use these seem like they really use them. | ❌ Seems less likely to spawn discovery. | 🟨 Only for people who bought into this particular ecosystem.  |
| **Managed Postgres**<br>Neon, Nile, Crunchy Bridge, ScaleGrid, Aiven, Prisma Postgres, etc. | **Medium**<br>This needs us to figure out the platform. | **Medium**<br>Postgres-specific is good for us | **High**<br>Seems good for distribution. | ❌ Seems too specialized for this group of people. | ✅ Seems really good for people who actually use Postgres a lot. | ✅ Seems like a good place for people in the Postgres ecosystem to discover things. | 🟨 People who are using hosted Postgres may want easier deploys for Mathesar.  |
| **Local installation**<br>apt package, snap, flatpak, AppImage, Homebrew, podman, systemd, Nix | **High**<br>Needs individual support per platform. | **Medium-low**<br>People asked for it in the past but not recently. | **Medium-low**<br>No specific use case we know of. | 🟨 Too technical? Evaluating *could* happen locally, but Docker should cover that. | ❌ Existing infrastructure is usually not local. | ❌ No discovery happening here. | ❌ Deployment is probably not happening locally. |


### NocoDB

For what it’s worth, NocoDB supports a few different types of hosting platforms, see all types below in the next section.

**“Auto upstall”:** This is their default script meant for a Linux server that installs everything including Postgres, sets up a DB, sets up SSL, upgrades, etc. I think it’s meant to be idempotentent.

**Simple platforms:** Digital Ocean, Railway, some other “one click deploy” buttons.

**Cloud marketplaces:** AWS Fargate, GCP Cloud Run

**DevOps tools:** Docker, Docker Compose, Helm chart

**Local installation:** Homebrew, Nix/NixOS, npm

**Self-hosted PaaS tools:** Cloudron, CapRover \+ they link to an external TrueNAS / FreeNAS guide.

### Baserow

Baserow supports a similar list of hosting services as NocoDB.

**DevOps tools:** Docker, Docker Compose, Helm chart, K8S. They have images that contain all dependencies and are ready to go.

**Simple platforms:** Digital Ocean, Heroku, Render, Railway \+ a page for other third-party hosting providers

**Cloud marketplaces:** AWS Fargate / other ways of deploying on AWS using Docker & Kubernetes

**Self-hosted PaaS tools:** Cloudron

Additionally, they have:

- Guides on how to set up various proxies: Traefix, nginx, Apache  
- A guide on how to set up logging and monitoring  
- A guide on how to save files securely

## Community Engagement

We should:

- seek input from community members who have asked for additional deployment options, to ensure that we're building the right set of features and addressing their use cases.
- set up a Community Guides section of our docs so that we can ask people to contribute their setups.
- update our blog with every new guide we write, even if it also goes on our documentation website.
- consider updating website copy with each new deployment method.
- consider posting on platform-specific or self-hosting communities when we add a new platform.
- consider adding one-click buttons to our website.
