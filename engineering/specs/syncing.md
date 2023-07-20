---
title: Syncing Database Objects
description: How we sync between the database and the web service
published: true
date: 2023-07-19T23:28:26.520Z
tags: 
editor: markdown
dateCreated: 2021-06-01T10:43:59.890Z
---

We synchronize database objects between the database and the web service layers through reflection of those objects. For any object created through the Mathesar web interface, we do this by having the web service create a model instance in its service database corresponding to the created object.  However, for objects created via other means, we reflect these in the Mathesar UI by capturing the state of relevant objects in the database, and propagating that state upwards to the web service's models, and then eventually the UI. For more information about database reflection, see the [SQLAlchemy docs](https://docs.sqlalchemy.org/en/14/core/reflection.html).

# Goal

The UI should reflect the current state of the DB, subject to performance constraints.

# Database object models

We include the `oid` field for each database object model (currently table or schema) in order to identify it in the database.

## Renew models whenever listing

Whenever we perform an action such as 'list all tables in schema' or 'list all schemata in database', we reflect all DB objects.  However, we only do so at most every 5 minutes.  This is accomplished by checking the Django cache for a particular key, `database_reflected_recently`.  We don't store any actual _data_ in the cache, but rather in the `Schema` and `Table` models.  The cache only serves to let us know when to re-reflect the underlying DB objects and make appropriate changes to the model tables.

In the current codebase, we trigger the function to check the cache and reflect DB objects when needed whenever we access the queryset for either the `SchemaViewSet` or `TableViewSet` (in `mathesar/views/api.py`). To do this, we use the special `get_queryset` function. This gets picked up and automatically run when the ViewSet is called. Using this allows us to run arbitrary code before returning the queryset. In particular, we call the function `reflect_db_objects` in the same module.  This function finds all DB objects by their `oid`, and notes any changes.

# Cache names of objects

Since we use the `name` property of DB objects more than anything else, we cache it using the Django cache framework.

# Importing a previously-existing DB

We'll "import" a previously existing DB simply by reflecting all schemata in the database, and then reflecting all tables in each schemata, adding the resulting objects to the `Schema` and `Table` model tables as we go.

# Objects which are always read on the fly

Records and Columns of tables are always read from the DB on the fly.
