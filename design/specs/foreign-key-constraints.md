---
title: Usage of Foreign Key Constraints
description: 
published: true
date: 2021-10-20T09:29:41.498Z
tags: 
editor: markdown
dateCreated: 2021-10-19T09:20:55.088Z
---

# Context
This design spec describes the proposed solution for the problem defined in the issue [Design for the usage of Foreign Key constraints](https://github.com/centerofci/mathesar/issues/243).

## Prototype Walkthrough
[Video](https://www.loom.com/share/65d596c2dbcd4225bc91c3ade7995c39)
[Prototype Link](https://mathesar-prototype.netlify.app/)

## Scenarios
A user has a table named 'artist' that contains records for artists in a music album collection. The user wants to link each artist to records in another table named 'track.' If successful, the user should be able to relate all tracks associated with an artist to each record in the 'artist' table.

### The user opens the 'track' table and adds a new column to link records from the 'artist' table
### The user opens the new column menu and selects the 'Link to Another Table' option
### The user selects a table from the list of available tables
### The user selects a column belonging to the selected table to create the link
### The user sets the new column as a foreign key for a column in the 'artist' table
### The user retrieves records from the linked table and adds them to the new column
### The user removes the foreign key constraint from the column