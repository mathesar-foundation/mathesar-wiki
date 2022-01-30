---
title: 01. Assumptions
description: 
published: true
date: 2022-01-30T23:32:33.037Z
tags: 
editor: markdown
dateCreated: 2022-01-24T22:53:50.652Z
---

I'm making the following assumptions in the rest of the spec about how we want to work with Views in Mathesar.

- We **do not** need to support creating or editing Views based on every conceivable database query in Mathesar. We will be focusing on allowing common use cases.
- We **do** need to support viewing Views based on any conceivable database query correctly, even if they can't be edited. Users should be able to connect a database with existing Views to Mathesar and have those Views show up correctly.
- At the moment, we **only** care about the final output of the views. If a view uses a subquery, CTE, union, intersection, etc. internally, we will not be representing those to the user in the UI (unless they look at the underlying SQL query).
- We eventually want to allow users to create Views using SQL queries through the web interface, but this will not be prioritized for the alpha release.