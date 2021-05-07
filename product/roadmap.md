---
title: Roadmap
description: Roadmap for upcoming Mathesar features
published: true
date: 2021-05-07T20:39:53.771Z
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

The roadmap below reflects the features needed to create a good user experience for this use case, while following our general [product principles](/product).

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
Users should be able to:
- Filter tables by various fields.
- Sort the tables by various fields.
- Group results by various fields.
- Apply multiple filters, groups, and/or sorts at once.

Each data type will support its own types of filtering and grouping. These will be detailed elsewhere.

## Computed Data
Users should be able to:
- Create a new column that computes data from other columns using forumulas.
- Create "subtotals" for grouped views
	- Support different types of subtotals: SUM, AVG, MIN, MAX, MED

## Views
Users should be able to view, create, edit, and delete the following types of views:
- Table view with custom filtering, sorting, and grouping
- Calendar view based on data of date and time types
- Histogram chart view
- Pie chart view
- Line graph view
- Summary view based on computed subtotals

## Sharing
- Users should be able to share any view publicly

## User Management
Users should be able to:
- Log in and log out
- Change their password

## Data Workflow Improvements
Users should be able to:
- Search for data across various tables and schemas
- Bulk edit data
- Bulk import new data into an existing collection
- Export data in common formats (to be defined)

## User Documentation
Users should be able to:
- Follow provided instructions to install Mathesar on a server
- Point Mathesar at an existing database or set up a new one
- Install Mathesar on different operating systems and environments
- Get help on how to use Mathesr

## API
Users should be able to:
- Create, update, or delete an API token
- Consult comprehensive API documentation

Users should not be able to use the API without a token.

# Future Features
> Please see [Feature Ideas](/feature-ideas) for a long and disorganized list of feature ideas that we're drawing from to create this roadmap.
{.is-info}
