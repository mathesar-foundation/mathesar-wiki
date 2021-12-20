---
title: Listing Views Spec
description: 
published: true
date: 2021-12-20T09:00:00.201Z
tags: 
editor: markdown
dateCreated: 2021-12-20T09:00:00.201Z
---

## Context

Database objects are defined objects in a database that store or reference data. In the context of Mathesar, two of those objects are listed and accessible to users as `Tables` and `Views`. Together, these objects are at the core of Mathesar's user experience. One part of that experience is finding and opening these objects and differentiating both.

## Prototype

### Link

[Prototype](https://mathesar-prototype.netlify.app/)

### Videos

- Scenario 1:
- Scenario 2:
- Scenario 3:

## User Experience

### Listing of Views and Searching by Name

With the introduction of `Views`, the user interface needs to be updated to retrieve and identify all objects easily. `Views` in the same manner as `Tables`, have names that allow users to identify them or search them.

Initially, users will only be able to search views by name. However, if a user hasn't encountered a particular object very often, relying on a name alone might not be sufficient to ensure a good user experience.

## Scenarios

### Scenario 1: User browses through a list of all available views in a currently open schema

#### Scenario 1a: From the schema details view

- User navigates to the schema details page by navigating directly to a URL that points to this page or by clicking on the schema link at the top navigation bar.
- User sees a list of all tables and views for the current schema.
  - By default, the list is sorted by the last accessed object.
- Above a certain number of objects, the list will be divided into pages. The user will then have to navigate the pages to access the entire list.

#### Scenario 1b: From the schema explorer view's sidebar

- User navigates to the schema explorer view by opening any object in the details page or navigating to an object URL.
- User sees a list of all tables and views for the current schema.
  - The list shows both object types by default, but can be filtered to only show tables or views using the filter bar at the top of the sidebar.

### Scenario 2: User encounters an error in loading a list of views for a currently open schema

#### Scenario 2a: From the schema details view

### Scenario 3: User encounters an error in opening a view for a currently open schema

#### Scenario 3a: From the schema explorer view's sidebar

#### Scenario 3b: From an open tab

### Scenario 4: User searches a view by name

#### Scenario 4a: From the schema details view

#### Scenario 4b: From the schema explorer view's sidebar

## Components

## Other Considerations

### Navigation Structure

- Database, schema, tables, and views.
