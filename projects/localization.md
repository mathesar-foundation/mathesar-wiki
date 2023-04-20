---
title: Localization Project
description:
published: true
date: 2023-03-15T00:00:00.000Z
tags:
editor: markdown
dateCreated: 2023-03-15T00:00:00.000Z
---

- **Name**: Localization
- **Status**: In-Review

## Team

**Project Owner:** Rajat

|               | Workers | Reviewers |
| ------------- | ------- | --------- |
| **UX design** | Rajat   | Ghislaine |
| **Front end** | Rajat   | Sean      |
| **Back end**  | Mukesh  | _TODO_    |

## Problem

As per the current architecture of Mathesar, it only works in the English language. It is not enabled to be translated into other languages, which reduces the reach of the product. Users whose native language is not English are not able to use the product.

## Solution

Localization in the context of Mathesar means translations.

The goal of this project is to enable Frontend and Backend codebase to support translations and create a translation strategy for all of the existing and future strings.

1. Write the technical spec for enabling Mathesar to support translations in the Frontend and Backend.
2. Get the spec reviewed and approved.
3. Implement the spec.
4. Test the implementation for just one string.
5. Write a doc for developers, outlining the approaches and best practices for making sure the new code written is translatable as per the spec.
6. Implement a linting rule to identify untranslated UI strings.
7. Write a doc outlining the workflow for sending the strings for translation, reviewing, and receiving the translations from a translator(non-technical person).
8. Publish documentation for volunteer translators, making it possible for community members to contribute to translations without very much technical knowledge.

NOTE:
This project does not concern with translating the product into any particular language. It also does not concern either with translating or creating a translation strategy for the content inside the Mathesar repo in the form of Readmes or docs.

## Timeline

This project should take 3 weeks of frontend implementation effort and 1 week of backend implementation effort which can be done in parallel, excluding the time to finalize the technical approach.

_A detailed timeline can be added once the proposal is approved and a start date is finalized._

## Risks

The project timeline may change depending on the finalized technical approach.
