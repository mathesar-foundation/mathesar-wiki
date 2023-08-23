# Kanban View

## Classification

- **Difficulty**: High
- **Skills needed**: JavaScript, frontend frameworks, Python, Django
- **Length**: Long (~350 hours)

## The Problem

Currently the only way to visualize data in Mathesar is using the `Table` format. We would like the users to visualize data in other formats to make it easy to use and comprehend some specific types of data. This project aims to implement one of those formats called the Kanban view. Kanban view visually depict work at various stages of a process using cards to represent work items and columns to represent each stage of the process.

## Feature Description

Think of kanban view as a way of presenting grouped data with a very specific UI. It starts with the user grouping the data using exactly one table column. Each group becomes one kanban column. The user can then save the grouped data as a kanban board by giving it a name.

The user can have multiple kanban boards using the same underlying table, ideally using different columns for grouping. Each kanban board will have its own grouping, filtering, and sorting configurations.

Each item inside the kanban column should be represented as a card. This card uniquely represents exactly one row inside the table view. Each card will have its own configuration to choose the table columns for showing the data on the card.

## UX Design Challenges

Please bear in mind that the kanban view is a part of a bigger feature called visualization. This feature enables users to visualize data in other formats like kanban, calendar, graphs etc as opposed to just tables. This feature also let the user save these visualizations to visit and edit them later.

## Tasks

- Work with the Mathesar design team to figure out and finalize specs for:
  - The user flow to create a new kanban board from a particular table.
  - The user flow to see all of the saved kanban boards.
  - The user flow to edit a kanban board's name.
  - The user flow to change the column used for grouping.
  - The user flow to toggle the visibility of any group.
  - The user flow to toggle the visibility of empty groups.
  - The user flow to add add filtering and sorting on the board's data.
  - The user flow to configure the columns shown on the card UI.
- Implement the frontend components for this feature.
- Implement the backend components for this feature including but not limited to:
  - API to list all of the saved boards. This API should be built in a way that it can be used later to list any visualization.
  - API to save a kanban board with a name and some configurations.
  - API to update the configuration for a board.

NOTE: APIs for filtering, sorting, and grouping already exists.

## Expected Outcome

Users should be able able to create kanban boards on top of the tabular data. The users should also be able to list, edit and delete these boards.

## Application Tips

- Demonstrate proficiency with the required skills.
- Share some of your initial ideas about UX of the feature.
- Share some of your initial ideas about how to save a particular visualization in the DB.

## Out of Scope

- This project only only concerns the kanban view and hence implementing other visualizations like calendar, graphs, etc are out of scope.
- Sub-grouping inside a kanban board.
- Drag & Drop to move cards across different groups(kanban columns).
- User permissions. For now all the views will be writable by the users having `read` access to the table on which they are built.

## Resources

- [What is a Kanban board?](https://en.wikipedia.org/wiki/Kanban_board)
- [How grouping works currently?](../../../design/specs/filter-sort-group.md)
- [Examples of existing design specs](../../../design/specs.md)
- [Running the codebase locally](https://github.com/centerofci/mathesar/blob/master/README.md#local-development)

## Mentors

**Primary Mentor**: Rajat Vijay

**Secondary Mentor(s)**: Brent Moran
