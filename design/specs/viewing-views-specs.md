---
title: Viewing a View
description: 
published: true
date: 2021-09-05T08:57:28.838Z
tags: 
editor: markdown
dateCreated: 2021-09-03T09:04:39.016Z
---

## Context

Views are a core part of Mathesar's value. It allows users to analyze data from their tables or other views. Users will want to know the data sources and how each column is defined when opening a view. For that purpose, views require an additional layer of information that helps users understand the definitions for the view and how they might modify it.

## Scenarios

### Operation 1: The user loads a View

#### Scenario 1: The view loads successfully

1. The user opens a view.
2. The view opens and shows the result of the view query in a table format.

#### Scenario 2: The view fails to load and displays an error message

1. The user opens a view.
2. The view fails to load.
3. An error message is displayed containing the error code and reason if available.

#### Scenario 3: The view fails to load and enters query mode

1. The user opens a view.
2. The view fails to load.
3. The view query is displayed along with an error summary and the error location.

### Operation 2: User inspects the data type of columns

#### Scenario 1: The data type is known

1. The user opens a view.
2. The view opens and shows the result of the view query in a table format.
3. The column headers display an icon representing the data type.

#### Scenario 2: The data type is unknown

1. The user opens a view.
2. The view opens and shows the result of the view query in a table format.
3. The column headers display the [unknown data type icon](#unknown-data-type-icon).

### Operation 3: User inspects the definition properties of a column

#### Scenario 1: The view column definition properties are available

1. The user opens a view.
2. The view opens and shows the result of the view query in a table format.
3. The user clicks on the `View Column Properties` button located in the toolbar.
4. The table goes into `Design Mode`.

#### Scenario 2: The view column definition properties are not available

1. The user opens a view.
2. The view opens and shows the result of the view query in a table format.
3. The `View Column Properties` button located in the toolbar is disabled.
4. The user hovers over the button, and a tooltip indicates that the view properties are not accessible.

### Operation 4: User inspects the view's query

#### Scenario 1: The query loads

1. The user opens a view.
2. The view opens and shows the result of the view query in a table format.
3. The user clicks on the `View Query` button located in the toolbar.
4. The table goes into `Query Mode`.

#### Scenario 2: The query fails to load

#### Scenario 3: The query is not available due to lack of permission

### Operation 5: User filters, sorts or groups a view

#### Scenario 1: The view had active filters, sorts or groups saves

#### Scenario 2: The view had no active filters, sorts, or groups saved

## User Interface

### Unknown Data Type Icon

Icons for data types

## Components

### Edit and Query Modes
