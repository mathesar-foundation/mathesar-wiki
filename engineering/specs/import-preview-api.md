---
title: Import Preview API
description: Spec for API to preview an imported CSV as a typed table
published: true
date: 2023-05-11T14:32:12.045Z
tags: 
editor: markdown
dateCreated: 2021-07-02T15:26:50.560Z
---

> This spec is accurate as of 2021-09-06, but we will not be updating it in the future.
{.is-warning}

Relevant issues are:

[\#199](https://github.com/centerofci/mathesar/issues/199), [\#200](https://github.com/centerofci/mathesar/issues/200), and [\#201](https://github.com/centerofci/mathesar/issues/201)

As specified in the table import [design spec](/design/specs/table-import), we need to be able to support a flow where the user imports a CSV, then sees a preview of the table which would be created, with inferred types.  Thus, we need to create a table preview endpoint.

## Changing whether the first row is a header

In order to change whether the first row of the CSV is used as a header or not, we will need update the data file and recreate the table from it. This is accomplished by changing the `header` parameter of the data file resource via a `PATCH` request. This controls whether to use the first row as headers.

## Possible type alterations for a column

The `columns` endpoint will now include the possible targets for type alteration of that column.  For example, a string can be altered to any type.  An integer, however, can't be altered to an email type. At the moment, possible target types will be determined _only_ by the current type of the column, and not the data it contains.

## Preview Endpoint behavior

For previewing the inferred types and names of columns, we will use a new `previews` endpoint under the table detail endpoint.  We'll submit a `POST` to the endpoint to create the preview, and then receive a JSON formatted as in the normal table detail endpoint in return with the modified table.
```
POST /api/db/vX/tables/<table_id>/previews/
```
could have submitted JSON like:
```json
{
    "columns": [
        {
            "name": "mathesar_id",
            "type": "INTEGER",
        },
        {
            "name": "Center2",
            "type": "VARCHAR"
        },
        {
            "name": "Status",
            "type": "VARCHAR"
        },
        {
            "name": "Case Number",
            "type": "VARCHAR"
        },
        {
            "name": "Patent Number",
            "type": "TEXT"
        }
    ]
}
```
The full table blob should be returned, so a return for the above request could be something like:
```json
{
    "id": 1,
    "name": "the_patents_table",
    "schema": 2,
    "created_at": "2021-07-07T09:00:30.108653Z",
    "updated_at": "2021-07-07T09:00:30.108707Z",
    "columns": [
        {
            "id": 1,
            "name": "mathesar_id",
            "type": "INTEGER",
            "type_options": null,
            "display_options": null
        },
        {
            "id": 2,
            "name": "Center2",
            "type": "VARCHAR",
            "type_options": null,
            "display_options": null
        },
        {
            "id": 3,
            "name": "Status",
            "type": "VARCHAR",
            "type_options": null,
            "display_options": null
        },
        {
            "id": 4,
            "name": "Case Number",
            "type": "VARCHAR",
            "type_options": null,
            "display_options": null
        },
        {
            "id": 5,
            "name": "Patent Number",
            "type": "TEXT",
            "type_options": null,
            "display_options": null
        }
    ],
    "records": "http://localhost:8000/api/v0/tables/1/records/",
    "data_files": [
        1
    ]
}
```


### Implementation of Preview

Because we eventually want to do type inference in a temporary table, we'll avoid using the table resulting from the current process in the preview action.  Instead, the implementation will simply put together a select with casts (using the custom casting functions defined by the Mathesar installation) and aliases.

## Saving changes

The changes to column types and names can be saved by submitting a `PATCH` request to the `tables` endpoint, with the column list being the same as the `previews` request.  

Table name changes should be submitted using the already existing `PATCH` behavior (i.e., a `PATCH` with the `name` key changed).

```
PATCH /api/db/vX/tables/<table_id>
```
could submit a JSON like:
```json
{
    "columns": [
        {},
        {
            "id": 2,
            "name": "Center"
        },
        {
            "id": 3,
            "type": "TEXT"
        },
        {
            "id": 4,
        },
        {
            "id": 5,
            "name": "Patent ID",
            "type": "INTEGER"
        }
    ]
}
```
The full table blob will be returned, so a return for the above request could be something like:
```json
{
    "id": 1,
    "name": "the_patents_table",
    "schema": 2,
    "created_at": "2021-07-07T09:00:30.108653Z",
    "updated_at": "2021-07-07T09:00:30.108707Z",
    "columns": [
        {
            "id": 1,
            "name": "mathesar_id",
            "type": "INTEGER",
            "type_options": null,
            "display_options": null
        },
        {
            "id": 2,
            "name": "Center",
            "type": "VARCHAR",
            "type_options": null,
            "display_options": null
        },
        {
            "id": 3,
            "name": "Status",
            "type": "TEXT",
            "type_options": null,
            "display_options": null
        },
        {
            "id": 5,
            "name": "Patent ID",
            "type": "INTEGER",
            "type_options": null,
            "display_options": null
        }
    ],
    "records": "http://localhost:8000/api/v0/tables/1/records/",
    "data_files": [
        1
    ]
}
```


This would set the columns in the preview to have the specified names and types. Any column which is unaltered would have and empty JSON object (as in the 0th column above), otherwise, only attributes of a column which are to be altered would be submitted in the request. So, in the example:
- we alter nothing about the 0th column,
- we alter the name of the 1st column, 
- we alter the type of the 2nd column,
- we dropped the 3rd column, and
- we alter both the name and type of the 4th column.

Please note that both name and columns cannot be changed in the same request at the moment.