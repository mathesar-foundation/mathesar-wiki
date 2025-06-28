# View and Edit Joined Data

!!! example "Add stakeholders"
	Add new stakeholders to the table below.

| **Role** | **Person / Item** | **Status** |
|-|-|-|
| **Requirements** | [Working with Joined Data reqs](/product/requirements/2025/jouned-data) | |
| **Author** | Kriti Godey |  🟢 Done |
| **Reviewer** | Brent Moran | 🔵 In review |
| **Reviewer** | Zack Krida | 🔵 In review |

## Solution

- Starting at a table, add related one-to-one columns that are "enum like" (are either a FK pointing back to the table, or are a many-to-many table) to the table view. See the values in that column.  
- Adding and removing existing items to one-to-many columns from the cell displaying them, with autocomplete based on values. 

## Tradeoffs

Things to watch out for while implementing:

* Scope creep and competing goals. We need to focus on fixing only this one issue.  
* Optimizing for edge cases.

Out of scope:

* Any additional query building functionality – only adding / removing columns that already exist.  
* Adding records that are not one-to-many  
* Any summarizations or transformations that aren’t lists.  
* Changing any existing table page functionality.  
* Editing / deleting related records – only adding / removing them or creating them are in scope.  
* Adding new related records with complex constraints.

## High-Level Implementation Plan

**Type of work needed**: Design, frontend, backend,

**Stakeholders**: Sean (implementer)

**Workflow**:
	- Design approved by Kriti and implementer.
	- Backend + frontend implemention.
	- Kriti approved final feature.

**Rough timeline**: 0.4.0.

## Research
### Comparison to Prior Work

**Worksheets:** 

* No new query paradigm, just added functionality to the query page.  
* Functionality is limited to what solves the immediate problem, but can be extended for future problems.  
* Tables are still the central organizing concept.

**Prior design concepts:** 

*We have had a bunch of designs related to this before.*

* [One-to-Many Relationships \- Mathesar Wiki](https://wiki.mathesar.org/design/specs/views-one-to-many-relationships/)  
* [Multiple Records Associated with a Single Record \- Mathesar Wiki](https://wiki.mathesar.org/design/specs/multiple-records-spec/)  
* [Editing Records Within a View \- Mathesar Wiki](https://wiki.mathesar.org/design/specs/eding-view-records/)


## Community Engagement

We should:

- seek input from community members who have asked for this, to ensure that we're building the right set of features and addressing their use cases.
- update mathesar.org and our `README.md` to include this as a featured use case.
	- On mathesar.org, this should include the product page and a few use cases.
	- We may want to create a new use case built around this feature because this unlocks a lot of workflows.
	- We'll need new screenshots too.
