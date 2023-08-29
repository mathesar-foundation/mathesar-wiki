# Support for JSON Data Type

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
  - What [Mathesar Types](/engineering/glossary/ui-types) to show
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
  - [Data Types "Concepts" page](/product/concepts/data-types)
  - [Mathesar UI Data Types engineering page](/engineering/glossary/ui-types)
- [Existing Data Type components design spec](/design/specs/global-data-type-components), to see how current data types work.
- Filters in Mathesar:
  - [Filters "Concepts" page](/product/concepts/filters)
  - [Filters engineering page](/engineering/glossary/filters)
- [PostgreSQL JSON types documentation](https://www.postgresql.org/docs/current/datatype-json.html)

## Mentors
- **Primary Mentor**: Brent Moran
- **Backup Mentor**: Mukesh Murali

See our [Team Members](/team/members) page for Matrix and GitHub handles of mentors.