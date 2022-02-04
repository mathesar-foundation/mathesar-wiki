---
title: GSoC 2022 Project Ideas
description: 
published: true
date: 2022-02-04T19:13:51.326Z
tags: 
editor: markdown
dateCreated: 2022-01-18T19:32:54.047Z
---

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

## Automatic Hint Reflection


### Functions API

Mathesar has an API that describes how a client can assemble Postgres functions into expressions that can later be used, for example, to filter table rows with. We call it the *functions API*. A basic example of such an expression could be: "does the title of this movie start with the same letter as its director's first-name".

For the functions API to not require hardcoding on the client side, and for clients to be able to effortlessly adapt to newly added functions, the API declares how the functions it exposes can be used. The API uses a system for assigning various types of information to individual functions and types. We're calling it the hint system.

We use it, for example, to describe the signature of the function `starts_with`: it takes two named arguments, one argument is called `string` and the other `prefix`, both arguments should be string-like, and the function returns a boolean:

```python
    hints = [
        hints.parameter(name='string', hints.string_like),
        hints.parameter(name='prefix', hints.string_like),
        hints.returns(hints.boolean),
    ]
```

Importantly, hints don't obligate the user of the API to follow them. A user should be able to assemble expressions that are in conflict with what is declared by the hints. The purpose of the hint system is to give hints to the user about how to assemble expressions, but the user should be free to assemble any expression he likes.

We chose for the hint system to be non-authoritative (allow users to ignore it) for two reasons. It empowers power-users that might want to use a function or a type in a way contrary to the declared hints. And, user developers (users that might also want to define their own Postgres functions or types) will not be obliged to master the hint system just to add a function: they'll be able to gradually start adding hints if/when they find that useful, which will cause the UX for using that function to become more streamlined with every hint added. An added bonus is that you don't have to strive to create very precise signature declarations that cover all use cases, which helps keep the way we declare signatures simple for new-comers.

### The Problem

Currently, the hints are compiled by hand, as seen in the above code sample. That could become cumbersome if the number of functions or types exploded. Also, user developers might find the hint system a barrier to using their own functions or types (though we're working to make it as accessible as possible).

We've discussed the possibility to reflect function (and possibly type) properties automatically, which would allow us to also assign (at least some) hints automatically.

The automatic reflection is not essential, but it could be a significant quality-of-life improvement. Its implementation seems too expensive for the core team to take up in the near term. At the same time, it's fairly isolated from the rest of Mathesar, which is good for new contributors.

### Classification
- **Difficulty**: High
- **Skills needed**: PostgreSQL, SQL
- **Length**: *Long (~350 hours)*

### Tasks
- Research what is the intersection between the things that would be useful for Mathesar to automatically reflect and what *can* be automatically reflected;
- Create an accurate picture of what cases the automatic reflection will fully cover and in what cases information (hints) will have to be overridden or supplemented manually;
- Figure out when to reflect and how to cache the reflections so as to minimally burden the wider system with more state;
- Do the implementation.

I would expect the above tasks to be performed (at least somewhat) asynchroniously.

### Expected Outcome
An automatic PostgreSQL function (and possibly type) property reflection mechanism tailored to automatically finding useful hints for the hint system.

These automatically generated hints will be exposed through the function and type APIs, alongside manually written hints (if necessary), so that frontends can procedurally generate expression builders and provide useful guidance with minimal prior knowledge.

### Application Tips
I'd say a good candidate would be one that is comfortable taking the time to explore Mathesar needs, as relates to the hint, function and type systems, as well as one that is comfortable investigating the various tid-bits of information that Postgres makes available for reflection. I see this as a very exploratory task that requires the willingness to get to know multiple interesting systems.

### Resources
[This](https://github.com/centerofci/mathesar/issues/1038)  is the tracking issue.

[This](https://github.com/centerofci/mathesar/pull/1022/) is the PR that will merge the hint system in.

[This](https://github.com/centerofci/mathesar/blob/ea3f200e19e4e1138e952ac1976e9f074db6c1c3/db/functions/hints.py) is the current (rudimentary) state of the hint system.

[This](https://github.com/centerofci/mathesar/blob/ea3f200e19e4e1138e952ac1976e9f074db6c1c3/db/functions/base.py) is the current (rudimentary) state of the functions system, that uses hints .

### Mentors
Dominykas (@dominykas:matrix.mathesar.org)

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
- Research and come up UX design specs and wireframes for grouped data visualization
- Create necessary issues based on the finalized specs after review
- Research graphing libraries and identify the one most suitable with Mathesar's architecture and goals
- Indentify missing APIs or changes required in exising APIs and implement the necessary changes on the backend
- Implement the frontend data visualization interface

### Expected Outcome
Once a user groups rows, there should be an option on the Mathesar UI to allow them to visualize the result. The interactions and user input required should be minimal.

### Application Tips
A good candidate would be someone who is able to emphathize and think from the perspective of a non-technical user, and align themselves with the goals of Mathesar. They should be willing to do a fair amount of research both in terms of UX and engineering. They will be working full-stack and would either know or be motivated to learn the necessary technologies in order to complete the project.

### Mentors
Pavish Kumar Ramani Gopal (@pavish:matrix.mathesar.org)
