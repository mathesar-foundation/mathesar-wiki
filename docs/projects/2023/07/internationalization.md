# Internationalization Implementation

- **Name**: Internationaliztion
- **Status**: In progress
- **Review status**: Approved

## Team

**Project Owner:** Rajat

|               | Workers | Reviewers        |
| ------------- | ------- | ---------------- |
| **UX design** | Rajat   | Ghislaine, Kriti |
| **Front end** | Rajat   | Sean             |
| **Back end**  | Rajat   | Mukesh           |

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

**Frontend**: Enable the frontend codebase to support translations.
**Backend**: Enable backend codebase to support translations for the server-side rendered pages and error messages that are shown to the users on UI as it is.
**Infrastructure**: Integration of a third-party translation automation service like [Transifex](https://www.transifex.com/open-source/)

## Timeline

This project should take 8 weeks of frontend implementation effort and 1 week of backend implementation effort, excluding the time to finalize the technical approach.

|                                              | End Date   | Status      |
| -------------------------------------------- | ---------- | ----------- |
| Get tech spec approved                       | 2023-05-26 | Done        |
| FE implementation                            | 2023-07-21 | In Progress |
| BE & Infra Work                              | 2023-07-21 | In Progress |
| Developer documentation                      | 2023-07-28 |
| Guide to get the strings translated          | 2023-07-28 |
| Contributing guide for volunteer translators | 2023-07-28 |

NOTE: Initial estimates - 4 weeks of FE effort and 1 week of BE effort in parallel.

## Resources

- [Project Approval Thread](https://groups.google.com/a/mathesar.org/g/mathesar-developers/c/dLRJjL5_t28)
- [Project Update Thread](https://groups.google.com/a/mathesar.org/g/mathesar-developers/c/a5DuC82BFaM)
- [Tech Specs](/engineering/specs/internationalization)
