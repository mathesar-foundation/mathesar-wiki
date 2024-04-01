# Permissions - Revamp

This spec describes the revamped product considerations for managing Permissions within Mathesar. This is targetted towards the Beta release.

## Goals
A. Improve our permissions architecture and user flows to utilize PostgreSQL's permission system for DB objects.
  * Our current permission handling is custom written and managed entirely within the Mathesar service layer.
  * Several users have expressed interest towards using PostgreSQL roles, a few even mentioned that it's a blocker for them to start using Mathesar.
  * Building our permission layer on top of PostgreSQL's permission system is future-proof and robust.
B. We should try to maintain feature parity with the flows we currently have.

## Features we intend to remove
* We will remove the ability to share credentials across databases.
  - We currently have this while creating/configuring a database.
  - We will revisit this feature later down the road when we have requirements from users.

## Terminologies
* User refers to Mathesar user.
* Admin refers to Mathesar admins.
* Role refers to PostgreSQL role/user.

## What we want the user to be able to do
### Adding/configuring a database
* A database should be unique. The same database cannot be added multiple times.
  - This is a change from the existing setup where a database can be added multiple times with different connection credentials.
#### Pre-existing database
* Mathesar admins should be able to configure a pre-existing database, using the following details:
  - DB server Host
  - DB server Port
  - Database name
  - PostgreSQL role -> username and password
* Mathesar admins should be able to optionally generate pre-defined roles for Manager, Editor, and Viewer, to satisfy Goal (B).
  - These roles will have similar hierarchial permissions to what we currently have at the database level.
  - This requires the PostgreSQL role used in the previous step to contain CREATEROLE attribute on the database server.
  - This step is optional and Mathesar should function normally without these roles.
#### New database
* Mathesar admins should be able to create a new database on the internal database server by only entering the database name.
  - This will use the same role utilized by the Django database.
    - The user should be able to change this, if they wanted to.
  - The role used should contain both CREATEDATABASE and CREATEROLE privileges.
* Mathesar admins should be able to create a new database on external servers, by specifying the same details as the 'pre-existing' database configuration.
  - The role used should contain both CREATEDATABASE and CREATEROLE privileges.
  - These privileges should be tested and proper errors and rectification steps should be provided to the admin.
* Pre-defined roles should be automatically created in this setup.

### Role configuration
* Admins should be able to configure existing roles in a database server, within a database page.
  - Wherever possible, we should reflect roles that already exist and let the admin add them by specifying the password.
* Admins should be able to create new roles on the database server and associate them with the database.
  - This will require the role used by the admin to have CREATEROLE privilege.
* Future considerations:
  - Roles exist on the database server and not under a database.
  - However, inorder to simplify the user flow, we are not introducing a UX dedicated for database servers.
  - We can explore this option in the future, based on user feedback or product strategy discussions.

### Access control options
* Admins should be able to provide Mathesar users access to each database configured in Mathesar.
* Each Mathesar user, including admins, should only be associated with a single role per database.
  - Admins should be able to update this user-to-role configuration.
* All Mathesar admins should be able to access all databases configured in Mathesar. Admins cannot be removed from a database.
  - When a Mathesar admin is newly added into the product, they will automatically be provided the 'default role' for all databases.
  - The concept of a 'default role' is explained further below in this document.
* The role for admins can be changed.
  - This can be restricted to reduce scope and we could mention that admins will always assume the default role.
  - The challenges are mentioned in further below in the 'Dealing with Ownership and Collaboration issues' section of this document.
* Standard Mathesar users can be added/removed from a database.
* Standard Mathesar users will not be able to access a database without being provided explicit access by a Mathesar admin.
* The permissions for DB objects will be determined by the priviliges of the role the user is associated with.
* For Mathesar specific objects, we will have a setting per user per database that allows the user to 'read' or 'read-write'.
  - This applies for explorations and metadata such as table and column settings.
  - Future consideration:
    - We can allow an additional option 'Infer from DB privileges' that will automatically identify access to each Mathesar-object based on the privileges on the underlying DB objects.

### Schema level access control options
* If a user has ownership access (or appropriate GRANT priviliges) to a schema based on their underlying role, they should be able to grant/revoke access to that schema to other roles configured in Mathesar.
* While granting access to a role, the user can choose access control at three different levels.
  - manage: USAGE, GRANT, SELECT, INSERT, UPDATE, DELETE, SET and ALTER
  - edit: USAGE, SELECT, INSERT, UPDATE, DELETE, SET and ALTER
  - view: USAGE, SELECT
* This setting will iteratively apply to all objects within the schema.
* For schemas created using the Mathesar UI, we will automatically grant view access to all configured roles, manage access to the 'default role', and we will provide access accordingly for auto-generated roles.
* This will not be present for the 'public schema'.
  - It should be made clear to the user that all users can access the public schema.
* The UX should make it clear that the roles are the ones being granted access, and should display a list of users per role to make it easier for the user to understand which Mathesar users get access.
* In the future, this option will be extended to all DB objects such as tables and views.

### Default role
* There should be one default role per database.
* When a database is first configured, the role used to connect to the database will be set as the default role.
* When new admins are added to an existing Mathesar instance which contains a number of databases, they will have access to all those databases by utilizing default roles (which are configured per database).
* It is also used to deal with ownership issues, mentioned later in this document.
* The default role cannot be changed. 
  - We can provide this option in the future.
  - This restriction is to reduce scope since changing the default role has more considerations such as changing ownerships.
* The other way to think of this role is as 'Mathesar server's role to connect to the database for operations that do not directly involve a user'.

### Dealing with Ownership and Collaboration issues
* PostgreSQL has ownership for all DB objects.
* Tables created by one role cannot be viewed/accessed by another role, unless the access is granted explicitly.
* When tables/schemas are created via Mathesar UI, it will cause collaboration issues among Mathesar users if they utilize different roles.
* We will be handling this by following the steps below:
  * When a DB object is created via the UI, the ownership is transferred to the 'default role'.
    - This is to maintain a cleaner ownership distinction between objects created using Mathesar and objects created externally.
    - It would be best for us to prevent changing the 'default role'.
      - If we allow updating it, we should also automatically transfer ownerships.
  * The user and their associated role that originally created the object via the UI will be granted all privileges including 'GRANT', but it will not be the owner.
  * All other priviliges are granted automatically to each role configured within Mathesar.
  * For auto-generated roles i.e. Manager, Editor, and Viewer, this will be granted in a granular restricted manner based on the role.
* We will still face collaboration issues when objects are created outside of Mathesar, however, we could handle that by mentioning in our docs to grant access to the 'default role' for any objects users create outside of Mathesar.
  - This way Mathesar admins will have access to those objects and can grant privilges within Mathesar accordingly.

## Related
- [Brent's architecture notes](https://github.com/mathesar-foundation/mathesar-wiki/pull/108)
- [Permissions for Beta - approaches & comparison](https://hackmd.io/@mathesar/Hkads67nT)
- [Rough figma design to explain permissions approach for Beta](https://www.figma.com/file/S97Mma0hAy5Syh1w85RWoB/Permissions-UX?type=design&node-id=109-98&mode=design)
