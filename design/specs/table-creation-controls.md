---
title: Table Creation Controls (discard modal update)
description: 
published: true
date: 2021-07-01T21:14:55.158Z
tags: 
editor: markdown
dateCreated: 2021-07-01T21:14:55.158Z
---

# Context

## Modal component removal
At the time of its creation, the original design for milestone [2. Tables from File Import](https://github.com/centerofci/mathesar/milestone/1) included a modal component to display the table creation controls as part of the process of adding a new table. However, after team discussion and intending to simplify, we decided to drop the modal component and favor incorporating controls at the page level and in the context of other tasks happening in parallel, such as file import.

# Scenarios
## User adds a new table from the sidebar
The way users add a new table remains unchanged. A new table is added by clicking on the add table button next to the tables list header.

<iframe style="border: 1px solid rgba(0, 0, 0, 0.1);" width="800" height="450" src="https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Fproto%2FUaf1ntcldzK2U41Jhw6vS2%2FMathesar-MVP%3Fpage-id%3D1825%253A9345%26node-id%3D1831%253A10912%26viewport%3D556%252C338%252C0.3983568251132965%26scaling%3Dcontain" allowfullscreen></iframe>

## User starts the add table process and decided on the table creation method
After the User starts the add table process, a new tab is displayed containing controls for selecting the table creation method. In the table toolbar area, a field exists to enter the table name. If left unchanged, it will default to a placeholder name, and it won't prevent the User from taking the following steps.

<iframe style="border: 1px solid rgba(0, 0, 0, 0.1);" width="800" height="450" src="https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Fproto%2FUaf1ntcldzK2U41Jhw6vS2%2FMathesar-MVP%3Fpage-id%3D1825%253A9345%26node-id%3D1825%253A9346%26viewport%3D556%252C338%252C0.3983568251132965%26scaling%3Dcontain" allowfullscreen></iframe>

### Table status
The system won't save the table until the empty table is created or the file import succeeds. While unsaved, the table tab and other navigational items representing the table should indicate the unsaved state.

### Schema Selection
Recent changes in the design might influence how schemas are presented within Mathesar. We assume that a single schema is being displayed, thus eliminating the requirement for a schema selector.

![](/assets/design/process/documents/design/table-creation-controls-spec/ksN9Z6d.png =200x)

## User completes table creation
Once the table creation process is over, the table name input is hidden while the table label remains. Clicking on the table label will show the input again.

<iframe style="border: 1px solid rgba(0, 0, 0, 0.1);" width="800" height="450" src="https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Fproto%2FUaf1ntcldzK2U41Jhw6vS2%2FMathesar-MVP%3Fpage-id%3D1825%253A9345%26node-id%3D1831%253A10494%26viewport%3D556%252C338%252C0.3983568251132965%26scaling%3Dcontain" allowfullscreen></iframe>