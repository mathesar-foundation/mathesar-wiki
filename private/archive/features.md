---
title: Features
description: Early notes on product features for Mathesar
published: true
date: 2021-04-20T20:47:41.018Z
tags: 
editor: markdown
dateCreated: 2021-04-20T20:47:41.018Z
---

> This page is in the **Archive** because it's out of date.
{.is-warning}

Features that the product could support. This is a long list and the project does not need to support all of these features in the MVP; the roadmap for the MVP will be detailed later and linked here when ready.

Please read the [Concepts](./concepts) section first to understand the terms mentioned in this document.

# Applications
Users should be able to:
- Create a new application 
- Edit an application's attributes
	- This includes changing how applications are shared
- Delete an application
- Archive unused applications so they're no longer visible by default
- Reorder applications in their UI
	- Sort applications automatically by:
		- Last updated
		- Created
		- Alphabetical
- Search data across a given application
- Save an Application as a Template

## Application Creation
- Applications should be able to be created in the following ways:
	- New blank application
	- Clone template
	- Paste from table/spreadsheet
	- Import TSV
	- Import CSV
	- Import XML
	- Import JSON
	- Import from Google Sheets via API
	- Import from Microsoft 365 Excel via API
	- Import from Collabora/LibreOffice Online via API
	- PostgreSQL dump
- When an application is created by importing external _tabular_ data, the project should support:
	- Creation of a collection based on the imported data.
	- Automatic detection of column names and column type sets based on interpreting the first row of data as headers and the rest of the rows as data
		- The user should be able to override guessed column column type sets manually
		- The user can opt to use the first row as data instead of headers
			- In this case, they will need to manually give each column a name
- When an application is created by importing external _non-tabular_ (JSON, XML) data, the project should support:
	- Creation of a collection based on the imported data.
	- Automatic detection of types for each record.
	- Suggesting an appropriate set of columns and their column type sets (could be an intersection or union of named elements in individual records).
  - Automatically generating appropriate linked column types / collections in the case of nested data structures with enough consistency.

## Application Views
Users should be able to:
- Switch between different views of a collection
- Create new views of all types
- Edit view attributes
- Delete views
- Save views
- Change sharing option for views
	- Public
	- Private
	- After filling form
	- Same permissions as parent Application
- Edit view parameters (filter, sort, aggregate, etc.) and "save as"
- Set a view as the default view for a collection
- Use natural language for filtering views
	- e.g. "next Thursday" for dates
- See and understand connections in their data (or proposed connections) using data modeling views
- Modify their data model using (internal) form views or data modeling views

# Collections
Users should be able to:
- Create a new collection in an application
- Edit a collection's attributes
- Delete a collection
- Reorder collections
  - Sort the set of collections automatically by:
	  - Last updated
    - Created
		- Alphabetical
- Search for data in a collection
- Comment on data in a collection
- Manipulate data in a collection _(see below)_.

## Data Manipulation
- Add new records to a collection, and modify the collection definition appropriately (and easily), if the record has a different type from others.
- Add records to collections in bulk, and modify the collection definition.
- Easily change the keys in records to make them consistent
- Easily reorder the keys in records (in bulk) to make them consistent
- Easily view / group by / modify the values in records of collections, including grouping by column types (for cleaning and consistency operations)
- Easily change the column types of records in collections to make them consistent.
- Define new collections in terms of the records in a given collection:
  - Filtering the given collection
  - Creating a record from each value associated with a given key in each record in the given collection, and collecting those into a collection.
- Specify a single column (or set of columns) of a collection and turn it into a new collection
  - This creates a new collection with the data and turns the column type corresponding in the existing collection into a Relationship column type
- Move records or columns from one collection into another collection
  - e.g. if there is a Deal collection and a Salesperson collection linked to it, then the user can easily move the "email" column type from the Deal collection to the Salesperson collection on the record linked from the salesperson Column Type in the Deal collection
  - Handle contradictory/messy data
  - In the above example, imagine that the same salesperson has multiple emails listed in different records.
    - Notify the user that there is a potential conflict, ask whether we should:
      - Create multiple records for the same salesperson, with each different email
      - Use one of the emails for all records
      - Do nothing and let the user correct the data manually
- Group data by a given Column smartly
  - examples:
    - group by quarters, or months if there's a date column type
    - group by location if there's an address column type
- Create new "computed" Columns in a collection
  - e.g. a sum of two columns, or multiplication of two columns
  - These should also be groupable just like manually managed Columns
- Create new column that uses a formula, similar to spreadsheets
  - e.g. AVG
- Add subtotals to groupings of numbers
  - SUM, AVG, MIN, MAX, MED
- Run SQL queries through the browser and see results.
- Work with views _(see above)_
- Generate appropriate collections (with appropriate column types) based on the JSON schema
- Find and merge similar column types (Name vs name, artist vs creator, etc.)
- Sort and order based on schema (essentially, easily sort by which column types are non-null for a record) to group similar records.

