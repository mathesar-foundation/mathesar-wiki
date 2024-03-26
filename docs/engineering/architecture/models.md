# Models

## Current Models (skipping unused batteries for now)

This section contains ad-hoc notes on our current models, and intended changes.

### Column

| Column           | Type                     |
|------------------|--------------------------|
| id               | integer                  |
| created\_at      | timestamp with time zone |
| updated\_at      | timestamp with time zone |
| attnum           | integer                  |
| display\_options | jsonb                    |
| table\_id        | integer                  |

The only actual info here is the display options for a given column, stored as a JSON blob. Rename to `ColumnMetadata`, restructure to validate display options, delete fkey fields. Consider moving to `ma_catalog` table on user DB.

We need to handle updating the table preview template when a new column is added (or rethink the implementation of this functionality)

We need to replace functionality to get `ui_type` from DB type.

To replace the dependent-getting functionality, we need to move the dependents module to SQL.

### Constraint

| Column      | Type                     |
|-------------|--------------------------|
| id          | integer                  |
| created\_at | timestamp with time zone |
| updated\_at | timestamp with time zone |
| oid         | integer                  |
| table\_id   | integer                  |

Nothing actually stored here. Delete this model. All functionality can be contained in User DB functions.

### Database

| Column      | Type                     |
|-------------|--------------------------|
| id          | integer                  |
| created\_at | timestamp with time zone |
| updated\_at | timestamp with time zone |
| name        | character varying(128)   |
| deleted     | boolean                  |
| db\_name    | character varying(128)   |
| editable    | boolean                  |
| host        | character varying(255)   |
| password    | text                     |
| port        | integer                  |
| username    | text                     |

Stores connection info to allow accessing a DB by creating an SQLAlchemy engine.

Referenced by DatabaseRole and Schema models.

