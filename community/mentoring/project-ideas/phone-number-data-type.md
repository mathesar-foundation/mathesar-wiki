---
title: Phone Number data type
description: 
published: true
date: 2023-02-02T20:18:17.304Z
tags: 
editor: markdown
dateCreated: 2023-02-02T20:18:17.304Z
---

> This is a draft.
{.is-warning}

## Classification
- **Difficulty**: Medium
- **Skills needed**: Python, SQL
- **Skills that could be helpful**: Django, SQLAlchemy, JavaScript, Svelte, TypeScript
- **Length**: 
  - Medium (~175 hours) if you're only working on the backend
  - Long (~350 hours) if you're working on both the backend and the frontend

## The Problem
- The Mathesar UI allows users to configure the column types for their data, choosing between types like "Number", "Date", "Text", and so on. All data entered into the column is then validated against the rules according to the type. So for example, in a Number column, Mathesar will allow input of `2` but will reject input of `hello`.
- We would to provide "Phone Number" as an available type, but Mathesar does not support this functionality.

## Feature Description
- We should have a custom Postgres data type for "Phone Number". Please refer to our email & URL p
- Users should be able to set a column's data type to "Phone Number".
- Data with the "Phone Number" data type set should be automatically formatted in a pretty way.
	 - e.g. 10-digit US/Canada phone numbers should be formatted as (XXX) XXX-XXXX
- 

*How this feature will work.*

## UX Design Problems
*Describe the UX design problems we need to solve as part of implementing this feature.*

*Remove this section if there's no UX design needed. Or replace with another section e.g. Architectural Problems if the problems are best described using another label.*

## Tasks
*A list of tasks that the intern is expected to complete as part of their work. Be specific about research, code, etc.*

## Expected Outcome
*Describe the expected outcome of the project.*

## Application Tips
*Tips for writing a successful proposal to complete this project. This could include what specific questions to answer or what details could help the application stand out.*

## Out of Scope
*Describe any tasks that are out of scope.*

## Resources
- [Falsehoods Programmers Believe About Phone Numbers](https://github.com/google/libphonenumber/blob/master/FALSEHOODS.md)

## Mentors
**Primary Mentor**: *Person*
**Secondary Mentor(s)**: *List of people*
