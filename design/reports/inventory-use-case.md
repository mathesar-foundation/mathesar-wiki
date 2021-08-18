---
title: Inventory Use Case
description: 
published: true
date: 2021-05-25T13:45:57.582Z
tags: 
editor: markdown
dateCreated: 2021-05-04T18:59:23.930Z
---

The inventory use case presented many opportunities to understand how the design of the Mathesar application could influence user goals. 
We selected the inventory use case because it combined simple data storage with minimal analysis needs.

> **See also**: [Mathesar Tool Category Exploration](/design/reports/tool-category)
{.is-info}

To learn from this use case, [wireframes that depicted the various user steps needed to build an inventory](/design/exploration/use-cases/inventory-use-case) were created and shared for feedback. An additional wireframe round was conducted to dig deeper into the [data exploration process](/design/exploration/inventory-data-exploration).

# Conclusions

## Installation and Configuration UX
* Although ease of installation and configuration are key adoption drivers, they are not a design priority due to low definition from the engineering side and should be revisited once more information is available.
* We have determined that the target user for the MVP will have sufficient technical skills to self-host, install and configure Mathesar related technologies such as the PostgreSQL database.
* We have determined that ideally, we want to offer multiple installation options similar to what Wiki.js provides.

## Onboarding or First Steps
* We are assuming, for the MVP, that a majority of first-time users will start from existing data. Thus the onboarding needs to consider their specific needs, such as import from file, file type support for standard file types, data type detection, and more.
* The initial design supports importing from CSV as it is likely that most platforms support exporting data as CSV. Pasting content directly from a spreadsheet will also enable users to start exploring the tool with little effort.
* We determined that it will be necessary for an optimal user experience to expose users to the concept of 'views' as soon as they start the database normalization process. The views automatically generated will help create a more cohesive experience for the user as they learn to navigate the different tables and relationships generated during the process.

## Import File into Existing Table
* We discussed the option of proposing a data table append if the same columns are detected in the imported file.

## Working from Tables and Views
* Unlike Dabble DB, users will be able to browse the different tables that make up their schema. However, it is still unclear how we'll handle modifications of table data at the view level. These interaction requirements are a potential UX priority.

## Error recovery and Prevention Experience
* Encouraging users to explore and try different things within the application is a primary concern, mainly because we aim to increase their knowledge regarding database design and normalization concepts. It will be necessary to prioritize features that enable users to recover from errors so that learning can take place.

# Proposed Next Steps
* Define the optimal experience, interactions, and UI for a user importing data from a CSV file into a new or existing table.
* Define the optimal experience, interactions, and UI for a user locating, preparing, modifying, and sharing a view of their table data.
