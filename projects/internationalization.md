---
title: Internationalization Implementation
description: 
published: true
date: 2023-05-04T11:00:15.207Z
tags: 
editor: markdown
dateCreated: 2023-03-15T20:52:51.896Z
---

- **Name**: Internationaliztion
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

The goal of this project is to enable Frontend and Backend codebase to support translations and create a translation strategy for all of the existing and future strings.

1. Write the technical spec for enabling Mathesar to support translations in the Frontend and Backend.
2. Get the spec reviewed and approved.
3. Implement the spec.
4. Test the implementation for just one string.
5. Write a doc for developers, outlining the approaches and best practices for making sure the new code written is translatable as per the spec.
6. Implement a linting rule to identify untranslated UI strings.
7. Write a doc outlining the workflow for sending the strings for translation, reviewing, and receiving the translations from a translator(non-technical person).
8. Publish documentation for volunteer translators, making it possible for community members to contribute to translations without very much technical knowledge.

## Scope

This project does not concern with translating the product into any particular language. It also does not concern either with translating or creating a translation strategy for the content inside the Mathesar repo in the form of Readmes or docs.

**Frontend**: Enable the frontend codeabse to support translations.
**Backend**: Enable backend codebase to support translations for the server side rendered pages and error messages that are shown to the users on UI as it is.
**Infrastructure**: Integration of a third party translation automation service like [Transifix](https://www.transifex.com/open-source/)

## Timeline

This project should take 3 weeks of frontend implementation effort and 1 week of backend implementation effort which can be done in parallel, excluding the time to finalize the technical approach.

|                                              | End Date   | Status |
| -------------------------------------------- | ---------- | ------ |
| Get tech spec approved                       | 2023-05-26 |
| FE implementation                            | 2023-06-16 |
| BE & Infra Work                              | 2023-06-16 |
| Developer documentation                      | 2023-06-23 |
| Guide getting strings translated             | 2023-06-23 |
| Contributing guide for volunteer translators | 2023-06-23 |

## Risks

The project timeline may change depending on the finalized technical approach.
