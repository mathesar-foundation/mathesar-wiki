# Models

Subject to minor changes.

We should be able to handle anything being discussed for beta through simple extensions of this model framework. Also, these models are intended to get us to beta, while providing flexibility to move forward afterwards. There will be a brief discussion of a desired next iteration at the end.

## User

| Column                   | Type                     | Notes            |
|--------------------------|--------------------------|------------------|
| id                       | integer                  | pkey             |
| password                 | character varying(128)   | not null         |
| last\_login              | timestamp with time zone |                  |
| is\_superuser            | boolean                  |                  |
| username                 | character varying(150)   | not null; unique |
| email                    | character varying(254)   |                  |
| is\_staff                | boolean                  |                  |
| is\_active               | boolean                  |                  |
| date\_joined             | timestamp with time zone |                  |
| full\_name               | character varying(255)   |                  |
| short\_name              | character varying(255)   |                  |
| password\_change\_needed | boolean                  |                  |

## DatabaseServer

| Column      | Type                     | Notes    |
|-------------|--------------------------|----------|
| id          | integer                  | pkey     |
| created\_at | timestamp with time zone |          |
| updated\_at | timestamp with time zone |          |
| host        | character varying        | not null |
| port        | integer                  | not null |

`(host, port)` pair is unique. 

Theoretically, we could also split the host out, but that seems like premature optimization.

We could consider making the `host` and `port` nullable when we're supporting `.pgpass`.

## Database

| Column              | Type                     | Notes                                             |
|---------------------|--------------------------|---------------------------------------------------|
| id                  | integer                  | pkey                                              |
| created\_at         | timestamp with time zone |                                                   |
| updated\_at         | timestamp with time zone |                                                   |
| db\_name            | text                     | not null                                          |
| display\_name       | text                     | not null; unique                                  |
| db\_server          | integer                  | not null; references DatabaseServer(id)           |
| editable            | boolean                  |                                                   |
| default\_credential | integer                  | not null; references DatabaseServerCredential(id) |

`(db_server, db_name)` is unique. We could consider making `db_name` nullable when supporting `.pgpass`. If a Mathesar Admin user doesn't have an entry in `UserDatabaseRoleMap` for a given database, they will use the `default_credential` defined here to connect.

## DatabaseServerCredential

| Column      | Type                     | Notes                                   |
|-------------|--------------------------|-----------------------------------------|
| id          | integer                  | pkey                                    |
| created\_at | timestamp with time zone |                                         |
| updated\_at | timestamp with time zone |                                         |
| username    | character varying        | not null                                |
| password    | character varying        | encrypted; not null                     |
| db\_server  | integer                  | not null; references DatabaseServer(id) |

We could consider making `username` and `password` nullable when supporting `.pgpass`.

## UserDatabaseRoleMap

| Column         | Type                     | Notes                                   |
|----------------|--------------------------|-----------------------------------------|
| id             | integer                  | pkey                                    |
| created\_at    | timestamp with time zone |                                         |
| updated\_at    | timestamp with time zone |                                         |
| user           | integer                  | references User(id)                     |
| database       | integer                  | references Database(id)                 |
| database\_role | integer                  | references DatabaseServerCredential(id) |
| metadata\_role | enum                     | ('read only', 'read write')             |

`(user, database)` pair is unique. The `metadata_role` isn't likely to be technically implemented as an `enum` on the DB for now. We'll use a Django-managed `TextChoices` field to save implementation time. See the current `DatabaseRole` model and its interaction with the `Role` class for an example. 

## Aside: Quick overview of connecting to a DB.

The Django permissions infrastructure should handle CRUD operations on `Database`, `DatabaseServerCredential`, `DatabaseServer`, and `UserDatabaseRoleMap` resources. Actually accessing a database wouldn't require the permissions infrastructure; we'd instead construct a connection string by joining the appropriate `database` to the other info found by looking up the `user, database` pair. For example, given a `(user, database)` pair like `(3, 8)`, we'd look up the appropriate row in the `UserDatabaseRoleMap` model to find the `role` (referencing `DatabaseServerCredential`). We also follow the foreign key to the `Database` to pick up the `db_name` and then the foreign key to `DatabaseServer` to pick up the `host` and `port`.

