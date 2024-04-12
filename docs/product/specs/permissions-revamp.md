# Permissions - Revamp

This spec describes the revamped product considerations for managing Permissions within Mathesar. This is targetted towards the Beta release.

## Goals
- A. Improve our permissions architecture and user flows to utilize PostgreSQL's permission system for DB objects.
  * Our current permission handling is custom written and managed entirely within the Mathesar service layer.
  * Several users have expressed interest towards using PostgreSQL roles, a few even mentioned that it's a blocker for them to start using Mathesar.
  * Building our permission layer on top of PostgreSQL's permission system is future-proof and robust.
- B. We should try to maintain feature parity with the flows we currently have.
- C. Provide a rudimentary UX for ownerships and get users aquainted with the concept.

## Features we intend to remove
* We will remove the ability to share credentials across databases.
  - We currently have this while creating/configuring a database.
  - We will revisit this feature later down the road when we have requirements from users.
* Mathesar admins will no longer be able to create a new database on external database servers (servers that do not contain the Django DB).

## Terminologies
* User refers to Mathesar user.
* Admin refers to Mathesar admins.
* Role refers to PostgreSQL role/user.

## What we want the user to be able to do
### Adding/configuring a database
* A database should be unique. The same database cannot be added multiple times.
  - This is a change from the existing setup where a database can be added multiple times with different connection credentials.
* We'll have separate onboarding instructions/flows in the UI for pre-existing and new databases.

#### Pre-existing database
* Mathesar admins should be able to configure a pre-existing database, using the following details:
  - DB server Host
  - DB server Port
  - Database name
  - PostgreSQL role -> username and password
* Mathesar admins should be able to optionally generate pre-defined roles for Editor, and Viewer, to partially satisfy Goal (B).
  - This requires the PostgreSQL role used in the previous step to contain CREATEROLE attribute on the database server.
  - This step is optional and Mathesar should function normally without these roles.
  - We should make it clear that these roles & their privileges would only apply for new objects created via the Mathesar UI.
  - For existing objects, we'll provide an option to iteratively provide privileges to these roles.
    - This will however depend on ownerships of each object and can fail.
  - We will no longer have the manager role as it would be the same as having admin access.
    - Future consideration: We could provide a concept of database admins as a Mathesar level access control option per database. This will help maintain feature parity with the 'DB level admins' feature we currently have.
#### New database
* Mathesar admins should be able to create a new database on the internal database server by only entering the database name.
  - This will use the same role utilized by the Django database.
    - The user should be able to create new roles on the internal db and use them if they wanted to.
  - The role used should contain both CREATEDATABASE and CREATEROLE privileges.
  - (Internal database server refers to the database server that contains the Django DB. It could be on a different host)
* Pre-defined roles should be automatically created in this setup, similar to pre-existing databases.

### Role configuration
* Admins should be able to configure existing roles in a database server, within a database page.
  - Wherever possible, we should reflect roles that already exist and let the admin add them by specifying the password.
* Admins should be able to create new roles within a database page. 
  - This will require the role used by the admin to have CREATEROLE privilege.
  - The new  roles will be created on the database server that the database belongs to and have CONNECT and CREATE privileges on the database.
  - The new roles will also have SELECT access to all items on the database that the role used by the admin has.
* Future considerations:
  - Roles exist on the database server and not under a database.
  - However, inorder to simplify the user flow, we are not introducing a UX dedicated for database servers.
  - We can explore this option in the future, based on user feedback or product strategy discussions.

### Access control options
#### Configuration
* Admins should be able to provide Mathesar users access to each database configured in Mathesar.
* Each standard Mathesar user should only be associated with a single role per database.
  - Admins should be able to update this user-to-role configuration.
* All Mathesar admins should be able to access all databases configured in Mathesar.
  - See 'Role for admins' section on how roles are used by Admins.
* Admins cannot be removed from a database.
* Standard Mathesar users can be added/removed from a database.
* Standard Mathesar users will not be able to access a database without being provided explicit access by a Mathesar admin.

