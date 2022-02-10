---
title: Implement Advanced SQL Query Builder
description: 
published: true
date: 2022-02-10T15:59:01.226Z
tags: 
editor: markdown
dateCreated: 2022-02-09T21:52:46.522Z
---

## The Problem
We are building a visual query builder into Mathesar to help the user find answers to questions using their data and to create [Views](/en/product/concepts/views). To make the visual query builder easy to use, we needed to make a bunch of assumptions that limits the types of queries that can be produced. 

To support the full range of queries that can be written using SQL, we should allow advanced users to write SQL queries.

## Classification
- **Difficulty**: Medium
- **Skills needed**: Python, JavaScript, frontend frameworks
- **Length**: Long (~350 hours)

## Tasks
- Work with the Mathesar design team to figure out a design for how to integrate the SQL editor into the product.
- Write a technical spec for how the SQL editor will work from a code perspective.
- Implement the backend necessary to process input from the SQL editor.
- Implement the SQL editor in the frontend.

## Expected Outcome
By the end of this project, we expect that the query builder web interface will have an option for advanced users to use SQL to build queries. This interface should be easy to use, including features like syntax highlighting and autocomplete.

## Application Tips
- Please provide as much technical detail as you can on how this will integrate into Mathesar's code. API schemas, libraries you plan to use, etc.
- Don't reinvent the wheel - use external libraries for the functionality where you can.
- It's helpful to start from the experience that you'd like the end-user to have and work backwards.

## Resources
- [Views "Concepts" page](/en/product/concepts/views)
- ["Views in Mathesar" product spec](/en/product/specs/2022-01-views)
- [Code Mirror text editor library](https://codemirror.net/)

## Mentors
**Primary Mentor**: Kriti
**Secondary Mentor(s)**: TBD