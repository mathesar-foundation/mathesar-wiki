---
title: Import Preview API
description: Spec for API to preview an imported CSV as a typed table
published: true
date: 2021-07-07T13:44:47.885Z
tags: 
editor: markdown
dateCreated: 2021-07-02T15:26:50.560Z
---

Relevant issues are:

[\#199](https://github.com/centerofci/mathesar/issues/199), [\#200](https://github.com/centerofci/mathesar/issues/200), and [\#201](https://github.com/centerofci/mathesar/issues/201)

As specified in the table import [design spec](/design/specs/table-import), we need to be able to support a flow where the user imports a CSV, then sees a preview of the table which would be created, with inferred types.  Thus, we need to create a table preview endpoint.

## Possible type alterations for a column

The `columns` endpoint will now include the possible targets for type alteration of that column.  For example, a string can be altered to any type.  An integer, however, can't be altered to an email type.  Possible target types will be determined _only_ by the current type of the column, and not the data it contains.

## Preview Endpoint behavior

For previewing the inferred types and names of columns, we will use the normal table detail endpoint, with a `alter_preview` query string parameter to define column modifications.  The columns will be given as a list of JSON objects, similar to the `PATCH` requests sent to alter columns via the `columns` endpoint.  We will allow multiple alterations of a given column in a preview, however.  If the columns are given, _all_ must be given with at least some JSON object representation of desired alterations.  In order to leave a column unaltered in the preview, the empty JSON object should be given.  To represent a dropped (or unshown) column, the JSON object should contain a key name set to `null`.  A request to a table with four columns, `mathesar_id`, `name`, `email`, and `backup_email` (in that order) might look like:
```
GET /api/vX/tables/<table_id>/?alter_preview=[{}, {"name": "Student Name"}, {"type": "email"}, {"name": null}]
```
In this example, we've left the `mathesar_id` column unaltered, changed the `name` column name to `Student Name`, changed the type of the `email` column to `email`, and dropped the `backup_email` column.

## Implementation of Preview

Because we eventually want to do type inference in a temporary table, we'll avoid using the table resulting from the current process in the preview action.  Instead, the implementation will simply put together a select with casts (using the custom casting functions defined by the Mathesar installation), aliases, and omitting "dropped" columns.

## Saving changes

The changes to column types and names can be saved by submitting a `PATCH` request to the `tables` endpoint, with the column list being as in the `alter_preview` query string parameter.  Table name changes should be submitted using the already existing `PATCH` behavior (i.e., a `PATCH` with the `name` key changed)
