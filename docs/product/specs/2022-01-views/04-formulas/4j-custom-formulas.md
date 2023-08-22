---
title: (j) Custom Formulas
description: 
published: true
date: 2023-07-19T23:48:40.672Z
tags: 
editor: markdown
dateCreated: 2022-03-02T00:30:44.664Z
---

Custom formulas provide a more flexible interface to let users build their own formulas. Users can use:

- Column references
- Any of our pre-created formulas
- Logical operators (`and`, `or` , `not`)
- Mathematical operators (`+`, `-`, `*`, `/`, `%`, `!`, `^`, etc.)
- Comparison operators (`>`, `<`, `>=`, `<=`, `=`, `!=`)

## Interface Requirements
We should provide a textual interface for users to enter custom formulas. This should support:
- Autocomplete for column references based on the available columns.
- Autocomplete for our pre-created formulas.
    - Once the user has started entering a formula, we should support autocomplete or dropdowns for formula options.
    - For freeform inputs, we should show placeholders.
- Some sort of help or autocomplete for operators.