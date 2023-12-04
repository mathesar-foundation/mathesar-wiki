# 2023-12-01 Design Session

## Topic

This design session will focus on the problems I found when trying to improve how we link records in bulk with many-to-many relationships in Mathesar.

## Problem

### Overview

Managing table relationships within a unified view is a key feature in most database products that offer a spreadsheet-like interface. Our survey results also show that it's a feature in all products our users compared with Mathesar.

In contrast, we handle table relationships differently. We exclusively use foreign keys to establish these relationships, requiring users to create an exploration to view linked data. This method varies from typical approaches in other products, which often use virtual columns to display relationships in the table view.

The Mathesar approach is more in line with relational database principles. However, it also makes it very hard to implement some of the features that users expect from a product in this space. For example, bulk linking of records is a very common feature in other products, but it is very hard to implement in Mathesar.

### Components

To address the issue of bulk linking records and managing many-to-many relationships within Mathesar, several key components of the product design must be considered:

- Unified Inline Table Editing for Multiple Tables
  - Users need the ability to edit interconnected data across multiple tables within a single interface, which is central to efficient bulk linking processes.
- Visual Relationship Mapping
  - A more intuitive and graphical representation of table relationships is required. Beyond just lists, users should be able to visually navigate and understand the complex connections between tables within Mathesar.
- Integration of tables and explorations
  - Explorations are disconnected from tables and that makes some workflows impossible or very complicated for users.
- Compatibility with existing databases and different data structures
  - We must ensure that any automatic relationship detection we plan to implement is compatible with all potential schema designs.
- Future Impact on UX for Forms
  - Survey results indicate that forms are a crucial feature expected from a product in this category. Since forms typically involve updating multiple tables simultaneously, addressing this issue might be a higher priority.

### Challenge

**How can we facilitate the management of relationships across different tables in a manner that remains consistent with the relational database principles fundamental to Mathesar?**

## Proposed Solutions

The strategies outlined below are the result of research and discussions with Brent and Pavish. In our conversations, we examined various approaches to meet the design needs for this issue. Here's a summary of the main ideas we discussed.

### Editable Explorations

Develop a feature that allows users to directly click and edit values within the exploration view, similar to the functionality of a spreadsheet. 

- Enable direct within-exploration editing for managing and modifying data in the related tables.
- Design the interface to visually represent editable areas, consistently distinguishing them from non-editable summary fields.
- Auto-generate explorations upon link creation to provide instant feedback and visual understanding of changes made.
- The UI should support an iterative process for managing relationships, potentially through a wizard or step-by-step guide to building many-to-many links, starting with a simpler one-to-many approach.

:::info
**How Editable Explorations Could Solve Bulk Linking and Many-to-Many Relationships**

Initially, users can group multiple records based on a one-to-many relationship within an exploration. Imagine a scenario where users can edit a dedicated field to bulk link records to a single item in another table.

![image](https://hackmd.io/_uploads/HyPjlBmHa.png)

By enabling this functionality on both sides of a one-to-many relationship, users would be able to establish many-to-many associations between tables.
:::

### Integrated Joining Experience

Create a feature in the table view that lets users perform joins directly, without needing to switch to a different view. Once a join is executed, this feature should generate an editable, combined view of the joined tables.

- Allow for direct table joins within the table view, simplifying the process of combining data from multiple sources.
- At the table level, there would be a prominently placed "Join Table" button. Upon clicking this button, users are presented with a modal or a panel overlay where they can initiate the join process.
- Once the secondary table is selected, the UI should then display a list of columns available for the join. The interface could visually highlight or suggest the foreign key column, if one exists, but also provide a dropdown or a selectable list for the users to choose their preferred join column.
- Columns from the joined table can be inserted into the view. To maintain a clear and structured display, these joined columns could be visually nested or indented underneath the primary table's columns or provided with a different styling to make it clear that they originate from a different table.
- Explorations, on the other hand, would become a dedicated feature for performing more sophisticated data analysis tasks, such as aggregations, summarizations, creation of complex filters, and generation of visual data representations like charts and graphs.

:::info
**How Integrated Joins Could Solve Bulk Linking and Many-to-Many Relationships**

By allowing users to integrate joined tables into the same view, we could enable various types of relationships to be represented and edited without losing context from the original tables where the data exists.

![image](https://hackmd.io/_uploads/r1tKMr7Bp.png)

This approach would enable users to transition from one-to-many to many-to-many relationships as needed and represent these changes in ways that are visually indicative of the relationship, such as through a nested structure or other methods.

![image](https://hackmd.io/_uploads/S13bUUmrT.png)
:::

## Discussion Points

- How easy or hard it is to edit directly in multiple tables, and what technical problems might come up.
  - Which of the two strategies we've thought of is easier to put into action?
      - The team agreed that editable explorations are preferable, however not in the way they are described above. The idea is to have explorations functionality integrated into the table view so that users can edit data directly in the table view. This would mean users can join other tables, select columns from those tables, and edit the data in the table view.
  - What might be the main challenges for each strategy?
      - Combining tables and explorations, would require implementing a UI that clearly differentiates between editable and non-editable fields.
    - We will need to change the definitions of Mathesar objects, such as tables to differentiate between base tables and these "unified" tables that are created by combining tables.
    - We will need ways to direct users to the base table if they need to see it or edit it.
  - What do we need to do at the very least to get started with one of these strategies?
    - We agreed that we need to design a flow for how users would create these "unified" tables and how they would edit them. Only then can we start thinking about how to implement this.
    - We need to think about how we would represent these tables in the UI, from listing them, to creating various "unified" tables, from the same base table and how we would edit them.
- Combining tables with explorations for better data handling.
  - How can we bring explorations and table views together?
      - We do this by combining the functionality of explorations and tables into one view. This would mean users can edit data directly in the table view.
  - What kinds of work would benefit from combining these two?
    - Less code complexity.
    - Less confusion for users.
    - Better workflows for users.

## Next Steps

- Write a design document for the "unified" tables feature.
- Design a flow for how users would create these "unified" tables and how they would edit them.
- Review the design with the team.
