---
title: Lookup Field Component Specs
description: 
published: true
date: 2021-06-29T18:28:42.400Z
tags: 
editor: markdown
dateCreated: 2021-06-17T07:13:36.093Z
---

# Context
The lookup field component was specified as part of the design for ['Add Table from Import'](/design/specs/table-import). Based on discussions held after the design review of the document, we determined the need to provide further detail on how users will use this component and what steps they must follow to complete the following tasks:

- Add a table to an existing schema
- Add a table to a new schema

# Scenario: Selecting a Schema

![](/assets/design/process/documents/lookup-field-component-specs/Cr6i2pU.png =320x)

The lookup field component allows the user to choose a value from a list to perform a specific action. A common task within Mathesar will be the creation of database objects such as tables and views. These objects belong to a schema, which is the structure of a database.

## List Values
The available values, in this case, are all the schemas associated with the users' Mathesar account, where the user has read access to them. Because write access is required to create a table within the schema, we will not allow users to select schemas for which they have insufficient privileges.

## Allowing Multiple Values
Our current use case doesn't contain instances where a lookup field might require multiple value selection. For this iteration, we will focus on the selection of a single value.


---

## Alternative #1

### Selecting from Existing Values
For a schema that already exists, the user will have to click on the desired schema to select it.

![](/assets/design/process/documents/lookup-field-component-specs/jRBFNUO.png)

In some cases, users might see an item listed but can't select it. This state could be due to insufficient privileges or other factors. In that case, the item will be grayed out and non-interactive.

![](/assets/design/process/documents/lookup-field-component-specs/eej36bN.png =240x)

### Add a New Schema and Select It
In some cases, a user might want to add the table to a new schema. To avoid leaving this view and restarting the process, the user can add it from the lookup menu.

![](/assets/design/process/documents/lookup-field-component-specs/aP3hoGa.png)

#### Pros
- Easier to transform into multi-select in the future as space can be handled better because 'Find a schema' is separated from 'Selected Schemas'
- New schema action is more deliberate and obvious

#### Cons
- Additional step to add a new schema

## Alternative #2

### Selecting from Existing Values

- Retrieve all schemas by clicking on the field

![](/assets/design/process/documents/lookup-field-component-specs/dKPcSq3.png =240x)

- Type to find existing schemas

![](/assets/design/process/documents/lookup-field-component-specs/hdL78gs.png =240x)

### Add a New Schema and Select It
- Type to create a new schema if no matches found

![](/assets/design/process/documents/lookup-field-component-specs/b92JFFc.png =240x)

#### Pros
- Fewer steps overall. User can both refine the list of schemas or create a new one without requiring additional steps

#### Cons
- Without a descriptive text, the user might not understand that they can create a new schema

# Review Summary

## Choosing Alternative #2
Alternative #2 is preferred as it is more ARIA friendly. 

Clicking the input field to reveal full list of options:

![](/assets/design/process/documents/lookup-field-component-specs/rygEN__i_.png =300x)

Typing the name of the schema to retrieve matching options:

![](/assets/design/process/documents/lookup-field-component-specs/BJuBNu_su.png =300x)


## Discarding 'Add Schema' functionality from the lookup field for now
Some concerns exist around the need for confirmation steps and system feedback requirements to prevent errors during schema creation. Contemplating these aspects of the user experience in a narrow context is likely to result in a less than optimal design for the use cases we are discussing.

**Concerns mentioned during the review:**
- Risk of typos failing to find schema and inadvertently create a new schema

**Ideas to improve the experience:**
- Allowing users to extend current schema names to create new ones 


## Simplifying Schema and Table Creation
Reducing the steps users need to take to create a schema or table should be our optimization focus. Some parts of our experience rely on overlay components (modals) to collect the information necessary for the creation of database objects like tables and schemas. We want to simplify these components to streamline the experience in future designs. For example, we integrate table creation details into tasks that require them, such as importing a new table from a file.
