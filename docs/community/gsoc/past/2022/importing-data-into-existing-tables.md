# GSoC 2022: Importing data into existing tables

**Author**: [Anish Umale](https://github.com/Anish9901)

## Introduction

Mathesar is a tool that provides a intuitive and user-friendly interface to databases along with great data analysis and visualization capabilities.

Mathesar can be used for data modeling, creating views, data storage and much more but, this requires data to be present in a database. What happens if the a partial amount of data is located on a local machine of the user and the rest is present in a database? This is where a feature like importing data into an existing table comes in handy.

My project during the Google Summer of Code was to enhance the capability of Mathesar's backend to support importing a CSV/TSV into an existing table. Take a look at the full project description [here](https://summerofcode.withgoogle.com/programs/2022/projects/oCtBUJHr). Below are the relevant links to the Pull Requests that were made by me for the implementation of this project.

## Completed tasks

### Import API and record insertion implementation

- Implementation for `/existing_import` API endpoint: https://github.com/mathesar-foundation/mathesar/pull/1442
- Implementation and tests for temporary table creation: https://github.com/mathesar-foundation/mathesar/pull/1457
- Implementation for `INSERT FROM SELECT` functionality : https://github.com/mathesar-foundation/mathesar/pull/1487

### Overcoming challenges caused by CSV imports and real-world data

- Implementation and tests for column mapper: https://github.com/mathesar-foundation/mathesar/pull/1506
- Constraint violation handling during import: https://github.com/mathesar-foundation/mathesar/pull/1548
- Implementation and tests for suggesting column mappings: https://github.com/mathesar-foundation/mathesar/pull/1698

## Additional context

- The issues related to this project are tracked here: https://github.com/mathesar-foundation/mathesar/issues/1416
- Link to my proposal: [Support Importing Data into Existing Tables](https://docs.google.com/document/d/1QIs9Wl0GmvS1XnDC0KK2Ovy3K3rv2adsWZCZ1deQSak/edit?usp=sharing)

## Acknowledgement

At the end, I would like to thank my mentor Brent Moran for his constant support, satisfying my curiosities and the informative and helpful weekly meetings through which this project was made possible, and also to everyone at Mathesar for providing me with a wonderful experience during the course of my internship.
