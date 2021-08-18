---
title: Add Table from File Import Specs
description: 
published: true
date: 2021-06-07T20:24:13.003Z
tags: 
editor: markdown
dateCreated: 2021-06-02T09:10:33.943Z
---


# Context
Adding a new table from a file import allows users to input data into Mathesar without populating tables manually. This feature is also convenient for users who need to import data for testing Mathesar's functionality.

While data file import is a baseline feature for most applications in this category, additional functionality will be implemented in the future to enhance the data import process, such as automatic type detection, data cleansing, error detection, and others.

# User Experience
## Impact
This feature will improve the user experience for users who need to input data into Mathesar by reducing the required effort when populating tables.

This feature will also support the experience of first-time users, as it is expected by users of similar applications and would cause dissatisfaction if missing.

## User Flow

![](/assets/design/specs/table-import/Z3ngzR9.png)


### User Adds a Table
The user starts the process of adding a table by clicking on any of the available options. The user can add a table from the sidebar menu(1) or the 'New' menu located on the top navigation bar in the main content area.

![](/assets/design/specs/table-import/DH3XRuj.png =400x)

#### Notes
- We can implement the 'New' menu at a later iteration.

### User Sets Table Options
Once the add table process starts, the user is prompted to set a name, confirm, or select the schema that will hold the table.
Using the lookup field, the user could also add a new schema from this dialog.

![](/assets/design/specs/table-import/ByfztC0tu.png =400x)

#### Valid and Invalid Table Names
Based on [PostgreSQL Documentation](https://www.postgresql.org/docs/13/sql-syntax-lexical.html#SQL-SYNTAX-IDENTIFIERS), some naming conventions apply to objects, including tables, views, and columns. For most cases, we'll handle any necessary quoting automatically and transparently and generate unique names when required by adding a number as the last character.

- You can use any character for the valid characters except for a literal `null` character in a name.
- For starting characters, anything goes (except a literal null) for our use case with the same caveats w.r.t. exotic characters above.

### User Selects Add Table Method
After confirming the table name and schema, the user must select one of the methods available for adding a table. 

![](/assets/design/specs/table-import/chcPbaV.png =320x)

Implementation Notes:
- Copy will be revised later with the purpose of supporting best practices while guiding the user during the table creation process. We want to be more explicit in regards to goals for every step. 

#### Implementation Note:
- Empty table flow will be designed in a future iteration.

### User Selects Data Import Method
Once the new table is created, The system will prompt the user to start the import data process. There are various options to import data, whether from a local file, clipboard, or remote location.
By default, Upload File is the selected option.

![](/assets/design/specs/table-import/zU9Csfe.png)


### User Uploads a File
The user then proceeds to upload a CSV file, and once it's completed, the system will render the file along with an option to remove it and upload another file.

![](/assets/design/specs/table-import/1FZ5Efd.png)

In most cases, when the file is large, processing will take longer. For that reason, a loading UI state is needed.

![](/assets/design/specs/table-import/By4JP0CK_.png)

If any errors prevent the file from being uploaded, an error message will be displayed.

![](/assets/design/specs/table-import/HJxJY0AY_.png)

#### Implementation Notes
- Paste and From URL methods will be designed in a future iteration. The current use case only uses the file import method. 

### User Confirms Data
If the system successfully processed the file, it will prompt the user to confirm if a preview of their data looks correct. The user can also choose to ignore columns, rename them, and change data types from this view. 

![](/assets/design/specs/table-import/Rpz9ZhV.png)

### User Opens the New Table
![](/assets/design/specs/table-import/JMtTnDZ.png)


## Feedback
- Does the impact and user experience for this functionality help users achieve the goals established in the [Inventory Use Case](/design/exploration/use-cases/inventory-use-case)?
- Is there an opportunity to allow a different user experience or workflow? Why or why not?

# Interactions (WIP)
Interactions for adding a table via file import focus on guiding the users through multiple steps, providing cues to help the user make decisions, and preventing unwanted outcomes by incorporating confirmation steps in error-prone steps.

## Wizards
Wizards are series of screens that guide users through multi-step processes.
In adding a table via file import, wizards are used to accomplishing some required tasks, such as selecting the data source to use (e.g., upload a file, paste, URL), mapping columns, and confirming field types.

![](/assets/design/specs/table-import/ByYAYLmq_.png)

The wizard elements should provide users with information regarding the length of the process, i.e., the number of steps. It should also provide controls to cancel the operation.

![](/assets/design/specs/table-import/Bk1x58Q9O.png)


## Pre-Determined Options
When triggered from a particular context, actions like adding a new table will have pre-determined options, i.e., the target schema for a new table.

For example, if calling the add new table function from the sidebar menu, the context will determine that the system must add the table to that particular schema. 

However, a user might choose to add a new table from a different context, where there's no pre-determined option. In this case, a user would have to select the desired option. 

Making pre-determined options visible and editable in the interface can be helpful for users when confirming outcomes where contextual cues are missing.

# User Interface (WIP)
## Components
### Input Controls
Input controls allow the user to enter or select different values needed to perform tasks within Mathesar. In file import, they will enable the user to specify column types and parameters required to map columns.

#### Text input
![](/assets/design/specs/table-import/rJoUmDX5_.png =140x)

#### Select input
![](/assets/design/specs/table-import/rkavQwXc_.png =140x)

#### Lookup input
![](/assets/design/specs/table-import/BysumDQqu.png =140x)

#### Radio buttons
![](/assets/design/specs/table-import/H1P5XPQcu.png =320x)

#### Checkbox input
![](/assets/design/specs/table-import/HJnhQP7cd.png =200x)

#### States
- Default
- On Focus
- Disabled

### Buttons
Buttons allow users to perform actions and obtain a result from the system.

#### Types
There are different types of buttons, and their use depends on several factors, e.g., the type of task they are to perform and their context.

![](/assets/design/specs/table-import/rkEwqImqd.png =200x)

Primary buttons are used for actionable (e.g., submit content, apply a change) and some exceptional navigational purposes (e.g., continue to a next step). However, their use should be restricted to priority or practical actions, with the ideal number of primary buttons being one per view.

Secondary buttons are used alone or in combination with primary controls to complement priority actions.


### Dialogs
Dialogs are a type of modal window that appears in front of content and is used when the system requires users to make decisions.
When active, dialogs will prevent other content from being interacted with. In most cases, they are driven by user action, and their unprompted use is discouraged.

![](/assets/design/specs/table-import/Hk02qLQc_.png =280x)

### System Notifications

#### Error Messages
![](/assets/design/specs/table-import/SJBTzvX9d.png)


