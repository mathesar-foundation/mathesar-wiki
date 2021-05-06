---
title: Roadmap
description: Roadmap for upcoming Mathesar features
published: true
date: 2021-05-06T15:01:06.174Z
tags: 
editor: markdown
dateCreated: 2021-04-20T19:43:28.320Z
---

# Introduction

This version of the roadmap is only for the alpha/minimum viable product (MVP) version of Mathesar, expected to ship fall 2021. Our plan is to build all the features required for a user for a very simple use case. Once we've shipped that, we will then expand the roadmap based on user feedback and enabling more complex use cases.

The initial use case we've chosen is a user creating and maintaining a basic inventory of their media collection using Mathesar. Please see the following design documents for more information:
- [Inventory Use Case exploratory document](/design/exploration/inventory-use-case)
- [Inventory: Data Exploration exploratory document](/design/exploration/inventory-data-exploration)
- [Inventory Use Case report/conclusions](/design/reports/inventory-use-case)

The roadmap below reflects the features needed to create a good user experience for this use case.

# General Principles
These principles are not directly applicable to the use case above, but are being followed to ensure that our architecture works for our eventual vision.

- Mathesar should be able to work with existing databases without altering data, even if not all features are available.
- Mathesar should support other frontend clients (all actions should be available via API)

# Roadmap

## Database
- Users should be able to configure a Postgres database to use with Mathesar.
- We should create the configured database if it does not exist.

## Schemas
- Users should be able to manage schemas using the GUI or API (view, create, edit, delete)

## Tables
- Users should be able to manage tables using the GUI or API (view, create, edit, delete)
- Users should be able to create a table through the following methods:
	- Uploading a CSV file
  - Uploading a TSV file
  - Copy/pasting from a spreadsheet.

## Records
- Users should be able to manage records using the GUI or API (view, create, edit, delete)

## TODO: Cleanup

## CRUD For Tables & Schemas
Users should be able to perform these actions in both the GUI and API:

### GUI & API
- Create a new table
	- in an existing schema
	- in a new schema
- Create a table via importing data via
	- CSV
	- TSV
- View a table and see what type each column is.
- Edit a table name
- Edit a schema name
- Delete a table
- Delete a schema

### GUI only
- Create a table via
	- copy/paste from a spreadsheet
- Edit the data in their table using a spreadsheet-like interface
	- e.g. fill down cells by dragging a corner

## Filtering, Sorting, Grouping
Users should be able to perform these actions in both the GUI and API:
- Filter the table by rules applied to data in various fields.
- Sort the table by various fields.
- Group results by the first character of any given field.
- Group results by the first word of any given field.
- Apply multiple filters, groups, and/or sorts at once.

## Multiple Types Support
Users should be able to perform these actions in both the GUI and API:
- Change the type of data per-column to any type supported by Postgres or PostGIS
	- The data in the column will be validated.
- Import data via any supported import method and have the types of data automatically detected during the import process
	- Types are suggestions and can be changed by the user.

## Boolean Type
- Add new type (use Postgres type if possible):
	- Boolean
- Autodetect this type during import
- Allow user to change columns to this type
- Add additional grouping options by value (yes/no)

## New Text Types
- Add new types:
	- Email
	- URL
- Autodetect these types during import
- Allow user to change columns to these types
- Add additional grouping options:
	- Email: Domain
	- URL: TLD, Protocol

## Numeric Types
- Add new types, using existing Postgres types where possible:
	- Money (with specified currency)
	- Percentage
	- Number
- Autodetect these types during import
- Allow user to change columns to these types
- Add additional grouping options:
	- Number: Range (calculate range options dynamically based on data, e.g. if data varies from 1-100, ranges could be 1-10, 10-20, etc.)
	- Money: Range, Currency
	- Percentage: Range
  
## Date and Time Types
- Add new types, using existing Postgres types where possible:
	- Date & Time
	- Date
	- Time
	- Duration
- Autodetect these types during import
- Allow user to change columns to these types
- Add additional grouping options:
	- Date & Time, Date, Time support all grouping options supported by Postgres EXTRACT function.
	- Duration: Range
- Allow filtering using natural language for dates (e.g. "next month")

## Relationship Type
Users should be able to:
- Create a column that represents a relationship to another record (e.g. Book --> Author)
- "Extract" a column from a table into a separate table (change the underlying schemas)
- Choose which field from the other table to use to represent the relationship (e.g. if I'm displaying the Author in the Book table, I want to see the Author's name, not ID)

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

> Please see [Feature Ideas](/feature-ideas) for a long and non-organized list of feature ideas that we're drawing from.
{.is-info}

