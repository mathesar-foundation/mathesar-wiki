---
title: Dynamic Defaults Proto-Spec
description: 
published: true
date: 2023-05-11T14:42:24.432Z
tags: 
editor: markdown
dateCreated: 2022-09-15T16:50:41.358Z
---

## Problem

We are considering implementing Dynamic Defaults as it increases the usability of adding new records.

For the purposes of the demo we need the following defaults

- Current date and time
    - `NOW()`
- Current date and time + a specific duration (e.g. 14 days)
    - `NOW() + '2 weeks'::INTERVAL`

The dynamic default options will depend on the field's data type.

We should consider implementing dynamic defaults using the same formulas that we plan to implement in the future


## Proposed User Flow
- User selects a column
- The inspector panel displays the properties for that column
- User toggles the "Default Value" option
- The user selects from a list of preset options

![upload_ebe944f590f61b67ea9a5646d45668a5.png](/assets/product/specs/dynamic-defaults-proto/upload_ebe944f590f61b67ea9a5646d45668a5.png)

Formulas to use from [our Formulas](https://wiki.mathesar.org/en/product/specs/2022-01-views/04-formulas/4f-datetime-formulas)

- Current date and time: "Current date & time" formula
- Current date and time + duration: "Add Duration to Date" formula
- A specific date and time: static default (not dynamic)
    - show date time picker