We should eventually add functionality to store some details in a [`.pgpass`](https://www.postgresql.org/docs/current/libpq-pgpass.html) dotfile (though probably in a custom location). `psycopg` can inject the password and/or other missing pieces automatically through these means.

## UIQuery

| Column           | Type                     | Notes                   |
|------------------|--------------------------|-------------------------|
| id               | integer                  | pkey                    |
| created\_at      | timestamp with time zone |                         |
| updated\_at      | timestamp with time zone |                         |
| database         | integer                  | references Database(id) |
| base\_table\_oid | integer                  | not null                |
| name             | character varying(128)   | not null; unique        |
| description      | text                     |                         |
| initial\_columns | jsonb                    | not null                |
| transformations  | jsonb                    |                         |
| display\_options | jsonb                    |                         |
| display\_names   | jsonb                    |                         |

- The JSONB columns are the same format, except now they refer to DB-layer ids, e.g., OIDs and attnums rather than Django-layer IDs.
- We should consider changing `display_options` to refer to instances of `ColumnMetadata` within the JSONB
- Permissions on this object will be derived from the `UserDatabaseRoleMap.metadata_role` via the `(database, user)` pair.

## ColumnMetadata

| Column                  | Type                     | Notes                             |
|-------------------------|--------------------------|-----------------------------------|
| id                      | integer                  | pkey                              |
| created\_at             | timestamp with time zone |                                   |
| updated\_at             | timestamp with time zone |                                   |
| database                | integer                  | not null; References Database(id) |
| table\_oid              | integer                  | not null                          |
| attnum                  | integer                  | not null                          |
| bool\_input             | enum                     | ('dropdown', 'checkbox')          |
| bool\_true              | text                     | default: 'True'                   |
| bool\_false             | text                     | default: 'False'                  |
| num\_min\_frac\_digits  | integer                  | min: 0, max: 20                   |
| num\_max\_frac\_digits  | integer                  | min: 0, max: 20                   |
| num\_show\_as\_perc     | boolean                  | Default: false                    |
| mon\_currency\_symbol   | text                     | Default?                          |
| mon\_currency\_location | enum                     | ('after-minus', 'end-with-space') |
| time\_format            | text                     |                                   |
| date\_format            | text                     |                                   |
| duration\_min           | character varying(255)   |                                   |
| duration\_max           | character varying(255)   |                                   |
| duration\_show\_units   | boolean                  |                                   |

- The `(database, table_oid, attnum)` tuple should be unique.
- Depending on Django's support for multicolumn `CHECK` constraints, we should ensure that `num_min_frac_digits < num_max_frac_digits`. 
- This has a number of fields to replace the current JSON storage of display options, and remove the need for the polymorphic serializer.
- The only foreign key we reference is the `Database(id)`, needed to map to a specific database where we find the relevant table and column.
- We don't need to reference any `schema_oid`, since a `(table_oid, attnum)` pair is unique per DB.
- Permissions to manipulate instances of this model would be derived from permissions to manipulate the relevant table and column in the underlying database.

## TableMetadata

| Column              | Type                     | Notes                             |
|---------------------|--------------------------|-----------------------------------|
| id                  | integer                  | pkey                              |
| created\_at         | timestamp with time zone |                                   |
| updated\_at         | timestamp with time zone |                                   |
| database            | integer                  | not null; references Database(id) |
| table\_oid          | integer                  | not null                          |
| import\_verified    | boolean                  |                                   |
| is\_temp            | boolean                  |                                   |
| import\_target\_oid | integer                  |                                   |
| column\_order       | jsonb                    |                                   |
| preview\_customized | boolean                  |                                   |
| preview\_template   | character varying(255)   |                                   |

I've left the preview template in the Mathesar layer. The hope is that we can find a sufficiently featureful and also sufficiently efficient algorithm for getting the template, thereby avoiding needing to move this down into the user Database. There will be more discussion of this below. Permissions to manipulate this should be derived from permissions on the relevant table in the underlying database.

## DataFile

| Column        | Type                     | Notes    |
|---------------|--------------------------|----------|
| id            | integer                  | pkey     |
| created\_at   | timestamp with time zone |          |
| updated\_at   | timestamp with time zone |          |
| file          | character varying(100)   | not null |
| created\_from | character varying(128)   |          |
| base\_name    | character varying(100)   |          |
| header        | boolean                  |          |
| delimiter     | character varying(1)     |          |
| escapechar    | character varying(1)     |          |
| quotechar     | character varying(1)     |          |
| user          | integer                  |          |
| type          | character varying(128)   |          |
| max\_level    | integer                  |          |
| sheet\_index  | integer                  |          |

When we have our desired logic for cleaning this up sorted out, we should consider removing this model. It's currently only used ephemerally, but then the actuaul instance hangs around indefinitely.

## SharedQuery

| Column      | Type                     | Notes                                   |
|-------------|--------------------------|-----------------------------------------|
| id          | integer                  | pkey                                    |
| created\_at | timestamp with time zone |                                         |
| updated\_at | timestamp with time zone |                                         |
| slug        | uuid                     | unique                                  |
| enabled     | boolean                  |                                         |
| query       | integer                  | not null; references UIQuery(id)        |
| credential  | integer                  | references DatabaseServerCredential(id) |

I've chosen to store the credential id, rather than the creating user, for flexibility. We can derive this from a creating user at the time the query is created, and could (theoretically) update it if the User's credential for a given DB changes (I wouldn't recommend this).

## SharedTable

| Column      | Type                     | Notes                                   |
|-------------|--------------------------|-----------------------------------------|
| id          | integer                  | pkey                                    |
| created\_at | timestamp with time zone |                                         |
| updated\_at | timestamp with time zone |                                         |
| slug        | uuid                     | unique                                  |
| enabled     | boolean                  |                                         |
| table\_oid  | integer                  | not null                                |
| credential  | integer                  | references DatabaseServerCredential(id) |

## After-beta-term vision

For the beta, I'm hoping to avoid some work by keeping things in the Mathesar service models that I'd rather store in the underlying User Databases in a `msar_catalog` schema. The relevant models are `ColumnMetadata` and `TableMetadata`. A big motivation to move this info to the User DB is performance w.r.t. the table previews. Our current algorithm requires lots of back-and-forth between the service layer and the User DB in order to recursively build these preview templates, and to fill them. I also think it's more natural to keep these metadata models in the User DB, since they're segregated by User DB, and each instance only refers to objects on that underlying database.

I also think in the even longer term that we should think about storing our `UIQuery` info on the underlying database in the form of views (perhaps in a special `msar_queries` schema). This presents some technical problems, however, that we haven't yet solved.

## What about names vs. OIDs?

I thought about adding another model to store a general map of names to OIDs for use when resolving missing tables, etc. This would be useful if someone drops and recreates a table, or when trying to export your Mathesar Explorations or Display Settings. I didn't add that at this stage, since:

- We'd use the underlying User DB for that map if we move the Metadata models down to the UserDB, and
- We aren't prioritizing the features requiring being able to export and reimport your Explorations for beta.
