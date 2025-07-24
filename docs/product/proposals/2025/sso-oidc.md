# SSO (OIDC)

!!! success "Project approved, implementation [tracked in GitHub](https://github.com/mathesar-foundation/mathesar/issues/4578)."

## Solution

Based on [these requirements](../requirements/2025/sso-oidc.md).

### High level plan

We use Django for our users, and there are several libraries we can just drop into our codebase.

* [juanifioren/django-oidc-provider](https://github.com/juanifioren/django-oidc-provider)  
* [jazzband/django-oauth-toolkit](https://github.com/jazzband/django-oauth-toolkit)  
* [mozilla/mozilla-django-oidc](https://github.com/mozilla/mozilla-django-oidc)  

OIDC is a protocol and any OIDC IdP can be used once we implement one of those libraries. For example, the [Mozilla Django OIDC](https://mozilla-django-oidc.readthedocs.io/en/stable/installation.html#quick-start) library's setup involves setting up:

```
OIDC_RP_CLIENT_ID = os.environ['OIDC_RP_CLIENT_ID']
OIDC_RP_CLIENT_SECRET = os.environ['OIDC_RP_CLIENT_SECRET']
OIDC_OP_AUTHORIZATION_ENDPOINT = "<URL of the OIDC OP authorization endpoint>"
OIDC_OP_TOKEN_ENDPOINT = "<URL of the OIDC OP token endpoint>"
OIDC_OP_USER_ENDPOINT = "<URL of the OIDC OP userinfo endpoint>"
# optional
OIDC_RP_IDP_SIGN_KEY = "<OP signing key in PEM or DER format>"
OIDC_OP_JWKS_ENDPOINT = "<URL of the OIDC OP jwks endpoint>"
```

Someone setting this up with Google Workspace would set up an internal [OAuth app](https://developers.google.com/identity/openid-connect/openid-connect) and then configure the above stuff using the info they got there. If they used a different provider e.g. Okta, they'd get the OIDC info from there.

### Implementation checklist

#### Integration Setup
* Pick an OIDC Django library (e.g., `mozilla-django-oidc`) and validate it supports configurable claims, custom user creation, and multiple providers.
* Add the chosen library to the codebase and set up minimal working OIDC flow.
* Define a config file format (e.g., YAML or JSON) for OIDC providers and role mappings.
* Implement config loader that parses this file and exposes settings to Django.
* Implement on/off switch for SSO in the configuration.

#### Authentication Flow
* Wire up Django auth to use the OIDC library's login flow (override login view if needed).
* Implement domain restriction check using `email` claim and allowed domain(s) from config.
* Add logic to handle fallback login (e.g., allow username/password login even if OIDC is enabled).
* Implement user lookup or creation on OIDC login based on email claim.
* Add optional merging logic if user already exists with same email but no OIDC identity.

#### Claims & Role Mapping
* Extract claims from ID token and/or UserInfo response (choose priority or allow both).
* Implement configurable mapping of claims to Postgres roles via config file.
* Allow fallback to a default role if no mapping matches.
* Support optional claim match modes: exact match, substring match, or regex (optional but useful for Okta-style groups).
* Assign Postgres role to Mathesar user object at time of login or provisioning.

#### User Provisioning
* Support just-in-time provisioning of user accounts if no match exists.
* Allow JIT-provisioned users to be assigned default or mapped Postgres roles.

#### Logging & Debugging
* Log received claims at login (to stdout or a debug logger).
* Log domain validation and failure reasons (unauthorized domain, missing claim, etc.).
* Log role mapping process: which claim matched, what role was assigned.
* Return readable error message on login failure, including mismatch reason if available.

#### Documentation
* Write user-facing docs explaining how to configure OIDC login with Google Workspace, Okta, or Auth0 using the config file.
* Include sample config files for each provider.
* Document how role mapping works, including fallback and group claim support.
* Include common troubleshooting scenarios and how to debug login failures.

#### Testing & Internal Use
* Set up Google Workspace OAuth client for internal test deployment.
* Configure internal.mathesar.org to use OIDC login only, with fallback enabled.
* Verify domain restriction, role assignment, and fallback login manually.

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

**Work needed**: 

- Selection of Django library
- Backend work on SSO and configuration (output: PR)
- Documentation work on how to use SSO (output: PR)
	- Can be split into outline + work

**Stakeholders**:

- Anish (implmenter + docs)
- Brent (reviewer + docs)
- Kriti (help with docs, docs and user-facing items approver)
- Zack (coordination + second reviewer if needed)

**Workflow**: usual code workflow + Kriti reviews.

**Rough timeline:** 0.4.0

**Next steps after approval:**

- Update the [project issue](https://github.com/mathesar-foundation/mathesar/issues/4578) with new links.
- Anish: make implementation tasks.
- Implementation proceeds as planned.
 
## Community Engagement

We should:

- seek input from community members who have asked for SSO, to ensure that we're building the right set of features and addressing their use cases.
- update mathesar.org and our `README.md` to include SSO in tandem with the next release.
	- On mathesar.org, this should include the homepage, product page, and a few use cases.
- post on self-hosting communities to let people know that we have free SSO.
- add ourselves to https://ssotax.org/friends-of-sso.html