#### Permission checks for objects
* The permissions for DB objects will be determined by the priviliges of the role the user is associated with.
* For Mathesar specific objects, we will have a setting per user per database that allows the user to 'read' or 'read-write'.
  - This applies for explorations and metadata such as table and column settings.
  - Future consideration:
    - We can allow an additional option 'Infer from DB privileges' that will automatically identify access to each Mathesar-object based on the privileges on the underlying DB objects.

#### Role for admins
* An admin is not associated with a single role.
* Admins should be able to utilize any role that's configured for a database.
* When an admin opens a DB object, lets say a table,
  - If the owning role of that table is configured, then any operation performed by the admin will utilize that role.
  - If the owing role isn't configured, we'll try to figure out the best role for the admin to use. In cases where it's not possible, we will use the `default` role.
* More information is provided in the 'Default role' and 'Dealing with Ownership and Collaboration issues' sections of this document.

### Default role
* There should be one default role per database.
* When a database is first configured, the role used to connect to the database will be set as the default role.
  - This role is used for installing/upgrading the functions on the DB.
* The default role cannot be removed.
  - This will ensure that the admins have atleast one role to connect to the database.
* The default role cannot be changed. 
  - We can provide this option in the future.
  - This restriction is to reduce scope since changing the default role has more considerations such as changing ownerships for the installed functions, which might affect upgrades.

### Dealing with Ownership and granting access
#### Considerations
* PostgreSQL has ownership for all DB objects.
* Tables/schemas created by one role cannot be viewed/accessed by another role, unless the access is granted explicitly.
* When tables/schemas are created via Mathesar UI, it may cause collaboration issues among Mathesar users if they utilize different roles.

#### Approach for tables
* When a table is created via the UI, the ownership will belong to the role of the Mathesar user that created that object.
  * Admins will have access to all roles on the DB and hence will be able to use the role that created the table and obtain full ownership.
  * Standard users associated with that role will be able to perform all operations.
* Ownerships should be conveyed on the UI for each table.
  - This should show the owning role and the users associated with that role.
* Owners can GRANT access to the object to other roles via the UI, at the following levels:
    - edit: SELECT, INSERT, UPDATE, DELETE
    - view: SELECT
* They should also be able to do this in a granular manner if they choose to.
* Owners can also allow users to GRANT these privileges to other users.
* If a user has GRANT access for any of the privileges, they should be able to provide the same privilege with GRANT to others via the UI.
* We will utilize the same approach for other similar DB objects such as views, when we implement them.

#### Approach for schemas
* Schemas should display the owning role and all Mathesar users with access to that role.
* When creating a schema via the UI,
  * Users should be able to set default privileges for the objects in the schema for other roles to use, while creating the schema.
  * We should allow granting access at the following levels:
    - edit: USAGE (for schema), SELECT, INSERT, UPDATE, DELETE
    - view: USAGE (for schema), SELECT
* For existing schemas,
  * Owners should be able to set default privileges for the objects in the schema, for other roles to use.
    - This will be at the same levels as mentioned above.
  * We should allow the user to iteratively update permissions for all existing objects present in the schema.
  * There is a chance that the schema owner does not have access to an underlying table, in which case, we will not do anything.
    - The owner of the table can still see that the schema owner does not have access and choose to provide access via Mathesar UI.
* Public schema:
  - Public schema access changed in PG 15 where the database owner is now the owner for it and access to other roles needs to be explicitly granted.
  - We'll detect PG version and have separate flows for PG version <15 and >=15.

#### Notes
* We will still face collaboration issues when objects are created outside of Mathesar, however, we could handle that by mentioning in our docs and on the UI to grant access to the 'default role' for any objects users create outside of Mathesar.
  - This way Mathesar admins will have access to those objects and can grant privileges within Mathesar accordingly.

## Related
- [Brent's architecture notes](https://github.com/mathesar-foundation/mathesar-wiki/pull/108)
- [Permissions for Beta - approaches & comparison](https://hackmd.io/@mathesar/Hkads67nT)
- [Rough figma design to explain permissions approach for Beta](https://www.figma.com/file/S97Mma0hAy5Syh1w85RWoB/Permissions-UX?type=design&node-id=109-98&mode=design)
- [DB object ownership meeting](https://tldv.io/app/meetings/660d6f5b8b0707001237cf0e)
