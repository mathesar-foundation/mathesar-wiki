---
title: Database Views
description: Support for read-only database views.
published: true
date: 2023-02-06T08:10:23.325Z
tags: gsoc
editor: markdown
dateCreated: 2023-02-06T05:41:26.115Z
---

## Classification
- **Difficulty**: Medium
- **Skills needed**: Python, JavaScript, SQLAlchemy, Svelte.js, PostgreSQL
- **Length**: Long (~350 hours)

## The Problem

If a user has [views](https://www.postgresql.org/docs/13/sql-createview.html) in their database before installing Mathesar, or if they create views through some other client, those views will not be reflected in Mathesar.

## Feature Description

Mathesar should support _read-only_ views. A user should be able to:
- Look at a view similarly to a table.
- Manipulate a view by sorting, filtering, and grouping on the view page (similarly to the table page)
- Explore the columns of a view in Data Explorer.

## UX Design Problems

- We need to figure out where/how to list views on the Schema page
- We need to determine which parts of the table page translate to a new "view page". For example,
  - Filtering works,
  - Grouping works, but
  - Opening the record details page from a view makes no sense.
- We need to determine how to integrate database views into the Data Explorer
  - It's likely this would look something like how a table looks in Data Explorer when it has no links to another table.
  
Overall, we expect a significant portion of this project to involve dealing with UX concerns before implementing.

## Tasks

- Add a `DBView` model.
- Add any related models needed (potentially `DBViewColumn`, for example)
- Set up at least the following _read-only_ endpoints in the API:
  - `/api/db/v0/views/`
  - `/api/db/v0/views/<id>/`
  - `/api/db/v0/views/<id>/rows/`
  - `/api/db/v0/views/<id>/columns/`
- Do front end work to create a view page similar to the current table page.
- Do front end work to add views as a selectable object in the Data Explorer.

## Expected Outcome

Views should be integrated into the UI of Mathesar by the end of the project. In particular, there should be:
- A View page
- A way to query a view in the Data Explorer
- Some list of views in the Schema Page

## Application Tips

- Demonstrate proficiency with the needed skills.
- Show that you understand the difficulty of this project, and have a grasp of the UX concerns involved.

## Out of Scope

- Editing data values in views.
- Editing the definition of a view.
- Showing deep information about a DB view, e.g., the data sources for columns.

## Resources

- https://www.postgresql.org/docs/13/sql-createview.html

## Mentors
**Primary Mentor**: Brent Moran
**Secondary Mentor(s)**: Rajat Vijay
