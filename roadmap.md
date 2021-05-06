---
title: Roadmap
description: Roadmap for upcoming Mathesar features
published: true
date: 2021-05-06T16:52:43.638Z
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
- Mathesar's frontend should have a really intuitive and delightful user interface

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
- Users should be able to edit records using a spreadsheet-like interface.

## Data Types
- Users should be able to view and change the data types of columns in their table.
- Users should be able to upload files to create tables and have Mathesar guess appropriate types for their data.
- We will support the following data types:
	- Text
	- Email
	- URL
	- Boolean
	- Number
	- Money
	- Percentage
	- Date
	- Time
	- Date & Time
	- Duration
	- Relationship
- Users should be able to see data types for their column correctly even if they are not on the above list (which means that Mathesar does not support changing to that type yet).

## Filtering, Sorting, Grouping
Users should be able to perform these actions in both the GUI and API:
- Filter the table by rules applied to data in various fields.
- Sort the table by various fields.
- Group results by the first character of any given field.
- Group results by the first word of any given field.
- Apply multiple filters, groups, and/or sorts at once.

# TODO: Cleanup



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

