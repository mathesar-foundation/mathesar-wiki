---
title: Multiple Records Associated with a Single Record
description: 
published: true
date: 2021-10-30T04:28:30.315Z
tags: 
editor: markdown
dateCreated: 2021-09-15T10:46:15.425Z
---

> This spec is outdated and should not be followed.
{.is-danger}

# Context
When setting up a relational database, users will want to organize their data to avoid duplication and maintain the integrity of their data. Therefore relationships need to be created between tables, for example, to relate 'tracks' to 'albums' or 'albums' to 'artists.' In cases where records are multiple, users will rely on features to help them summarize or quantify those relationships.

By introducing many-to-many relationships, users accustomed to the spreadsheet model will have to understand more advanced database concepts like junction tables, primary and foreign keys, etc. This increase in complexity will make user errors more likely, so the design needs to address how the features are introduced and how users learn those concepts. 

# Prototype
[Prototype for Associating Multiple Records](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?page-id=5192%3A55284&node-id=5279%3A55303&viewport=324%2C48%2C0.66&scaling=contain&starting-point-node-id=5279%3A55303)

# User Experience

## Scenarios
A user adds a 'related table' column that allows multiple records to be linked.
From a table view, a new or existing column can be linked to a table. By default, the column will allow a single record to be linked unless the 'Allow Multiple' option is checked. 
When the user checks the 'Allow Multiple' option, a text is displayed explaining the system will create an additional table to map related keys for both tables.

### A user edits a multiple record field to add or remove records.
Users can edit a multiple records field to add or remove records from the records lookup menu. Records that are already selected will be marked as such, and the user can click again to deselect.
The user can also remove a record reference by clicking on the 'X' icon when the field is active.

### A user learns about junction or join tables and understands why they must be created.
When a user sets a field to 'Allow Multiple Records,' the system creates a table to map both sets of keys. This table looks like any other table. However, a naming convention is applied so that users can identify them.

### A user creates a view from a table that contains columns with multiple records.
When a view is added from a table that contains a column with multiple records, that same column is ported over to the view. The user can then add a column to summarize the records on that field.

### A user adds a summary column from a view.
When rows have fields with multiple associated records, a user might want to summarize any related table's fields. In that case, they can choose a summary type from the column selection menu. The default setting is 'Values,' which will display a comma-separated list of the values. 

## Future Considerations
In the future, more summary options will be available, including formulas. Users will require further instructions or examples to apply them correctly. Filters will also enable the creation of columns that limit the summarized records based on set criteria. For example, a user might want to create a column only to summarize award-winning releases or tracks with featured artists. There are hints to these elements in this prototype, but they will be specced in a future milestone.