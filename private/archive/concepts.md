---
title: Concepts
description: Early notes on product concepts for Mathesar
published: true
date: 2021-04-20T20:49:23.126Z
tags: 
editor: markdown
dateCreated: 2021-04-20T20:44:01.795Z
---

> This page is in the **Archive** because it's out of date.
{.is-warning}

These are concepts that are relevant to the product. In general, these are user-facing concepts (with a few exceptions). This is not intended to be a spec of the necessary technical/implementation concepts.

# Application
The base unit for the simple database is an _application_. Each application is equivalent to a database ("Base" in Airtable parlance). 

## Attributes
- **Name**
- **Order**: Determines the display order on UI
- **Sharing Option**:
	- Public
	- Team(s)
	- Organization
	- Private
	
# Record

A _record_ is a struct (or ordered dict, or named tuple) of data belonging to an application. Typed.

_internal thought_: should the user care about "struct"?

## Attributes
- **Type**: a key-value map from keys to types (instances of _column types_ (see below)) of the values. So,
`{"column_type1": 1, "column_type2": "a", "column_type3": {"alice": "bob"}}`  might have the type `Record(column_type1: int, column_type2: str, column_type3: struct(alice: str))`. Note that we descend into the inner struct.

# Column Type
_Column Types_ are classes, instances of which can represent a data type in a record. I.e., a type for a _value_ in one of the key-value pairs of that record. If the value of a record passes the validation function (see below) of a column type, we say that record _satisfies_ that column type. There are many different types of column type, but all column types have the following attributes:

## Attributes
- **Validation**: A function that validates input into the column type. Some default validators can be provided:
	- **Allow Blank Values**: Whether the column type can be left blank
	- **Choices**: A set of values that the data in the column type must be limited to.
	- **Types**: A set of allowed primitive data types for the column type (int, str, etc.).

Each column type also has set of options that it can be grouped by (given a set of data fulfilling a given column type), documented under each column type below as **Group By Options**.

You use a specific type of column type rather than Column Type directly. Types of column types are documented below.

## Primary Key Column Type
This column type is an incrementing integer which identifies the record and is not exposed to the user.

## Row Number Column Type
This column type is an incrementing-ish integer which identifies the record from the user's perspective, but is mutable (i.e., the user could move a record from row _x_ to row _y_).

## Text Column Type
**Attributes**:
	- Formatting *(Markdown, HTML, plaintext)*
**Group By Options**: First letter

## Email Column Type
**Group By Options**: First letter, domain

## URL Column Type (Web Link)
**Group By Options**: First letter, domain TLD, Protocol

## IP Address Column Type
- **Attributes**:
	- Protocol *(IPv4 or IPv6)*
- **Group By Options**: Protocol, Block

## Phone Number Column Type
- **Group By Options**: Country Code, Area Code

## Number Column Type
- **Group By Options**: Range (options calculated intelligently based on data stored)

Number column types can have the sub-types, which support the above group by options:

### Money Column Type
- **Attributes**:
	- Currency
- **Group By Options**: Currency, Range (same as Number Column Type)

### Percentage Column Type
_No special attributes, for UI only._

