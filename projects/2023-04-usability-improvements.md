---
title: 2023-04 Usability Improvements
description: 
published: true
date: 2023-06-05T20:32:15.185Z
tags: 
editor: markdown
dateCreated: 2023-03-15T20:52:30.876Z
---

- **Name**: 2023-04 Usability Improvements
- **Status**: Cut short to move on to other work

## Team

**Project Owner:**  Sean 

|               | Workers | Reviewers         |
| --            | --      | --                |
| **UX design** | Sean    | Ghislaine, Pavish |
| **Front end** | Sean    | Pavish            |
| **Back end**  | Sean    | Mukesh            |

## Problem

This project is a collection of smaller usability-related tickets that seem to present low-hanging fruit for improving UX.

## Solution

### Work plan

| Task                                        | Work       | Days | Deadline   | Status |
| --                                          | --         | --   | --         | --     |
| (Project start date)                        |            | 0    | 2023-03-29 |    |
| [Clipboard UX design][2377]                 | UX design  | 5    | 2023-04-07 | ✅ Done: [PR][w-90], [Specs][spec] |
| [Copy from Mathesar, paste elsewhere][1688] | Front end  | 3    | 2023-04-07 | ✅ [Done][2773] |
| [Drag to select from active cell][1885]     | Front end  | 2    | 2023-04-14 | ✅ [Done][2792] |
| [Selection stuck in drag mode][1917]        | Front end  | 1    | 2023-04-14 | ✅ [Done][1917-done] |
| [Filtering via column header][2232]         | Front end  | 2    | 2023-04-14 | ✅ [Done][2782] |
| [Persistent column widths][1421]            | Full stack | 3    | 2023-04-21 | ❌ To do |
| [Resizable sidebars][2362]                  | Front end  | 3    | 2023-04-26 | ✅ [Done][2808] |
| [Persistent sidebar widths][2387]           | Front end  | 1    | 2023-04-26 | ✅ [Done][2808] |
| [TSV serialization improvements][2811]      | Front end  | 1    | 2023-05-10 | ✅ [Done][2867] |
| [Paste into cells][2812]                    | Full stack | 9    | 2023-05-10 | 🛑 Blocked by [API work][2844] |

**TOTAL TIME:**  20 days (4 weeks)

### Notes

- Note that [Copy from Mathesar, paste elsewhere][1688] is an implementation task that falls within the broader design covered by [Clipboard UX design][2377]. It's a relatively narrow subset of the total implementation that the design will eventually specify, but it's the most straightforward piece to implement and design, so that's why it's included in this project. This project does _not_ include any other _implementation_ for the copy-paste functionality. The idea here is to take some baby steps toward better clipboard behavior by doing the research and design work we need in order to better specify all the work that we'll _need_ to do later.
- I plan to tackle [Clipboard UX design][2377] and [Copy from Mathesar, paste elsewhere][1688] concurrently, at least to start. I need to gain an understanding of the behavior and limitations of clipboards and web clipboard APIs. Working to implement the "paste elsewhere" feature will help me lay groundwork for the broader clipboard UX questions.
- I plan to timebox the clipboard design. When this project is completed, there may still be additional clipboard design work left, I'll organize the remaining work into more detailed tickets.

## Risks

- [Clipboard UX design][2377] contains many unknowns and runs the risk of ballooning in scope.

## Timeline

(See work plan)

[1421]: https://github.com/centerofci/mathesar/issues/1421
[1688]: https://github.com/centerofci/mathesar/issues/1688
[1885]: https://github.com/centerofci/mathesar/issues/1885
[1917-done]: https://github.com/centerofci/mathesar/issues/1917#issuecomment-1505572348
[1917]: https://github.com/centerofci/mathesar/issues/1917
[2232]: https://github.com/centerofci/mathesar/issues/2232
[2362]: https://github.com/centerofci/mathesar/issues/2362
[2377]: https://github.com/centerofci/mathesar/issues/2377
[2387]: https://github.com/centerofci/mathesar/issues/2387
[2773]: https://github.com/centerofci/mathesar/pull/2773
[2782]: https://github.com/centerofci/mathesar/pull/2782
[2792]: https://github.com/centerofci/mathesar/pull/2792
[2808]: https://github.com/centerofci/mathesar/pull/2808
[2811]: https://github.com/centerofci/mathesar/issues/2811
[2812]: https://github.com/centerofci/mathesar/issues/2812
[spec]: https://wiki.mathesar.org/en/design/specs/clipboard-interactions
[w-90]: https://github.com/centerofci/mathesar-wiki/pull/90
[2844]: https://github.com/centerofci/mathesar/issues/2844
[2867]: https://github.com/centerofci/mathesar/pull/2867

