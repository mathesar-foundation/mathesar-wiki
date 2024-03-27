# Deprecated Models 

This section contains ad-hoc notes on our current models, and intended changes.

## Column

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

## Constraint

| Column      | Type                     |
|-------------|--------------------------|
| id          | integer                  |
| created\_at | timestamp with time zone |
| updated\_at | timestamp with time zone |
| oid         | integer                  |
| table\_id   | integer                  |

Nothing actually stored here. Delete this model. All functionality can be contained in User DB functions.

## Database

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

Replace this with `Database`, `DatabaseServer`, `DatabaseServerCredential`, and `UserDatabaseRoleMap` models. See the [New models](./models.md) for details.

## DatabaseRole

| Column       | Type                     |
|--------------|--------------------------|
| id           | integer                  |
| created\_at  | timestamp with time zone |
| updated\_at  | timestamp with time zone |
| role         | character varying(10)    |
| database\_id | integer                  |
| user\_id     | integer                  |

This stores a role on a given database for a given user. We will repurpose this, and it will be applied (for now) only to `UIQuery` instances namespaced under a given database.

## DataFile

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

## PreviewColumnSettings

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

## Schema

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

## SchemaRole

| Column      | Type                     |
|-------------|--------------------------|
| id          | integer                  |
| created\_at | timestamp with time zone |
| updated\_at | timestamp with time zone |
| role        | character varying(10)    |
| schema\_id  | integer                  |
| user\_id    | integer                  |

This should be deleted, and the permissions should be instead managed on the underlying DB.

## SharedQuery

| Column      | Type                     |
|-------------|--------------------------|
| id          | integer                  |
| created\_at | timestamp with time zone |
| updated\_at | timestamp with time zone |
| slug        | uuid                     |
| enabled     | boolean                  |
| query\_id   | integer                  |

This model should stay. No changes here. We need to add metadata about a credential for running the actual query.

## SharedTable

| Column      | Type                     |
|-------------|--------------------------|
| id          | integer                  |
| created\_at | timestamp with time zone |
| updated\_at | timestamp with time zone |
| slug        | uuid                     |
| enabled     | boolean                  |
| table\_id   | integer                  |

Only change is that we need to refer directly to a table OID, and handle permissions.

## Table

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

## TableSettings

| Column                | Type                     |
|-----------------------|--------------------------|
| id                    | integer                  |
| created\_at           | timestamp with time zone |
| updated\_at           | timestamp with time zone |
| column\_order         | jsonb                    |
| preview\_settings\_id | integer                  |
| table\_id             | integer                  |

This stores Mathesar-specific metadata about tables. Should be combined with remains of `Table` model.

## UIQuery

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

## User

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

This stores user metadata. I think we should  mostly keep it as is. It will be referenced by the `UserDatabaseRoleMap` model.
