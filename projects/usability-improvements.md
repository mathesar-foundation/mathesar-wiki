---
title: Usability Improvements
description: 
published: true
date: 2023-03-15T00:00:00.000Z
tags: 
editor: markdown
dateCreated: 2023-03-15T00:00:00.000Z
---

- **Name**: Usability Improvements
- **Status**: in review 

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

| Task                                        | Work       | Days | Deadline |
| --                                          | --         | --   | --       |
| (Project start date)                        |            | 0    | TBD      |
| [Clipboard UX design][2377]                 | UX design  | 5    | TBD      |
| [Copy from Mathesar, paste elsewhere][1688] | Front end  | 3    | TBD      |
| [Drag to select from active cell][1885]     | Front end  | 2    | TBD      |
| [Selection stuck in drag mode][1917]        | Front end  | 1    | TBD      |
| [Filtering via column header][2232]         | Front end  | 2    | TBD      |
| [Persistent column widths][1421]            | Back end   | 3    | TBD      |
| [Resizable sidebars][2362]                  | Front end  | 3    | TBD      |
| [Persistent sidebar widths][2387]           | Front end  | 1    | TBD      |

### Notes

- Note that [Copy from Mathesar, paste elsewhere][1688] is an implementation task that falls within the broader design covered by [Clipboard UX design][2377]. It's a relatively narrow subset of the total implementation that the design will eventually specify, but it's the most straightforward piece to implement and design, so that's why it's included in this project. This project does _not_ include any other _implementation_ for the copy-paste functionality. The idea here is to take some baby steps toward better clipboard behavior by doing the research and design work we need in order to better specify all the work that we'll _need_ to do later.
- I plan to tackle [Clipboard UX design][2377] and [Copy from Mathesar, paste elsewhere][1688] concurrently, at least to start. I need to gain an understanding of the behavior and limitations of clipboards and web clipboard APIs. Working to implement the "paste elsewhere" feature will help me lay groundwork for the broader clipboard UX questions.
- I plan to timebox the clipboard design. When this project is completed, there may still be additional clipboard design work left, I'll organize the remaining work into more detailed tickets.

## Risks

- [Clipboard UX design][2377] contains many unknowns and runs the risk of ballooning in scope.

## Timeline

(See work plan. Deadlines will be filled in once the project begins)


[2377]: https://github.com/centerofci/mathesar/issues/2377
[1688]: https://github.com/centerofci/mathesar/issues/1688
[1885]: https://github.com/centerofci/mathesar/issues/1885
[1917]: https://github.com/centerofci/mathesar/issues/1917
[2232]: https://github.com/centerofci/mathesar/issues/2232
[1421]: https://github.com/centerofci/mathesar/issues/1421
[2362]: https://github.com/centerofci/mathesar/issues/2362
[2387]: https://github.com/centerofci/mathesar/issues/2387
