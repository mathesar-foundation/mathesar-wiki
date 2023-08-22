# Support for File & Image Data Types

## The Problem
Mathesar currently only allows the user to use a small set of data types. We'd like to expand the data types we offer in our product to include custom data types for dealing with files, images, and potentially other file types.

## Classification
- **Difficulty**: High
- **Skills needed**: Python, PostgreSQL
  - **Bonus skills**: JavaScript, frontend frameworks
- **Length**: Long (~350 hours)

## Tasks
- Work with the Mathesar design team to figure out how end users can interact with file and image data types in the UI, including:
  - How data is displayed
  - How data is entered
  - What [Mathesar Types](/en/engineering/glossary/ui-types) to show
  - What filtering options to support for each type
  - What grouping options to support for each type
  - What display options to support for each type
- Implement custom PostgreSQL types in the `db` module (similar to existing email and URI types).
- Implement storage of files or images in the desired storage backends. Users should be able to configure different storage backends (such as the local disk, AWS S3, etc.)
- Implement support for all frontend features in the backend `db` module and REST API.
- Optionally, implement the frontend portion of these features as well.

## Expected Outcome
By the end of this project, we expect that users will be able to seamlessly use file, image, and any other data types proposed (e.g. videos) within the Mathesar backend and API.

If the candidate is interested, it would be great to also have the types integrated into the Mathesar UI.

## Application Tips
- It's helpful to start from the experience that you'd like the end-user to have and work backwards. Think through the use cases for each data type.
  - For example, a user might want to see previews of images or view PDFs in the browser.
- Backend and database experience is critical for this project, so please emphasize your previous work there.

## Resources
- Data Types in Mathesar:
  - [Data Types "Concepts" page](/en/product/concepts/data-types)
  - [Mathesar UI Data Types engineering page](/en/engineering/glossary/ui-types)
- [Existing Data Type components design spec](/en/design/specs/global-data-type-components), to see how current data types work.
- Filters in Mathesar:
  - [Filters "Concepts" page](/en/product/concepts/filters)
  - [Filters engineering page](/en/engineering/glossary/filters)

## Mentors
- **Primary Mentor**: Kriti Godey
- **Backup Mentor**: Mukesh Murali

See our [Team Members](/en/team/members) page for Matrix and GitHub handles of mentors.