# SSO (OIDC)

!!! example "Add stakeholders"
	Add new stakeholders to the table below.

| **Role** | **Person** | **Status** |
|-|-|-|
| **Author** | Kriti Godey |  🟢 Done |
| **Reviewer** | Brent Moran | 🔵 In review |
| **Reviewer** | Zack Krida | 🔵 In review |

## The Problem

Mathesar users would like to reduce the number of separate passwords they need to use.

Mathesar admins would like:

- All of their internal users using the same secure login that can be managed in one place.
- Reuse their existing groups and roles.
- Create users automatically and avoid manual work to create users.

Mathesar maintainers would like Mathesar to be adopted at organizations with IT policies that require SSO.

### Pain points for users

* The current user creation process in Mathesar involves setting up users through the UI, plus getting them credentials manually. It's slow and cumbersome.
* Organizations that use SSO cannot benefit from their SSO setup when using Mathesar.
* Separate passwords also create a security risk, especially for a tool like Mathesar that may connect to a production database.
* People ***don’t adopt Mathesar*** because of this.


### Why it's worth solving

We are currently focusing on major issues that are blocking people from adopting Mathesar. **SSO is one of the lowest effort / highest impact ways to do that.** It has [several comments and upvotes](https://github.com/mathesar-foundation/mathesar/discussions/2291) in our GitHub.

SSO may also help us grow Mathesar adoption, because:

* Other products charge for SSO as part of their open core offering, but we would be releasing it under GPL.
* Mathesar supports Postgres DB-based permissions, but organizations who care about access control enough to use it are also likely to care about SSO.

### Is it feasible to solve?

Yes! We use Django for our users.

* [juanifioren/django-oidc-provider](https://github.com/juanifioren/django-oidc-provider)  
* [jazzband/django-oauth-toolkit](https://github.com/jazzband/django-oauth-toolkit)  
* [mozilla/mozilla-django-oidc](https://github.com/mozilla/mozilla-django-oidc)  

Further feasibility research is unnecessary, it should be quick to implement. I briefly considered just implementing it instead of writing this.

## Success Criteria

How we'll know we've succeeded with our goals for adding SSO:

* We should transition [internal.mathesar.org](http://internal.mathesar.org) to this login style and not hate it.  
* We track SSO usage growing in analytics.  
* We see an uptick in conversion from our website (after we advertise SSO)  
* We see qualitative positive user feedback on GitHub / Reddit, etc.

## Requirements

### Minimal Scope

Setup:

* Configure OIDC (Google Workspace / Okta / Auth0, etc) via config file.  
* Restrict access to a specific email domain in config.  
* Manually pre-create accounts and link to OIDC identities, at minimum.  
* Define a default Postgres role for all SSO users in the config file.

Maintenance:

* Retain fallback login method in case SSO is misconfigured.  
* Get clear error messaging for others if login fails.  
* See clear error if a user is unauthorized based on domain or mapping.

End user experience:

* Users see a “Sign in with Google” / “Sign in with Okta” option on the login page.  
* Sign in and immediately access the right data without manual setup.  
* Use their existing work account to access data self-serve.

Documentation:

* Access clear documentation for OIDC setup, domain restriction, role mapping, and debugging.

Analytics (for us):

* Track SSO setup as an event in analytics.

### Full Scope

Assuming we can do the full scope without too much additional effort, we should do so, since it will make Mathesar useful for a much wider variety of users.

JIT provisioning:

* Automatically provision accounts on first login. No manual creation of users needed.  
* View group claims received from IdP and role assignment in logs, to help debug issues.  
* Understand why a user failed to authenticate or received incorrect access.

Group-based role mapping:

* Map IdP groups to Postgres roles via config.  
* Automatically assign roles based on IdP group membership.

Merging users automatically:

* Signing in with username/password or SSO should be the same account if the email is the same.
	
## Use Cases

This is background information that I used to help me think through the requirements. I started with the use cases first and derived everything else from there. The use cases are made up, but people have described their use cases on [our SSO (single sign-on) support GitHub discussion](https://github.com/mathesar-foundation/mathesar/discussions/2291), which may also be helpful to read. 

### Most Minimal User: Alice

Alice is a tech generalist who manages databases and IT (among other things) for her 30-person organization, but neither of those are her main job. She wants to set up Mathesar to help non-technical people who need access to data self-serve. 

Their organization uses Google Workspace to manage accounts, and she knows that if Mathesar doesn’t support Google Workspace login, she’s going to have more tech support on her hands, not less. She also wants to ensure that users accessing the DB through the Mathesar UI use a Postgres role with limited permissions.

Since they have a small organization, she doesn’t mind creating/updating/deleting the users manually in Mathesar. She does need to configure email domain based whitelisting in Mathesar, and she'd like to be able to set the default Postgres role for all users, rather than have to set a role for individual users. Deprovisioning is not a priority because once they lose access to their Google email, they can’t get into Mathesar either.

Alice already has Google Workspace set up. She’s fine with doing the configuration on the command line or through config files. All she needs is:

1. A way to configure Google Workspace SSO in Mathesar. (Google supports both OIDC and SAML).
2. A way to limit who can access Mathesar to a particular email domain.
3. A way to set up what Postgres role people automatically get when they sign in – a single role is fine.
4. A way to create users in Mathesar and map them to the accounts they’ll be signing in with – manual is fine.
5. A UI for users to log in to Mathesar with their Google account.

#### User stories

Alice (tech generalist, small org admin)

* As Alice, I want to configure OIDC SSO with our Google Workspace account via a config file so that my users can sign in with their Google accounts.  
* As Alice, I want to restrict Mathesar access to users with a specific email domain so that unauthorized users can’t sign in even if they have a valid Google account.  
* As Alice, I want to define a default Postgres role in the config file that all SSO-authenticated users get, so that they don’t accidentally have too much access.  
* As Alice, I want to either pre-create user accounts in Mathesar and link them to their Google account or have Mathesar automatically create user accounts linked to the Postgres role in the config file, for anyone new that signs in from the specific email domain.  
* As Alice, I want my users to see a login screen that includes a “Sign in with Google” button so they can access Mathesar easily without needing credentials from me.

David (non-technical staff at Alice’s org)

* As David, I want to sign in to Mathesar using my Google Workspace account so I don’t have to remember a new password or ask Alice for access.
* As David, I want to be granted access with the right permissions when I sign in so I can immediately use the product without extra steps.

### More Common User: Bob & Carol

Bob works on the data science team at a 80-person company, and often collaborates with non-technical users e.g. sales and customer success. They also work with a team of outsourced data entry workers to populate their data. 

Mathesar would really make his job easier by allowing the data entry team to input data directly and simplifying data gathering. Mathesar would also allow the sales and support team to self-serve without the data science team being a bottleneck. Bob needs to work with Carol, his organization's IT person, to install Mathesar.

Carol is comfortable installing Mathesar and connecting to their production database as long as Mathesar supports the following:

* Integration with Okta / Auth0, the identity provider used in the organization.  
* Separate Postgres roles for the data entry people, sales, and customer success – with proper RBAC. Carol is willing to set these up manually through `psql`.
* Automatic provisioning of roles based on groups – Carol does not want to make individual users, Carol has already set up groups in Okta and wants Mathesar to assocale ‘sales’ in the authorization headers with the ‘sales’ DB role, etc.  
* Documentation on how all this works, so Carol can learn about Mathesar comfortably.  
* Some information on how to debug failures, if someone can’t log in.

Carol also needs the basic requirements that Alice needs. Carol still doesn’t need a UI for any of this.

#### User stories

Bob (power user at medium org, internal advocate)

* As Bob, I want Mathesar set up at our organization so that I have more time to devote to data science and less to logistics.  
* As Bob, I want to hand off SSO configuration to our IT admin but still use Mathesar confidently once access is set up.  
* As Bob, I want to enable multiple Postgres roles for different kinds of users so that each group gets only the access they need.

Carol (IT admin, medium org)

* As Carol, I want to configure OIDC SSO via a config file using our existing IdP (e.g., Okta/Auth0) so that I don’t have to create new identity workflows.  
* As Carol, I want to map IdP groups to specific Postgres roles in a config file so that access is automatically assigned based on group membership.  
* As Carol, I want to see logs showing which groups were received in the login assertion and what role was assigned, so I can debug access issues.  
* As Carol, I want clear documentation explaining how to configure OIDC, role mapping, and email domain restrictions so I can deploy Mathesar without reverse engineering.  
* As Carol, I want Mathesar to show users an unauthorized error if they don’t match allowed domains or mappings so that access failures are clear and traceable.  
* As Carol, I want a fallback login method to remain available so I don’t get locked out if the IdP is misconfigured.

Frank (data entry contractor)

* As Frank, I want to sign in using my work email and immediately have access to the parts of the database I need, without having to be invited or manually added.

Grace (customer success team)

* As Grace, I want to access live customer data in Mathesar by signing in with my usual company account so that I can self-serve metrics without waiting on the data team.
