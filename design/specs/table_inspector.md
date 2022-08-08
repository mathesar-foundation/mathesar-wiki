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

Users can access information and setting options for each table component using the table inspector, including columns, rows, and cells.

### Design Goals

- Provide easy access to table component settings.
- Make features easier to discover.

## Enabling and Disabling the Table Inspector

The table inspector can be enabled or disabled manually or automatically based on event triggers.

To manually enable the table inspector:

- Directly click on the inspector toggle located in the table toolbar to show the table inspector.

Some events will automatically display the table inspector:

- Navigating to a newly created table after completing the data import process.
- Navigating to a newly created table after completing the column extraction process.

To disable the table inspector:

- Directly click on the inspector toggle located in the table toolbar to hide the table inspector.

### Positioning

When users enable the table inspector, a panel will appear on the right side of the screen, sharing the same container as the table and pushing its contents rather than being stacked on top of it.

In some cases, this will cause the table portion of the layout to have a horizontal scroll.

### Inspector Modes

At the top of the inspector panel is a row of tabs. Each tab includes table component-specific attributes and actions.

The tabs are listed in the following order:

- Table (Default)
- Column
- Record
- Cell

## Using the Table Inspector

Selecting different inspector modes in the table inspector allows users to examine at the properties, options and settings of table components. Aside from that, various actions can also be initiated through the inspector.

### Table Mode

Shown when inspector mode is set to `Table`.

Properties:

- Table Name
- Table Descriptions

Settings:

- Record Summary
- Table Links (Constraints)
  
![image](/assets/design/specs/table_inspector/183378847-b942ecd3-6f3c-4cd4-8cc4-3080a041b2a4.png)

![image](/assets/design/specs/table_inspector/183380108-b3db8d3b-7301-4a19-bc38-cd777a4dde46.png)

### Column Mode

Shown when inspector mode is set to `Column`.

Properties:

- Column Name
- If Column is Link:
  - Link Source

Options:

- Allow NULL
- Allow Duplicates
- Data Type
  - Database Options
  - Format Options

![image](/assets/design/specs/table_inspector/183432613-ead6315e-3802-4345-9427-820c66094797.png)
  
![image](/assets/design/specs/table_inspector/183433425-9a906a91-28a4-4045-9300-732af811ed8d.png)

### Record Mode

Shown when inspector mode is set to `Record`.

![image](https://user-images.githubusercontent.com/845767/183444464-fb268bfc-77e2-45cf-9180-373cf950ca63.png)

### Cell Mode

Shown when inspector mode is set to `Cell`.

![image](https://user-images.githubusercontent.com/845767/183445209-a2d7bf2c-453b-4cae-84e8-94b645ce9271.png)

### Actions Panel

The actions panel provides users with ready-to-use actions for quickly manipulating tables, columns, or cells. The available actions are dependent on the active inspector mode.

#### Future Considerations

I think the 'Actions' panel could include the data modeling suggestions in the future. It could also include shortcuts to create queries that include the filters set in a table or the group options into a summary.

![image](/assets/design/specs/table_inspector/182186186-91449400-5608-42a2-8f05-33506cb2532b.png)

### Selection Modes

#### Cell Selection

![image](/assets/design/specs/table_inspector/182121672-eaa8e422-7277-4421-8927-04637c182e6c.png)

#### Column Selection

![image](/assets/design/specs/table_inspector/182121417-8eb51f90-8767-4a01-bc36-a9c55c1614b5.png)

#### Row Selection

![image](/assets/design/specs/table_inspector/182122068-c08fecea-7d18-48ad-a8de-1cb1992ca8aa.png)

#### To Deselect

Deselect all selected items by clicking on a currently selected item, on an empty space, or pressing the escape key.

#### To Select All

For records, the option to select all is available, which would include all columns and cells in the selection. The column header should include a control for this.

The current page's viewable records would be included in the selection. The user will be given the option to select all records in the table if they want.

#### Extending a Selection

We may consider including a "Selection" area in the inspector so that users can change the selection they're currently working with.

This section could contain options such as:

- Extend selection
- Select all
  - Select all columns with the same data type

## Keyboard Controls and Touch Devices Considerations

Users would be better served if the software could support keyboard controls. We'll look at how the inspector options are accessed and updated using the keyboard in a separate issue. We'll also look at how multi-object selection works on touch devices.

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
