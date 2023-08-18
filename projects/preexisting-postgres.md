---
title: Investigating compatibility with pre-existing databases 
description: 
published: true
date: 2023-08-09T15:07:52.165Z
tags: 
editor: markdown
dateCreated: 2023-08-09T15:07:52.165Z
---

**Status**: Draft 
**Review status**: Draft
**Theme**: Work with current databases

## Team
**Project owner**: Brent

| Role              | Assignee         | Reviewer      | Notes                                       |
|-------------------|------------------|---------------|---------------------------------------------|
| **Requirements**  | Brent, Ghislaine | Kriti, Pavish | *Product spec, requirements, GitHub issues* |
| **Design work**   | Ghislaine        | Pavish, Brent | *UI and UX*                                 |
| **Backend work**  | Brent            | ???           | *Backend specs and code*                    |
| **Frontend work** | Pavish, Sean     | ???           | *Frontend specs and code*                   |

## Problem

We've decided to focus on getting Mathesar working on preexisting live databases as a primary goal for the product. We need to solve some problems to satisfy common use cases. This project should cover research to help us prioritize which features to support in which order, as well as (maybe) some prototyping. Here are a few examples of features which may be used from PostgreSQL in a preexisting database, but which we don't currently support properly:

### Views

The bare minimum would be to show the views that already exist on a DB in the UI.
- Where should they be shown?
- Can we get away without enabling editing of the view definition, or editing data in the underlying tables at this time?
- Most difficult work here is UI/UX.
- This potentially overlaps with data explorer (or at least it will seem to for users). 
  - How should we deal with this?
  - We either need a distinct representation from saved explorations or an integrated approach.

### Permissions

Mathesar may not be allowed to run as a super user or highly-privileged user. We need to be able to use Mathesar in those cases without throwing errors everywhere (at a minimum).
- Do we need to have more sophisticated permissions handling?
- We probably need some way to show a user what privileges they have without trial-and-error on their part.

### Types
- Composite types are not going to go well with SQLAlchemy. It doesn't support them unless you have a custom class defined in python for each composite type on the DB. We may have to (for now) code up some widget that generates these classes and registers them into the SQLAlchemy constant upon reflection of type info from the DB.
- Array types are not currently well-supported by Mathesar, but we have a clear path on those.
- Unknown scalar types should be the easiest case.

### Generated columns

These should be pretty low-effort to get working, and we already have some of the needed concepts in the UI. These could simply be treated as uneditable dynamic default columns. That way, we can show the generated values in the UI, and disallow trying to update those values manually (which won't work for PostgreSQL generated columns). We’re already flagging these columns as a dynamic default in the back end, it’s a matter of whether the front end is then handling that with enough fidelity.

We could also trivially show the generating expression (in fact this might already happen if we’re showing dynamic defaults somehow), but I’d consider that a bonus.

### Supporting different pkey setups

This may be the thing we need the most work on overall
- Currently, we will fail pretty badly if we get a table with a multicolumn primary key, or any non-sequential primary key.
- We may have to start by making any such table read-only.

### Supporting different fkey setups

We may not act correctly for multicolumn foreign keys, or foreign keys that don't refer to the primary key of the referent table.

### Constraints

We currently break and don't even return the constraints we _do_ know if we stumble across a constraint type we don't support. Thus, we at least need to fix that. We also need to verify that the behavior when trying to update a value that would violate some unsupported constraint is reasonable.
- How do we determine which database configurations to show in the UI?
- We should find a balance to avoid overwhelming users if we opt to display all database configurations in the UI.

### Column moving dangerous in some preexisting DBs

I think we should really try to do the project to fix up the column moving, or remove that feature, and wiring up to a preexisting DB makes this even more relevant. The current functionality lets you screw things up irreversibly, and it won’t be obvious to a user when they’re in danger from our current UI. It also has the potential to silently delink taables under certain multicolumn foreign key conditions which may occur in preexisting DBs.


## Solution

For this project, we need to 
- Go through commentary and issues from users to ensure nothing has been forgotten in the problems listed above.
- Find realistic sample PostgreSQL databases and try connecting Mathesar to see if we've forgotten anything else.
  - [This thread](https://groups.google.com/a/mathesar.org/g/mathesar-developers/c/H532ebtiLb0/m/vs87RhyGBQAJ) from the dev mailing list has some suggestions.
- Work through UX problems associated with connecting to preexisting databases
  - Brainstorm what UX problems may occur
  - Determine which problems could cause data loss or actual breakage of the front end
- Have product-level discussions to determine what we want to prioritize.
  - Top of the list should be any problems that we believe could cause data loss, or which break the front end experience.
  - Some features may be more useful for target user groups.
  - Some features may have implications for other parts of the product.
- Write issues and meta-issues based on those discussions describing the work to be done.
  - Issues should be grouped by category above, and should cover design as well as implementation; multiple issues per category will generally be needed.
  - We should have complete, ready-to-implement issues for at least data losing or breaking problems found by the end of the cycle. This may imply doing some of the design work during the cycle so that we can spec and write implementation issues.

It may be that we end up prototyping or even implementing some features during this project, but any implementation work should be done _solely_ to help us understand the UI/UX concerns better so we can more clearly spec out said UX and any related issues. Design should be done insofar as it's needed to write implementation-related issues.

### Prioritization of implementation

 When we get to implementation, we want to prioritize solutions to problems that break Mathesar's ability to work with existing databases over adding new functionality. E.g., we should make sure that our column moving features don't cause data loss, no matter what types of foreign and primary key arrangements might exist on the connected database before we add features to let users see views. We want to reflect this in the issues and meta-issues we create.

## Outcome

Users should be able to connect Mathesar to a preexisting database
- Without any risk of corrupting their data in confusing ways
- With the ability to see all their data in Mathesar in some fashion
- With the ability to use the Mathesar interface safely, and without crashing into unhandled errors due to unsupported PostgreSQL features.

## Risks

- Prioritization will involve some guesswork at this stage

## Timeline

Within the coming cycle, we should at least get as far as writing up (meta)issues for any problems we discover that will result in either data loss, or breakage of the front end experience while they remain unsolved. As a bonus, we'd like to have issues for other categories of problems, prioritized and triaged. 
