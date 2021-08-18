---
title: Feature Ideas
description: Ideas for features that aren't in our roadmap yet.
published: true
date: 2021-07-16T19:22:39.942Z
tags: 
editor: markdown
dateCreated: 2021-04-20T19:47:31.098Z
---

These are potential feature ideas for Mathesar. Each section represents a conceptual grouping of features.

> Please note that this list is long and disorganized. Some are slated to be built in our roadmap, and others we might not build at all. Features ideas that are already specced out in our roadmap are not listed here.
{.is-warning}


## Views
Users should be able to:
- Save filtered/sorted/grouped tables as views.
- Create a calendar view based on date and time fields in their data
- Create a histogram chart view based on their data
- Create a pie chart view based on their data
- Create a line graph view based on their data
- Create a scatter plot view based on their data
- View all saved views and switch between views
- Set a default view for a table/schema
- Delete a view
- Rename a view

## Computed Data
Users should be able to:
- Create a new column that computes data from other columns using forumulas.
- Create "subtotals" for grouped views
	- Support different types of subtotals: SUM, AVG, MIN, MAX, MED
- Create summary views based on subtotals, and use that data in views
	- e.g. given a database of sales with dates, create a summary view of sales per quarter and put that into a histogram


## Installation and Configuration
Users should be able to:
- Follow provided instructions to install Mathesar on a server.
	- The installation process should only install PostgreSQL if needed.
- Access existing PostgreSQL databases via Mathesar using existing PostgreSQL user credentials.
	- Existing databases should reflect all columns and types correctly in the user interface.
- Set up a PostgreSQL server automatically if none exists.
- Create a new database from scratch.
- Create an initial user if needed.
- Configure sending email (for password resets, notifications)

## User Management
Users should be able to:
- Log in
- Log out
- Create a new user with permissions: admin, editor, viewer
- Change a user's permissions
- Reset a user's password
- Reset their own password (if email is enabled)

## Collaboration
- Users should be able to share tables, schemas, and/or views with either:
	- the general public (no sign in required)
	- all signed in users
	- specific users
- Each of these should support:
	- admin, view, edit permissions
- Existing postgres permissions should be respected/reflected

## Data Workflow Improvements
Users should be able to:
- Search for data across various tables and schemas
- Bulk edit data
- Bulk import new data into an existing collection
- Export data to:
	- SQL
	- CSV
	- TSV
	- JSON
	- Excel
	- XML



## Additional Imports
Users should be able to import data in the following additional formats:
- SQL
- JSON
- XML
- Google Sheets import (via API)
- Excel file upload
- Excel web import (via API)
- Apple Numbers file upload
- Collabora import
- Airtable

## Location Type
- Add new type, using existing PostGIS type where possible:
	- Location
- Autodetect this type during import
- Allow user to change columns to this type
- Add additional grouping options:
	 Street Address
	 Country
	 Administrative Area Level 1 *(in the US, these are states)*
	 Administrative Area Level 2 *(in the US, these are counties)*
	 Administrative Area Level 3
	 Administrative Area Level 4
	 Administrative Area Level 5
	 Locality *(city/town)*
	 Sublocality *(subdivision of city/town)*
	 Neighborhood
	 Postal Code
	 Latitude
	 Longitude

The attributes of the location column type are based on results returned by the [Google Maps Geocoding API](https://developers.google.com/maps/documentation/geocoding/overview), Since they\'ve done the work of putting addresses into a global format.

## Phone Number Type
- Add new type
	- Phone Number
- Autodetect this type during import
- Allow user to change columns to this type
- Add grouping options:
	- Country Code
	- Area Code

## Additional Fields
- File field (for images, attachments, etc.)
- IP Address field
- Formula field (use of spreadsheet like formulas)
- JSON field

## Additional Views
- Map view
- Card (Gallery) view
- Kanban view
- Data modeling view (of entire schema or database)

## Forms
- Create forms that allow users to enter data into views

## Data Syncing
Users should be able to sync data both ways from:
- Google Sheets
- Airtable
- Excel (web)
- Airbyte connectors?

## Data Suggestions
Users should get suggestions about:
- Visualizations they can apply to their data
- Aggregations they can apply to their data
- Schema imporovements they can make to their data

## Versioning
Users should be able to:
- Save a snapshot of their database, schema, or table.
- Revert to a previous version of their database, schema, or table.
- Undo and redo recent actions.

## Events
Events in the system should be exposed via an API. e.g.
- New table created
- Table schema changed
- New data added

## Notifications
Users should be able to:
- Get email notifications of various events.
- Get web notifications of various events.

## Templates
Users should be able to:
- Save databases, schemas, applications as templates.
- Use a template to create a new database, schema, or application.
- Edit template attributes.
- Delete a template.
- Browse existing templates.
- Search for templates.

## Improved User Management
Users should be able to:
- Create teams of users, teams can have similar permissions to users.

## API
- API key management
- API documentation

## Freeform Data Support
- UI to handle freeform data (JSON) well
- Suggest conversion of non-tabular data to tabular data based on schema
- Automatically generate appropriate tabular data if consistency exists in imported freeform data

## SQL Exploration
- Run SQL from the web interface

## Comments
- Comment on data

## Database Feature Support
- Handle editing, deleting, and infinite scroll for tables without primary keys or with multiple primary keys.
- Cursor based pagination.