Replace this with `Database`, `DatabaseServer`, `DatabaseServerCredential`, and `UserDatabaseMap` models. See the [New models](#new-model-setup) for details.

### DatabaseRole

| Column       | Type                     |
|--------------|--------------------------|
| id           | integer                  |
| created\_at  | timestamp with time zone |
| updated\_at  | timestamp with time zone |
| role         | character varying(10)    |
| database\_id | integer                  |
| user\_id     | integer                  |

This stores a role on a given database for a given user. We will repurpose this, and it will be applied (for now) only to `UIQuery` instances namespaced under a given database.

### DataFile

| Column                  | Type                     |
|-------------------------|--------------------------|
| id                      | integer                  |
| created\_at             | timestamp with time zone |
| updated\_at             | timestamp with time zone |
| file                    | character varying(100)   |
| created\_from           | character varying(128)   |
| base\_name              | character varying(100)   |
| header                  | boolean                  |
| delimiter               | character varying(1)     |
| escapechar              | character varying(1)     |
| quotechar               | character varying(1)     |
| table\_imported\_to\_id | integer                  |
| user\_id                | integer                  |
| type                    | character varying(128)   |
| max\_level              | integer                  |
| sheet\_index            | integer                  |

This stores metadata about files which have been uploaded for import into Mathesar. We should keep this model. `table_imported_to_id` should be removed (it's not used anywhere is it?). Also `max_level` seems like less of a data file attribute and more of an import setting.

### PreviewColumnSettings

| Column      | Type                     |
|-------------|--------------------------|
| id          | integer                  |
| created\_at | timestamp with time zone |
| updated\_at | timestamp with time zone |
| customized  | boolean                  |
| template    | character varying(255)   |

This stores the template defining what should be shown in a referencing fkey column for this table. This would be _much_ better as a `ma_catalog` table for efficiency reasons.

In that case, a table's preview settings would be "global", i.e., it would be attached to the table rather than a user, table pair.

Referenced by TableSettings.

### Schema

| Column       | Type                     |
|--------------|--------------------------|
| id           | integer                  |
| created\_at  | timestamp with time zone |
| updated\_at  | timestamp with time zone |
| oid          | integer                  |
| database\_id | integer                  |

Nothing stored here. 

Referenced by SchemaRole and Table models.

Delete this model. All permissions handled by the referencing SchemaRole should instead be handled by the underlying user's permissions on the actual schema in the DB

### SchemaRole

| Column      | Type                     |
|-------------|--------------------------|
| id          | integer                  |
| created\_at | timestamp with time zone |
| updated\_at | timestamp with time zone |
| role        | character varying(10)    |
| schema\_id  | integer                  |
| user\_id    | integer                  |

This should be deleted, and the permissions should be instead managed on the underlying DB.

### SharedQuery

| Column      | Type                     |
|-------------|--------------------------|
| id          | integer                  |
| created\_at | timestamp with time zone |
| updated\_at | timestamp with time zone |
| slug        | uuid                     |
| enabled     | boolean                  |
| query\_id   | integer                  |

This model should stay. No changes here. We need to add metadata about a credential for running the actual query.

### SharedTable

| Column      | Type                     |
|-------------|--------------------------|
| id          | integer                  |
| created\_at | timestamp with time zone |
| updated\_at | timestamp with time zone |
| slug        | uuid                     |
| enabled     | boolean                  |
| table\_id   | integer                  |

Only change is that we need to refer directly to a table OID, and handle permissions.

### Table

| Column             | Type                     |
|--------------------|--------------------------|
| id                 | integer                  |
| created\_at        | timestamp with time zone |
| updated\_at        | timestamp with time zone |
| oid                | integer                  |
| import\_verified   | boolean                  |
| is\_temp           | boolean                  |
| import\_target\_id | integer                  |
| schema\_id         | integer                  |

Stores info about:

- whether the initial data import for the table has been manually verified by a user or not, and
- whether the table is actually a temporary holder for data intended for a preexisting table.

Referenced by Column, Constraint, DataFile, SharedTable, Table, TableSettings, and UIQuery models

We should combine this with the `TableSettings` model to create a `TableMetadata` model that just has that info, and drop all fkeys and references.

### TableSettings

| Column                | Type                     |
|-----------------------|--------------------------|
| id                    | integer                  |
| created\_at           | timestamp with time zone |
| updated\_at           | timestamp with time zone |
| column\_order         | jsonb                    |
| preview\_settings\_id | integer                  |
| table\_id             | integer                  |

This stores Mathesar-specific metadata about tables. Should be combined with remains of `Table` model.

### UIQuery

| Column           | Type                     |
|------------------|--------------------------|
| id               | integer                  |
| created\_at      | timestamp with time zone |
| updated\_at      | timestamp with time zone |
| name             | character varying(128)   |
| description      | text                     |
| initial\_columns | jsonb                    |
| transformations  | jsonb                    |
| display\_options | jsonb                    |
| display\_names   | jsonb                    |
| base\_table\_id  | integer                  |

This stores a definition of a stored query that can be run on command. The main changes are that it should refer directly to DB-layer ids (oids and attnums) rather than Django-layer.

### User

| Column                   | Type                     |
|--------------------------|--------------------------|
| id                       | integer                  |
| password                 | character varying(128)   |
| last\_login              | timestamp with time zone |
| is\_superuser            | boolean                  |
| username                 | character varying(150)   |
| email                    | character varying(254)   |
| is\_staff                | boolean                  |
| is\_active               | boolean                  |
| date\_joined             | timestamp with time zone |
| full\_name               | character varying(255)   |
| short\_name              | character varying(255)   |
| password\_change\_needed | boolean                  |

This stores user metadata. I think we should  mostly keep it as is. It will be referenced by the `UserDatabaseMap` model.

## New Model setup

Some of this is tentative pending decisions in our Users and Permissions work. We should be able to handle anything being discussed through simple extensions of this model framework. Also, these models are intended to get us to beta, while providing flexibility to move forward afterwards. There will be discussion of a desired next iteration at the end.

### User

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

### DatabaseServer

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

### Database

| Column        | Type                     | Notes                                   |
|---------------|--------------------------|-----------------------------------------|
| id            | integer                  | pkey                                    |
| created\_at   | timestamp with time zone |                                         |
| updated\_at   | timestamp with time zone |                                         |
| oid           | integer                  | not null                                |
| db\_name      | text                     | not null                                |
| display\_name | text                     | not null; unique                        |
| db\_server    | integer                  | not null; references DatabaseServer(id) |
| editable      | boolean                  |                                         |

`(db_server, oid)` pair is unique, or `(db_server, db_name)` is. Should consider whether we should even store the `oid`, since we can't look up the `db_name` to connect without ... connecting, which requires the `db_name` rather than the `oid`. We could consider making `db_name` nullable when supporting `.pgpass`

### DatabaseServerCredential

| Column      | Type                     | Notes                                   |
|-------------|--------------------------|-----------------------------------------|
| id          | integer                  | pkey                                    |
| created\_at | timestamp with time zone |                                         |
| updated\_at | timestamp with time zone |                                         |
| username    | character varying        | not null                                |
| password    | character varying        | encrypted; not null                     |
| db\_server  | integer                  | not null; references DatabaseServer(id) |

We could consider making `username` and `password` nullable when supporting `.pgpass`.

### UserDatabaseMap

| Column      | Type                     | Notes                                   |
|-------------|--------------------------|-----------------------------------------|
| id          | integer                  | pkey                                    |
| created\_at | timestamp with time zone |                                         |
| updated\_at | timestamp with time zone |                                         |
| user        | integer                  | references User(id)                     |
| database    | integer                  | references Database(id)                 |
| role        | integer                  | references DatabaseServerCredential(id) |

`(user, database)` pair is unique.

### Aside: Quick overview of connecting to a DB.

The Django permissions infrastructure should handle CRUD operations on `Database`, `DatabaseServerCredential`, `DatabaseServer`, and `UserDatabaseMap` resources. Actually accessing a database wouldn't require the permissions infrastructure; we'd instead construct a connection string by joining the appropriate `database` to the other info found by looking up the `user, database` pair. For example, given a `(user, database)` pair like `(3, 8)`, we'd look up the appropriate row in the `UserDatabaseMap` model to find the `role` (referencing `DatabaseServerCredential`). We also follow the foreign key to the `Database` to pick up the `db_name` and then the foreign key to `DatabaseServer` to pick up the `host` and `port`.

We should eventually add functionality to store some details in a [`.pgpass`](https://www.postgresql.org/docs/current/libpq-pgpass.html) dotfile (though probably in a custom location). `psycopg` can inject the password automatically through these means.

### UIQuery

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
- Permissions on this object will be derived from the `DatabaseUIQueryRole` via the `(database, user)` pair.

### DatabaseUIQueryRole (consider different name)

| Column      | Type                     | Notes                             |
|-------------|--------------------------|-----------------------------------|
| id          | integer                  | pkey                              |
| created\_at | timestamp with time zone |                                   |
| updated\_at | timestamp with time zone |                                   |
| role        | character varying(10)    |                                   |
| database    | integer                  | not null; references Database(id) |
| user        | integer                  | not null; references User(id)     |

This will be used to store Manager, Editor, Viewer permissions on Explorations. The reason to keep this (derived from the current `DatabaseRole`) for now is to give us a namespace where we can organize permissions for `UIQuery` instances (Explorations in the current UI). If we want to use "Projects" for such a namespace, or derive these roles from the `DatabaseServerCredential` associated with a user on a `Database` via the `UserDatabaseMap`, then we will have to change or remove this model. More discussion needed here.

### ColumnMetadata

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

### TableMetadata

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

### DataFile

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

### SharedQuery

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

### SharedTable

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

### What about names vs. OIDs?

I thought about adding another model to store a general map of names to OIDs for use when resolving missing tables, etc. This would be useful if someone drops and recreates a table, or when trying to export your Mathesar Explorations or Display Settings. I didn't add that at this stage, since:

- We'd use the underlying User DB for that map if we move the Metadata models down to the UserDB, and
- We aren't prioritizing the features requiring being able to export and reimport your Explorations for beta.
