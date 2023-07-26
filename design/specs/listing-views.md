---
title: Listing Views Spec
description: 
published: true
date: 2023-07-19T23:21:30.901Z
tags: 
editor: markdown
dateCreated: 2021-09-17T08:28:58.527Z
---

## Context

Database objects are defined objects in a database that store or reference data. In the context of Mathesar, two of those objects are listed and available to users as `Tables` and `Views`. Together, these objects are at the core of Mathesar's user experience. A component of that experience is retrieving, listing, and identifying these objects and their types in different contexts.

## Prototype

### Link

[Prototype](https://mathesar-prototype.netlify.app/)

### Videos

- Scenario 1: [Video](https://www.loom.com/share/8d064b4c16244927b5135f2a5e4ebf36)
- Scenario 2: [Video](https://www.loom.com/share/c3b2f63a7f1e4f08bb805d46e713913a)
- Scenario 3: [Video](https://www.loom.com/share/e1437b383f0b4752b8478efb235a2973)
- Scenario 4: [Video](https://www.loom.com/share/dea6f03e20f64860a708d1b882a6f20a)

## User Experience

### Listing of Views and Searching by Name

With the introduction of `Views`, the user interface needs to be updated to easily display and identify all database objects and types of an object.

`Views`, like `Tables`, have names that allow users to identify them or search for them. Icons that represent each are also used to differentiate each.

Initially, users will only be able to search views by name. However, relying on a name alone might not be sufficient to ensure a good user experience when trying to find views created a long time ago or by other users. We will consider more sophisticated search functionality in the future.

## Scenarios

### Scenario 1: User browses through a list of all available views in a currently open schema

#### Scenario 1a: From the schema details view

- User opens a schema and sees the [schema details page](#schema-details-page).
- User sees a list of views [recently opened](#recently-opened) in Mathesar for the current schema.

#### Scenario 1b: From the schema explorer sidebar

- User opens a schema and sees the [schema explorer sidebar](#schema-explorer-sidebar).
- User sees a list of all tables and views for the current schema.
  - The list shows both object types by default but can be filtered to only show tables or views using the [sidebar tabs](#sidebar-tabs) at the top of the sidebar.

### Scenario 2: User encounters an error in loading a list of views for a currently open schema

#### Scenario 2a: From the schema details view

- User opens a schema and sees the [schema details page](#schema-details-page).
The list of objects for the schema fails to load.
- Under the schema name, an error message is displayed indicating that the loading of objects failed.
- The error notice contains details about the error and actions, if available, that the user can perform to correct the problem.

#### Scenario 2b: From the schema explorer sidebar

- User opens a schema and sees the [schema explorer sidebar](#schema-explorer-sidebar).
The list of objects for the schema fails to load.
- An error message is displayed indicating to the user that the loading of objects failed.
- The error notice contains details about the error and actions, if available, that the user can perform to correct the problem.

### Scenario 3: User encounters an error while opening a view in a currently open schema

#### Scenario 3a: From the schema explorer sidebar

- The user opens the schema explorer by navigating to it via the sidebar or by URL pointing to that object.
- The object fails to load, and the system displays an error notice.

#### Scenario 3b: From an open tab

- The user navigates to a tab, which represents a previously open view.
- The object fails to load, and the system displays an error notice.

### Scenario 4: User searches a view by name

#### Scenario 4a: From the schema explorer view's sidebar

- The user opens the schema explorer by navigating to it via the sidebar or by URL pointing to that object.
- The user enters a search term in the search input box located at the top of the sidebar list.
- The list is filtered to show objects whose name matches the search term.
- The list contains metadata associated with the objects like record and column count.
  - If no results are found, the system displays a notice to indicate the lack of results and potential causes.
- Users can clear the search by clearing the input box content or clicking on the `Clear Search` link displayed along with the results summary.

## Views

### Schema Details Page

The schema details page will be shown if a schema is open and there aren't any tables selected. It will contain the schema's name, the total number of tables and views, and additional sections that we can use to present the user with relevant information or links.
The detail page should also show a list of recently opened views or tables.

In the future additional content could be considered for this section, such as:

- Activity summary for recent events
- Getting started options for common actions

## Components

### Schema Explorer Sidebar

The schema explorer sidebar contains the entire list of objects for any schema available in Mathesar. The user can open any object from the sidebar by clicking on its navigation link. The sidebar also includes an input for searching through the listed objects.

### Sidebar Tabs

Sidebar tabs will allow users to filter the sidebar's contents to show only a particular object type. When set to ' All ', the content will include both tables and views. Setting the tabs to `Tables` will display only table objects, while `Views` will display only view objects.

## Other Considerations

### Regular vs. Materialized Views

Regular views need to be differentiated from materialized views as the use cases might differ. However, we don't want to create a rigid distinction between both as it could confuse users being introduced to the concept of views. For this purpose, an indicator, such as the letter 'M' should be added next to the view icon to show that it is of the type 'Materialized'.

### Recently Opened

The method to generate a list of recently opened objects is still under discussion. Ideas like using local storage to provide that information have been considered. The idea is to provide users with a quick way to access their more recently used tables or views or continue their work.
