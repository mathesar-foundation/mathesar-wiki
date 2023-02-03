---
title: Single Select data type
description: 
published: true
date: 2023-02-03T21:59:17.917Z
tags: 
editor: markdown
dateCreated: 2023-02-03T16:50:06.632Z
---

> Draft
{.is-warning}

## Classification
- **Difficulty**: High
- **Skills needed**: Python, JavaScript, Svelte
- **Skills that could be helpful**: Django, SQLAlchemy, TypeScript
- **Length**: Long (~350 hours)

## The Problem
Currently, Mathesar users have no way to restrict values in a column to a pre-defined set of values. We would like to offer users a way to create a "single select" field.

## Feature Description
The Mathesar UI has the concept of links between tables. Links create a new column with a foreign key constraint. This column show a summary of the linked record, and adding or editing data involves selecting or creating a record from another table via the "record selector".

"Single select" fields should be a configuration of a column with a foreign key constraint. When a foreign key column is designated as a "single select field", the following behavior should change:

### Showing and editing "single select" data
- Editing data in the following places should use a dropdown instead of the record selector:
	- A table cell
  - An input field on a record page
  - An input to set a default value for a column
  - An input for a filter condition
  - An input to filter records within the record selector
- Each choice (i.e. linked record) should be associated with a different color and displayed in that color
  - The colors should be able to be turned off.
- Users should not be able to add new choices from the dropdown, they can only choose from existing choices.

### Table inspector
- The column should show that it's a single select field in the table inspector
- Columns should be able to be switched between "normal" FK mode and "single select" mode.
- There should be a link to the table that stores the "choices" for this field so the user can edit choices.

### Tables with choices
- Tables that linked to a single select field should display differently in the UI
- There should be a place to set and change each record's associated color if colored choices are turned on.

### Creating single select fields
- Users should be able to find the "single select" option easily when creating a column
- Users should be able to find the "single select" option easily when creating a new link

## UX Design Problems
- What new options will the table inspector need? 
- How do we choose colors for each choice?
- How do we distinguish tables that are being used for choices in the UI?
	- Should we distinguish them when they are in a list or only on the table page?
- How can users easily find this option both when they're creating a new column and a new link?

## Tasks
1. Write a UX design document describing the manner in which the single select field will be incorporated into Mathesar's UI. Then work with the front end team and product designer to solidify the UX design.
1. Write an API spec to 
    1. store and retrieve information about whether a column is a regular FK or a single select field.
    2. store color information for linked records
1. Get feedback from the back end team to solidify the API behavior.
1. Implement the backend API changes.
1. Show single select fields as dropdowns in the UI instead of using the record selector.
1. Implement colors for each record.
1. Implement table inspctor changes.
1. Implement design for showing tables that store choices differently in the UI.
1. Implement features to help users find single select fields more easily.

## Expected Outcome
Users should be able to use single select fields as described in "Feature Description"

## Resources
Other tools like Airtable, Baserow, and NocoDB have single select fields. Please explore their UX.

## Mentors
**Primary Mentor**: Pavish
**Secondary Mentor(s)**: TBD
