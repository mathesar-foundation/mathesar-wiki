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

- Scenario 1: [Video](https://www.loom.com/share/179070149f00419e9125bd8fba675aa4)
- Scenario 2: [Video](https://www.loom.com/share/e32500bc744246e5b926852231577fd7)
- Scenario 3: [Video](https://www.loom.com/share/d553e7edbb28481b8aed02b055270154)
- Scenario 4: [Video](https://www.loom.com/share/91a20c4770ef4439860425a1bcd84db6)

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
  - The list shows both object types by default but can be filtered to only show tables or views using the filter bar at the top of the sidebar.

### Scenario 2: User encounters an error in loading a list of views for a currently open schema

#### Scenario 2a: From the schema details view

- User opens the schema details page for an existing schema
The list of objects for the schema fails to load, and the system displays an error notification.
- The error notice contains details about the error and actions, if available, that the user can perform to correct the problem.

### Scenario 3: User encounters an error while opening a view in a currently open schema

#### Scenario 3a: From the schema explorer view's sidebar

- The user opens the schema explorer by navigating to it via the sidebar or by URL pointing to that object.
- The object fails to load, and the system displays an error notice.

#### Scenario 3b: From an open tab

- The user navigates to a tab, which represents a previously open view.
- The object fails to load, and the system displays an error notice.

### Scenario 4: User searches a view by name

#### Scenario 4a: From the schema details view

- User navigates to the schema details page by navigating directly to a URL that points to this page or by clicking on the schema link at the top navigation bar.
- The user enters a search term in the search input box located at the top of the list.
- The list is filtered to show objects whose name matches the search term.
  - If no results are found, the system displays a notice to indicate the lack of results and potential causes.
- Users can clear the search by clearing the input box content or clicking on the `Clear Search` link displayed along with the results summary.

#### Scenario 4b: From the schema explorer view's sidebar

- The user opens the schema explorer by navigating to it via the sidebar or by URL pointing to that object.
- The user enters a search term in the search input box located at the top of the sidebar list.
- The list is filtered to show objects whose name matches the search term.
  - If no results are found, the system displays a notice to indicate the lack of results and potential causes.
- Users can clear the search by clearing the input box content or clicking on the `Clear Search` link displayed along with the results summary.

## Components

### Sidebar Filters

Sidebar filters will allow users to filter the sidebar's contents to show only a particular type of object. The content will include both tables and views when set to' All'. Setting the filter to `Table` will display only table objects, while `View` will display only view objects.

### Sidebar Sort Control

The sidebar sort control will allow users to select the sorting criteria for the objects displayed in the sidebar.

## Other Considerations

### Navigation Structure

Users of Mathesar will be able to connect multiple databases containing multiple schemas and navigate between them. This prototype assumes there's a single schema and database. For that reason, the interface presented is limited in functionality.
