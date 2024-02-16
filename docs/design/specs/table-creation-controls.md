# Table Creation Controls (discard modal update)

## Context

### Modal component removal
At the time of its creation, the original design for milestone [2. Tables from File Import](https://github.com/mathesar-foundation/mathesar/milestone/1) included a modal component to display the table creation controls as part of the process of adding a new table. However, after team discussion and intending to simplify, we decided to drop the modal component and favor incorporating controls at the page level and in the context of other tasks happening in parallel, such as file import.

## Prototype
['Table Creation Controls' Prototype](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?page-id=1825%3A9345&node-id=1831%3A10912&viewport=570%2C566%2C0.10280735790729523&scaling=min-zoom)

## Scenarios
### User adds a new table from the sidebar
The way users add a new table remains unchanged. A new table is added by clicking on the add table button next to the tables list header.

### User starts the add table process and decided on the table creation method
After the user starts the add table process, a new tab is displayed containing controls for selecting the table creation method. In the table toolbar area, a field exists to enter the table name. If left unchanged, it will default to a placeholder name, and it won't prevent the user from taking the following steps.

#### Table status
The system won't save the table until the empty table is created or the file import succeeds. While unsaved, the table tab and other navigational items representing the table should indicate the unsaved state.

#### Schema Selection
Recent changes in the design might influence how schemas are presented within Mathesar. We assume that a single schema is being displayed, thus eliminating the requirement for a schema selector.

![](/assets/design/specs/table-creation-controls/ksN9Z6d.png =200x)

### User completes table creation
Once the table creation process is over, the table name input is hidden while the table label remains. Clicking on the table label will show the input again.

## Review Notes
### Fixed Headers for Overflowing Content
Controls that are located in headers must remain accessible to users at all times. When a list of items grows more extensive than the space available, the headers must remain fixed, and the list of items will scroll vertically.
