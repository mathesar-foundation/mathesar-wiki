# Data Type Options

## Context

Data types are used to define the type of data that a column can hold. Each data type has a set of options that can be configured to define how the data is interpreted and displayed. These set of options are split into two categories:

- **Database**: These options are used to define how the data is stored in the database.
- **Format**: Defines how the data is displayed to the user.

## Problem

The current implementation uses tabs to switch between the two categories of options. This is not ideal because data type options are used in Table Inspector, where tabs are already used to switch between different sections. We are trying to avoid having a tabbed interface within a tabbed interface.

## Vertical Space Considerations

The solution should consider the challenges in displaying the options in a small vertical space, such as the dropdown menu. Scroll bars should be avoided if possible.

## Proposed Solution

### Replace tabs with stacked sections

Update Database and Format options to be stacked sections inside the Data Type section. The user should be able to access the options without the need of tabs.

### Use a dropdown menu for the data type selection instead of the scrollable list

Replace the current scrollable list with a dropdown menu to save vertical space.

### Align some of the label and field groups inline

Inline alignment can be used for groups of fields in order to save vertical space.

![image](/assets/design/specs/data-type-options/6VPzH8Cd7USbhf6jZpzQvc.png)

### Clearly identify the database-level options

A warning message can be displayed inline when the user tries to change a database-level option. The icon can then be used for other instances where the user needs to be aware of database-level options.

![image](/assets/design/specs/data-type-options/fpnLR7JtkJJZXGybZoYL8d.png)

### Visibility of Save and Cancel buttons

In the context of table inspector, the 'Save' and 'Cancel' buttons will be hidden by default. They will be displayed when the user changes any of the options. This is consistent with the current behavior of the 'Save' and 'Cancel' buttons in the table inspector.

### Confirmation dialog when user tries to save

A confirmation dialog would be displayed based on the user's changes. The warning message in this dialog would be based on the implications of the changes.

* Changes to Database type:
  - Confirmation dialog is shown.
  - Message: This change may lead to data loss since it changes the way the database stores data.
  - If a default value is present, an additional message would be displayed: The current default value `${Current_Default_Value}` will be cleared.
* Only formatting changes: Confirmation dialog is not shown.

### Default Value Section

The default value section will be its own section instead of being part of the Data Type section.
