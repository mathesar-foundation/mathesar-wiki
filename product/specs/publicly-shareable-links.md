---
title: Publicly shareable links
description: 
published: true
date: 2023-06-27T06:32:04.063Z
tags: 
editor: markdown
dateCreated: 2023-06-26T05:03:37.643Z
---

> This spec is a work in progress.
{.is-warning}

This spec describes the working principle of the initial versions of Publicly shareable links and ability to embed tables & explorations in other sites.

## Goals
* Users should be able to publicly share tables & explorations via links.
* Users should be able to embed tables and explorations in other sites.

## Scope
* The links are focused only on tables and explorations.
* The links would produce a read-only version of tables and explorations, i.e. only 'viewer' access.
* The public links will not contain default filters, groups, and sorting. If users want them, they can create explorations and share them.
* Control panel (i.e. bar to filter, group, sort) will always be present for now.
* Inspector will not be visible in shared tables & explorations.

## Assumptions
* Only users with manager access would want to share tables & explorations publicly.
* Embedding is assumed to take less work as the idea is only to provide code for an iframe with the public link. This may be removed from the initial verison as part of scope reduction if the work takes longer than anticipated.

## Suggested UX flow
- UX for sharing
  - Dropdown with option to generate a public link.
  - Button is also present within inspector.
  - If link is already generated, we highlight the dropdown button to indicate that it's already shared.
  - Option to clear link.
  - Option to regenerate link.
  - Help content & link to docs.
- UX for shared table/exploration
  - Read-only.
  - Has control pane to filter, sort, group etc.,
  - Does not contain inspector.

## Backend implementation approach
### Endpoints & DB schema:
- A django model `public_links`, with fields:
  - "hash": UUID, not null, unique.
  - "entity": string, enum of 'table', 'query'. (In the future, this would extend to 'record', 'form' etc.,).
  - "entity_id": integer, Django id of the related entity.
  - Unique constraints:
    - hash
    - entity + entity_id
- APIs to:
  - generate link, clear link, regenerate link, retrieve link for entity (manager access)
  - retrieve entity for link (public access - no authentication required)
- A pg trigger will be added to the tables `mathesar_table` and `mathesar_query` which will execute when a row is deleted. This trigger will delete any public hash that is present for the table/query in the `public_links` table.
  - I'm not certain if there's an easy way of doing this with Django. I need some suggestions/ideas around this from the backend team.
### Accessing the public url:
- Handling routing:
  - An url path `/public/<hash>/` would be added. This will have a view associated with it, and would render `common_data` similar to the existing schema ui paths.
  - `common_data` will contain scoped information based on the requested resource identified from the hash. Eg., If the requested resource is a table, we will provide only the related databases, schema, and table information within `common_data`.
- Bypassing authentication for APIs needed by frontend:
  - For publicly shared content, we should be able to bypass login for the GET requests required to display the table/ query in the UI. This includes GET endpoints in tables, queries, columns, records etc.,
  - The frontend will set a request header `public_link_hash` when attempting to access these endpoints via a publicly shared url. The value of this request header will be the same as the hash of the public link.
    - Eg., `public_link_hash`: `f2eea1b0-591f-4414-89ae-87d1688bf1d6` 
  - This can be done by adding custom permission classes to these specific endpoints, which override the default `rest_framework.permissions.IsAuthenticated` class, and changes the condition to:
    - If isAuthenticated, provide access.
    - If not authenticated, Check if the request contains the `public_link_hash` header. If no, reject request.
      - If `public_link_hash` header is present, Check if the `public_links` table contains the hash. If no, reject request.
        - If `public_links` table contains the hash, identify the entity the hash relates to. Check if the requested object (column, record, table etc.,) is either the same entity or a sub-entity of it. Eg., If a column is requested and the hash is linked to a table, check if the column is part of the table. If no, reject request.
          - If yes, allow request.
- Bypassing authorization for APIs needed by frontend:
  - The custom auth mentioned above would only be applied to GET methods of selected endpoints for actions like list, retrieve. Essentially, everything a viewer would have access to.
  - Since the user is autonomous, we do not have to specify a custom `scope_queryset` since the access to the requested resource is public.
  - If the user is already logged in, we do not have to do any of this and let the existing logic take over.

## Frontend implementation approach
- Handling routing:
  - Route would be `/public/<hash>`.
  - Upon request, the frontend will call the `public_links` retrieve the entity associated with the link. Based on the entity, it would show a table view or an exploration view.
- Sending an additional request header:
  - A request header `public_link_hash` will be sent will all API requests when the current parent route is `/public/`. The value of this header would be the same as the hash.

## Appendix

### Scheduled for later iterations
- Shared views with persisted filters, grouping etc.,
- Option to restrict link access by password
- Sharing record page & forms
- Option to share as editor
- Option to show table/exploration inspector

### Competitive research

#### Airtable
- Option to generate link & embedding view is present in menu bar.
- Shared views are read-only.
- Option to share entire bases.
- Links:
  - Once link is generated, there are options to clear it, generate new link.
  - Options to restrict/allow users to copy data from view. Options to restrict/show all fields, including ones created in future.
  - Option to restict by password or by email domain (needs higher plan).
- Embed:
  - Provides code to embed iframe.
  - Shows desktop and mobile preview.
  - Option to show/hide controls bar.
- Filters, groups, and sorting added to a table is applied to the shared output view.
  - This is possible because this configuration is always persisted.
- Option to share form for cases where adding data is required.

#### NocoDB
- Link is automatically generated for all tables.
- Option to restrict access via a password.
- Option to restrict/allow download.
- Filters, hidden columns, sorting etc., are automatically applied to shared link.
  - This is possible because this configuration is always persisted.
- Shared content is read-only.

#### Google sheets
- Option to share content as viewer, commenter, and editor.