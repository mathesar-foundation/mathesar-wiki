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

## Roles

**Project Owner:**  Sean 


|               | Workers | Reviewers         |
| --            | --      | --                |
| **UX design** | Sean    | Ghislaine, Pavish |
| **Front end** | Sean    | Pavish            |
| **Back end**  | Sean    | Mukesh            |

## Summary

This project is a collection of smaller usability-related tickets that seem to present low-hanging fruit for improving UX.

## Work

| Task                                        | Work | Days estimated |
| --                                          | --   | --: |
| [Clipboard UX design][2377]                 | 🎨   | 5 |
| [Copy from Mathesar, paste elsewhere][1688] | 🕶️   | 3 |
| [Drag to select from active cell][1885]     | 🕶️   | 2 |
| [Selection stuck in drag mode][1917]        | 🕶️   | 1 |
| [Filtering via column header][2232]         | 🕶️   | 2 |
| [Persistent column widths][1421]            | ⚙️   | 3 |
| [Resizable sidebars][2362]                  | 🕶️   | 3 |
| [Persistent sidebar widths][2387]           | 🕶️   | 1 |

**TOTAL TIME:**  20 days (4 weeks)

- 🎨 = design
- 🕶️ = frontend
- ⚙️ = backend

## Risks

- [Clipboard UX design][2377] contains many unknowns and runs the risk of ballooning in scope.

## Notes

- Note that [Copy from Mathesar, paste elsewhere][1688] is an implementation task that falls within the broader design covered by [Clipboard UX design][2377]. It's a relatively narrow subset of the total implementation that the design will eventually specify, but it's the most straightforward piece to implement and design, so that's why it's included in this project. This project does _not_ include any other _implementation_ for the copy-paste functionality. The idea here is to take some baby steps toward better clipboard behavior by doing the research and design work we need in order to better specify all the work that we'll _need_ to do later.
- I plan to tackle [Clipboard UX design][2377] and [Copy from Mathesar, paste elsewhere][1688] concurrently, at least to start. I need to gain an understanding of the behavior and limitations of clipboards and web clipboard APIs. Working to implement the "paste elsewhere" feature will help me lay groundwork for the broader clipboard UX questions.
- I plan to timebox the clipboard design. When this project is completed, there may still be additional clipboard design work left, I'll organize the remaining work into more detailed tickets.

[2377]: https://github.com/centerofci/mathesar/issues/2377
[1688]: https://github.com/centerofci/mathesar/issues/1688
[1885]: https://github.com/centerofci/mathesar/issues/1885
[1917]: https://github.com/centerofci/mathesar/issues/1917
[2232]: https://github.com/centerofci/mathesar/issues/2232
[1421]: https://github.com/centerofci/mathesar/issues/1421
[2362]: https://github.com/centerofci/mathesar/issues/2362
[2387]: https://github.com/centerofci/mathesar/issues/2387
