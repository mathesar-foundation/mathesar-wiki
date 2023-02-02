---
title: "JSON Editor" project idea
description: 
published: true
date: 2023-02-02T19:59:42.747Z
tags: 
editor: markdown
dateCreated: 2023-02-02T19:05:44.259Z
---

## Classification

- **Difficulty**: *Medium* or *High*, depending on experience
- **Skills needed**: HTML, CSS, TypeScript, JavaScript, Svelte, UX design
- **Length**:  *Medium (~175 hours)* or *Long (~350 hours)*, depending on experience

## The Problem

- The Mathesar UI allows users to configure the column types for their data, choosing between types like "Number", "Date", "Text", and so on. All data entered into the column is then validated against the rules according to the type. So for example, in a Number column, Mathesar will allow input of `2` but will reject input of `hello`.

- Mathesar currently has *partial* support for two new types:

    - **JSON Object** columns, which should allow user input such as:
    
        ```json
        {
          "foo": "bar",
          "baz": { "bat": [ 1, 2, 3] }
        }
        ```

    - **JSON Array** columns, which should allow user input such as:
    
        ```json
        [
          { "foo": "bar", "baz": 0 },
          { "bat": null }
        ]
        ```

    The goal with these types is to allow users to enter JSON data into Mathesar.

- The backend and API work is already complete for these two types. The front end work has begun but needs to be finished. The front end currently allows users to convert Text columns to JSON Object and JSON Array. And the front end is able to displays JSON values already stored in the database. But...

- **The UI does not yet allow users to *input* JSON values into table cells.** There are also some other contexts which require user-entry of JSON values. We need a dedicated JSON editor for the user to input JSON.

## Feature Description

The JSON editor should meet all the following requirements:

- It should provide syntax highlighting, and be compatible with dark mode too.
- It should give users feedback on when their entry is not valid JSON.
- It should give users feedback on when their entry is valid JSON but is not valid for the column type. For example, the JSON Object column should not accept a JSON Array, and neither of our JSON column types should accept JSON values like `1`.
- It should display server errors 
- It should load all its resources (e.g. JavaScript, static assets) asynchronously so that the initial page load is not degraded after adding this feature.
- It should provide a graceful experience for the user while loading.
- It should be easy to use.
- Its 3rd party libraries should be compatible with Mathesar's license (GPLv3).

## UX Design Problems

- We have the following contexts in which we may want to accept entry of JSON values
    - A table cell
    - An input field on a record page
    - An input to set a default value for a column
    - An input for a filter condition
    - An input to filter records within the record selector
- In each of the contexts above, we need to answer the following design questions:
    - Do we need a full-fledged JSON editor for the given context, or will a simple text input suffice?
    - Can the user choose between a simple text input and a larger JSON editor? If so, how?
    - How does the user open the JSON editor?
    - Where does the JSON editor display after opening?
    - How does the user submit their value once they are done entering their JSON?
    - How does the user close the JSON editor without submitting a value?
    - How do we indicate invalid JSON?
    - When the user's input is valid JSON but invalid for the column type, should we perform that validation on the front end or the back end? How should these errors display?
    - Where should we display general server errors that we get after the user has saved their value? (e.g. value violates a unique constraint)
    - How does the user set the entire value to `NULL`? Do we need to make a distinction between a `null` JSON value and a `NULL` PostgreSQL value?

## Tasks

1. Research available 3rd party libraries for accepting JSON input and present your findings to the Mathesar front end team for consideration. Then select the 3rd party library, in collaboration with the front end team.
1. Write a UX design document describing the manner in which the JSON editor will be incorporated into Mathesar's UI. Then work with the front end team and product designer to solidify the UX design.
1. Get the JSON editor to load an empty document asynchronously within the desired UI location.
1. Get the JSON editor to load and display the cell contents, as fetched from the API.
1. Get the JSON editor to save cell values via the API.
1. Handle client-side error validation for cases where the input is valid JSON but invalid for the column type.
1. Handle server-side errors after saving

## Expected Outcome

Users can easily enter JSON data into cells within JSON Object and JSON Array columns.

## Application Tips

- Demonstrate proficiency with the required skills.
- Present some preliminary research into 3rd party JSON editors.
- Share some of your initial ideas about how best to integrate the JSON editor into the existing Mathesar UI.

## Out of scope

These are some features we may consider adding in the future, but which are out of scope for this project

- More complex per-column validation of the JSON schema, beyond it being an object or array
- More ways to filter on JSON columns

## Mentors

- **Primary Mentor**: Sean Colsen
- **Secondary Mentor(s)**: Pavish Kumar Ramani Gopal

