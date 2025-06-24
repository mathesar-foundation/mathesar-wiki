# How to migrate from 0.1.7 to 0.2.0-testing.1

There are some specific challenges, and the general recommendation is _not_ to migrate, but rather to reinstall and reimport your data.

However, it's possible. Here is an outline of what needs to be done.

## Gather info

First, get the following:

- All Django IDs of relevant user DBs, and notes about who should access them.
- All Django IDs of relevant Mathesar users, and notes about what DBs they should access.

These IDs are visible in the path to the Database or User respectively. Alternatively, you can see them by logging into the Django Database with `psql` and looking at the relevant tables: `mathesar_connection` for the Database IDs, and `mathesar_user` for the User IDs.

## Do the usual upgrade

This would follow the general instructions for either install from scratch or docker.

## Upgrade Mathesar schemata on all user databases

For this, you need to get to a Django shell by running
```
python manage.py shell
```
in the correct context. This could be within the `mathesar_service` docker container, or in a python virtual environment associated with your Mathesar installation. Then, do the following:

```python
from db.install import install_mathesar
from mathesar.models.deprecated import Connection
for db_model in Connection.objects.all():
    install_mathesar(
        database_name=db_model.db_name,
        hostname=db_model.host,
        username=db_model.username,
        password=db_model.password,
        port=db_model.port,
        skip_confirm=True
    )
```

## Migrate connections, assign to users

Again, open a Django shell (or keep using the same one as above).

Then, do the following:

```python
from mathesar.rpc.connections import grant_access_to_user
# Migrate a connection for the user with ID 1 to the new models. This call will:
# - Create models (if needed) in the new architecture to represent the connection with ID 1, and
# - Assign that connection to the User with ID 1.
grant_access_to_user(connection_id=1, user_id=1)  # EXAMPLE! fill in with desired IDs
```
Repeat the call to `grant_access_to_user` for each User-Connection pair desired.



