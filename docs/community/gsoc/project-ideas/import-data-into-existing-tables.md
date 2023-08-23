# Support Importing Data into Existing Tables

## The Problem
Currently, Mathesar only supports creating a new table when a CSV or TSV file is imported. We would like to expand this functionality to allow users to import new data into existing tables.

## Classification
- **Difficulty**: Medium
- **Skills needed**: Python, Django, PostgreSQL
  - **Bonus skills**: JavaScript, frontend frameworks
- **Length**: Long (~350 hours)

## Tasks
- Work with the Mathesar design team to figure out a design for how to integrate this functionality into the product.
- Write a technical spec for how this functionality will fit into the current Mathesar code.
- Implement the backend necessary to make the feature work, including both the import process in the database and APIs for the frontend to interact with.
- Optionally, implement the frontend changes needed for the feature as well.

## Expected Outcome
By the end of this project, we expect that the backend code and APIs will support importing CSV data into an existing table.

If the candidate is interested, they can also implement the feature on the frontend.

## Application Tips
- Please provide as much technical detail as you can on how this will integrate into Mathesar's code. API schemas, libraries you plan to use, etc.
- Don't reinvent the wheel - use external libraries for the functionality where you can.
- It's helpful to start from the experience that you'd like the end-user to have and work backwards.
- Think through different cases for how to reconcile data, e.g. what happens when the field names in a CSV file don't match column names, or what happens when the table has more or fewer columns than the file being imported.

## Resources
- [Import Preview API technical spec](/engineering/specs/import-preview-api)

## Mentors
- **Primary Mentor**: Mukesh Murali
- **Backup Mentor**: Brent Moran

See our [Team Members](/team/members) page for Matrix and GitHub handles of mentors.