## Location Column Type
The attributes of the location column type are based on results returned by the [Google Maps Geocoding API](https://developers.google.com/maps/documentation/geocoding/overview), since they've done the work of putting addresses into a global format.

- **Attributes**:
	- Street Address
	- Country
	- Administrative Area Level 1 *(in the US, these are states)*
	- Administrative Area Level 2 *(in the US, these are counties)*
	- Administrative Area Level 3
	- Administrative Area Level 4
	- Administrative Area Level 5 
	- Locality *(city/town)*
	- Sublocality *(subdivision of city/town)*
	- Neighborhood
	- Postal Code
	- Latitude
	- Longitude
- **Group By Options**: Any of the attributes above except lat/lng, lat/lng to some level of precision, radius around specific lat/lng

## Date Column Type
- **Group By Options**: Day, Week, Month, Quarter, Year

## Time Column Type
- **Group By Options**: Minute, Hour

## Date Time Column Type
- **Group By Options**: Minute, Hour, Day, Week, Month, Quarter, Year

## Duration Column Type
- **Group By Options**: Range (options calculated intelligently based on data stored)

## Boolean Column Type (Checkbox)
- **Group By Options**: Yes/No

## JSON Column Type
Store arbitrary JSON.

- **Group By Options**: Values of common keys, intelligently calculated.

## Struct Column Type
Store JSON, but restricted to have the same format for each key-value entry in the column.

## Linked Column Type
This is a link to data stored elsewhere.

- **Attributes**:
	- Type:
		- Column Type in another record
		- User (this would be a user of the system)
	- Allow Multiple Links *(Yes/No)*

## File Column Type
Store uploaded files in supported formats here.

- **Attributes**:
	- Type:
		- Image
		- PDF
		- 3D Model
		- ???

# Column
Given a set of records, a _column_ is a set of key-value pairs, one from each record, along with a set of global constraints on those records. Under the hood, this will almost always be the equivalent of a database column.

## Attributes
- **Name**: A name for the column. Each key in the key-value pairs of the column must be equal to the name of the column.
- **Column Type Set**:  An array of column types such that every value in the column must satisfy the one of the column types in the set (or rather its validation function)
- **Data**: The key-value pairs in the column.
- **Default Value**: Default value for the values in the column if the user does not specify a value
- **Unique**: Whether data in each key-value pair of this column needs to be unique
	
# Collection
A _collection_ is a set of records, and a set of _columns_ associated with those records. Each collection belongs to a single application. Applications can have multiple collections. Orderings can be imposed on collections, and there may be some default ordering for a given collection. An ordered collection of records of the same type could be represented in a tabular form to the user. By extending the column array so that at least one column has an appropriate name and constraints for each key-value pair contained in the union of all records in the collection, the entirety can be represented in tabular form (indeed this may be the default internal representation in most cases).

## Attributes
- **Name**
- **Column Array**
- **Record Set*

# View
Views are a particular visual representation of the data in an Application. The data could come from a collection in that Application, or multiple collections. All views allow filters to be applied and the filters used are saved along with the view. Some views are discussed in more depth in the [features](features.md) document.

Views can be in many forms, see below:

## Grid View
Grid views take the traditional tabular form. Grid views can have custom:
- Columns displayed
- Sort applied
- Aggregation applied

## Summary View
Summary views show only summaries of grouped data.

Here is an example from Dabble DB:
![summary_view.png](/assets/summary_view.png)

## Map View
Shows a map based on a Location Column Type.

## Calendar View
Shows a calendar based on date & time data.

## Form View
Allows users to enter a new record. Meant to be shared with external users who do not have access to the Application.

## Bulk Form View
Allows users to enter several records in a convenient way. Meant to be shared with external users who do not have access to the Application.

## Card / Gallery View
Shows data as cards or galleries. They can have custom:
- Columns displayed
- Sort applied

## Kanban View
Shows data as cards in specific columns based on a column type in the collection. They can have custom:
- Columns displayed
- Sort applied

## Aggregation/Chart View
Shows typical charts that spreadsheet users may want:
- Histograms
- Pie Charts
- Scatter Plots
- Line Graphs

## Data Modeling View
Shows an abstract overview of the collections in an application, how different column types relate, and any dependencies. This could also be a UI for proposing data model improvements to the user. Possible types of these views are:
- [Entity–relationship diagrams](https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model#/media/File:ER_Diagram_MMORPG.png)
- [IDEF1X diagrams](https://en.wikipedia.org/wiki/IDEF1X#/media/File:B_5_1_IDEF1X_Diagram.jpg)

# Template
A template is a type of Application with pre-configured Collections, Columns, Column Types, and Views. It can be used to start a new Application instead of starting from scratch. It can also be shared with other users for their own applications.

# Users and Permissions
The permission model outlined here is based on GitHub. Individual users have accounts, and can create and administer organizations and teams within those organizations.

## User
A user is a person with an account that uses the software. Users have the following attributes:
- **Name**
- **Email**
- **URL Namespace**: This is where the user's applications are hosted.
- **Organization**: The organization to whom the user belongs, optional.

## Team
A team is a set of users. Teams have the following attributes:
- **Name**
- **Organization**: The organization to whom the team belongs, mandatory.
- **URL Namespace**: This is where the team's applications are hosted.
- **Users**: The list of users in the team. Users can have one of three roles:
	- **Owner**: Can delete applications, invite new users to the team, delete users, in addition to other permissions
	- **Editor**: Can add new applications, edit existing applications.
	- **Viewer**: Can view applications

Teams are not necessary to use the software, they are an organizational tool to simplify collaboration and permissions.

## Organization
An organization is analogous to a company or institution. Organizations have the following attributes:
- **Name**
- **URL Namespace**: This is where the team's applications are hosted.
- **Users**: The list of users in the team. Users can have one of three roles:
	- **Owner**: Can invite new members to the organization, remove members, add people to teams, delete people from teams, can delete applications.
	- **Member**: Can add new applications, edit existing applications.
		- Members can be Owners of a Team and will have more permissions on applications related to that team.

Organizations are not necessary to use the software, users can sign up individually.

# Event
An event is a type of change in the state of the project that can be used as a trigger to perform other actions. Events will be exposed via API.

Events supported are:
- Add, update, delete events for:
	- Application
	- Collection
	- Column
	- Record
	- User
	- Organization
	- Team
	- Template
	- View
