# Roadmap

Our feature roadmap is tracked via [GitHub milestones](https://github.com/mathesar-foundation/mathesar/milestones?direction=asc&sort=due_date&state=open). You can find out more about each feature in our [Concepts](/product/concepts) page.

## About the Roadmap

Our initial roadmap is aimed at creating a very basic version of Mathesar that demonstrates our value proposition. To help us pick which features to build for the initial release, we are using three criteria:

- Users should have the features needed to manage a basic collaborative media inventory using Mathesar. We do not have a specific set of features, but keeping a simple use case in mind helps us cut features that may be too advanced.
  - Please see the following design documents for our initial exploration on this topic:
    - [Inventory Use Case exploratory document](/design/exploration/use-cases/inventory-use-case)
    - [Inventory: Data Exploration exploratory document](/design/exploration/inventory-data-exploration)
    - [Inventory Use Case report/conclusions](/design/reports/inventory-use-case)
- Mathesar should work with any existing Postgres databases gracefully. We may not be able to support full editing functionality for all database configurations, but we should not show the user erroneous or missing information.
  - We're aiming for users to be able to connect Mathesar as a GUI to their existing databases and see its potential immediately.
- We think the [Dabble DB demo video](https://www.youtube.com/watch?v=MCVj5RZOqwY) is a good demonstration of end-to-end data management features.
- Also see our [Product Principles](/product).

Once we've released our alpha release, we will then expand the roadmap based on user feedback and enabling more complex use cases.

### Target users
We're initially targeting users of differing technical skill levels who want to collaborate on the same data. We assume that the person who sets up Mathesar for a group of users will be a developer or sysadmin, but the remaining users may have no pre-existing knowledge of database or database concepts.

Mathesar will be designed so that developers can use the Mathesar API or SQL to work with the database instead of the GUI (or build an entirely new GUI).

## Future Features
Please see [Feature Ideas](/product/feature-ideas) for a long and disorganized list of feature ideas that we're drawing from to create this roadmap.
