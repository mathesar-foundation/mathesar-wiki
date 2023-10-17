# Proposed Backend Architecture

The main pieces of the back end code base are described here, and more depth is available in specific pages.

## Initial Definitions

We need a couple of terms to get started:

- **web service**: the Django service
- **Django DB**: the DB (postgres or sqlite3) where Django keeps model data
- **User DB**: a DB owned by a Mathesar user, with their tables on it. This is a DB shown in the Mathesar UI.

## Bird's Eye View

The big goal of this architectural redesign is that we want to move away from using Django models to represent DB objects, and instead use functions to act on those DB objects directly. Insofar as we need to enrich the data about DB objects with other metadata, we'll do that after gathering the relevant info from the User DB.

## Example: Getting the table info in a schema

To get the table info in a schema, we call the endpoint `GET /api/db/v0/tables/`. We use a query string parameter to indicate we want to filter results from that endpoint based on a schema (identified by a Django-assigned integer id). Internally, then the following happens:

1. Django builds a query that gets some `Table` model instances from the Django DB, filtered based on the desired schema, and runs it. This gets the following info for each table:
    - `created_at` -- The date of createion of the table model instance (not the actual table)
    - `updated_at` -- The date of last modification of the table model instance (not the actual table)
    - `import_verified` -- Whether the import process was verified by the user for this table
    - `is_temp` -- Whether this table is supposed to be copied into a preexisting table, then deleted
    - `import_target_id` -- A preexisting table which should receive this table's data
    - `schema_id` -- The Django id of the schema containing the table
    - `data_files` -- A list of any data files imported to the table
    - `settings` -- Some metadata describing how the table is displayed
1. We then gather the following info _for each table_ by querying the user DB. These queries are initiated by `@property` annotations in the Django models. 
    - `name`
    - `description` -- The comment (description) of the table, defined in the User DB.
    - `has_depenents` (many requests for this, actually)
    - `columns` -- These are found by following a foreign key link on the Django DB. Each column model instance then runs a bunch of queries to gather relevant info from the user DB and Django DB.
1. For each column of each table, we gather the following info by querying the Django DB (can be batched):
    - `display_options` -- These describe table-wide metadata about how to show the table in the UI.
1. For each column of each table, we gather the following info by querying the user DB, again with queries initiated by `@property` annotations on the Django `Column` model. For these, we end up making separate requests:
    - `name` (multiple requests to user DB for each column)
    - `type`
    - `type_options` -- e.g., the precision specified for a `numeric` column

All of this gets joined together, then sent back as a response from the API. 

With the new architecture, we'll instead:

1. Call a PL/pgSQL function installed on the user database called `get_schema_table_details` It will run on the user database to gather 
    - `name`
    - `description`
    - `has_dependents`
    - `columns`
        - `name`
        - `type`
        - `type_options`
    - `preview_settings` -- describes how we should show each table's rows when it's linked to by a foreign key
1. Using the returned info, filter a `TableMetadata` model based on returned `oid`s, and gather
    - `import_verified`
    - `is_temp`
    - `import_target_id`
    - `schema_id`
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

- `GET /api/db/v0/tables/` should result in a call to some function `get_tables(sch_oid oid)` on the database.

To achieve this, we will install the following on the user database(s)

- Some custom Mathesar types
- Some tables holding metadata that needs to be kept near the tables
- A set of functions that provide the bulk of Mathesar's back end logic and functionality.

### Python `db` library

This library should mostly serve to provide thin wrapper functions around the User DB layer functions. These functions should take parameters from requests (never request objects themselves) and engines, and then call underlying DB functions. They should then pass the results up towards the API

### Web service

This service should provide an API and some views for use by the front end. When an API endpoint is called (or view is loaded), the service should:

- Grab an appropriate engine from the `DatabaseConnection` model
- Call the relevant `db` library function (should be only one in most cases)
- Gathers data from the service database via models if needed (this is for metadata that's inappropriate for storage in the User DB for some reason)
- Returns it to the API

## Permissions and users

We should, whenever possible, derive the access to any Django model based on access to the underlying DB object in real time. Details are [here](./permissions.md).

### Example

A user lists the columns for a table. Because they have access to read the columns of the table, they can read (their) display options for a table. If they have access to modify a column of a table, they have access to modify the relevant display options. This works as long as their isn't a dedicated `display_options` endpoint which could receive requests directly.

### Exceptions

There are some metadata and other models that we'll be keeping which _can_ receive direct requests. Currently, these are:

- Database connections
- Shareable links
- Explorations

Access to these will be managed using the Django permissions framework (i.e., with access policies).

### We should avoid

We should absolutely avoid caching or storing permissions and access to Django models based on permissions for underlying DB models. For example, if we ever want a user to manage display options directly, they should own _any_ display option they've created (and have access to it) regardless of their access (or lack of it) to the underlying DB object.
