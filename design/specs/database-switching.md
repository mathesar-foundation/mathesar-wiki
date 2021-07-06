---
title: Multiple Database Switching
description: 
published: true
date: 2021-07-05T10:23:12.466Z
tags: 
editor: markdown
dateCreated: 2021-07-01T21:19:29.919Z
---

# Context
Users might have multiple databases, and they need to switch between them as necessary, in a seamless manner, without worrying about the current status of open tables or views.

# Prototype Link
[Multiple Database Switching](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?page-id=1207%3A0&node-id=1212%3A0&viewport=516%2C327%2C0.3535313010215759&scaling=scale-down-width)

# Scenarios

## Open Single Schema vs. Multiple Schemas
Having users create multiple related tables inside a schema, rather than having their related data split into different schemas, is desired for our intended use cases. It also reduces complexity, and it's easier to manage.
For this reason, a navigation component is proposed so that the system can open only one schema at a time.

## Errors Preventing Schema Changes to be Saved
If a table within the open schema has unsaved changes, a warning will inform the user and provide the options to discard them and leave or stay and fix them.

## Persist Tabs for Schemas
The status of tabs should be persistent when reopening a schema.

![](/assets/design/specs/database-switching/qMsmiZo.png =400x)

## Missing Default Database
When opening Mathesar, the default database is the one that was most recently open. If this database no longer exists, then Mathesar should show an error message and direct the user to open a different database or troubleshoot the connection.

# Interactions
## Indicating Tables with Errors
If a table contains errors, the interface should help identify those by adding a visual indicator to the corresponding tab.

![](/assets/design/specs/database-switching/mCwwg8S.png =400x)

## Showing Recent Objects
A list of recent objects is available to help users access their most frequently used objects, such as tables and views.

![](/assets/design/specs/database-switching/0vScHwP.png =240x)

# User Interface

## Database Navigation Menu
The database navigation menu provides a context for the various databases and schemas that users can access through Mathesar.
From this menu, the user can search through all databases and navigate to schemas.

![](/assets/design/specs/database-switching/JGIqCOi.png)

# Review Notes
## Database Names
Mathesar will use the database connection key to identify databases within Mathesar. If we want a human-readable name in the future, we will need a way to capture that preference.

## Recent Tables
Showing a list of the most recently updated tables can help users manage their work progress, and access recently created objects. As part of the implementation of this spec, we will store user-session information locally until we have the structure for user accounts in place.

## Loading of a Large Number of Tables
Some concerns exist about fully loading a list of tables that exceeds what can be managed without disrupting the users' experience in terms of performance. However, we don't think that our current use case will be affected by this. A task has been added to optimize the loading of tables after the MVP is released.

## Using Icons to Identify Databases
Using visual identifiers to differentiate between databases can help users quickly find and access their databases. As part of implementing this spec, we will add the necessary functionality to display and generate the database icons.