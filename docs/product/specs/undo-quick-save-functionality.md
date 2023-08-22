# Quick Save Functionality

# Quick Save Functionality

## Objective

Implement a quick save functionality to protect users from unintended actions and allow them to recover their work to a specific point in time.

## Functionality Scope

The functionality scope for the quick save button covers saving changes for tables and explorations. This includes creating, deleting, renaming, and updating columns, records, properties, filters, sorting, and groupings in tables, as well as adding columns, changing transformation steps, and updating column and exploration properties in explorations.

## Features

### Quick Save Functionality

- Users can create a save point to store the current state of their work.
- Save points should be timestamped.
- Users can recover their work from a save point, reverting to the saved state.

### Visibility and User Experience

- The quick save status should be visible to users, possibly by displaying a timestamp or a notification.
- The system should provide clear feedback to users when they save their work.

## User Interface Design

To accommodate the new quick save functionality, the user interface should be updated to ensure that the new feature is easily accessible and communicated to the user.

This includes:

- Controls for the quick save functionality
- Notifications for the quick save functionality
- Error handling for the quick save functionality

### Quick Save Button

- A dedicated button should be added to initiate a quick save. This button should be placed in an easily accessible location, such as the toolbar or menu, within both table and exploration views.