---
title: GSoC 2022: Dependents graph
description: 
published: true
date: 2022-10-05T16:36:06.811Z
tags: 
editor: markdown
dateCreated: 2022-10-05T16:36:06.811Z
---

**Author**: [Yurii Palaida](https://github.com/Jyuart)

Mathesar is a tool that helps non-technical users to utilize the capabilities of a PostgreSQL database with an intuitive and user-friendly interface.

Like most other databases, PostgreSQL cares a lot about data integrity. So, it’s almost impossible to *accidentally* delete some object (table, view, constraint, etc.). If you’re deleting any referenced object, a database will restrict this operation with a warning that’ll be clear only to the developer.

My project during this Google Summer of Code was to construct this warning manually for the end user so that they could read it: the so-called dependency graph. It includes two parts:

1. Backend query for getting the graph (fully done)
2. UI-representation so that the user can understand what they are about to lose when deleting a referenced object (not ready)

# Deliverables

At the project finale, there were three new endpoints for getting dependents graphs for schema, table and table column objects, and a bunch of unit and integration tests to validate the query behavior.

A separate specifications page describes both the technical intricacies of implementation and the high-level overview of the project. With it, it’ll be easy to add this graph to other resources in the project.

## Closed pull requests:

- https://github.com/centerofci/mathesar/pull/1478 - an initial pull request that served as a proof of concept at the beginning (returns a full dependents graph for tables)
- https://github.com/centerofci/mathesar/pull/1540 - the first refactoring to make code more readable and include more info into the query result
- https://github.com/centerofci/mathesar/pull/1572 - tests refactoring to match with the project’s single use-case
- https://github.com/centerofci/mathesar/pull/1577 - adding more types as possible dependent objects (like views and indexes)
- https://github.com/centerofci/mathesar/pull/1585 - endpoint for returning schema dependents
- https://github.com/centerofci/mathesar/pull/1608 - endpoint for returning column dependents
- https://github.com/centerofci/mathesar/pull/1638 - backend filters to completely remove dependents of a specific type from the result

# Main challenges

The main challenges while working on the project were:

- Writing a pretty comprehensive recursive query using the SQL Alchemy statements (the main Mathersar library for communication with the database as per the time of writing)
- Creating tests to validate the query results, especially the recursive parts of it
- Factorization of the work. It was my first experience working on a project like this with planning the work by myself

# Further improvements

Next steps for improving the project:

- Adding a UI layer to show a graph to a user (preferably as a modal window)
- Adding SQL functions as dependents

# Acknowledgements

Special thanks to Mukesh Murali for constant support and help during our weekly meetings and the Mathesar team for being an excellent place for open-source newcomers.

# References

- The initial proposal for the project: [Construct Dependency Graph for Database Objects (GSoC 2022 Proposal by Yurii Palaida) (summerofcode.withgoogle.com)](https://summerofcode.withgoogle.com/media/user/746462d805d7/proposal/gAAAAABjPFsNHDKT8MmRc7wvBWHNqHVhZZa2zdgOwgCAVO1hVouvPx9F8Fem2qViSJH1jZBtN9IC84krrl5sxqew5zkjgGkcqXQBv0wGrexvNZCNX7lB1J0=.pdf)
- A blog post with impressions on the first part of the project: [How I Spent My [Google] Summer [of Code] Part 1 | by Yurii Palaida | Aug, 2022 | Medium](https://jyuart.medium.com/how-i-spent-my-google-summer-of-code-part-1-d7ab7fdc04d7)
- All the issues done during the project: https://github.com/centerofci/mathesar/issues/398
- [The tech spec of the implemented feature](engineering/specs/dependents-graph.md)