# Users and Permissions

The big picture is that we will implement access management for DB objects (including databases themselves) by giving admin users of Mathesar the ability to use database-layer permissions management tools (e.g., `GRANT`). For web service resources (e.g., Django model instances), permissions will be managed in Django.

## Database Connection Model

As described in [the models section](./models.md), This will store the information needed to create an engine and connect to a database. Because the information includes a role (to define the initial connection role), it necessarily defines a set of privileges available on the database with that connection.

## Adding Connections (backend perspective)

Regardless of UI, the backend should receive a `POST` request defining a new connection. It should store this in the `DatabaseConnection` model, and initially no users should have access to that. Then, the backend should receive `PATCH` requests to modify various users, giving them access to use that connection. Note that this does _not_ directly modify anything to do with permissions on actual database objects (e.g., schemata or tables). I don't think our "Manager", "Editor", "Viewer" framework makes sense here. You have two levels: "Admin" (this should be a proper Mathesar superuser), and "Connecter" (a user who's allowed to use a given connection). Thus, we don't actually need most power of the access policy framework. A simple many-to-many map between connections and users suffices to control usage privileges, and the ability to modify that mapping (or indeed to look at the mapping) should be locked behind a superuser login.

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
    - Create a DB role owning the desired tables, and `GRANT` that role to DB users connectible by the relevant Mathesar users.
    - Have at least one DB superuser available for use with a connection, and give relevant Mathesar users access to that DB superuser.
    
## Single-user metadata object privileges

There are some metadata objects for which privileges shouldn't really be granted or revoked. An example is the display options for a column. For these types of objects, we should simply keep an 'owning user' attribute of each object instance, and use that to apply the correct version of the metadata when returning object info from the database.

## Multi-user metadata object privileges

Examples of these are table properties like preview columns. We've decided these should be per-table, and so this metadata will be stored on the user DB in a `msar_cat` namespace. Thus, modifying this metadata will occur in a request to modify the associated table, and the privilege check will be whether the relevant DB user is allowed to `ALTER` that table.

## Standalone Mathesar objects

An example of this would be an Exploration. The privileges needed to actually _run_ the query are handled on the database as described above, but a user should have access to look at the exploration definition itself (as well as edit/delete) it handled by the Django access policy framework. It seems like our current Manager/Editor/Viewer framework should suffice, but needs to be applied directly to such objects.

!!! question "UX Question"
    How should viewing others' objects work for these? Should they be namespaced under some "workspace" concept (currently we're using database/schema)?
