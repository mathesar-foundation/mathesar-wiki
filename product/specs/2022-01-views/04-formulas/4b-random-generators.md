---
title: (b) Random Generators
description: 
published: true
date: 2022-02-23T01:43:47.593Z
tags: 
editor: markdown
dateCreated: 2022-02-23T01:43:47.593Z
---

These formulas generate random data.

# Random Number

**Data Type**: Double Precision
**Description**: Generates a random value in the range 0.0 <= x < 1.0
**Variables Accepted**: None
**Date Editable?**: No

## Implementation
The `random()` PostgreSQL function. [Docs](https://www.postgresql.org/docs/current/functions-math.html), see Table 9.6.

# Random UUID

**Data Type**: UUID
**Description**: Generates a random UUID
**Variables Accepted**: None
**Date Editable?**: No

## Implementation
The `gen_random_uuid()` PostgreSQL function. [Docs](https://www.postgresql.org/docs/current/functions-uuid.html).