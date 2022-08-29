---
title: Inline Saving and Editing
description: 
published: true
date: 2022-08-19
tags: 
editor: markdown
dateCreated: 2022-08-19
---

## Context

Some actions contained in Table Inspector require an explicit save action as they introduce change to the database. Some of these actions are:

- Changing Table Name
- Changing Column Name
- Changing Column Type

This spec introduces a new pattern to the application that allows users to edit values inline and save them. It is meant for Table Inspector but should be easily extendable to other application parts if required.

## Design Goals

- Allow users to edit values inline
- Allow users to save changes
- Allow users to cancel changes
- The user should be able to edit and save values by using the keyboard only

## Not in scope

- Allow users to edit multiple values at once

## Scenarios

### User updates the name of a table

1. The user clicks on the table name input
1. The user types the new name
1. Save and cancel buttons appear
1. The user saves the change by:
    - Clicking on the save button
    - Pressing Enter
1. The user sees the new name in the input
1. The save and cancel buttons disappear

![image](/assets/design/specs/inline-save-edit/185621416-fe829bc5-9016-48e4-8633-647b365857ef.png)

Alternatively, we might use icon buttons instead of text buttons. This design could save space and make the UI less cluttered.

![image](/assets/design/specs/inline-save-edit/185630760-1e0360d4-f286-4b99-ab8e-0b22e719ed76.png)

### User discards the changes to the name of a table

1. The user clicks on the table name input
1. The user types the new name
1. Save and cancel buttons appear
1. The user discards the change by:
    - Clicking on the cancel button
    - Pressing Escape
1. The user sees the old name in the input
1. The save and cancel buttons disappear

### User updates the data type of a column

1. The user clicks on the data type select input
1. The user selects the new data type
1. Save and cancel buttons appear
1. The user saves the change by:
    - Clicking on the save button
    - Pressing Enter
1. The user sees the new data type in the input
1. The save and cancel buttons disappear

## Additional Considerations

### Editing other values while an active edit is in progress

To avoid confusion, the user should not be able to edit other values while an active edit is in progress. For example, editing the name of a table while editing the data type of a column.

A possible solution is to disable other inputs while editing is in progress.

We should also block the user from navigating to other inspector tabs while the edit is in progress.

### Making edit action explicit by clicking on an edit button

I have considered making the edit action explicit by clicking an edit button. However, we have a mix of controls that require save and some that don't (e.g., the table name input). This would make the UI inconsistent and confusing.

![image](/assets/design/specs/inline-save-edit/185633330-26a682a5-50b1-4bd0-a4f9-828bed43d0c0.png)
