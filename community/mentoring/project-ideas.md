---
title: GSoC 2022 Project Ideas
description: 
published: true
date: 2022-02-08T23:58:14.590Z
tags: 
editor: markdown
dateCreated: 2022-01-18T19:32:54.047Z
---

## Ideas

- [Automatic Hint Reflection ***Skills**: Python, PostgresSQL, **Length**: ~350 hours, **Difficulty**: Hard*](/en/community/mentoring/project-ideas/automatic-hint-reflection)
{.links-list}

## Template

> Please use this template while adding new project ideas.
{.is-info}

### The Problem
*Describe the problem that the project is expected to solve.*

### Classification
- **Difficulty**: *Low/Medium/High*
- **Skills needed**: *List of technologies or other skills needed*
- **Length**: *Medium (~175 hours) / Long (~350 hours)*

### Tasks
*A list of tasks that the intern is expected to complete as part of their work. Be specific about research, code, etc.*

### Expected Outcome
*Describe the expected outcome of the project.*

### Application Tips
*Tips for writing a successful proposal to complete this project. This could include what specific questions to answer or what details could help the application stand out.*

### Resources
*A list of links to documentation/code/wiki pages, etc. relevant to the project idea.*

### Mentors
*List of mentors for this project.*

-----------



## Break columns out to new table

### The Problem
A user may have a column in their table which would be better as a separate table, linked by a foreign key relationship. For example, if they have a `Students` table in a database for a school district with a `School Name` column, it's likely that such a column could be a separate `Schools` table, and the students would be linked to their schools by a foreign key in the `Students` table linking to the primary key in the `Schools` table. Setting this up by hand would be tedious.

### Classification
- **Difficulty**: Easy
- **Skills needed**: PostgreSQL, Python, Pytest, Django
- **Length**: Medium (~175 hours)

### Tasks
- Determine the current state of the solution in the code base in the `db/tables/operations/split.py` file.
- Double check the tests for the current solution and find any bugs.
- Fix any bugs found, add tests if needed.
- Connect the splitting functionality to the API so it can be called.
- If there's time, we will also attack the table merging logic in the `db/tables/operations/merge.py` file.

### Expected Outcome
There should be an appropriate API endpoint (to be determined in collaboration with the Mathesar team) that lets a caller give a `database`, `schema`, `table`, and `column` as either a query parameter string or POST (depending on the design we choose).  The result should be the extraction of the column, creation of a new table consisting of a copy of that column (including data) plus the default Mathesar `id` primary key column, and the replacement of the extracted column in the original table with a foreign key column linking to the `id` column of the new table.  The foreign key column should be populated so that the natural join between the original and new tables results in the extracted data being matched up with the rows of the original table correctly.

### Application Tips
The successful candidate will be able to understand and articulate the usefulness of automatically extracting a column to a separate table. They'd thus be able to design and implement tests that ensure the expected behavior is actually satisfied by the current functions.  Finally, they'd either know or be willing to learn about Django in order to be able to wire things up.

