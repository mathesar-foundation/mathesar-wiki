---
title: 2023-07 Frontend Fixes
description: 
published: true
date: 2023-07-13T17:20:51.670Z
tags: 
editor: markdown
dateCreated: 2023-07-10T13:31:46.556Z
---

**Name**: 2023-07 Frontend Fixes
**Status**: Draft 

## Team

| Role | Assignee |
|-|-|
| **Owner** | Sean |
| **Frontend code review** | Pavish |
| **Frontend code review** | Rajat |

## Problem

Time for some fixes.

## Solution

This project focuses on the cell selection functionality. It starts by addressing some long-due refactoring of the cell selection code. The front end team recently discussed the need for this refactor because it has been a particularly buggy area of the front end codebase. Improving it will lay groundwork for fixing other bugs related to the cell selection logic and implementing new features.

- [Change the data structure to store selections in the selection store](https://github.com/centerofci/mathesar/issues/1732)
- [Cell selection partially broken after selecting columns when table is filtered to be empty](https://github.com/centerofci/mathesar/issues/2845)
- [Do not select columns when hovering column headers in a table with no rows](https://github.com/centerofci/mathesar/issues/2130)
- [Weird cell selection behavior when dragging from cell to header](https://github.com/centerofci/mathesar/issues/2122)
- [Cell Context menu event should maintain the cell selection when triggered within the selection](https://github.com/centerofci/mathesar/issues/1771)

## Risks

(none)

## Resources
- [Introduction thread on dev mailing list](https://groups.google.com/a/mathesar.org/g/mathesar-developers/c/lUajMP3nxxY/m/kwi8_G2nAAAJ)
- [Project approval discussion on dev mailing list](https://groups.google.com/a/mathesar.org/g/mathesar-developers/c/bfGBAIN0M6Y/m/5FCrWHQDAAAJ)

## Timeline

To fit within the cycle

## Email threads

- [project approval](https://groups.google.com/a/mathesar.org/g/mathesar-developers/c/bfGBAIN0M6Y/m/Iq1w4lyvAAAJ)
- [update 2023-07-14](https://groups.google.com/a/mathesar.org/g/mathesar-developers/c/GJIzUwk3Zs8/m/2C8TUaI6AAAJ)
