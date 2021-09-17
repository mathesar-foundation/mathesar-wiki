---
title: Listing and Searching Views
description: 
published: true
date: 2021-09-17T08:29:11.810Z
tags: 
editor: markdown
dateCreated: 2021-09-17T08:28:58.527Z
---

# Context
When using Mathesar, users should rely on views for most analysis tasks and tables for more structural tasks like modeling and data transformation. However, both objects are similar and share some functionality. A clear distinction needs to be made between tables and views. Views should also take a more prominent space, and users in a table context should understand that saving as a view will allow them to choose a subset of columns or combine with other tables. 

# Prototype
[Prototype for Listing and Finding Views](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?page-id=5343%3A76906&node-id=5343%3A76907&viewport=338%2C48%2C0.72&scaling=contain&starting-point-node-id=5343%3A76907)

# User Experience
## Scenarios

### User sees a list of all views and can filter or sort the list items
A user can see a list of all views for a schema in the sidebar area. They can filter the list using the search input or sort them by alphabetical order or last modified. Last modified is the default sorting for the list of views.

### User sees a default view when they open a schema
A view can be set as the default that a user will see when they open a schema. Users can set the default view from the 'View Options' menu in a view.

### User can see a list of views referencing a table
A user from a table can access a list of views referencing that table. This menu also contains a brief description of how users should use views. 