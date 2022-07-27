---
title: Navigation Updates
description: 
published: true
date: 2022-08-25 18:02:53
tags: 
editor: markdown
dateCreated: 2022-08-25 18:02:58
---

## Context

Mathesar users must be able to navigate between pages and know where they are at any point while using the system.

### Design Goals

- Users clearly understand which page they're on
- Users easily navigate to other pages
- Users may anticipate the result of navigation interactions

### Hierarchical Structure

The navigation design will be based on the following navigational structure:

- Database
  - Schema
    - Table
      - Record
    - Query

### Phasing Out Tab Navigation

Tabs will be phased out as part of the new navigation improvements.

## Navigation Methods

Navigation within Mathesar will take place in three different ways:

- Through the site header
- Through links in pages
- Direct access through page URLs

### Navigation via site header

- The logo in the site header will link to the site root, in this case the database homepage.
- As the user navigates across the pages, a breadcrumb-like navigation will be presented in the top part of the site's header.
- Clicking on a breadcrumb element opens a selector with a list of schemas or entities based on the current page level.
- The breadcrumb will not include the current page.
- The current page label will be placed in a sub-header component underneath the top header part.
- Each type of page will be identified by an icon (table, schema, record etc.)
- When we finally add support for many databases, we'll require CRUD UI for databases, and at that time we may create some extra UI that stays within the header.

Wireframes:
[Wireframes](https://share.balsamiq.com/c/gxcTvc7VrSANmndaHABNWC.png)

### Navigation via links within pages

Throughout Mathesar, the following links exist within pages which allow for more targeted navigation to other pages.

- **Database Page**
  - Links to **Schema Pages** in a list of schemas.

- **Schema Page**
  - Links to **Table Pages** in a list of tables.
  - Links to **Query Pages** in a list of queries.

- **Table Page**
  - Within the table data:
    - Links to the **Record Page** for each row via the row's primary key cell value. _Note: Links within cell values will only be clickable when the cell is selected. This UX should be consistent with the behavior of the "URL" UI Type._
    - Links to **Record Pages** for related records via the FK cell values
  - Links to the **Table Page** for related tables via a section within the Table Inspector.

- **Data Explorer**
  - Features the same links as described by the "Within the table data" bullet point on Table Page above.

- **Record Page**
  - Links to other **Record Pages** via FK fields on directly on the record.
  - Links to other **Record Pages** via tabular displays of _other records linking to this record_ via the same UI as the Table Page which has links in the PK cells.

### Navigation via page url

- **Home Page**:
  - Route: `/`
  - Note: the Home Page route responds with an HTTP 302 redirect to the Database Page for the database configured when installing Mathesar. When we eventually add support multiple databases, we may wish to give this design more thought.

- **Database Page**:
  - Route: `/{database_name}/`
  - Favicon: Mathesar logo
  - `<title>`: `{database_name} | Mathesar`

- **Schema Page**:
  - Route: `/{database_name}/{schema_id}`
  - Favicon: Schema
  - `<title>`: `{schema_name} | Mathesar`

- **Table Page**:
  - Route:  `/{database_name}/{schema_id}/{table_id}/`
  - Favicon: Table
  - `<title>`: `{table_name} | {schema_name} | Mathesar`

- **Query Editor Page**:
  - Route: `/{database_name}/{schema_id}/query/{table_id}/`
  - Favicon: Query
  - `<title>`: `{query_name} | {schema_name} | Mathesar`

- **Record Page**:
  - Route: `/{database_name}/{schema_id}/{table_id}/{record_id}`
  - Favicon: Record
  - `<title>`: `{record_summary} | {table_name} | {schema_name} | Mathesar`
