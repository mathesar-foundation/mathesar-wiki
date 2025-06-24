# Better Support for Default PostgreSQL Data Types

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
  - What [Mathesar Types](/engineering/glossary/ui-types) to show
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
  - [Data Types "Concepts" page](/archive/product/concepts/data-types)
  - [Mathesar UI Data Types engineering page](/engineering/glossary/ui-types)
- [Existing Data Type components design spec](/archive/product/design/specs/global-data-type-components), to see how current data types work.
- Filters in Mathesar:
  - [Filters "Concepts" page](/archive/product/concepts/filters)
  - [Filters engineering page](/engineering/glossary/filters)
- [PostgreSQL types documentation](https://www.postgresql.org/docs/current/datatype.html)


## Mentors
- **Primary Mentor**: Kriti Godey
- **Backup Mentor**: Dominykas Mostauskis 

See our [Team Members](/team/) page for Matrix and GitHub handles of mentors.