---
title: GSoC 2022 Project Ideas
description: 
published: true
date: 2022-02-09T00:02:17.574Z
tags: 
editor: markdown
dateCreated: 2022-01-18T19:32:54.047Z
---

## Ideas

- [Automatic Hint Reflection ***Skills**: Python, PostgreSQL, **Length**: Long, **Difficulty**: Hard*](/en/community/mentoring/project-ideas/automatic-hint-reflection)
- [Break Columns out to New Table ***Skills**: Python, Django, PostgreSQL, **Length**: Medium, **Difficulty**: Easy*](/en/community/mentoring/project-ideas/break-out-columns)
- [Suggest Candidate Columns to Create Separate Table ***Skills**: PostgreSQL, database theory, statistics, **Length**: Long, **Difficulty**: High*](/en/community/mentoring/project-ideas/suggest-candidate-columns)
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
