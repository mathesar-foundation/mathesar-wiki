# "Database Connections" Page Design Specs

**Design Link:**
[Figma Design](https://www.figma.com/file/xHb5oIqye3fnXtb2heRH34/Styling?type=design&node-id=6423-3425&mode=design)

## Overview

- The goal is to create a dedicated page titled "Database Connections." This will serve as the primary entry point for managing and setting up connections. Read more about the issue here: [Github Issue](https://github.com/centerofci/mathesar/issues/3244)
- This page should be accessible from the main navigation menu when clicking on the Mathesar logo.
- Post-installation, this will be the initial onboarding step for users.

## List of Connections

The list of connections is the main content of the page. It should be a table with the following columns:

- Connection Name
- Database Name
- Host
- Port
- Action Buttons (Edit & Delete)

**Interactions:**

- Users should be able to search for a specific connection by its 'Connection Name'.
- Column header interactions: Sorting by any column. Default sort by 'Connection Name'.
- On-hover state for each row.
- Click on 'Connection Name' to view database and schemas.

**Functionality:**

- The list should support pagination if the number of connections exceeds a predefined limit. The goal should be to have the table fit within the viewport without scrolling so that the header is always visible.

**Empty State:**

When no database connections are present:

- Display a message: "No database connections yet. Seems you haven't set up any connections. To use Mathesar, you'll need to connect one."
- Provide an "Add Database Connection" button that opens the "New Database Connection" modal.

## Adding New Database Connection

**Modal Form:**

- The modal should be titled "New Database Connection".
- The modal fields are dependent on the following spec: [“New Database Connection” Form Design Specs](https://wiki.mathesar.org/design/specs/new-db-connection-form/).

**Interactions:**

- The modal should be opened by clicking on the "Add Database Connection" button in the empty state.
- The modal should be opened by clicking on the "New Database Connection" button in the Connections List page.

## Editing Database Connection

**Modal Form:**

- The modal should be titled "Edit Database Connection".
Provide an inline form (or modal) similar to the addition form but pre-filled with the existing details.
- The modal is pre-filled with the existing details except for the 'Password' field.
- Users should be able to update all the fields except the 'Connection Name'.

## Deleting Database Connection

Before deletion, prompt users with a confirmation dialog.

**Confirmation Dialog:**

- The modal should be titled "Delete Database Connection?".
- The modal should display the name of the connection to be deleted.
- The modal includes a checkbox to "Also delete associated Mathesar schemas".
- The modal should provide a warning note explaining that deleting the associated Mathesar schemas will delete all the related data.

**Interactions:**

- The modal should be opened by clicking on the "Delete" button in the Connections List table.

## Database Page Modifications
As part of this design, the current database page must be modified to remove the sidebar database navigation. 

<img width="1511" alt="image" src="https://github.com/centerofci/mathesar-wiki/assets/845767/6d6c97f8-a9c1-4d5e-9be3-7571bcdff284">



