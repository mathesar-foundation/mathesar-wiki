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

## Navigation structure diagram

The navigation design will be based on the following structure:

| 1st Level         | 2nd Level       | 3rd Level       | 4th Level   |
|-------------------|-----------------|-----------------|-------------|
| Database Page     | Schema Page     | Table Page      | Record Page |
|                   | Data Explorer   | Exploration Page|             |
|                   | Data Import     |                 |             |

- 1st level: Database
- 2nd level: Schema
- 3rd level: Entities
- 4th level: Record

[Navigation by Page](https://balsamiq.cloud/sjfrgln/pbe3tnu/r7FA3?f=N4IgUiBcCMA0IDkpxAYWfAMhkAhHAsjgFo4DSUA2gLoC%2BQA%3D)

## Phasing Out Tab Navigation

Tabs will be phased out as part of the new navigation improvements.

## Changing 'Queries' to 'Explorations'

We've decided to alter the name of "Queries" to "Explorations" based on team input. When used with "Data Explorer," the term "query" becomes problematic. Also, because Mathesar queries are distinct from database queries, using the name "query" for them may cause confusion.

## Navigation Methods

Navigation within Mathesar will take place in three different ways:

- Through the site header
- Through links in pages
- Direct access through page URLs

### Navigation via site header

![image](/assets/design/specs/navigation/182923064-c3ad8df1-98a4-47e6-a7a7-5fc8eed8821f.png)

- The database page is linked via the logo in the site top (We'll require CRUD UI for databases when we finally add support for many databases, and we may create some extra UI that stays within the header at that point).
- Next to the logo is a breadcrumb navigation.
- The breadcrumb navigation content will display the user's trail of pages visited as well as toggles to search inside each navigation level using [page selectors](#page-selector).
- Upon reaching the record level, the top navigation will show a search records button, which will open the [Record Selector](/design/specs/record-selector.md) component.
- The current page will be excluded from the breadcrumb trail.
- The current page label will be displayed in the toolbar component below the top header component.
- Each type of page will be identified by an icon (table, schema, record etc.)

#### Note on Excluding the Current Page from the Breadcrumb Trail

We choose not to include the current page in the breadcrumb trail because the user can see it in the subheader area of the page. There aren't several ways to go to the same page in our link hierarchy, thus it's more like a `hierarchical navigation` than just a breadcrumb.

### Navigation via links within pages

Throughout Mathesar, the following links exist within pages which allow for more targeted navigation to other pages (This list is not comprehensive and may include additional link options when further features are implemented).

- **Database Page**
  - Links to **Schema Pages** in a list of schemas.

- **Schema Page**
  - Links to **Table Pages** in a list of tables.
  - Links to **Exploration Pages** in a list of queries.

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
  - Route: `/{database_name}/{schema_id}/`
  - Favicon: Schema
  - `<title>`: `{schema_name} | Mathesar`
  - By default, redirects to "Schema Page - Tables tab".

- **Schema Page - Tables tab**:
  - Route: `/{database_name}/{schema_id}/tables/`
  - Favicon: Schema
  - `<title>`: `Tables in {schema_name} | Mathesar`

- **Schema Page - Explorations tab**:
  - Route: `/{database_name}/{schema_id}/explorations/`
  - Favicon: Schema
  - `<title>`: `Explorations in {schema_name} | Mathesar`
  
- **Data Import: Upload file/Specify data**:
  - Route:  `/{database_name}/{schema_id}/import/`
  - Favicon: Mathesar logo
  - `<title>`: `Import Data | {schema_name} | Mathesar`

- **Data Import: Preview table - Confirmation page**:
  - Route:  `/{database_name}/{schema_id}/import/{table_id}/`
  - Favicon: Mathesar logo
  - `<title>`: `Confirm {table_name} | {schema_name} | Mathesar`

- **Data Explorer - New Exploration**:
  - Route: ``/{database_name}/{schema_id}/data-explorer/`
  - Favicon: Data Explorer
  - `<title>`: `Data Explorer | {schema_name} | Mathesar`
  
- **Data Explorer - Open Exploration**:
  - Route: ``/{database_name}/{schema_id}/explorations/{exploration_id}/`
  - Favicon: Data Explorer
  - `<title>`: `{exploration_name} | {schema_name} | Mathesar`

- **Table Page**:
  - Route:  `/{database_name}/{schema_id}/tables/{table_id}/`
  - Favicon: Table
  - `<title>`: `{table_name} | {schema_name} | Mathesar`

- **Record Page**:
  - Route: `/{database_name}/{schema_id}/tables/{table_id}/{record_id}`
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
- Focus the input on opening, allowing the user to begin typing immediately.
- Allow keyboard navigation to select an item using Up/Down/Enter keys.

[Schema Selector Wireframe](https://share.balsamiq.com/c/ucdy2SPtAMPxErX4wh3fdS.png)

[Entities Selector Wireframe](https://share.balsamiq.com/c/qVGHzaycnKF5u8pLBsvrvS.png)
