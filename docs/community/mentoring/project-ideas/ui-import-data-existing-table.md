---
title: UI for Importing data into existing table
description: 
published: true
date: 2023-05-11T14:45:08.408Z
tags: 
editor: markdown
dateCreated: 2023-02-06T00:49:25.264Z
---

## Classification
- **Difficulty**: Medium
- **Skills needed**: HTML, CSS, JavaScript, Svelte
- **Skills that could be helpful**: TypeScript, UX design
- **Length**: Medium (~175 hours) or Long (~350 hours) depending on experience level

## The Problem
* Mathesar currently allows users to import data into a new table through the UI by uploading CSV/TSV files, remote links, or copy/paste.
* However, there is no option to import data into an existing table.
* The backend work and APIs have already been implemented.
* The goal of this project is to implement the frontend.

## Feature Description
* Provide an option in the UI to import data into existing tables.
* Allow users to upload valid CSV/TSV files to append data to an existing table.
* Enable users to copy and paste data into existing tables.
* Provide a column mapping option to map the columns from the uploaded data to match the table columns.

## UX Design Problems
* Where do we place the option to import data into existing tables?
  - Would this be part of the existing import flow, or a different flow on the table page, or both?
* Should copy/paste have an additional flow compared to csv/tsv uploads?
  - Should we allow copy/pasting directly onto the table cell?
* How would we allow the user to map columns from uploaded data to the table columns?
* How would we represent errors?

## Tasks
* Familiarize yourself with the current import flow and the backend APIs.
* Come up with a UX design document outlining the step-by-step user actions.
* Work closely with the frontend team and our product designer to finalize the UX design.
* Write down architectural specifications and a task list based on the UX design. Create Github issues for them.
* Implement the frontend work needed.

## Expected Outcome
Users should be able to import data into existing tables as described in the "Feature Description" section.

## Application Tips
* Show proficiency in the required skills.
* Provide a preliminary UX design document.
* Demonstrate a good understanding of the Mathesar frontend codebase and required APIs.

## Resources
* [Backend work for Importing data into existing tables: GSoC 2022](https://wiki.mathesar.org/en/engineering/reports/gsoc-2022-importing-data-into-existing-tables)
* Explore other tools such as Airtable and NocoDB for their approach and UX for importing data into existing tables.

## Mentors
**Primary Mentor**: Pavish Kumar Ramani Gopal
**Secondary Mentor(s)**: Anish Umale