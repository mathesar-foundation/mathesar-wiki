---
title: Better Support for Default PostgreSQL Data Types
description: 
published: true
date: 2023-05-11T14:37:59.050Z
tags: 
editor: markdown
dateCreated: 2022-02-09T21:23:58.352Z
---

## The Problem
Mathesar currently only allows the user to use a small set of data types. We'd like to expand the data types we offer in our product to include [more default PostgreSQL types](https://www.postgresql.org/docs/current/datatype.html) such as Network Address types, Geometric Types, UUID Types, and Range Types. 

## Classification
- **Difficulty**: Medium
- **Skills needed**: Python, Django, PostgreSQL
  - **Bonus skills**: JavaScript, frontend frameworks
- **Length**: Long (~350 hours)

## Tasks
- Determine which types you'd like to work on.
- Work with the Mathesar design team to figure out how end users can interact with file and image data types in the UI, including:
  - How data is displayed
  - How data is entered
  - What [Mathesar Types](/en/engineering/glossary/ui-types) to show
  - What filtering options to support for each type
  - What grouping options to support for each type
  - What display options to support for each type
- Implement support for all frontend features in the backend `db` module and REST API.
- Optionally, implement the frontend portion of these features as well.

## Expected Outcome
By the end of this project, we expect that users will be able to seamlessly use any data types proposed (e.g. videos) within the Mathesar backend and API.

If the candidate is interested, it would be great to also have the types integrated into the Mathesar UI.

## Application Tips
- Please specify the types you'd like to implement.
- It's helpful to start from the experience that you'd like the end-user to have and work backwards. Think through the use cases for each data type.
- Backend and database experience is critical for this project, so please emphasize your previous work there.

## Resources
- Data Types in Mathesar:
  - [Data Types "Concepts" page](/en/product/concepts/data-types)
  - [Mathesar UI Data Types engineering page](/en/engineering/glossary/ui-types)
- [Existing Data Type components design spec](/en/design/specs/global-data-type-components), to see how current data types work.
- Filters in Mathesar:
  - [Filters "Concepts" page](/en/product/concepts/filters)
  - [Filters engineering page](/en/engineering/glossary/filters)
- [PostgreSQL types documentation](https://www.postgresql.org/docs/current/datatype.html)


## Mentors
- **Primary Mentor**: Kriti Godey
- **Backup Mentor**: Dominykas Mostauskis 

See our [Team Members](/en/team/members) page for Matrix and GitHub handles of mentors.