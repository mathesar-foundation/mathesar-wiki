---
title: Support Data Export
description: 
published: true
date: 2023-07-19T23:42:27.684Z
tags: 
editor: markdown
dateCreated: 2022-02-18T00:03:46.048Z
---

## The Problem
Currently, Mathesar does not have any functionality that allows users to export data. We'd like to allow users to export data from tables or views. We should support exporting to the following formats
- CSV/TSV files
- SQL files
- Excel files
- Google Sheets
- Airtable
- JSON files

## Classification
- **Difficulty**: Medium
- **Skills needed**: Python, Django, PostgreSQL
  - **Bonus skills**: JavaScript, frontend frameworks
- **Length**: Medium (~175 hours)

## Tasks
- Work with the Mathesar design team to figure out a design for how to integrate this functionality into the product.
  - This includes what kinds of data we want to export. Do we want to support exporting tables, views, and/or entire schemas? Should we take currently applied filters and sorts into consideration?
- Write a technical spec for how this functionality will fit into the current Mathesar code.
- Implement the backend necessary to make the feature work, including both the import process in the database and APIs for the frontend to interact with.
- Optionally, implement the frontend changes needed for the feature as well.

## Expected Outcome
By the end of this project, we expect that the backend code and APIs will support exporting data to one or more of the file formats listed above.

Also, we expect that exporting will transfer as much information as is supported by the target format, which might include column names, column types and table names (and possibly other bits of information).

If the candidate is interested in working on the frontend, we'd also love to see the frontend feature implemented.

## Application Tips
- Please provide as much technical detail as you can on how this will integrate into Mathesar's code. API schemas, libraries you plan to use, etc.
	- Mathesar is a self-hosted product. You'll need to think through any requirements that the administrator of a Mathesar instance will need to perform (e.g. if you plan on exporting being an asynchronous process, then the administrator will need to install a task queue and a task cache)
- Don't reinvent the wheel - use external libraries for the functionality where you can.
- It's helpful to start from the experience that you'd like the end-user to have and work backwards.

## Resources
- This is an entirely new feature so there are no existing resources.

## Mentors
- **Primary Mentor**: Mukesh Murali
- **Backup Mentor**: Dominykas Mostauskis

See our [Team Members](/en/team/members) page for Matrix and GitHub handles of mentors.