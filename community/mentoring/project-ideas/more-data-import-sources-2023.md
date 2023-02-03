---
title: Support importing Excel and JSON files
description: 
published: true
date: 2023-02-03T16:25:20.421Z
tags: 
editor: markdown
dateCreated: 2023-02-03T16:25:20.421Z
---

## Classification
- **Difficulty**: Medium
- **Skills needed**: Python, SQL
- **Skills that could be helpful**: Django, SQLAlchemy
- **Length**: Long (~350 hours)

## The Problem
- The Mathesar UI allows users to import data from CSV and TSV files.
- We'd like to support importing Excel and JSON files.

## Feature Description
- The existing import UI should support importing JSON and Excel files.
- Importing a file should create a single table, and we should allow the user to preview that table, remove/rename columns, change data types etc.
  - If the JSON or Excel files are not in a format where they can be easily imported as a single table, we should develop algorithms to convert the files into a suitable format.
  - If the algorithm doesn't work, we should refuse to import the files and provide the user with a readable error.
- Column data types should be guessed during the import process.
- We have APIs for importing data into existing tables. Ideally, those should also work with the two new file types.

## Architectural Problems
JSON and Excel files are more complex than CSV/TSV files. The primary architectural challenges for this project are:
- Figuring out a good algorithm for importing a single JSON file into a single table.
- Figuring out a good algorithm for importing a single Excel file into a single table.
- Integrating the new file types into our our existing import process while preserving all our functionality.

## Tasks
1. Determine what kinds of JSON files can and cannot be imported easily into a single table.
1. Determine if other types of JSON files can be easily converted into a format that works.
1. Implement importing JSON files and integrate with current import APIs and UI.

Repeat for Excel files.

## Expected Outcome
Users should be able to upload JSON and Excel files in the current import UI seamlessly. If the file is structured so that it cannot be imported, they should see a clear error message explaining why.

As a stretch goal, our APIs for importing data into existing tables should also support JSON and Excel files.

## Application Tips
- Demonstrate proficiency with the required skills.
- Demonstrate your understanding of Mathesar's current import code and how it will need to be extended to support these features.

## Resources
- [Tutorial on using Postgres COPY to import JSON files](https://konbert.com/blog/import-json-into-postgres-using-copy)
- [Tutorial on using Pandas to read messy Excel files](https://pbpython.com/pandas-excel-range.html): *this is provided as an example of how messy Excel files can be, not as an implementation suggestion.*

## Mentors
**Primary Mentor**: Dom
**Secondary Mentor(s)**: Anish
