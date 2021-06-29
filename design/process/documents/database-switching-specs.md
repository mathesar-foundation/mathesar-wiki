# Database Switching Specs
## Context
Users might have multiple databases, and they need to switch between them as necessary, in a seamless manner, without worrying about the current status of open tables or views.

## Scenarios

### Default Database
When opening Mathesar, the default database is the one that was most recently open. If this database no longer exists, then Mathesar should show an error message and direct the user to open a different database or troubleshoot the connection. 

<iframe style="border: 1px solid rgba(0, 0, 0, 0.1);" width="800" height="450" src="https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Fproto%2FUaf1ntcldzK2U41Jhw6vS2%2FMathesar-MVP%3Fpage-id%3D1207%253A0%26node-id%3D1706%253A13775%26scaling%3Dscale-down-width" allowfullscreen></iframe>

### Open Single Schema vs. Multiple Schemas
Having users create multiple related tables inside a schema, rather than having their related data split into different schemas, is desired for our intended use cases. It also reduces complexity, and it's easier to manage. 
For this reason, a navigation component is proposed so that the system can open only one schema at a time. 

<iframe style="border: 1px solid rgba(0, 0, 0, 0.1);" width="800" height="450" src="https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Fproto%2FUaf1ntcldzK2U41Jhw6vS2%2FMathesar-MVP%3Fpage-id%3D1207%253A0%26node-id%3D1212%253A0%26scaling%3Dscale-down-width" allowfullscreen></iframe>

### Errors Preventing Schema Changes to be Saved
If a table within the open schema has unsaved changes, a warning will inform the user and provide the options to discard them and leave or stay and fix them.

### Persist Tabs for Schemas
The status of tabs should be persistent when reopening a schema.

![](/assets/design/process/documents/database-switching-specs/qMsmiZo.png =400x)

## Interactions
### Indicating Tables with Errors
If a table contains errors, the interface should help identify those by adding a visual indicator to the corresponding tab.

![](/assets/design/process/documents/database-switching-specs/mCwwg8S.png =400x)

### Showing Recent Objects 
A list of recent objects is available to help users access their most frequently used objects, such as tables and views.

![](/assets/design/process/documents/database-switching-specs/0vScHwP.png =240x)


## User Interface

### Database Navigation Menu
The database navigation menu provides a context for the various databases and schemas that users can access through Mathesar.
From this menu, the user can search through all databases and navigate to schemas.

![](/assets/design/process/documents/database-switching-specs/JGIqCOi.png)



