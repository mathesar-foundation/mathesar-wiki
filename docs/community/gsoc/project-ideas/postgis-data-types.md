# Support for PostGIS Data Types

## The Problem
Mathesar currently only allows the user to use a small set of data types. We'd like to expand the data types we offer in our product to include the spatial data types provided by [PostGIS](http://postgis.net/).

## Classification
- **Difficulty**: Hard
- **Skills needed**: Python, PostgreSQL, PostGIS
  - **Bonus skills**: JavaScript, frontend frameworks
- **Length**: Long (~350 hours)

## Tasks
- Work with the Mathesar design team to figure out how end users can interact with PostGIS data types in the UI, including:
  - How data is displayed
  - How data is entered
  - What [Mathesar Types](/engineering/glossary/ui-types) to show
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
- You'll need to do considerable research into PostGIS for this project. Demonstrate that as much as you can in your application.

## Resources
- Data Types in Mathesar:
  - [Data Types "Concepts" page](/archive/product/concepts/data-types)
  - [Mathesar UI Data Types engineering page](/engineering/glossary/ui-types)
- [Existing Data Type components design spec](/archive/product/design/specs/global-data-type-components), to see how current data types work.
- Filters in Mathesar:
  - [Filters "Concepts" page](/archive/product/concepts/filters)
  - [Filters engineering page](/engineering/glossary/filters)
- PostGIS resources:
  - [PostGIS website](http://postgis.net/)
  - [PostGIS Data Types reference](https://postgis.net/docs/reference.html#PostGIS_Types)

## Mentors
- **Primary Mentor**: Kriti Godey
- **Backup Mentor**: Brent Moran

See our [Team Members](/team/) page for Matrix and GitHub handles of mentors.