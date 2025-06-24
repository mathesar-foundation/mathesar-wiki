# Additional Deployment Options

## The Problem

Additional deployment options are actually solving four different problems:

1. Makes it **easier for people to evaluate Mathesar quickly.**
2. It makes it easy for people **with existing infrastructure to integrate Mathesar** into their infrastructure.
3. It **helps new people discover Mathesar** (e.g. Supabase users looking at their marketplace, or Vercel users trying to integrate a DB)
4. It makes it **easier for people to actually deploy Mathesar in production**.

Some intangible benefits include:

* **Bridges technical trust gaps:** Mathesar is still new, and offering a known, reproducible setup path option reduces perceived risk of adoption. Engineers trust tools that use platforms they trust.
* **Unblocks adoption for semi-technical users:** There are plenty of people who are uncomfortable with Docker but are comfortable hitting a “Deploy on DigitalOcean” button, given that DigitalOcean sets up backups, has support, etc.
* **Validates Mathesar’s maturity and longevity:** People use availability and ubiquity as a proxy for viability. If we’re on AWS and GCP and Supabase marketplace, we must be legit.
* **Enables real testing:** If my infrastructure’s all on AWS locked in a private VPC, an AWS AMI or CloudFormation template means the barrier to me trying out Mathesar with real data is much, much lower.
* **Signals real-world usage and deployment:** Currently, the *lack* of easy installation options when so many other projects have that as the first thing in their README makes us look immature in comparison.

### Why it’s worth solving