- Define grid views in terms of the records of a given collection
  - Make a grid view from the set of records with a consistent type.
  ```
  {"cat": "hat", "dog": "log"}
  {"cat": "mat", "dog": "bog"}
  {"frog": "smog"}
  ```
  would become
  ```
  | cat | dog |
  +-----+-----+
  | hat | log |
  +-----+-----+
  | mat | bog |
  +-----+-----+
  ```
  - Make a grid view from a subset of the entries in the record set with consistent type:
  ```
  {"cat": "hat", "dog": "log"}
  {"cat": "mat", "frog" "smog"}
  ```
  would become
  ```
  | cat |
  +-----+
  | hat | 
  +-----+
  | mat |
  +-----+
  ```
  - The grid view creation operations above should be possible in bulk (i.e., create multiple grid views in cases where there is more than one way to achieve consistency), and recursive (i.e., descend into struct values to create linked grid views when possible).

# Data analysis / inference
Users should be able to:
- Predict new records (or fill remaining column types with predictions) based on previously entered data.
- Find records that have likely mistakes (based on their probability of existence)
- Infer possible correlations between column types (with proposed relations)
- Help user find redundant data, or sets of columns which should be extracted to a separate collection.
- Determine probable changes in dependent variables given assumed changes in data:
  - How much will sales increase if I hire another salesperson? (Note: Salespeople generally have overlapping territory)
  - What will the increase in grocery bill be if I eat out 20% less? What will the total savings be (assuming eating out is more expensive than cooking in)?
  - What will be my total caloric intake be if I fast M,W,F, but do unrestricted eating other days? (Note that you'd probably eat more on non-fast days in this scenario)
- Generate anonymized/fake data similar to existing data to share publicly

# User Management
Users should be able to:
- Sign up
	- Using third party logins:
		- Google
		- Apple
		- Facebook
		- Twitter
- Log in
- Log out
- Reset their password
- Unlink third-party accounts
- Work with organizations
	- Create a new organization
	- Edit an organization's attributes
	- Delete an organization
	- Join an organization
	- Leave an organization
	- Invite people to organizations (based on permissions)
	- Remove people from organizations (based on permissions)
	- Manage teams within organizations
		- Create teams (based on permissions)
		- Delete teams (based on permissions)
		- Edit a team's attributes (based on permissions)
		- Invite users to teams (based on permissions)
		- Remove users from teams (based on permissions)
		- Join teams
		- Leave teams

# Templates
_Most Template functionality is covered under Application._

Users should be able to:
- Browse Templates and create an Application from one
- Search availble Templates

# Interoperability
The product should support interoperating with other data sources and services easily.

Users should be able to:
- Automatically sync data from competitors:
	- Airtable
	- Baserow
- Connect events to:
	- Zapier
	- IFTTT
- Automatically sync data from where it's generated through:
	- Airbyte
	- Segment
- Export data in the following formats:
	- SQL
	- CSV
	- TSV
	- XML
	- JSON
	- Excel
  - PostgreSQL dump (or whatever backend)
- Clean data in OpenRefine

# User Friendliness
This is a special area of interest for us.

Users should be able to:
- Get suggested visualizations based on the type of data they have.
	- examples:
		- suggest a calendar view if they have a date column type
		- suggest a map view if they have a location column type
- Get suggested aggregations based on the type of data they have.
	- examples:
		- suggest location based aggregation if they have a location column type
		- suggest quarter/year/month based aggregation if they have a date column type
- Get suggested schema improvements based on their data
	- examples:
		- if all data a particular Column consists of only a few strings, offer to make it a separate collection
		- if two or more Columns in a collection have data that's almost perfectly correlated with each other, offer to move all those columns into a new collection
- Generate multiple proposed schema(ta?) based on unstructured (JSON, XML) data, and choose one that best represents their intent.
  - Get help fitting data into that schema if any inconsistencies arise.
- Add data over time, and get help with fitting it to the existing data model, or modifying the existing data model to be consistent with new data.
- Automate any processing/schema changes, and export a description of the processing for replication.
- Undo and redo all data manipulations since import (maybe with an undo tree)
  - The undo/redo tree should be exportable, modifiable, and runnable. That is, one should be able to recreate someone's data model and current data set using an exported set of manipulations, or take a different route based on the beginning portion of the manipulations.
- Get notifications for triggers of their choice through:
	- Email
	- Web
  
# Collaboration
Users should be able to work with others on their data and data modeling. 
- It should be possible (perhaps even default) to "publish" an application for public consumption, including the history of modeling and data manipulation changes.
- It should be possible to invite others to collaborate on an application.
- It should be possible to "fork" someone's application and work with it in one's own account (even starting from some previous state).

# Streaming/Updating
- It should be possible, once an application has been created, to hook it up to data sources (e.g., 3rd party APIs), ingest new data, and have the data automatically flow to the correct collections in the correct format.
- It should be easy to handle the case when data so ingested fails to import for some reason (for example, by appropriately updating the data model).

# Monetization
Users on the hosted service should be able to:
- See pricing options
- Use a paid plan for their personal user
	- Sign up for a paid plan
	- Cancel a paid plan
	- Switch to a different paid plan
- Use a paid plan for their organization
	- Sign up for a paid plan
	- Cancel a paid plan
	- Switch to a different paid plan
