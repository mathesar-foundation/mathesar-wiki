# Requirements Template

!!! example "Add stakeholders"
	Add new stakeholders to the table below.

| **Role** | **Person** | **Status** |
|-|-|-|
| **Author** | Kriti Godey |  🟢 Done |
| **Reviewer** | Brent Moran | 🔵 In review|
| **Reviewer** | Zack Krida | 🔵 In review |

## The Problem

Mathesar users would like an easy way to view and edit data from related tables while looking at a table.

Direct user request:

> It would be really useful if, when looking at a table, a user could also see a column from a different table, either due to a foreign key relationship or simply via a join

### Why it’s worth solving.

We are currently focusing on major issues that are blocking people from adopting Mathesar. 

Many people use Mathesar for both querying and data entry. But it’s extremely inconvenient or inefficient to work with joined data in Mathesar. Users need to use the following workarounds right now:

* Use the record page or multiple windows to add related data.  
* Use multiple windows to edit data across multiple records and multiple tables.
* Switch from the table page to the data explorer page to view data related to the data you’re currently editing.
* Use the many to many tables to edit, but there’s not enough context to see what rows you’ve already added and what you haven’t (e.g. if associating five genres with a movie)  

Users have told us they cannot adopt Mathesar without this process being easier, and users who are happy with Mathesar have also requested this. It seems urgent to solve this to make Mathesar more useful.

### Is it feasible?

Yes, it will require design changes, but it’s absolutely feasible. We’ve already done the technical feasibility work on this as part of Worksheets and Table Query Integration investigation so I will not repeat it here.


## Success Criteria

How we'll know we've succeeded with our goals:

* Users who’ve requested the feature saying that it works for them.  
* Kriti being able to do product planning in Mathesar.  
* People using this feature, as shown in analytics.
* Uptick in DAUs and MAUs (may not be conclusively linked to this feature).

## Requirements

Minimum necessary:

* Starting at a table, add related one-to-one columns that are "enum like" (are either a FK pointing back to the table, or are a many-to-many table) to the table view. See the values in that column.  
* Remove columns from the current view, either from the table or joined tables  
* A way to distinguish between hiding new columns from deleting table columns.  
* A way to distinguish between adding brand new columns to the current table and showing new columns from an existing table.  
* A way to distinguish between columns in the current table and columns from other tables.  
* Adding and removing existing items to one-to-many columns from the cell displaying them, with autocomplete based on values.  
* Ensuring that filtering / sorting / grouping tables still works as usual.

Additional scope (not necessary for MVP):

* Save the current view (global, not per-user)  
* Switch between multiple saved views associated with a table  
* Remove saved views (global, not per-user)  
* Creating new one-to-many records from a cell  from the cell displaying them.  
  * This can be limited to things that are easy (e.g. no NOT NULL constraints, disable creation for complicated records)  
* Adding any kind of related column to the table:
	* Any join distance
	* Multiple paths to the table
	* Natural joins

## Use Case

I’m just using myself as the user here. I have a [product planning schema](https://internal.mathesar.org/db/8/schemas/49870/) in Mathesar. 

I think of the [**Ideas**](https://internal.mathesar.org/db/8/schemas/49870/tables/49873/) table as the primary concept in this schema.. I’m organizing product ideas. Everything else is scaffolding.

Each idea has multiple [**categories**](https://internal.mathesar.org/db/8/schemas/49870/tables/49884/). In order to organize ideas in a way that’s useful to me, I need to have a single work area where I can:

* Start from the ideas list and add in a category column so I can see all categories associated with an idea.  
* Add and remove categories associated with an idea.  
  * Create new categories inline if needed.

I also realized midway through making this schema that I want to associate multiple [**impact**](https://internal.mathesar.org/db/8/schemas/49870/tables/49931/)s to the same idea. I’d like to be able to:

* Extract the impact foreign key column into a mapping table and preserve existing mappings (this is tracked as a [GitHub issue](https://github.com/mathesar-foundation/mathesar/issues/4570)).  
* Add the impact column to the ideas list (which already has the category column)  
* Manipulate impacts associated with an idea in the same way as categories.

I don’t want to keep adding these columns every time, so I’d like to save this as my default view of the table, since I always use this the same way.
