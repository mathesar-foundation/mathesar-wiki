---
title: Undo and Quick Save Functionality
description: 
published: true
date: 2023-04-26T21:25:06.862Z
tags: 
editor: markdown
dateCreated: 2023-04-26T21:17:36.980Z
---

# Undo and Quick Save Functionality

## Objective

Implement an undo and quick save functionality to recover from errors resulting from database inputs or transformations and protect users from unintended actions.

The undo would allow users to revert changes to their work, while the quick save would allow users to save their work at a specific point in time.

## Functionality Scope

The undo and quick save functionalities should apply to saving and undoing changes to the following operations:

- Table operations:
  - Creation of columns, records
  - Deletion of columns, records
  - Renaming of columns, records
  - Updating of column properties
    - Name changes
    - Data type changes
    - Constraints changes
  - Updating of table properties
    - Name changes
    - Record summary changes
  - Adding, updating, and removing filters
  - Sorting and changing sort options
  - Adding, updating, and removing groupings
- Exploration operations:
  - Adding columns
  - Changing transformation steps
  - Updating column properties
    - Name changes
    - Aggregation changes
  - Updating exploration properties
    - Name changes

## Features

### Undo Functionality

- Users can undo changes to operations performed within Mathesar.
- Users can undo multiple steps, allowing them to revert to a previous state easily.
- The undo functionality should be easily accessible, possibly through a button or keyboard shortcut.

### Quick Save Functionality

- Users can create a save point to store the current state of their work.
- Save points should be timestamped.
- Users can recover their work from a save point, reverting to the saved state.

### Visibility and User Experience

- The quick save status should be visible to users, possibly by displaying a timestamp or a notification.
- The system should provide clear feedback to users when they undo or quickly save their work.

### Change Tracking and Compatibility

- The system should track changes made within Mathesar. However, it might be challenging to track changes made directly to the database outside Mathesar. Two potential approaches can be considered:
  1. Inform users that changes made outside Mathesar may not be tracked, and they might not be able to go back to a previous step if the database is altered externally.
  2. Investigate the potential of using database triggers or other mechanisms to capture changes made directly to the database outside Mathesar.

## Implementation Considerations

- Evaluate the performance impact of the undo and quick save functionalities, especially for large data and complex operations such as data type changes or constraints changes.
- Consider potential edge cases and limitations of the undo and quick save functionalities.

## User Interface Design

To accommodate the new undo and quick save functionalities, the user interface should be updated to ensure that the new features are easily accessible and communicated to the user.

This includes:

- Controls for the undo and quick save functionalities
- Notifications for the undo and quick save functionalities
- Error handling for the undo and quick save functionalities

### Quick Save Button

- A dedicated button should be added to initiate a quick save. This button should be placed in an easily accessible location, such as the toolbar or menu, within both table and exploration views.

### Undo Functionality Access

- The undo functionality should be easily accessible, either through a button or a contextual menu item in both table and exploration views.
- The interface should show the availability of undo actions, such as through the activation or deactivation of the undo button or menu item, depending on whether there are actions available to undo.

### Communication of Changes

- The user interface should communicate to the user what changes have been made, such as through highlighting changed elements, displaying notifications