### Resources
- [relevant code](https://github.com/centerofci/mathesar/blob/afac35483cd56626778acf01df41cae9423636d5/db/tables/operations/split.py)
- [relevant tests](https://github.com/centerofci/mathesar/blob/afac35483cd56626778acf01df41cae9423636d5/db/tests/tables/operations/test_split.py)

### Mentors
Brent Moran (@brent:matrix.mathesar.org)

## Suggest candidate columns to create separate table

### The Problem
In order to normalize a data model, one needs to understand correlations between different rows in the data of a table.  For example, if there is a column `student email` that is dependent on a proper subset of the key `(class id, student id)` in some `class_rosters` table, then a separate `students` table with columns `(student id, student email)` should be created, and `student email` should be dropped from the original `class_rosters` table. This would potentially move the data model closer to achieving the Second Normal Form (2NF). We need to build functions that notice this sort of correlations.  Ideally, we'd start with functions that notice when a relation is not in 2NF (but _is_ in 1NF), and suggest fixes. If that's achieved, we'd then proceed to suggest fixes to achieve 3NF.

### Classification
- **Difficulty**: *High*
- **Skills needed**: PostgreSQL, Database theory, a bit of statistics.
- **Length**: Long (~350 hours)

### Tasks
- Research method of automatically determining the violating correlations disallowed by 2NF.
- Research whether a "hard rule" makes more sense, or whether it makes more sense to have some correlation score.
- Based on answers to the above, implement functionality so that we can call a python function that takes a table as input, and returns sets of columns that could be extracted.
- Repeat with 3NF as the goal.

### Expected Outcome
We should end up with python functions backed by SQL that let us determine whether a relation in a DB is in 2NF (or 3NF), and suggest column sets to extract to separate tables that would promote the data model to a higher normal form (at least the subset of the data model involving the relation in question).

### Application Tips
The successful candidate would understand the motivation for normalizing a database. They'd also understand some basics about stats and be able to relate the idea of correlations between columns of a table to how different sets of columns might be able to be extracted.

### Resources
- [relevant code](https://github.com/centerofci/mathesar/blob/afac35483cd56626778acf01df41cae9423636d5/db/tables/operations/split.py)
- [relevant tests](https://github.com/centerofci/mathesar/blob/afac35483cd56626778acf01df41cae9423636d5/db/tests/tables/operations/test_split.py)
- [Database normalization wikipedia page](https://en.wikipedia.org/wiki/Database_normalization)

### Mentors
Brent Moran (@brent:matrix.mathesar.org)

## Visualization of grouped data

### The Problem
One of the common needs that arises when analyzing data is to group similar results, aggregate them, and gain insights from them. For eg., Consider the scenario where we have a list of employee records and would like to figure out how many employees reside in a particular country, and further categorize them by age group, gender etc., Databases make these kind of usecases easier by providing powerful grouping behaviours. However, inorder to leverage it users would need to work with SQL which requires technical knowledge.

Mathesar is focused on providing an intuitive interface over databases for non-technical users. They should be able to gain data insights through grouping with as simple interactions as possible. Mathesar currently provides the ability to group records and displays them as linear rows, separated by group headers, further narrowed down by pagination. While this allows users to group data as per their requirements, it would be more helpful to provide a bird's eye view on the entire dataset.

An additional option to visualize the grouped results in the form of graphs or a summary view would be highly effective.

### Classification

- **Difficulty**: Low
- **Primary skills needed**: Frontend development knowledge
- **Secondary skills needed (or willing to learn)**: UX design, SQL, Python, Django
- **Length**: Medium (~175 hours)

### Tasks
- Research and come up UX design specs and wireframes for grouped data visualization.
- Create necessary issues based on the finalized specs after review.
- Research graphing libraries and identify the one most suitable with Mathesar's architecture and goals.
- Identify missing APIs or changes required in exising APIs and implement the necessary changes on the backend.
- Implement the frontend data visualization interface.

### Expected Outcome
Once a user groups rows, there should be an option on the Mathesar UI to allow them to visualize the result. The interactions and user input required should be minimal.

### Application Tips
A good candidate would be someone who is able to emphathize and think from the perspective of a non-technical user, and align themselves with the goals of Mathesar. They should be willing to do a fair amount of research both in terms of UX and engineering. They will be working full-stack and would either know or be motivated to learn the necessary technologies in order to complete the project.

### Mentors
Pavish Kumar Ramani Gopal (@pavish:matrix.mathesar.org)

## Sharable forms to add data to tables

### The Problem
Mathesar currently offers a spreadsheet-like interface for data entry into tables. One of Mathesar's potential usecases is to allow data entry through surverys from a large group of individuals. Sharing the spreadsheet-like interface for such data entry is unfeasible and also comes with privacy and access-level implications.

A simpler solution is to share forms to the individuals. The creators/admins would have direct access to Mathesar's interface, share a form view for the table, and everyone participating in the survey would only be seeing and entering data into that form. An entry through the form will reflect on the associated table(s) as a row.

### Classification

- **Difficulty**: Low
- **Primary skills needed**: Frontend development knowledge
- **Secondary skills needed (or willing to learn)**: Requirement analysis, UX design, SQL, Python, Django
- **Length**: Medium (~175 hours)

### Tasks
- Research similar products and come up with product-level specs on the requirement.
- Research and come up with the UX required for form construction for Mathesar admins, and the form displayed to end-users (participants).
- Identify API requirements and create new endpoints or update existing ones as required.
- Implement the frontend work essential for building, sharing and entering data into the form.

### Expected Outcome
We should have an interface for table owners to construct and share forms. The fields on the form should map to table columns and owners should have the ability to omit, align, organize those fields. They should also be able to provide additional descriptions. Participants viewing the form should be able to enter and submit data using it, which should reflect on the table.

### Application Tips
A good candidate should take the time needed to understand the requirements, research and suggest changes or improvements. They should be motivated in providing a good user experience. They will be working full-stack and would either know or be willing to learn the necessary technologies.

### Mentors
Pavish Kumar Ramani Gopal (@pavish:matrix.mathesar.org)


## Construct Dependency Graph for Database objects

### The Problem
We'd like to be able to know what other database objects depend on a database object like a Schema or a Table.

This is useful in various situations
- To show to the user in the frontend before they decide to delete a `Schema` or a `Table`.
- To show how a `View` was constructed 
- To get a high level overview of the Data Model


### Classification
- **Difficulty**: Medium
- **Primary Skills needed**: PostgreSQL, Python, Pytest, Django
- Secondary skills needed (or willing to learn): UX design, Front End Development Knowledge
- **Length**: Long (~350 hours)

### Tasks
- Build a python API to query for a database object dependency.
- Extract dependency information from [System Catalog tables](https://www.postgresql.org/docs/8.4/catalogs.html) for the queried object
- System Catalog Tables does not contain the dependency information of a function as functions are stored as text on the database. So [pglast](https://github.com/lelit/pglast) should be used to extract dependency information from the function body.
- Build Dependency graph based on the dependency information.
- Add Django dependency API to resources [listed in this issue](https://github.com/centerofci/mathesar/issues/398), making use of the underlying python dependency api

### Bonus Tasks
- UI Graph View - Using the Dependency API, create a component on the frontend to visualize the dependency graph
### Expected Outcome
There should an appropriate python api backed by SQL functions which would take in the `oid` or `name` of the database object whose dependency graph has to be constructed along with some filtering parameters to limit the listed dependent objects and return a hierarchical dependency graph which contains information of the dependent object. The dependency query varies based on the type of the database object, so the queries for each type should be split into composable `CTE` for readability.   
### Application Tips
A good candidate would be someone who has good understanding of SQL, and align themselves with the goals of Mathesar. They should be willing to do a fair amount of research both in terms of UX and engineering. They will be working full-stack and would either know or be motivated to learn the necessary technologies in order to complete the project.
### Resources
- [Reference code](https://wiki.postgresql.org/wiki/Pg_depend_display)
- [Relevant discussion](https://github.com/centerofci/mathesar/issues/398)
### Mentors
Mukesh (@mukesh:matrix.mathesar.org)
