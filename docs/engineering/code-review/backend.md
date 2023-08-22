---
title: Backend Code Review
description: Guidelines for reviewing backend code
published: true
date: 2023-07-19T23:25:51.207Z
tags: 
editor: markdown
dateCreated: 2021-08-20T11:58:11.271Z
---

These are general guidelines to follow when reviewing backend code. Please feel free to add to them.

## Additional Reviewers
If you'd like a second opinion before merging the code, please tag another reviewer and ask them to also review the PR.

It's especially recommended to tag authors of specific features if the feature they built is being touched, or to tag (other) maintainers in case there are architectural changes to existing code or to support new features.

## Documentation
1. If there are any lines that are not immediately understandable to you, ask the author to add a comment explaining the line.
1. If you're not sure why the author chose a particular approach, or if there's some context on the pull request description that would be useful in the future, ask the author to add it as a comment to the code.

## Style
Linting should handle many style issues, but here's some to check manually:

1. Imports should be ordered in alphabetical order, with standard library imports first, third-party imports second, and local imports third.
1. All class attributes should be defined _before_ class methods.
1. Internal functions (not meant to be used outside the class or file) should be prefixed with an underscore (`_`).
1. Variable names should _not_ be reused within the same function.

## Testing
1. There should be tests for new functionality.
1. There should be tests for both failure and success cases (as applicable)
1. New functionality that applies to both the API and the database code should be tested in both places.

## User Experience
1. If there are any user-facing changes to the product that are not directly defined by the GitHub issue, please run them by Kriti.