---
title: 2023-07 Frontend Fixes
description: 
published: true
date: 2023-07-19T23:10:55.257Z
tags: 
editor: markdown
dateCreated: 2023-07-10T13:31:46.556Z
---

**Name**: 2023-07 Frontend Fixes
**Status**: In progress
**Review status**: Approved

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

Unrelated frontend issues we'd also like to work on during this cycle

- [Make column type inference optional](https://github.com/centerofci/mathesar/issues/2358)
- [Copying FK cells should copy the record summary instead of the PK value](https://github.com/centerofci/mathesar/issues/3085) (because it's a regression with a quick fix)

## Risks

(none)

## Resources

Email threads:

- [project intro](https://groups.google.com/a/mathesar.org/g/mathesar-developers/c/lUajMP3nxxY/m/kwi8_G2nAAAJ)
- [project approval](https://groups.google.com/a/mathesar.org/g/mathesar-developers/c/bfGBAIN0M6Y/m/Iq1w4lyvAAAJ)
- [weekly updates](https://groups.google.com/a/mathesar.org/g/mathesar-developers/c/GJIzUwk3Zs8)

## Timeline

To fit within the cycle
