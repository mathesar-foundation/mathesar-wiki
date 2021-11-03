---
title: Roadmap
description: Roadmap for upcoming Mathesar features
published: true
date: 2021-11-03T20:14:52.575Z
tags: 
editor: markdown
dateCreated: 2021-04-20T19:43:28.320Z
---

Our feature roadmap is tracked via [GitHub milestones](https://github.com/centerofci/mathesar/milestones?direction=asc&sort=due_date&state=open). You can find out more about each feature in our [Concepts](/product/concepts) page.

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

Once we've released our alpha release, we will then expand the roadmap based on user feedback and enabling more complex use cases.

Also see our [Product principles](/product).

## Future Features
Please see [Feature Ideas](/product/feature-ideas) for a long and disorganized list of feature ideas that we're drawing from to create this roadmap.