Mathesar's primary need right now is user adoption and growth, ASAP. It's essential for both impact and sustainability, because we’re still “[default dead](https://paulgraham.com/aord.html)”.

Offering more deployment options is relatively low-effort and high-impact. 

How it helps users:

* People are asking us for [AWS AMIs](https://github.com/mathesar-foundation/mathesar/issues/4042#issuecomment-2957642159), [Helm charts](https://github.com/mathesar-foundation/mathesar/issues/2633#issuecomment-2978206692), etc.
* People with existing infrastructure are having to spend a lot of time and effort into integrating Mathesar into their workflow.
* People seem to be finding it hard to go from evaluating Mathesar to deploying it in production.
* The people that might benefit most from Mathesar are not the ones finding Mathesar.

It helps us grow by:

* Making people aware of us when they’re looking to solve a specific problem e.g. if they’re on Supabase’s integrations site thinking “how do we do better data entry for this DB?”
* Becoming available on platforms ASAP. People who need us on specific platforms won’t use us until we’re there. The sooner we’re there, the better.
* Helping us learn by things and see what works and what doesn’t. Lack of information is worse than failure.

### Is it feasible?

Yes\! It’s not feasible to implement *every single* way to deploy Mathesar, but there’s some low-hanging fruit that could have a real impact.


## Evaluation and Guardrails

How we'll know we've succeeded with our goals:

* We’re seeing more people installing Mathesar and using it (DAUs / MAUs trackable to that install method).
* We’re specifically seeing people using any new installation method we set up.
* Ideally we also get an uptick in user feedback / new issues, etc, but that should not be a formal success criterion since that also depends on other issues. 
* The number and variety of installation methods we offer are equivalent to other products in the ecosystem.

Things to watch out for while implementing:

* Not making installation methods easily discoverable in our documentation. See [Self-hosting](https://nocodb.com/docs/self-hosting) (NocoDB) and [Install with Docker](https://baserow.io/docs/installation%2Finstall-with-docker) (Baserow, see sidebar) for positive examples.
* Trying to make our documentation too preemptively perfect – let’s just put it out there.
* Not implementing things because of prioritizing hypothetical maintainability concerns, or not imagining that something might be useful, or worrying about cluttering the documentation (these have all come up in the past).
* Spending a lot of time stuck on one installation method without raising it / figuring out if we should keep going.


## Requirements

This is not a single task, it is a series of discrete tasks. Each task may be fairly small. We should aim to get 1 thing from this list shipped every week, in order of highest leverage.

**Initial Goals:** Get Mathesar integrated into a variety of different categories of platform, prioritizing low effort and high impact outcomes.

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

- Users should be able to find and install Mathesar through [fly.io](http://fly.io).
- Our documentation should include deploying with fly.io as a first class citizen in the installation section, with accompanying documentation on how to work with it.
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


## Community Engagement

We should:

- seek input from community members who have asked for additional deployment options, to ensure that we're building the right set of features and addressing their use cases.
- set up a Community Guides section of our docs so that we can ask people to contribute their setups.
- update our blog with every new guide we write, even if it also goes on our documentation website.
- consider updating website copy with each new deployment method.
- consider posting on platform-specific or self-hosting communities when we add a new platform.
- consider adding one-click buttons to our website.

## What We’re Not Doing (Yet)

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

## Use Cases

I thought it would be useful to consider a wide range of potential installers so that we could be thoughtful about what we can support and what we’re putting off. Only some of them have been prioritized for the actual proposal.

### Alex: Cloud-friendly engineer

**Alex** is a mid-level full-stack dev at a data-savvy startup. He’s comfortable with Docker, CLI tools, and VPS provisioning. He likes open-source and self-hosts side projects. He wants to try Mathesar as a potential internal tool to replace messy spreadsheets. He's spinning up a test environment on a Hetzner VPS.

He wants a well-documented `docker-compose.yml` he can modify, clear instructions for TLS setup (he’ll use nginx \+ Certbot), and persistent volumes that survive reboots or image rebuilds. He doesn’t want to reverse-engineer random scripts. He orefers to run things in containers for portability.

User stories:

1. Alex wants to clone a GitHub repo with a ready-to-use `docker-compose.yml` that he can launch with one command.
2. Alex wants to connect Mathesar to an existing Postgres instance running on another VPS or in the same stack so he can manage access to live data.
3. Alex wants to be able to edit environment variables and config files directly so he can fine-tune behavior and performance.
4. Alex wants SSL to be set up automatically using Let’s Encrypt or documented clearly enough for him to do it.
5. Alex wants to see logs and test endpoints during setup to make sure everything is working before he invites collaborators.
6. Alex wants updates to be handled via Docker image pulls so he doesn’t have to reconfigure every time.

### Blair: nonprofit technology generalist

**Blair** manages websites, tools, and sometimes databases for a 30-person nonprofit. She wants to set up Mathesar to give program staff easy access to donor and outreach data without bugging her constantly.

She’s stretched thin and not a full-time sysadmin. She does not self-host regularly and cannot spend hours debugging YAML or unfamiliar infra. She wants to avoid hand-editing config files after deployment.

User stories:

1. Blair would like to find Mathesar on a VPS platform marketplace that she’s familiar with and be able to set it up through the website.
2. Blair wants to complete setup without ever using the command line or having to make any decisions about database size, SSL, etc.
3. Blair wants installation to take less than 15 minutes and produce a working HTTPS endpoint with a login screen.
4. Blair wants to be walked through connecting her organization’s existing DB to Mathesar in the UI or linked documentation.
5. Blair wants clear UI documentation with screenshots so she can hand off post-setup usage to her colleagues.

### Casey: DevOps engineer

**Casey** is an early technical hire at a YC startup. He uses fly.io for microservices, values fast deploys and infra-as-code. He sees Mathesar as a good admin UI for internal ops data. He wants it in their staging environment fast.

He wants a `fly.toml` file and Dockerfile that integrate with fly’s builder and volume mounts. He’d like HTTPS out of the box, maybe via built-in certs. He’d ideally like a deployable Postgres image or docs on using fly.io's PG add-on. He needs logs and rollbacks to work with fly CLI. He has to deploy in a way that can be repeated in CI. He’ll run `fly deploy`, and expect it to work the first time, but will do *some* debugging before giving up. 

User stories:

1. Casey wants to deploy Mathesar to fly.io using a `fly.toml` config so it integrates cleanly with our existing infra.
2. Casey wants Mathesar to connect securely to their internal Postgres instance (via IP allowlist or fly.io’s internal networking).
3. Casey wants TLS to be automatically configured so he doesn’t have to handle certs manually.
4. Casey wants to manage Mathesar deployment through CI/CD or fly’s CLI so he can version and track deployments.
5. Casey wants logs and health checks exposed via fly’s dashboard so I can monitor the app’s status.

### Drew: Freelance data consultant

**Drew** is a freelance data consultant that does short-term dashboarding and analysis work for small teams. She prioritizes speed and simplicity, and usually uses Railway for quick, low-effort deployments of whatever tool she needs.She wants to host Mathesar temporarily during a client project to give them data editing access, without touching infrastructure.

She just wants to click a “Deploy” button in the Railway UI and have everything pre-configured for her. She’ll move on in 15 min if there’s confusing errors or setup isn’t done. She just wants to look good to her client fast.

User stories:

1. Drew wants to deploy Mathesar to Railway with a single click so she can quickly give clients access to their data.
2. Drew wants to easily point Mathesar to a Postgres instance provisioned on Railway or a client’s host (she has access to a connection string).
3. Drew does not want to have to figure out environment variables or a Postgres DB configuration or DNS or SSL, Railway should handle all that.
4. Drew wants to be able to shut down or delete the Mathesar instance easily when the project ends.
5. Drew wants to reuse the same deploy template for multiple clients as needed,

### Elliot: Data product owner on RDS

**Elliot** manages internal analytics tools and workflows for a 100-person company that uses AWS heavily and has a managed Postgres RDS instance powering multiple apps. He wants to give non-technical team leads (e.g. product, ops) access to structured data without involving engineering. He can't expose RDS publicly — Mathesar must live in a private subnet or behind IAM-controlled ingress. And the setup must comply with existing AWS security policies. 

He wants to deploy Mathesar into the same VPC as RDS with minimal friction, through hosting on the AWS service that makes sense. He’d like the ability to choose where to host (e.g. EC2 vs. EKS vs. Fargate). He aims to integrate Mathesar into a Terraform or CloudFormation stack. He expects SSL, secrets handling, and logging to work within existing AWS tooling.

User stories:

1. Elliot wants to deploy Mathesar within their AWS VPC so it can connect securely to their private RDS instance.
2. Elliot wants to use Terraform or CloudFormation to provision Mathesar so it integrates with their infrastructure-as-code.
3. Elliot wants Mathesar to support IAM roles or long-lived credentials to connect to RDS without opening public access.
4. Elliot wants to configure role-based access in Mathesar that mirrors their internal RBAC model.
5. Elliot wants the ability to audit user activity and log access attempts so they stay compliant with internal security policies.
6. Elliot wants Mathesar updates to be packaged in a way that doesn’t interfere with the rest of their infrastructure stack.

### Frances: Engineer on Supabase-based app

**Frances** works at a startup whose app runs on Supabase’s hosted Postgres service. She wants to give internal ops \+ support staff controlled access to some tables. She’s looking for an Airtable-like interface that connects directly to Supabase’s DB without breaking the row-level security she has set up on the DB.

Frances is primarily concerned with maintaining the integrity of the DB and engineering setup. She wants to ensure that RLS is respected and that Supabase auth and APIs are unaffected. She does not want the schema to be overwritten or for any problems with production. She wants to use known tools like a Helm chart. She also wants to use existing Postgres roles, she does not want to do a lot of additional setup. 

User stories:

1. Frances would like to connect Mathesar to their Supabase-hosted Postgres using an existing connection string so she doesn’t have to move or duplicate data.
2. Frances wants Mathesar to respect row-level security (RLS) and not interfere with Supabase’s roles or policies.
3. Frances wants to deploy Mathesar via Helm chart so she can host it alongside their internal tooling stack. 
4. Frances wants to pre-define user roles that match their Supabase access patterns so internal users only see the data they need.
5. Frances wants minimal or no schema modification so Mathesar works purely as a frontend and doesn’t change her DB structure.
6. Frances wants to onboard non-technical users quickly without needing to explain SQL or Supabase internals.

### Gray: Researcher using GCP

**Gray** maintains datasets in a GCP CloudSQL instance for his research lab. His grad students keep asking for access or CSV exports. He wants to set up Mathesar so students can view and edit structured data themselves without messing up raw tables.

Gray is familiar with GCP patterns, but not self-hosting in general. He has time and budget; he cannot babysit the server. He needs support for how to set up his server on GCP (as a VM, or using App Engine, or Cloud Run… he doesn’t care) with access to his database, which is in a private VPC.

User stories:

1. Gray would like to deploy Mathesar to a GCP VM or App Engine so it lives close to his CloudSQL database.
2. Gray wants to connect Mathesar to his existing CloudSQL instance without opening it to the public internet.
3. Gray would like to use default options for things like SSO or networking because he does not have the time to learn about the different options and decide.
4. Gray wants to ensure he knows how to set up Mathesar so that his students do not have access to edit the schema (definition) of the data.
5. Gray wants to know that he can just read through some documentation tailored to GCP and follow it and end up with a fully working and secure server.

### Harper: On-premise Mathesar setup

**Harper** works at a mid-size company with strict data policies and manages tools in a secure, air-gapped network. The Postgres DB runs on bare-metal in a secured internal network. She wants Mathesar for ops and finance teams to self-serve data reporting, but can’t put data or tools in the cloud — Mathesar needs to run fully offline.

She’ll install Mathesar inside their firewalled network, ideally via Docker Compose. She needs to build from source or use pre-scanned container images, since no external network access means no public Docker Hub. She aims to connect to the existing internal DB without breaking security assumptions. She has to manage auth via internal LDAP or SSO. She reads install docs carefully, runs things on airgapped servers, and uses the company’s own CA for SSL certs.

User stories:

1. Harper wants to install Mathesar from a pre-built tarball or internal image registry so she doesn’t require internet access.
2. Harper wants to run Mathesar entirely inside their internal network using Docker Compose or a VM so it conforms to their security boundaries.
3. Harper wants to connect Mathesar to their existing Postgres instance via localhost or private IP so no external routing is needed.
4. Harper wants to configure everything via files—no external API calls, license checks, or telemetry.
5. Harper wants Mathesar to respect their internal CA and certificate setup so TLS works with their existing infra.
6. Harper wants to restrict access via internal SSO (e.g., LDAP, Keycloak) so no cloud-based login is involved.

### Isa: Self-hoster

**Isa** manages a handful of apps for a community organization and side projects. She uses CapRover to avoid dealing with Docker or cloud config directly. Her stack already includes Postgres (via a CapRover one-click app). She wants to use Mathesar to give non-technical volunteers a way to edit structured data—without building custom UIs or giving raw DB access.

She deploys through CapRover’s GUI and uses its container orchestration. She prefers apps that behave like other CapRover-deployed tools—one click, then domain \+ login. She cannot use command-line tooling to install or configure apps. She doesn’t want to manage Dockerfiles, ports, or SSL.

User stories:

1. Isa wants to deploy Mathesar via CapRover’s “One Click Apps” UI using a prefilled form so she doesn’t have to touch Dockerfiles or terminal commands.
2. Isa wants to specify the Postgres host, port, DB name, user, and password in the form during setup so Mathesar connects to the existing database.
3. Isa wants Mathesar to start with a default admin user (or let her create one on first login) so she can log in immediately and verify it works.
4. Isa wants Mathesar to automatically use SSL via CapRover’s built-in TLS proxy so she doesn't have to set up certificates or proxies manually.
5. Isa wants to access Mathesar at a subdomain she configures in CapRover, like `mathesar.community.org`, so it’s easily shareable with others.
6. Isa wants a simple way to back up the Mathesar container’s config or bind mount so she can restore it if needed.

### John: Mac user

**John** is a macOS-native developer who tries out new open source tools locally before considering them for work or side projects. John saw Mathesar on GitHub or Hacker News and wants to see if it’s a viable lightweight Airtable replacement. His DB is a local Postgres instance from Homebrew, already populated with app data.

He installs Mathesar with `brew install mathesar` or `brew tap mathesar/cli`. Expects a local server to run with `mathesar start` and launch in browser.

User stories:

1. John wants to install Mathesar via Homebrew with a single command like `brew install mathesar` or `brew tap mathesar/cli` so he doesn't have to download anything manually.
2. John wants to launch Mathesar locally with a command like `mathesar start` so it runs a local server and opens in his browser.
3. John wants to connect Mathesar to his local Postgres DB so he can work with real data.
4. John wants the app to bind to `localhost:8000` or similar and serve a working UI without needing certificates or proxies.
5. John wants Mathesar to install with local defaults (e.g., SQLite or bundled Postgres) if he doesn’t configure anything, so he can test it instantly.
6. John wants to uninstall Mathesar cleanly using `brew uninstall mathesar` and remove any runtime artifacts, so his system stays clean.

## Comparison of hosting platforms vs. benefits

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


## Comparison of user personas

| 🧑‍💻Persona   | Background | Motivation | Needs | Constraints | Behavior | Environment |
|---|---|---|---|---|---|---|
| **🚧Alex** | Mid-level full-stack dev at a data-savvy startup.  Comfortable with Docker, CLI tools, and VPS provisioning. Likes open-source and self-hosts side projects. | He wants to try Mathesar as a potential internal tool to replace messy spreadsheets.  He's spinning up a test environment on a Hetzner VPS. | A well-documented `docker-compose.yml` he can modify. Clear instructions for TLS setup (he’ll use nginx \+ Certbot). Persistent volumes that survive reboots or image rebuilds.  | Doesn’t want to reverse-engineer random scripts. Prefers to run things in containers for portability. | Will clone the GitHub repo, tweak env vars, and expect the README to “just work.” | Uses Hetzner Cloud and DigitalOcean for VPS hosting. Deploys apps using Docker Compose, stored in GitHub repos with `.env` files and config directories. Local machine is Linux (Pop\!\_OS), CLI-focused, uses `docker-compose`, `curl`, `vim`, `tmux`, and `nginx`. DNS handled via Cloudflare; HTTPS via Certbot \+ nginx reverse proxy. Has multiple running services on custom ports; uses `ufw` for basic firewalling. Postgres either runs in a separate container or remotely (DO managed DB).     |
| **🧑‍💻🧱Blair**    | Works at a 30-person nonprofit. Technical but stretched thin—manages email, websites, analytics, and occasional server tasks. | Wants Mathesar to give program staff easy access to donor and outreach data without bugging her constantly. | A one-click DigitalOcean Marketplace install that handles TLS and Postgres. A public-facing UI and admin login within 5 minutes of clicking. Docs she can link to when training staff.  | Cannot spend hours debugging YAML or unfamiliar infra. She wants to avoid hand-editing config files after deployment. | Will only install if the Marketplace flow works without SSH.  Might use the web console but avoids CLI unless necessary. | Uses DigitalOcean for hosting; prefers Marketplace apps or Droplets with minimal manual setup. Primarily manages apps through web dashboards, not CLI. Public domain registered via Namecheap, DNS managed through DigitalOcean. Prefers browser-based UIs, HTTPS out of the box. Has deployed Ghost, WordPress, and Plausible using DO Marketplace before. Uses Gmail and Google Workspace; all user management happens there.     |
| **⚒️🧱Casey**  | Early technical hire at a YC startup.  Uses fly.io for microservices, values fast deploys and infra-as-code. | Sees Mathesar as a good admin UI for internal ops data. He wants it in their staging environment fast. | A `fly.toml` file and Dockerfile that integrate with fly’s builder and volume mounts. HTTPS out of the box, maybe via built-in certs. Ideally a deployable Postgres image or docs on using fly.io's PG add-on.  | Needs logs and rollbacks to work with fly CLI. Has to deploy in a way that can be repeated in CI. | Will fork your repo, run `fly deploy`, and expect it to work the first time.  Tolerant of minor friction if it aligns with platform conventions. | Entire internal toolchain lives on fly.io—app platform, Postgres, Redis. Deploys via `fly launch`, `fly deploy`, and GitHub Actions. Uses `fly secrets` for env vars, `fly volumes` for persistent storage. Monitors app health with `fly status`, logs with `fly logs`. TLS handled automatically via fly.io platform; custom domains configured via DNS provider. Very comfortable with Dockerfiles, CI/CD, and internal service networking.     |
| **🧑‍💻🧱Drew**    | Freelance data consultant who does short-term dashboarding and analysis work for small teams.  Uses Railway for quick, low-effort deployments. | Wants to host Mathesar temporarily during a client project to give them data editing access, without touching infrastructure. | One-click Railway deploy (template \+ environment vars pre-filled). Zero infra management beyond clicking "Deploy". Temporary Postgres DB bundled or easily linked.  | No access to client’s infra, no SSH. Doesn’t want to manage DNS or SSL—Railway should handle it. | Will abandon setup if it takes more than 15 minutes or requires non-obvious tweaking.  Wants to look good to her client fast. | Uses Railway for temporary infra during client engagements. Launches Postgres and backend services with one-click templates. Avoids terminal/CLI entirely; prefers GUI and prefilled deploy forms. Domain use is minimal; relies on Railway's auto-generated app URLs. Uses browser for everything: GitHub, Figma, GDrive, and Railway. Shares tools with clients via public or invite-only URLs, often disposably.     |
| **⚒️Elliot** | Runs internal tools for a 100-person company.  They use AWS heavily and have a managed Postgres RDS instance powering multiple apps. | Wants to give non-technical team leads (e.g. product, ops) access to structured data without involving engineering. | Deploy Mathesar into the same VPC as RDS with minimal friction. Configure DB connection using env vars (hostname, username, etc.). Option to self-host Mathesar on an EC2 or EKS instance.  | Can't expose RDS publicly—Mathesar must live in a private subnet or behind IAM-controlled ingress. Must comply with existing AWS security policies. | Will integrate Mathesar into a Terraform or CloudFormation stack.  He expects SSL, secrets handling, and logging to work within existing AWS tooling. | Manages internal tools on AWS, including EC2, RDS (Postgres), and S3. Infra defined with Terraform; uses GitOps-style workflows. Private VPC with RDS instances in isolated subnets, no public access. Uses IAM roles and Secrets Manager for credentials. Services are containerized but deployed via ECS or EC2 AMIs. Requires TLS, audit logging, and secure access paths for all tools.     |
| **🚧⚒️Frances**  | Built the app on Supabase, including its hosted Postgres. She wants to give internal ops \+ support staff controlled access to some tables. | She’s looking for an Airtable-like interface that connects directly to Supabase’s DB without breaking row-level security. | Point Mathesar at a Supabase connection string (with RLS policies respected). Avoid any breakage in JWT-based Supabase auth or PostgREST setup. Run Mathesar via Helm chart alongside other internal tools.  | Must not interfere with production Supabase config or overwrite schema. Wants to reuse existing roles, not manage separate DB access paths. | Will experiment locally first, then deploy if integration is clean.  Not afraid of K8S, Docker, or env files but wants to stay inside known patterns. | Backend built on Supabase; uses its hosted Postgres, auth, and edge functions. No separate backend servers—everything is managed inside Supabase. Uses VSCode and GitHub for coding, Supabase Studio for DB/admin. Postgres connection string used in multiple tools via `.env` files. RLS policies are enforced on tables; auth tokens tie to DB roles. Occasionally deploys internal tools via Helm chart.     |
| **⚒️🧱Gray**  | Maintains datasets in a GCP CloudSQL instance for his research lab.  His grad students keep asking for access or CSV exports. | Wants Mathesar so students can view and edit structured data themselves without messing up raw tables. | Deploy Mathesar as a GCP VM or App Engine app connected to CloudSQL. Secure access with Google Identity SSO. Read-only DB role for most users, one editor role for himself.  | Limited time and budget; cannot babysit the server. Needs support for IP whitelisting or private IP access to CloudSQL. | Follows GCP patterns, uses Google Docs heavily, wants to integrate with what he already knows. | Stores data in a CloudSQL Postgres instance managed by GCP. SSH tunneling or private IP access configured via IAM permissions. Google Workspace account handles all login and identity. Occasionally spins up GCE VMs or Cloud Run instances using the console. DNS is rarely touched; uses direct IPs or auto-generated app URLs. Sensitive research data—access must be auditable, minimal-exposure.     |
| **🚧⚒️Harper**  | Works at a mid-size company with strict data policies.  The Postgres DB runs on bare-metal in a secured internal network. | Wants Mathesar for ops and finance teams to self-serve data reporting, but can’t put data or tools in the cloud. | Install Mathesar inside their firewalled network, ideally via Docker Compose. Configure it to connect to existing internal DB without breaking security assumptions. Manage auth via internal LDAP or SSO.  | No cloud, no external network access, no public Docker Hub. Needs to build from source or use pre-scanned container images. | Reads install docs carefully, runs things on airgapped servers, uses their own CA for SSL certs. | Airgapped internal network, no access to internet or cloud. Services run on physical servers, some virtualized with KVM or VMware. Postgres hosted locally, locked down by firewall \+ VPN access. TLS via internal CA; client machines trust this CA. Uses internal Docker registry; images are scanned and promoted manually. LDAP or Keycloak used for internal identity; no cloud auth permitted. Infrastructure maintained via shell scripts, Ansible, and occasional systemd services.      |
| **⚒️🧱Isa**  | Isa manages a handful of apps for a community org and side projects. She uses CapRover to avoid dealing with Docker or cloud config directly. Her stack includes Ghost, Outline, Plausible, and Postgres (via a CapRover one-click app). | Isa wants to use Mathesar to give non-technical volunteers a way to edit structured data—like translation strings, schedule data, or membership records—without building custom UIs or giving raw DB access. | Isa wants to install Mathesar from an app catalog with a few clicks. She doesn’t want to manage Dockerfiles, ports, or SSL. Must deploy through CapRover’s GUI and use its container orchestration. Prefers UI-based deployment.   | Cannot use command-line tooling to install or configure apps. Might use built-in Postgres from the platform or link to external DB. Will not run SSL setup scripts or reverse proxies manually. Prefers apps that behave like other CapRover-deployed tools—one click, then domain \+ login.  | Isa starts by scanning CapRover’s “One Click Apps” list for anything that might be a UI for Postgres. If Mathesar isn’t there, Isa looks for a `captain-definition` file or a deployable Docker image with clear setup instructions. Isa uses the CapRover UI exclusively—logs into the dashboard, picks “Apps > One Click App,” fills out env vars in a web form, and clicks deploy. Once deployed, Isa uses the “Visit App” button in CapRover to verify it loads under HTTPS. Isa pastes in DB credentials during setup, copied from CapRover’s own Postgres app output. If Mathesar doesn’t connect on first try, Isa reopens the CapRover UI and looks for logs via the “App Logs” tab. After first login, Isa manually creates 2–3 user accounts and sends links to teammates via email. If any problems arise, Isa searches the Mathesar GitHub issues, CapRover forums, or posts a question tagged "self-host" on a community thread.       | CapRover installed on a small VPS (1 core, 2 GB RAM, 50 GB SSD). CapRover's one-click Postgres container already running. Uses CapRover UI to deploy all services. Public domain with auto-SSL via CapRover’s built-in Let’s Encrypt integration.   |
| **🚧John** | John is a macOS-native developer who tries out new open source tools locally before considering them for work or side projects. Uses `brew` for everything: installs Redis, postgres, psql, httpie, etc. | John saw Mathesar on GitHub or Hacker News and wants to see if it’s a viable lightweight Airtable replacement. His DB is a local Postgres instance from Homebrew, already populated with app data. | He installs Mathesar with `brew install mathesar` or `brew tap mathesar/cli`. Expects a local server to run with `mathesar start` and launch in browser. Uses embedded Postgres for local test, or connects to test DB.  | Doesn’t use Docker unless necessary. Avoids GUI installers or browser-based setup wizards. Will abandon the tool if local install takes more than 10 minutes or requires registering accounts. Needs good local defaults. Fast setup and teardown expected.   | John finds Mathesar through GitHub or a blog post and immediately runs `brew install mathesar` or `brew tap mathesar/tap`. <br>After install, John runs `mathesar start`, expects it to spin up locally and open `http://localhost:8000` in the browser. <br>If it asks for DB config, John pastes in a connection string to his local dev database (`postgres://noah@localhost/myproject_dev`)<br>John tests the UI using real data from a side project—opens a table, changes a few rows, checks Postgres in another terminal to confirm it worked. <br>Any time something doesn’t work, John opens Console.app or terminal logs to look for stack traces or port conflicts.<br>John may file a GitHub issue or PR if something’s broken, but will move on if the tool isn’t usable in 10–15 minutes. <br>If satisfied, John may suggest the team use it internally, fork the repo, or write a wrapper script for quick reuse. | macOS Sonoma, using Terminal + iTerm + brew. <br><br>Local Postgres installed via `brew install postgresql@15`<br><br>Runs local services via `brew services start postgresql`. <br><br>Data lives in `myproject_dev` DB.<br><br>No Docker installed, avoids Compose setups for tests. |

## Ecosystem Research

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
