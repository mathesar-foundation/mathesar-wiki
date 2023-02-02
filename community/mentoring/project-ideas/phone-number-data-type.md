---
title: Phone Number data type
description: 
published: true
date: 2023-02-02T23:06:49.514Z
tags: 
editor: markdown
dateCreated: 2023-02-02T20:18:17.304Z
---

> This is a draft.
{.is-warning}

## Classification
- **Difficulty**: Medium
- **Skills needed**: Python, SQL, JavaScript
- **Skills that could be helpful**: Django, SQLAlchemy, Svelte, TypeScript
- **Length**: Medium (~175 hours) or Long (~350 hours) depending on your experience

## The Problem
- The Mathesar UI allows users to configure the column types for their data, choosing between types like "Number", "Date", "Text", and so on. All data entered into the column is then validated against the rules according to the type. So for example, in a Number column, Mathesar will allow input of `2` but will reject input of `hello`.
- We would to provide "Phone Number" as an available type, but Mathesar does not support this functionality.

## Feature Description
- We should have a custom Postgres data type for "Phone Number". Please refer to our email & URL implementations.
- Users should be able to set a column's data type to "Phone Number".
- Data with the "Phone Number" data type set should be automatically formatted in a pretty way where possible.
	 - e.g. 10-digit US/Canada phone numbers should be formatted as (XXX) XXX-XXXX
- Phone numbers that cannot be automatically formatted should be formatted as text    
- Phone numbers should be able to be grouped by country code or area code

## Architectural Problems
We need to figure out
- how to structure the Postgres type.
- how to parse and store country and area codes at the DB level so that they can be used in grouping.
- the logic for identifying columns with phone number data when data is imported.
- how to format phone numbers in the frontend. Using an existing library would be preferable to implementing our own parsing and formatting.

## Tasks
1. Implement the Phone Number database type
2. Integrate the Phone Number data type with our data type inference logic.
3. Integrate the Phone Number data type with our existing APIs.
4. Build custom grouping functions for area code and country code grouping.
5. Integrate the grouping functions with our API.
6. Research available phone number formatting libraries and present your findings to the Mathesar front end team for consideration. Then select the 3rd party library, in collaboration with the front end team.
7. Implement phone number formatting in the frontend.

## Expected Outcome
- Users can set columns to the Phone Number data type.
- Phone numbers should be correctly formatted in table cells, explorations, default value inputs, filter inputs, and record selector inputs.
- Users can group by country code & area code.

## Application Tips
- Demonstrate proficiency with the required skills.
- Present some preliminary research into phone number formatting.
- Demonstrate an understanding of how Mathesar data types are implemented in the backend and APIs.

## Out of Scope
We shouldn't implement any custom logic for validating phone numbers since phone numbers can be quite complex.

## Resources
- [Falsehoods Programmers Believe About Phone Numbers](https://github.com/google/libphonenumber/blob/master/FALSEHOODS.md)
- Airtable has a phone number column data type, feel free to play around with it.

## Mentors
**Primary Mentor**: TBD
**Secondary Mentor(s)**: TBD
