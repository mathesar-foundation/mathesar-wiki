# Proposed Back End Architecture

The main pieces of the back end code base are described here, and more depth is available in specific pages.

## Initial Definitions

We need a couple of terms to get started:

- **web service**: the Django service
- **Django DB**: the DB (PostgreSQL or sqlite3) where Django keeps model data
- **User DB**: a DB owned by a Mathesar user, with their tables on it. This is a DB shown in the Mathesar UI.

## Bird's Eye View

The main goals of this architectural redesign are to

- improve the speed of the back end, and
- reduce the complexity of the back end.

Secondary goals are to

- improve the convenience of the API for the use case of our front end, and
- make it easier for users and contributors to identify which back end code supports a given front end feature.

We plan to do this by:

- Removing Django models representing User DB objects (e.g., tables), replacing them with functions that query and act on those DB objects directly. Insofar as we need to enrich the metadata about User DB objects with Mathesar-managed metadata, we'll do that after gathering the relevant info from the User DB.
- Changing our API to use a JSON-RPC (2.0) spec.

## A Motivating Example: Getting the table info in a schema

To get the table info in a schema using our current architecture,

1. The front end calls the endpoint `GET /api/db/v0/tables/` using a query string parameter to filter results from that endpoint based on a schema (identified by a Django-assigned integer id). Internally, then the following happens:

1. The web service builds a query that gets some `Table` model instances from the Django DB, filtered based on the desired schema, as well as filtered according to applicable access control policies, and runs it. This gets the following info for each table:

    - `created_at` -- The date of creation of the table model instance (not the actual table)
    - `updated_at` -- The date of last modification of the table model instance (not the actual table)
    - `import_verified` -- Whether the import process was verified by the user for this table
    - `is_temp` -- Whether this table is supposed to be copied into a preexisting table, then deleted
    - `import_target_id` -- A preexisting table which should receive this table's data
    - `schema_id` -- The Django id of the schema containing the table
    - `data_files` -- A list of any data files imported to the table
    - `settings` -- Some metadata describing how the table is displayed

1. The web service determines which connection to use with the User DB by querying for which `Database` model (called connections in the API) the requested schema lives under, and asking that model to give it a connection string.

1. The web service then gathers the following info _for each table_ by querying the User DB. These queries are initiated by `@property` annotations in the Django models. 

    - `name`
    - `description` -- The comment (description) of the table, defined in the User DB.
    - `has_depenents` (many requests for this, actually)
    - `columns` -- These are found by following a foreign key link on the Django DB. Each column model instance then runs a bunch of queries to gather relevant info from the user DB and Django DB.

1. _For each column of each table_, the web service then gathers the following info by querying the Django DB (can be batched):

    - `display_options` -- These describe table-wide metadata about how to show the table in the UI.

1. _For each column of each table_, we gather the following info by querying the user DB, again with queries initiated by `@property` annotations on the Django `Column` model. For these, we end up making separate requests:

    - `name` (multiple requests to user DB for each column)
    - `type`
    - `type_options` -- e.g., the precision specified for a `numeric` column

All of this gets joined together, then sent back as a response from the API. 

With the new architecture, to get the same info,

1. The front end calls an RPC endpoint `/api/v0/rpc/`, calling a function `get_schema_table_details` with `database` and `schema` parameters. The database is identified by a Django id referring to a database model, and the schema is identified by an OID.

1. The web service uses the `user` and `database` (the user is picked up from the request object) to acquire a connection string.

1. Using that connection, the web service calls a PL/pgSQL function installed on the User DB called `get_schema_table_details` to gather 

    - `name`
    - `description`
    - `has_dependents`
    - `columns`
        - `name`
        - `type`
        - `type_options`
    - `preview_settings` -- describes how we should show each table's rows when it's linked to by a foreign key

1. Using the returned info, the web service filters a `TableMetadata` model based on the passed `database` and returned `oid`s, and gathers

    - `import_verified`
    - `is_temp`
    - `import_target_id`
    - `data_files`
    - `column_order` -- describes the order in which columns should be displayed

1. Using the same returned info, filter a `ColumnMetadata` model based on returned `oid, attnum` pairs to gather (for each column)

    - `display_options`

We then join all of this together, and return it as a response from the API.
    
The fundamental difference is that in the current version, we use foreign keys between Django models to find tables for the schema, then columns for each table. Then all queries on the User DB are initiated by functions on these model instances. In the new version, we instead run a query on the User DB to gather all relevant table and column info available on that DB, then enrich that data with metadata stored in non-foreign-key-linked metadata models in the Django DB.

## Introduction to relevant layers

The layers introduced here will be discussed in more detail in other sections.

### User database

For each API call, there should be an identifiable DB function that performs all User Database operations needed to satisfy that call. For example,

- Calling the function `get_tables(database, schema)` should result in a call to some function `get_tables(sch_oid oid)` on the `database`.

To achieve this, we will install the following on the user database(s)

- Some custom Mathesar types. These are used to validate passed JSON at the User DB level. For example, we create the type
  ```
  TYPE __msar.col_def AS (
    name_ text, -- The name of the column to create, quoted.
    type_ text, -- The type of the column to create, fully specced with arguments.
    not_null boolean, -- A boolean to describe whether the column is nullable or not.
    default_ text, -- Text SQL giving the default value for the column.
    identity_ boolean, -- A boolean giving whether the column is an identity pkey column.
    description text -- A text that will become a comment for the column
  )
  ```
  This type describes and validates the column info we need to add that column to a table.
- A set of functions that provide the bulk of Mathesar's back end logic and functionality.

### Python `db` library

This library should mostly serve to provide thin wrapper functions around the User DB layer functions. These functions should take parameters from requests (never request objects themselves) and engines, and then call underlying DB functions. They should then pass the results up towards the API

### Web service

This service should provide an JSON-RPC API for use by the front end. When an API function is called, the service should:

- Grab an appropriate engine from the by combining the `user` associated with the request with the `database`. See the [models](models.md) page for more detail.
- Call the relevant `db` library function (should be only one in most cases).
- Gathers data from the service database via models if needed (this is for metadata that's inappropriate for storage in the User DB for some reason)
- Returns it to the API

## Permissions and users

- All permission checks for accessing a User DB object (e.g., table) should happen on the User DB. We should not add another layer of checks for these objects in the web service.
- Permission checks for accessing and managing info in the Django DB (e.g., Exploration definitions) are handled in the web service.
- We should, whenever possible, permissions on Django models based on access to the underlying DB object in real time. Details are [here](./permissions.md).

### Example

A user lists the columns for a table. Because they have access to read the columns of the table (checked on the DB), they can read display options for a table. If they have access to modify a column of a table, they have access to modify the relevant display options. This works as long as there isn't a dedicated `display_options` endpoint which could receive requests directly. Even in that case, we could add logic to check permissions on the relevant User DB.

### Exceptions

There are some metadata and other models that we'll be keeping which _can_ receive direct requests. Currently, these are:

- Database connection and credential info
- Shareable links
- Explorations

Access to these will be managed using the Django permissions framework (i.e., with access policies).
