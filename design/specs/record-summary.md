---
title: Record Summary
description: 
published: true
date: 2022-07-18T21:06:26.165Z
tags: 
editor: markdown
dateCreated: 2022-07-18T17:49:31.605Z
---

## Context 

Record summaries are strings that represent a record's data. They are specified by users and can include variable values from the record's fields, or include symbols and text characters.

## Usage throughout the product

Wherever we want to represent one record, we use the record summary. Here is a non-exhaustive list of some places in the product where record summaries will be used.

- In FK cells, to represent the records that are linked via a foreign key.

    ![image](/assets/design/specs/record-summary/179570423-e41b54e2-ebd7-4e73-acb2-8337ec6bb2db.png)

- In the Record Page, to serve as both a header and a representation of linked records.

    ![image](/assets/design/specs/record-summary/179571077-3ab610ff-d0ca-4d70-b840-e760dd567edb.png)

- In group header rows, when the table page is grouped by a FK column.

- In the input within a filter condition that filters on a FK column.

- In the input when setting a default value for a FK column.

## Rendering one record summary

## Template

1. The backend provides a record summary **template** for each table from the `tables` API. This is a string such as `{78}` that specifies the ids of the columns to be used to render the record summary.

1. The template can include multiple columns, and other characters too, such as `{1}-{2}`, which will render two columns separated by a dash.

1. By default, the backend dynamically generate the template such that it includes only the first non-PK column and no other characters.

1. The user may customize the record summary template, in which case the customized template will be stored at the table level (for all users).

## Examples and edge cases

Say We are rendering a summary for a row having the following data (which maps column ids to cell values):

```json
{
    "101": 1,
    "102": "Foo"
}
```

- If table's template is `{102}`, then we render `Foo`

- If table's template is `{999}`, then we render `{999}` (because there is no column in the table having an id of 999).

- If table's template is `{101}: {102}`, then we render `1: Foo`

- Let's pretend that (for some weird reason), _we'd like to_ render `{101}: Foo` (keeping that `{101}` text static across all rows). In this case we are actually unable to configure the record summary template to render such a value because **the templating system has no escaping mechanism**. This is a design limitation made for the sake of simplicity and ease of implementation.

## Transitive summaries

When a foreign key column is used within the record summary template, the text used when rendering the record summary is taken from the rendered record summary for that record.

## Customizing the record summary template

Here's an example where a user customizes the Authors template to show the author's first name and last name separated by a space.

### From the Authors table

1. The user navigates to the Authors table page.

1. Within the table inspector, the "Table" pane contains a section titled "Record Summary" below the "Properties" section and expanded by default. Below is a mockup of hhe UI in that section:

    ![image](https://user-images.githubusercontent.com/42411/195416813-cd6a7d4a-d8f9-4693-ad34-ff0fb0b8dc7e.png)

1. The "Preview" area shows the record summary for the first record from the table as displayed with the current sorting/filtering/grouping/pagination. If the table shows no rows, then the "Preview" area will be absent.

1. When the Template area contains three inputs: (1) a "Customization" radio button fieldset, (2) a "column inserter" select element, and (3) a "template value" text input.

1. The "column inserter" and "template value" fields are only displayed when "Customization" is set to "Default".

1. The Cancel/Save buttons are only displayed when the user has modified the form since its last save. The buttons disappear after saving.

1. As the user customizes the "template value" contents, the preview updates immediately, allowing the user to inspect their changes before applying them.

1. The "template value" input is a plain text input, and offers no special syntax highlighting or means of differentiating a valid column token from an invalid one.

1. The "column inserter" is a select element which displays all columns directly in the table as options. Upon selecting a column, the token for that column (e.g. `{First Name}`) is appended to the existing text within the "template value" input and the "template value" input is programmatically focused, allowing the user to continue typing.

1. To remove a column, the user must edit the "template value" and manually delete all the characters which comprise the column token.

1. When saving, the front end replaces column tokens like `{First Name}` with their corresponding column ids (e.g. `{78}`) before submitting the API request to persist the template value. Likewise, when populating the initial value for the "template value" input, the front end performs the reverse replacement, substituting column ids for their respective names.

    This design introduces an _additional_ limitation with regard to escaping which only applies to the UI -- there is no way to use the UI to configure the template that renders `{First Name}: Stephanie {Last Name}: Davis` because there is no way to to escape the column name (in addition to the column id as described above).

### From the Publications table

1. The user navigates to the Publications table page.

1. The user selects a cell within the "Author" column.

1. Within the table inspector, the "Column" pane contains a section titled "_Authors_ Record Summary" which presents all the same UI described above.

1. The values for the preview are taken from the _distinct_ FK cell values within the "Author" column.


