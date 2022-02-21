---
title: 02. View Data
description: 
published: true
date: 2022-02-18T21:01:52.251Z
tags: 
editor: markdown
dateCreated: 2022-01-24T22:54:40.594Z
---

> This page is out of date.
{.is-danger}

Here's how to model views in our backend and API. Each heading represents an attribute of Views.

## Query
This is the SQL query that defines the view. This is **required**. 

Query attributes are defined [in a separate page](/product/specs/2022-01-views/03-modeling-view-query).

## Columns
Output columns of the View's Query, they will be shown in the UI.  At least one column is **required** for a view.

Column attributes are defined [in a separate page](/product/specs/2022-01-views/04-modeling-view-columns).

## Rows
These are the output rows of the View's Query. Rows are **not required**, Views can contain 0 rows.

## Filters
Views can have filters applied to the data in the View. This is similar to Table filters.

## Sorting
Views can have sorting applied to the data that's present in the View. This is similar to Table sorting.

## Groups
Groups are similar to table grouping, they sort and then visually group rows into sections.
