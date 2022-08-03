---
title: Table Inspector
description: 
published: true
date: 2022-08-02
tags: 
editor: markdown
dateCreated: 2022-08-02
---

## Context

Using the table inspector, users can access information and configuration options for each individual table component, including columns, rows, and cells.

### Design Goals

- Provide easy access to table component configurations.
- Make features easier to discover.

## Enabling the Table Inspector

The table inspector can be enabled or disabled manually or automatically based on triggers.

To enable the table inspector:

- Directly click on the inspector toggle located in the table toolbar to show the table inspector.
- Open a newly created table, as part of another flow like [data import](#data-import) or [column extraction](#column-extraction).

When users enable the table inspector, a panel will appear on the right side of the screen, sharing the same container as the table and pushing its contents rather than being stacked on top of it.

- In its default mode, the inspector will provide information and configurations for the current table.
- The inspector provides additional information and configuration options depending on what's currently selected.

To disable the table inspector:

- Directly click on the inspector toggle located in the table toolbar to hide the table inspector.

## Using the Table Inspector

Whatever is presently selected will determine the content of the table inspector. During non-selection mode, the inspector simply displays properties for the current table.

### Table Inspector Modes

The current selection is what triggers the various inspection modes. The inspector panel's header contains a brief description of what is included in the selection.

### Table Properties

Shown during non-selection mode.

Table properties include:

- Table Name and Description
- Table Links
- Table Display Options
  - Record Summary
  
![image](/assets/design/specs/table_inspector/182566720-3622f073-24ee-4aff-8460-64442f271fea.png)

### Column Properties

Shown when a [column](#column-selection) or [cell](#cell-selection) are selected.

Column properties include:

- Column Name
- Column Constraints
  - Allow NULL
  - Allow Duplicates
- Column Data Type
  - Select Type
  - Database Options
  - Format Options
  
![image](/assets/design/specs/table_inspector/182350473-c20ebabb-2a41-4bf7-ad50-dfda965b1081.png)

### Link Column Properties

Shown when a foreign key column or cell is selected.

Link column properties include:

- Column Name
- Link Information
  - Table source
  - Column source
  
![image](/assets/design/specs/table_inspector/182350542-a5af060c-16f7-40b5-9a00-b7b6cc32e2a2.png)

### Multiple Columns

Shown when multiple columns are selected.

Multiple column properties:

- Data Type

![image](/assets/design/specs/table_inspector/182350659-10d1b6f7-2cbf-44cb-a728-8241ad9f7335.png)

### Actions Panel

Shown at all times, the content might change depending on the selection status.

The actions panel provides users with ready to use actions for quickly manipulating tables, columns or cells. The available actions are dependent on the selection.

#### Future Considerations

In the future I'm thinking the 'Actions' panel could include the data modeling suggestions. It could also include shortcuts to create queries that include the filters set in a table, or the group options into a summary.

![image](/assets/design/specs/table_inspector/182186186-91449400-5608-42a2-8f05-33506cb2532b.png)

### Selection Modes

#### Cell Selection

![image](/assets/design/specs/table_inspector/182121672-eaa8e422-7277-4421-8927-04637c182e6c.png)

#### Column Selection

![image](/assets/design/specs/table_inspector/182121417-8eb51f90-8767-4a01-bc36-a9c55c1614b5.png)

#### Row Selection

![image](/assets/design/specs/table_inspector/182122068-c08fecea-7d18-48ad-a8de-1cb1992ca8aa.png)

#### To Deselect

Deselect all selected items by clicking on a currently selected item, on an empty space or pressing the escape key.

#### Extending a Selection

We may think about including a "Selection" area in the inspector so that users can make changes to the selection they're currently working with.

This section could contain options such as:

- Extend selection
- Select all
  - Select all columns with same data type

## Keyboard Controls and Touch Devices Considerations

Users would be better served if the software could support keyboard controls. In a separate issue, we'll look at how the inspector options are accessed and updated using the keyboard. We'll also look at how multi-object selection works on touch devices.

## User Interface Considerations and Examples

### Collapsible Sections

To make the table inspector's user interface more flexible, it should have expandable parts that can be collapsed and scrolled to.

![image](/assets/design/specs/table_inspector/182355968-c9129949-344a-4e41-a685-90700a816141.png)

### Examples

#### Retool

![d1568b5ad2e1ce13d51ad419e60b8fdb0b7238c8](/assets/design/specs/table_inspector/182356613-1b222a0b-f77f-4a15-a9df-84ed874ce5f3.gif)

#### Palantir

![image](/assets/design/specs/table_inspector/182356749-88273bdb-d4c8-4495-9aa8-c10816171059.png)

#### Balsamiq

![image](/assets/design/specs/table_inspector/182357016-aba81b9e-a45a-4466-808a-6e4963a01038.png)
