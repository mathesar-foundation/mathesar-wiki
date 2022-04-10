---
title: Support More Data Import Sources
description: 
published: true
date: 2022-02-17T23:58:38.190Z
tags: 
editor: markdown
dateCreated: 2022-02-09T22:07:34.086Z
---

## The Problem
Currently, Mathesar only supports importing data from CSV-like files. We'd like to expand the types of data we can import, including support for:
- SQL files
- Excel files
- Google Sheets
- Airtable
- JSON files

## Classification
- **Difficulty**: Medium
- **Skills needed**: Python, Django, PostgreSQL
  - **Bonus skills**: JavaScript, frontend frameworks
- **Length**: Long (~350 hours)

## Tasks
- Work with the Mathesar design team to figure out a design for how to integrate this functionality into the product.
- Write a technical spec for how this functionality will fit into the current Mathesar code.
- Implement the backend necessary to make the feature work, including both the import process in the database and APIs for the frontend to interact with.
- Optionally, implement the frontend changes needed for the feature as well.

## Expected Outcome
By the end of this project, we expect that the backend code and APIs will support importing data from one or more of the data sources listed above.

If the candidate is interested in working on the frontend, we'd also love to see the frontend feature implemented.

## Application Tips
- Please provide as much technical detail as you can on how this will integrate into Mathesar's code. API schemas, libraries you plan to use, etc.
	- Mathesar is a self-hosted product. You'll need to think through any requirements that the administrator of a Mathesar instance will need to perform (e.g. if you plan to use an external API, will the administrator need a developer key for that API?) 
- Don't reinvent the wheel - use external libraries for the functionality where you can.
- It's helpful to start from the experience that you'd like the end-user to have and work backwards.

## Resources
- [Import Preview API technical spec](/en/engineering/specs/import-preview-api)

## Mentors
- **Primary Mentor**: Mukesh Murali
- **Backup Mentor**: Kriti Godey

See our [Team Members](/en/team/members) page for Matrix and GitHub handles of mentors.