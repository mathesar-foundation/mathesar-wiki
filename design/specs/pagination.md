---
title: Pagination Specs
description: 
published: true
date: 2021-06-07T20:26:42.338Z
tags: 
editor: markdown
dateCreated: 2021-06-02T09:10:30.296Z
---

# Context
The team identified the need for a pagination component during the review of the design specs for [Read-Only Tables](/design/specs/read-only-table). The team decided to add pagination to read-only tables during the [May 19th team meeting](/meeting-notes/may-2021). The team chose pagination against the original requirement of having infinite scrolling to prevent issues with real-time data causing data duplication.

# Pagination Component Details
![](/assets/design/specs/pagination/HyZR_lN9d.png)


The pagination component contains the controls for navigating across the parts (pages) of records from a table that the UI can't fully display. It usually sits at the bottom of a table.

The pagination component is always visible, even if the table does not reach the number of records required to be split into parts.

## Controls
The pagination component controls are:
- Records per page selector
- Link to first and last pages
    - Helpful when applying filters or sorting criteria (i.e., What is the oldest/newest item?)
- Navigation arrows for next and previous pages
- Page range and total records indicator
- Logarithmic Page Navigation

## Scrolling Area
The scrolling settings of the table should allow the pagination component to be fixed at the bottom.

![](/assets/design/specs/pagination/1oghfOu.png)
In this figure, the two red horizontal lines delineate the scrolling area.

## Page Size
The ideal number of records per page will depend on the desired user experience. For real-time data, the minimum may be several thousand. For most tables, pagination won't be required as most data will fit on a single page.

### Questions
What are reasonable max and minimum page sizes?

# UX Considerations

## Offset-Based Pagination vs. Cursor-Based
Based on discussion with the team, the first version of the read-only table will use offset-based pagination. This is the preferred choice as it is already implemented and does not prevent the roadmap from being built and allow other methods to be used later.

Some of the following points were discussed and shall be reconsidered later when we have more evidence of limitations imposed by our current pagination method:
- Offset-based allows users to jump into any arbitrary page instead of forcing them to scroll through the entire content.
- Offset-based is unreliable when the list of items frequently changes, causing problems when records are added or deleted.
- Cursor-based pagination is not affected by the addition or removal of items.
- Cursor-based pagination requires users to traverse through the entire result set page by page.

> Please see ["Pagination options" on GitHub Discussions](https://github.com/centerofci/mathesar/discussions/177) for more detail.
{.is-info}
