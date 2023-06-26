---
title: Publicly shareable links
description: 
published: true
date: 2023-06-26T06:48:29.729Z
tags: 
editor: markdown
dateCreated: 2023-06-26T05:03:37.643Z
---

> This spec is a work in progress.
{.is-warning}

This spec describes the working principle of the initial versions of Publicly shareable links and ability to embed tables & explorations in other sites.

## Goals
* Users should be able to publicly share tables & explorations as links.
* Users should be able to embed tables and explorations in other sites.

## Scope
* The links are focused only on tables and explorations.
* The links would produce a read-only version of tables and explorations.
* The public links will not contain default filters, groups, and sorting. If users want them, they can create explorations and share them.
* Control panel (i.e. bar to filter, group, sort) will always be present for now.
* Inspector will not be visible in shared tables & explorations.

## Assumptions
* Only users with manager access would want to share tables & explorations publicly.

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

## Backend implementation feasibility
- Bypassing login for APIs involved in displaying a readonly table/query.
  - Get DB, schema, table, records, columns, query etc.,
- APIs to generate links, clear link, regenerate link, get link for table/query, and get table/query for link.
- URL routing to public links.

## Frontend implementation feasibility

## Appendix

### Scheduled for later iterations
- Shared views with persisted filters, grouping etc.,
- Option to restrict by password
- Sharing record page & forms
- Option to share as editor
- Option to show inspector

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
