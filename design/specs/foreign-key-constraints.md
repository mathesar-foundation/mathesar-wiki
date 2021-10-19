---
title: Usage of Foreign Key Constraints
description: 
published: true
date: 2021-10-19T09:21:29.028Z
tags: 
editor: markdown
dateCreated: 2021-10-19T09:20:55.088Z
---

# Context
This design spec describes the proposed solution for the problem defined in the issue [Design for the usage of Foreign Key constraints](https://github.com/centerofci/mathesar/issues/243).

## Prototype Walkthrough
[Video]()
[Prototype Link](https://mathesar-prototype.netlify.app/)

## Scenarios
From a table named 'artist' that contains records for artists in a music album collection, a user wants to link records from a table named 'track.' If successful the user should be able to relate all tracks associated with an artist to each record in the 'artist' table.

### The user opens the 'track' table and adds a new column to link records from the 'artist' table
### The user opens the new column menu and selects the 'Link to Another Table' option
### The user selects a table from the list of available tables
### The user selects a column from the selected table to create the link
### The user validates their selection based on the options presented
### The user sets the new column as a foreign key for a column in the 'artist' table