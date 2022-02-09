---
title: Support for PostGIS Data Types
description: 
published: true
date: 2022-02-09T20:54:29.287Z
tags: 
editor: markdown
dateCreated: 2022-02-09T20:54:12.599Z
---

## The Problem
Mathesar currently only allows the user to use a small set of data types. We'd like to expand the data types we offer in our product to include the spatial data types provided by [PostGIS](http://postgis.net/).

## Classification
- **Difficulty**: Medium
- **Skills needed**: Python, PostgreSQL, PostGIS
  - **Bonus skills**: JavaScript, frontend frameworks
- **Length**: Long (~350 hours)

## Tasks
- Work with the Mathesar design team to figure out how end users can interact with PostGIS data types in the UI, including:
  - How data is displayed
  - How data is entered
  - What [Mathesar Types](/en/engineering/architecture/mathesar-types) to show
  - What filtering options to support for each type
  - What grouping options to support for each type
  - What display options to support for each type
- Implement support for these features in the backend `db` module and REST API.
- Optionally, implement the frontend portion of these features as well.

## Expected Outcome
By the end of this project, we expect that if a user has PostGIS installed, they will be able to have a seamless experience of using PostGIS types within the Mathesar backend and API.

If the candidate is interested, it would be great to also have the types integrated into the Mathesar UI.

## Application Tips
- It's helpful to start from the experience that you'd like the end-user to have and work backwards. Think through the use cases for each data type.
- Backend and database experience is critical for this project, so please emphasize your previous work there.

## Resources
- Data Types in Mathesar:
  - [Data Types "Concepts" page](/en/product/concepts/data-types)
  - [Mathesar UI Data Types engineering page](/en/engineering/architecture/mathesar-types)
- [Existing Data Type components design spec](/en/design/specs/global-data-type-components), to see how current data types work.
- Filters in Mathesar:
  - [Filters "Concepts" page](/en/product/concepts/filters)
  - [Filters engineering page](/en/engineering/architecture/filters)
- PostGIS resources:
  - [PostGIS website](http://postgis.net/)
  - [PostGIS Data Types reference](https://postgis.net/docs/reference.html#PostGIS_Types)

## Mentors
**Primary Mentor**: Kriti
**Secondary Mentor(s)**: TBD