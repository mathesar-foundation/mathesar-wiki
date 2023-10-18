# Users and Permissions

The big picture is that we will implement access management for DB objects (including databases themselves) by giving admin users of Mathesar the ability to use database-layer permissions management tools (e.g., `GRANT`). For web service resources (e.g., Django model instances), permissions will be managed in Django.

## Database Connection Model

As described in [the models section](./models.md), This will store the information needed to create an engine and connect to a database. Because the information includes a role (to define the initial connection role), it necessarily defines a set of privileges available on the database with that connection.

## Adding Connections (backend perspective)

Regardless of UI, the backend should receive a `POST` request defining a new connection. It should store this in the `DatabaseConnection` model, and initially no users should have access to that. Then, the backend should receive `PATCH` requests to modify various users, giving them access to use that connection. Note that this does _not_ directly modify anything to do with permissions on actual database objects (e.g., schemata or tables). I don't think our "Manager", "Editor", "Viewer" framework makes sense here. You have two levels: "Admin" (a proper Mathesar superuser), and "User" (a user who's allowed to use a given connection).

!!! question "UX Question"
    Is there a use-case for having a non-admin "Manager" role who can grant access to a given connection string, but not others?

## Granting database object privileges

The backend will provide an endpoint that lets an admin (who has access to a sufficiently-privileged role via a connection) access database-level permission granting functionality directly. So, to grant access to create tables in a schema to a Mathesar user, the admin needs to send a `PATCH` request to CRUD endpoint that defines a privilege-granting query (via a function) on the database. Note that this `PATCH` request doesn't actually modify any model instance. We should probably namespace this endpoint differently than the Mathesar user admin for clarity.

- Privileges on DB objects are thus not granted directly to Mathesar users.
- Privileges on DB objects are granted to DB roles, which may be accessible to some (or all) Mathesar users.

!!! question "UX Question"
    Should access to Connections and access to DB objects via connections be presented the same way in the UI?

!!! question "UX Question"
    Should the admin think in terms of groups of Mathesar users, or specifically in terms of connections when dealing with DB-level privileges?
    
!!! danger "Potential Confusion"
    In case the admin or DBA want multiple Mathesar users to be able to modify various DB objects, three options are available:
    - Give all relevant Mathesar users access to connect as the owning DB user.
    - `GRANT` the owning DB role (ostensibly a user) to DB users connectable by the relevant Mathesar users.
    - Have at least one DB superuser available for use with a connection, and give relevant Mathesar users access to that DB superuser.
    
## Single-user metadata object privileges

There are some metadata objects for which privileges shouldn't really be granted or revoked. An example is the display options for a column. For these types of objects, we should simply keep an 'owning user' attribute of each model instance, and use that to apply the correct version of the metadata when returning object info from the database. Note that if we end up exposing an endpoint to work on these metadata models directly, then we'll need access policies.

## Multi-user metadata object privileges

Examples of these are table properties like preview columns. We've decided these should be per-table, and so this metadata will be stored on the user DB in a `msar_cat` namespace. Thus, modifying this metadata will occur in a request to modify the associated table, and the privilege check will be whether the relevant DB user is allowed to `ALTER` that table. Viewing this metadata would check whether the relevant DB user is allowed to `SELECT` that table.

## Standalone Mathesar objects

An example of this would be an Exploration. The privileges needed to actually _run_ the query are handled on the database as described above, but a user should have access to look at the exploration definition itself (as well as edit/delete) it handled by the Django access policy framework. It seems like our current Manager/Editor/Viewer framework should suffice, but needs to be applied directly to such objects.

!!! question "UX Question"
    How should viewing others' objects work for these? Should they be namespaced under some "workspace" concept (currently we're using database/schema)?

## Shared links

A shared table or exploration needs access to a `DatabaseConnection` to run (or be viewed). We should bypass any permission checks when actually retrieving data. The shared object model should include an attribute giving the `DatabaseConnection` instance needed to run (or view).

!!! danger "Tech/Product concern"
    The safest (and easiest) implementation would be to have specialized view-only users who are `GRANT`ed `SELECT` on relevant DB objects when needed. Then, sharable links would _only_ use those users. But, we'll need to justify this choice in documentation somewhere.

## Note on hierarchical permissions

We can allow an "admin" DB user by automatically granting the role associated with each Mathesar-managed connection to to a given admin DB user. So, if we have a user `mathesaradmin`, and a regular user `joe`, we can run `GRANT joe TO mathesaradmin` (as a role with sufficient privileges; At least `ADMIN` is needed on `joe` to run this). This would let `mathesaradmin` act as a Manager on anything created by `joe`.

Our `Manager` concept implies (co-)ownership of all managed sub-objects. I.e., a Database Manager owns all objects in that database (using the description in our docs)

Our `Editor` concept implies `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `TRUNCATE`, `REFERENCES` (sort of; with the way Mathesar currently treats fkeys)

Our `Viewer` concept implies `SELECT` on objects (obviously)

Thus, _if_ we want to recreate our current conceptual framework, it's possible (and not too difficult).
