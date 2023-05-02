---
title: List Data Type - Project Draft 
description: Draft for defining the list data type implementation project. 
published: false
date: 2023-05-02T21:44:56.744Z
tags: 
editor: markdown
dateCreated: 2023-05-02T21:44:56.744Z
---

> This project is ridiculous on purpose. We are not doing this.
{.is-info}

**Name**: Adding support for list data type in Mathesar
**Status**: Draft 
**Theme**: List data type
> Options for status:
> **Draft**: The owner is still writing up the project.
> **In review**: The project has been written up, but hasn't been approved yet.
> **Approved**: The project has been approved, but work hasn't started yet.
> **In progress**: Work on the project has started.
> **Complete**: The project is over.
{.is-info}

> **Theme** is the broader goal or theme associated with the project.
{.is-info}

## Team
> We probably don't need to be this detailed for everything; this is just to show the range of options.
{.is-info}

| Role | Assignee | Notes |
|-|-|-|
| **Owner** | Kriti | |
| **Approver (project plan)** | Kriti | *Needs to approve project plan* |
| **Approver (product)** | Kriti | *Needs to approve product spec and design* |
| **Approver (frontend)** | Pavish, Sean | *Needs to approve frontend spec* |
| **Approver (backend)** | Mukesh, Brent | *Needs to approve backend spec* |
| **Contributor (requirements)** | Kriti | *Creates product spec, requirements, GitHub issues* |
| **Contributor (design)** | Ghislaine | *Creates designs* |
| **Contributor (backend)** | Dom | *Creates backend specs and implements backend* |
| **Contributor (frontend)** | Rajat | *Creates frontend specs and implements frontend* |
| **Contributor (backend review)** | Mukesh | *Reviews backend code* |
| **Contributor (frontend review)** | Pavish | *Reviews frontend code* |

## Problem
The Mathesar UI allows users to configure the column types for their data, choosing between types like "Number", "Date", "Text", and so on. All data entered into the column is then validated against the rules according to the type. So for example, in a Number column, Mathesar will allow input of `2` but will reject input of `hello`.

So far, we've been assuming that users will only store a single point of data in any given table cell. However, PostgreSQL supports the ability to store an array instead of a single point of data, and we'd like to support that.

We already have support for arrays in explorations (and the Data Explorer), but those are read-only. This project is for adding support for lists to tables.

## Solution
### Backend
1. Implement the List database type
1. Integrate the List data type with our data type inference logic.
1. Integrate the List data type with our existing APIs.
1. Build custom grouping functions for number of list items
1. Build custom filtering functions for lists
1. Integrate the filtering and grouping function with our API.
1. Figure out how to identify unsupported arrays in the API so that the frontend shows them as text.

### Frontend
1. Write a UX design document describing how lists will be edited. Then work with the front end team and product designer to solidify the UX design.
1. Implement the list viewing and editing behavior.
1. Ensure filtering and grouping works well.

- Investigate pizza companies with good APIs.
- Collect address information from users.
- Figure out how to store pizza company API keys in config.
- Check if address can be delivered to using API.
- Figure out what a default pizza should be (e.g. cheese pizza)
- If yes, add "Order Pizza NOW!!!" button to UI.
- When user presses button, order default pizza.

To simplify implementation, we are not going to allow users to customize their pizza yet.

## Risks
- Mathesar may be connected to PostgreSQL databases that have columns with arrays of non-supported data types (e.g.: geometric like polygons) or multi-dimensional arrays. We need a way to let the frontend know that those kinds of lists aren't supported. Should we show them as *"other"* in the UI?


## Resources
> This section collects project related resources. It's expected that there might not be anything here until the project plan is approved, and this section will grow over the project's timeframe.
{.is-info}

- **Issues**: [GitHub meta issue]()
- **Wiki pages**:
  - [Product spec]()
  - [Backend spec]()
  - [Frontend spec]()  

## Timeline
This project should take **5 weeks**.

> Please adjust as needed depending on the steps for the project.
{.is-info}

| Date | Outcome |
| - | - |
| 2023-03-01 | Work starts | 
| 2023-03-08 | Implementation spec complete | 
| 2023-03-15 | Implementation spec approved | 
| 2023-03-22 | Design work complete |
| 2023-03-27 | Backend work complete |
| 2023-04-05 | Frontend work complete |
