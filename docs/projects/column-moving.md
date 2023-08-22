---
title: Column Moving Improvements
description: 
published: true
date: 2023-08-09T15:07:52.165Z
tags: 
editor: markdown
dateCreated: 2023-08-09T15:07:52.165Z
---

**Status**: Draft 
**Review status**: Draft
**Theme**: Data modeling features

## Team
**Project owner**: Brent

| Role              | Assignee     | Reviewer         | Notes                                       |
|-------------------|--------------|------------------|---------------------------------------------|
| **Requirements**  | Brent        | Ghislaine, Kriti | *Product spec, requirements, GitHub issues* |
| **Design work**   | Ghislaine    | Kriti, Brent     | *UI and UX*                                 |
| **Backend work**  | Brent, Anish | Mukesh           | *Backend specs and code*                    |
| **Frontend work** | ???          | ???              | *Frontend specs and code*                   |

## Problem
It came to my attention during RSQLA1 that our column extraction and moving feature isn't complete, and the current state is sort of dangerous. In fact, I'm concerned the current state is so bad that attempts to use this feature could well lead to justified ragequits from Mathesar entirely. I've written some problems up in roughly descending order of priority (IMO).

The column moving operation has the potential for data loss, or at least for jumbling up the link in certain edge cases, e.g., if the foreign key was created outside of Mathesar and is on a text column rather than integer.

The column moving operation is one-way only. Currently, you can only move columns along a foreign key link from the referrer table to the referenced table. E.g., from a remainder table to an extracted table. This asymmetry is not portrayed to the user, and they could easily tinker themselves into an irreversible situation. 

Merging tables is not available from the UI. This means you can't un-extract your columns.

If you extract a foreign key column, you'll lose the foreign key link. Start with:

**Roster**

| id | Student Name | Student Email   | Subject | Grade | Teacher |
|---:|--------------|-----------------|---------|------:|--------:|
|  1 | Alice        | alice@yahoo.com | Math    |    73 |       2 |
|  2 | Alice        | alice@yahoo.com | Music   |    87 |       1 |
|  3 | Alice        | alice@yahoo.com | Reading |    93 |       1 |
|  4 | Bob          | bob@lycos.com   | Math    |    58 |       2 |
|  5 | Bob          | bob@lycos.com   | Music   |    94 |       3 |
|  6 | Bob          | bob@lycos.com   | History |    83 |       1 |

**Teachers**
| id | Name      | Email          |
|---:|-----------|----------------|
|  1 | Ms. Smith | asmith@abc.edu |
|  2 | Mr. Jones | bjones@abc.edu |
|  3 | Mrs. Li   | eli@abc.edu    |

Suppose The **Teacher** column references the **Teachers** table ID, and I want to extract the **Subject** and **Teacher** columns from the **Roster** table to create a new table. Currently, this breaks the foreign key link between the **Teacher** column and the **Teachers** table.

If you extract or move some portion of the columns involved in a multi-column constraint (e.g., a unique constraint), the constraint is silently dropped with no warning or error. See [the issue](https://github.com/centerofci/mathesar/issues/1437).

It's not possible to extract a non-orderable set of columns, or rather when doing so you end up jumbling up the foreign key links. See [the issue](https://github.com/centerofci/mathesar/issues/1490).

If you try to extract a column referenced by a foreign key column, we currently throw an error, and fail. See [the issue](https://github.com/centerofci/mathesar/issues/1433). 

If you extract columns from the middle of a table, the new foreign key column is still the last column of the table. See [the issue](https://github.com/centerofci/mathesar/issues/1681).


## Solution

We need to start this with a product-level discussion to determine what we want to accomplish with the feature from end to end, and if there's any subset that we can put out that will at least avoid irreversible column moving operations, and avoid any data loss.

Depending on that discussion, or those discussions, we should then modify the column extraction and moving logic accordingly. This will involve lots of back end work, some design work, and a bit of front end work.

## Outcome

Users will no longer be in danger of corrupting their data or making irreversible data modeling mistakes when using this feature.

## Risks
- Column extraction and moving is really technical, and it will be difficult to portray to users in an easy-to-understand way, especially when considering things like multicolumn keys and preexisting foreign keys.

## Links

## Timeline
I think we'd need one cycle to work through the product considerations and plan an attack, and another cycle to implement.
