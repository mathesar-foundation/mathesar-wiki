---
title: Syncing Database Objects
description: How we sync between the database and the web service
published: true
date: 2021-06-01T08:25:56.898Z
tags: 
editor: markdown
dateCreated: 2021-06-01T08:20:27.438Z
---

We synchronize database objects between the database and the web service layers through reflection of those objects. For any object created through the Mathesar web interface, we do this by having the web service create a model instance in its service database corresponding to the created object.  However, for objects created via other means, we reflect these in the Mathesar UI by capturing the state of relevant objects in the database, and propagating that state upwards to the web service's models, and then eventually the UI. For more information about database reflection, see the [SQLAlchemy docs](https://docs.sqlalchemy.org/en/14/core/reflection.html).

# Goal

The UI should reflect the current state of the DB, subject to performance constraints.

# Database object models

We include the following fields for each database object model (currently table or schema):

- `name` (character) -- displayed to user
- `last_synced` (datetime) -- used for determining whether to renew the state of the model under certain conditions.
- `oid` (integer) -- used to precisely identify the object in question in the database.
- `deleted` (boolean) -- we mark an object `deleted` when it's been removed.

## Renew models whenever listing

Whenever we perform an action such as 'list all tables in schema', we update all table resources associated with that schema. This will also be the case for 'list all schemata in database'.

In the current codebase, we have two relevant viewsets where we want to trigger a refresh whenever we access their queryset, the `SchemaViewSet` and the `TableViewSet` (both in `mathesar/views/api.py`)

## Use cache whenever an object is called directly

Whenever we get a specific object by ID, we'll simply use the model for performance reasons rather than re-reflecting each time. This means we'll need to have error handling for whenever the underlying resource has changed in some incompatible way.
