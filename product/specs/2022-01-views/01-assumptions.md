---
title: 01. Assumptions and Limitations
description: 
published: true
date: 2022-03-08T21:47:02.288Z
tags: 
editor: markdown
dateCreated: 2022-01-24T22:53:50.652Z
---

Although Queries and Views represent underlying database concepts, we will only be supporting building a subset of possible database queries in the first version of Mathesar. Our goal is to ship a proof of concept that demonstrates common use cases that might be used for an [Inventory Use Case](/en/design/exploration/use-cases/inventory-use-case).

> Please note that the assumptions and limitations outlined in this page are **only for the alpha release** of Mathesar. We will reevaluate these assumptions after our first release.
{.is-info}


## Viewing Views
We **will** support viewing Views based on any conceivable database query correctly, even if they can't be edited. Users should be able to connect a database with existing Views to Mathesar and have those Views show up correctly.

If the query powering the view is not something we can break down into the concepts in the rest of this spec, we will only show the query and not allow the view's query to be edited.

## Building Queries
- We **will not** support creating or editing Views based on every conceivable database query in Mathesar.
- We **will not** support using Views in database queries for the first version of the product. We will only support tables and other columns in the query.
- We will **only** support building queries using foreign key relationships to join tables. We eventually want to do "best guess" natural joins but this is not planned for the alpha release.
- At the moment, we **only** care about the final output of the views. If a view uses a subquery, CTE, union, intersection, etc. internally, we will not be representing those to the user in the UI (unless they look at the underlying SQL query).
- We will **only** be allowing users to build queries using a guided web interface. We eventually want to allow users to create Views using textual SQL queries, but this is not planned for the alpha release.