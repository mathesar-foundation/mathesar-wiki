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

### Navigation structure diagram

The navigation design will be based on the following structure:

| 1st Level         | 2nd Level       | 3rd Level     | 4th Level   |
|-------------------|-----------------|---------------|-------------|
| Database Homepage | Schema Homepage | Table Page    | Record Page |
|                   |                 | Query Page    |             |
|                   |                 | Data Explorer |             |

### Phasing Out Tab Navigation

Tabs will be phased out as part of the new navigation improvements.

## Navigation Methods

Navigation within Mathesar will take place in three different ways:

- Through the site header
- Through links in pages
- Direct access through page URLs

### Navigation via site header

- The logo in the site header will lead visitors to the site's root, in this case the database homepage.
- A breadcrumb-like navigation will be displayed at the top part of the site's header as the user navigates through the pages.
- When users click on a breadcrumb element, a [page-selector](#page-selector) component is displayed with a list of schemas or entities based on the breadcrumb level.
- Upon reaching the record level, the top navigation will show a 'Go to Record' action, which will open the [Record Selector](/engineering/specs/record-selector) component.
- The current page will not be included in the breadcrumb path.
- The current page label will be placed underneath the top header component in a sub-header component.
- An icon will be used to identify each type of page (table, schema, record etc.)
- When we eventually add support for several databases, we'll need CRUD UI for databases, and we may design some additional UI that stays within the header at that point.

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

## Components

### Page Selector

Pages within a group can be accessed through the top navigation's page selector component.

- Users can click on a expand icon next to each of the breadcrumb level's items.
- If the current page is a schema homepage, the user expands the database level item to see a list of all the database schemas.
- If the user's current page contains a table, the schema level item will expand to show all tables inside that schema.
- From the page selector a user can scroll through all the listed items.
- A search input is provided so that users can match the desired item by name.
- Highlight will be used to indicate the text portion that was matched.
