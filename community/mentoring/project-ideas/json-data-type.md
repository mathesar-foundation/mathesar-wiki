---
title: Support for JSON Data Type
description: 
published: true
date: 2022-02-18T00:12:28.125Z
tags: 
editor: markdown
dateCreated: 2022-02-09T21:20:20.298Z
---

## The Problem
Mathesar currently only allows the user to use a small set of data types. We'd like to expand the data types we offer in our product to include better support for [PostgreSQL JSON types](https://www.postgresql.org/docs/current/datatype-json.html).

## Classification
- **Difficulty**: Medium
- **Skills needed**: Python, Django, JavaScript, frontend frameworks
- **Length**: Long (~350 hours)

## Tasks
- Work with the Mathesar design team to figure out how end users can interact with the JSON data types in the UI, including:
  - How data is displayed
  - How data is entered
  - What [Mathesar Types](/en/engineering/architecture/mathesar-types) to show
  - What filtering options to support
  - What grouping options to support
  - What display options to support
- Implement support for all frontend features in the backend `db` module and REST API.
- Implement the frontend portion of these features as well.

## Expected Outcome
By the end of this project, we expect that users will be able to seamlessly use JSON data types within the Mathesar backend, API, and UI.

## Application Tips
- It's helpful to start from the experience that you'd like the end-user to have and work backwards. Think through the use cases for each data type.
  - For example, users to expand and minimize individual keys in the JSON object stored in the UI
- Frontend experience is critical for this project, so please emphasize your previous work there.

## Resources
- Data Types in Mathesar:
  - [Data Types "Concepts" page](/en/product/concepts/data-types)
  - [Mathesar UI Data Types engineering page](/en/engineering/architecture/mathesar-types)
- [Existing Data Type components design spec](/en/design/specs/global-data-type-components), to see how current data types work.
- Filters in Mathesar:
  - [Filters "Concepts" page](/en/product/concepts/filters)
  - [Filters engineering page](/en/engineering/architecture/filters)
- [PostgreSQL JSON types documentation](https://www.postgresql.org/docs/current/datatype-json.html)

## Mentors
- **Primary Mentor**: Brent Moran
- **Backup Mentor**: Mukesh Murali

See our [Team Members](/en/team/members) page for Matrix and GitHub handles of mentors.