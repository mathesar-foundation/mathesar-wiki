---
title: Mathesar Data Types
description: Mapping Mathesar data types to PostgreSQL types
published: true
date: 2022-01-05T22:22:42.669Z
tags: 
editor: markdown
dateCreated: 2022-01-05T22:22:42.669Z
---

Please see the ["Data Types" product concept page](/product/concepts/data-types) for more information about the idea behind Mathesar data types (a.k.a. "Mathesar types" for brevity).

## Goals
The main goal of the Mathesar type system is to create a better user experience for non-technical users. We aim to do this by:
- **Making data types understood in simple, non-technical terms.**
  - e.g. users should not need to know or think about what a `DOUBLE PRECISION` is in order to set their column to accept decimal numbers.
- **Reducing cognitive load while picking a data type.**
  - A user should not need to look through every single data type to figure out how to set up their column.
  - e.g. if a user knows their data is numeric, they shouldn't have to look through every data type to figure out which ones are numeric and how they're different.

## Implementation
A Mathesar type can be thought of as a set of one or more PostgreSQL data types. Every PostgreSQL type should be mapped to exactly one Mathesar type, but a Mathesar type can be mapped to many PostgreSQL types.

We will need to extend the Mathesar type system over time as we support more data types. When doing so, we should follow these criteria for what PostgreSQL types can be grouped into a single Mathesar type:
- TBD


