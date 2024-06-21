# Permissions - Revamp

This spec describes the revamped product considerations for managing Permissions within Mathesar. This is targetted towards the Beta release.

## Goals
1. Improve our permissions architecture and user flows to utilize PostgreSQL's permission system for DB objects.
	1. Our current permission handling is custom written and managed entirely within the Mathesar service layer.
	1. Several users have expressed interest towards using PostgreSQL roles, a few even mentioned that it's a blocker for them to start using Mathesar.
	1. Building our permission layer on top of PostgreSQL's permission system is future-proof and robust.
1. We should maintain feature parity with the flows we currently have.

## Terminologies
* User refers to Mathesar user.
* Admin refers to Mathesar admin.
* Role refers to PostgreSQL role/user.
* Group refers to any PostgreSQL role that is inherited by another role.

## Adding a database
- Only Mathesar admins can add new databases.
- When adding a database:
	- Mathesar admin will provide:
		- database server host
		- database server port
		- database name
		- a db login role username
		- a db login role password

## Granting Mathesar users collaboration access to a database
- Only Mathesar admins can grant Mathesar users collaboration access to databases.
- Inorder to do add a Mathesar user as a collaborator to a database:
	- Mathesar admins would have to specify a *Login DB role* for the Mathesar user to connect to the database.
	- The *Login DB roles* will be automatically reflected. The admin can choose one of them.
		- (Refer Role management section for more details).
- Admins can change their own login role.
- Only admins can change the login roles of other Mathesar users.
- Only admins can remove Mathesar users from a database.
- Initially, only the admin who connected to the database will have access to it.
	- They will automatically be assigned the login role that was used to connect to the database.
- Any Mathesar admin can add themselves as a collaborator to any database configured in Mathesar.

## Role management
- Mathesar will reflect all roles in a database server.
- Inorder to configure a Login DB role in Mathesar:
	- For a pre-existing login role,
		- the admin would have to enter the password for the Login DB role and configure it in Mathesar.
	- To create a new login role,
		- the role used by the admin will need to have CREATEROLE privilege.
		- the admin would have to specify a username and a password.
		- this role will automatically get a CONNECT and CREATE privilege on the database.
- Admins can remove the configured login roles.
	- This will simply remove the stored password in the internal database.
	- The role will still be displayed but Mathesar cannot connect using the role since it would not have the password.
- Admins can drop login roles configured in Mathesar.
	- If the admin's role has CREATEROLE privilege and ADMIN OPTION over a role ([Refer PG docs](https://www.postgresql.org/docs/current/sql-droprole.html#:~:text=To%20drop%20a%20superuser%20role,will%20be%20raised%20if%20so)), the admin will have an UI option to drop the role in the underlying DB.
	- Before deleting a role, the objects owned by the role need to be transferred to another role/group.

## Group roles
- Any Mathesar user having a role that has CREATEROLE privilege can create new non-login roles (i.e. a group roles) via the Mathesar UI. ([Refer PG docs](https://www.postgresql.org/docs/current/role-membership.html)).
- The user's role that created a group role will be able to grant membership to it for other users' roles.
	- This role would have ADMIN OPTION on the group role. We'll refer to it as admin access on the UI.
- When granting membership, the user that created the group can choose if other roles should have admin access or normal membership on the group role.
- If a role has admin access over a group, the users with that role can:
	- grant/revoke memberships for other roles
	- delete the group
		- Before deleting a group, the objects owned by the group need to be transferred to another role/group.
	- rename the group
- Normal members will only be able to use the group role for sharing ownerships. They will not be able to manipulate the group itself.
- For pre-existing roles on the database:
	- Admin access can be determined for existing group roles on the database by checking if the user's role has ADMIN OPTION on it ([Refer PG docs](https://www.postgresql.org/docs/current/sql-grant.html#:~:text=The%20ADMIN%20option%20allows%20the,WITH%20ADMIN%20OPTION%20on%20itself)).
	- Membership can be determined by checking if the user's role has SET ROLE, or INHERIT privileges.

## Ownership of DB objects
* When creating a new DB object, the user will have an option to choose the owner. They will not be able to create new roles here. They can set the owner to:
	* their own login role (this is the default selection)
	* one of the group roles they are a member of
* The owner of an object can transfer the ownership to any login or group role configured in Mathesar.

### Ownership of container objects
* Owning a container object such as a schema does not guarantee owning objects within it. We will make this behaviour clear to the user using appropriate documenation in the UI and our docs. 
* We will support recursive reassignment of ownership of contained objects for which the user's role has ownership of. This will be an optional checkbox.
	* For eg., while transfering ownership,
		* for schemas, we will display a list of tables within it whose ownership belong to the user's role (or any of their group roles).
		* the user can choose to transfer ownership for the schema along with this subset of tables within it.

## Providing access to DB objects
* The owner can provide access to DB objects to other roles in the following ways. We will present a dropdown in the case of schemas & tables.
	* Database
		* Connect to database (CONNECT)
		* Create schemas in database (CREATE)
		* No access
	* Schema
		* Use schema (USAGE)
		* Create tables within schema (USAGE & CREATE)
		* No access
	* Table
		* View table (SELECT)
		* Edit table rows (SELECT, INSERT, UPDATE, DELETE)
		* Custom (the user can select granular privileges)
		* No access
* We will not allow any user other than the owner to manage permissions, for the beta release.
	* This includes users who have WITH GRANT over some of the privileges.

## Explorations & Table Metadata
All Mathesar users will have full control over explorations & table metadata in the databases they have access to.
