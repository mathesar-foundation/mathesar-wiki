# Users and Permissions

The big picture is that we will implement access management for DB objects (including databases themselves) by giving admin users of Mathesar the ability to use database-layer permissions management tools (e.g., `GRANT`). For web service resources (e.g., Django model instances), permissions will be managed in Django.

## Database Model

This model will be reduced to store nothing more than metadata about a given database, as well as its name for use when constructing an actual connection to that database.

## Database Server Model

This model holds the `host` and `port` information for a given database.

## Database Server Credential Model

As described in [the models section](./models.md), This will store the authentication information needed to create an engine, but won't provide a database (a required part of a connection definition in PostgreSQL). Because the information includes a role (to define the initial connection role), it necessarily defines a set of privileges available on the database with that connection.

## User Database Role Map Model

This map uses a `user, database` pair to look up the needed credentials, then provides a connection to the database using those credentials (if possible).

## Adding Connections (backend perspective)

Regardless of UI, the backend should receive a `POST` request to the new RPC endpoint defining a new connection. We'll use the same functions set up in [PR \#3348](https://github.com/mathesar-foundation/mathesar/pull/3348). The relevant info should be stored in the `Database`, `DatabaseServer`, and `DatabaseServerCredential` models. Also, if the user does not already have an entry defining their role on the given database, we could create such an entry automatically in the `UserDBRoleMap` model. This is optional, and doesn't really affect the architecture. Then, to let some other users access that connection, we will provide an RPC function that lets an admin set different users' credentials for the given database by creating or updating `UserDBRoleMap` resources. Note that this does _not_ directly modify anything to do with permissions on actual database objects (e.g., schemata or tables).

## Granting database object privileges

The backend will provide RPC functions that let an admin (who has access to a sufficiently-privileged database role via a connection) access database-level permission granting functionality directly. So, to grant access to create tables in a schema to a Mathesar user, the admin uses an RPC function that defines a privilege-granting query (via a PL/pgSQL function) on the database. Note that this request doesn't actually modify any model instance.

- Privileges on DB objects are thus not granted directly to Mathesar users.
- Privileges on DB objects are granted to DB roles, which may be accessible to some (or all) Mathesar users.
- Anytime an RPC function requiring DB access runs, it runs using the connection defined via the `UserDBRoleMap`, with the associated privileges on that database.

!!! question "UX Question"
    Should the admin think in terms of groups of Mathesar users, or specifically in terms of connections when dealing with DB-level privileges?
    
!!! danger "Potential Confusion"
    In case the admin or DBA want multiple Mathesar users to be able to modify various DB objects, three options are available:
    - Give all relevant Mathesar users access to connect as the owning DB user.
    - `GRANT` the owning DB role (ostensibly a user) to DB users connectable by the relevant Mathesar users.
    - Have at least one DB superuser available for use with a connection, and give relevant Mathesar users access to that DB superuser.
    
## Mathesar object privileges

Examples of such objects are Explorations, and table properties like preview columns or display options. Permissions on these will be:
- None,
- read only, or
- read write
These permissions will be tracked in the `UserDBRoleMap` model via the `metadata_role` attribute. Note that these permissions are only related to CRUD operations on these objects. In the case of Explorations, actually _running_ the exploration is dependent on:
- at least the read permission on the object, and
- the database-level permissions associated with the connection available to the user.

### Current plan

In the case of Explorations (`Exploration` model), this will be derived from a policy scoped via the `Database` associated with the Exploration:

- A super user of Mathesar will set the policy for a given `User` on a given `Database` instance via the UI.
    - When a `User` wants to view/edit/manage an Exploration, the web service will check the `user, database` pair (where `database`) is the `Database` associated with the Exploration to find a relevant policy.
    - Based on the policy, the user can then act on the Exploration.

### Alternative plan

In the case of Explorations (`Exploration` model), this will be derived from a policy scoped via the `Database` associated with the Exploration:

- A super user of Mathesar will set the policy for `DatabaseServerCredential` instances via the UI.
    - Each credential instance represents a Role on the DB.
    - When a User wants to view/edit/manage an Exploration, the web service will check the `user, database` pair (where `database`) is the Database associated with the Exploration to get a `DatabaseServerCredential` if one exists (otherwise, no permissions are granted)
    - Based on the policy applied to that credential, the user can then act on the Exploration.

This plan would require a minor change to the [models](models.md), but isn't very difficult to implement. The author considers it a UX question which way we go on this.

## Shared links

A shared table or exploration needs access to a `Database` and `DatabaseServerCredential` to run (or be viewed). We should bypass any permission checks when actually retrieving data. The shared object model should include an attribute giving the `DatabaseServerCredential` instance needed to run (or view).

!!! danger "Tech/Product concern"
    The safest (and easiest) implementation would be to have specialized view-only users who are `GRANT`ed `SELECT` on relevant DB objects when needed. Then, sharable links would _only_ use those users. But, we'll need to justify this choice in documentation somewhere.

## Note on hierarchical permissions

We can allow an "admin" DB user by automatically granting the role associated with each Mathesar-managed connection to to a given admin DB user. So, if we have a user `mathesaradmin`, and a regular user `joe`, we can run `GRANT joe TO mathesaradmin` (as a role with sufficient privileges; At least `ADMIN` is needed on `joe` to run this). This would let `mathesaradmin` act as a Manager on anything created by `joe`.

Our `Manager` concept implies (co-)ownership of all managed sub-objects. I.e., a Database Manager owns all objects in that database (using the description in our docs)

Our `Editor` concept implies `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `TRUNCATE`, `REFERENCES` (sort of; with the way Mathesar currently treats fkeys)

Our `Viewer` concept implies `SELECT` on objects (obviously)

Thus, _if_ we want to recreate our current conceptual framework, it's possible (and not too difficult).
