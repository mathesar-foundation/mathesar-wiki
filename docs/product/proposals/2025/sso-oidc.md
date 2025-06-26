# SSO (OIDC)

| **Role** | **Person / Item** | **Status** |
|-|-|-|
| **Requirements** | [SSO (OIDC) requirements](/product/requirements/2025/sso-oidc) | |
| **Author** | Kriti Godey |  🟢 Done |
| **Reviewer** | Brent Moran | 🔵 In review |
| **Reviewer** | Zack Krida | 🔵 In review |

## Solution

Yes! We use Django for our users, and there are several libraries we can just drop into our codebase.

* [juanifioren/django-oidc-provider](https://github.com/juanifioren/django-oidc-provider)  
* [jazzband/django-oauth-toolkit](https://github.com/jazzband/django-oauth-toolkit)  
* [mozilla/mozilla-django-oidc](https://github.com/mozilla/mozilla-django-oidc)  

## Tradeoffs

Things to watch out for while implementing:

* Adding more scope to these requirements for the feature to be “more useful”.  
	* e.g. “SAML isn’t that much harder…”  
* Over-indexing on all user needs. This is an initial MVP and won't solve everyone’s needs and that's okay. We can always add more features later.

This is explicitly an MVP, so the following things are out of scope:

Authentication Methods:

* No SAML support (OIDC only)  
* No support for IdP-initiated login flows (SP-initiated only)  
* No social login (e.g. GitHub, Facebook, etc.)  
* No password-based SSO fallback except for Mathesar admins.

Provisioning and Role Management:

* No SCIM or automatic deprovisioning  
* No UI for managing users, roles, or SSO config  
* No per-user or per-session role overrides  
* No multi-role assignment per user  
* No support for assigning roles via UI or API based on group claims (config file only)

Access Control:

* No support for multi-tenancy or per-project IdP config  
* No other permissions mapping beyond Postgres roles  
* No email-based whitelists beyond domain restriction  
* No support for conditional logic on access (e.g. “this group *and* this claim”)

Observability and Admin Tools:

* No UI for viewing login attempts, group mappings, or audit trails  
* No real-time SSO diagnostics or health checks  
* No alerting for failed logins or misconfigurations

User Experience:

* No role-selection prompt on login  
* No way for end-users to request access or change roles  
* No customization of login UI

## High-Level Implementation Plan

!!! example "Create high-level plan."
	- Types of work needed: design / backend / frontend / documentation / other.
	- Types of work output for each type of work.
	- Stakeholders / reviewers / implementers.
	- Infrastructure needs.
	- Workflow: who does what, in what order.
	- Rough timeline.

## Community Engagement

We should:

- seek input from community members who have asked for SSO, to ensure that we're building the right set of features and addressing their use cases.
- update mathesar.org and our `README.md` to include SSO in tandem with the next release.
	- On mathesar.org, this should include the homepage, product page, and a few use cases.
- consider posting on self-hosting communities to let people know that we have SSO.
- consider adding ourselves to https://ssotax.org/friends-of-sso.html
