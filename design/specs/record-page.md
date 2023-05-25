---
title: Record Page Design
description: 
published: true
date: 2023-05-11T14:41:07.605Z
tags: 
editor: markdown
dateCreated: 2022-07-18T13:41:06.809Z
---

## Design Goals

Allow the user to perform focused operations on one record at a time, as well as other records linking to it.

## Terminology

Within this spec...

- **"this record"** refers to the record being displayed on the page
- **"this table"** refers to the table containing this record

## Parts of the page

- The page contains the following parts, all of which are described in greater detail below
    - Title
    - Direct fields
    - Widgets
- The layout of these parts within the page (and of the content within each part) is subject to improvisation during implementation. Because continued adjustment of layout design is relatively low-cost, we are currently prioritizing the implementation of basic functionality over the perfection of aesthetics within this feature.

## Title

- One line in large font size. It contains:
    - A "record" icon. (E.g. something like [this](https://fontawesome.com/icons/memo-pad?s=solid))
    - The **Record Summary** string
    - A dropdown icon that opens a menu to perform the following actions on the record:
        - Delete
        - *Potentially other actions in the future, such as "Add field", "Duplicate", etc.*

## Direct Fields

- This is a section of the page which comes after the title.
- It contains a form-like area which has many labeled input fields. One field exists for each column in this table.
- The fields are presented in the same order that they occur in the Table Page.
- Field labels display the column name along with the icon used within the column header on the Table Page.
- Edits to the field values are saved on blur, with a similar UX to editing cell values in a table. There is no save button.
- Similar to the Table Page, a persistent but subtle status message appears at the top of all the fields which reads "Saving" or "All changes saved" when appropriate.
- FK fields display the record summary for the linked record and allow the user to navigate to its Record Page.
- The layout of fields and their associated labels can be improvised during development (and adjusted during future design iterations).


## Widgets

One "widget" allows the user to see (and potentially modify) other data in the same schema *from the context of this record*.

**Example:** On a Patrons record, we use a widget to see the Checkouts records associated with the patron.

*Note: The name "widget" may be a bit awkward, we're open to replacements. A widget is kind of like a query or a view -- but "query" and "view" already mean very specific things and a widget may not necessarily be either a Mathesar query or a Postgres view. Also, although these specs describe a limited set of initial functionality, we expect widgets to gradually evolve into a flexible and powerful feature (more details at the end of these specs), so we've coined a unique (and somewhat generic) name for it.*

### Basic widget specs for alpha release

- One widget appears on the Record Page **for each foreign key which references this table**.

- Each widget has a **title** like:
    
    > Related `Checkouts` Records

    If this table is referenced by multiple FKs from the same (other) table, or this table is referenced by an FK within this table itself, then the widget title will be:
    
    > Related `Checkouts` Records *(via `Patron Id`)*

- Each widget displays the related records in a sheet UI similar to the sheet within the Table Page.

    Commonalities between the widget and the Table Page:

    - Cell display, selection, and editing
    - Filtering/sorting/grouping (though any modifications herein will be ephemeral)

    Differences between the widget and the Table Page:

    - Actions which modify the table (e.g. "Rename", "Delete", "Constraints", "Link") are not available within the widget.
    - Actions which modify columns are not available within the widget.
    - The Table Inspector is not available within the widget.
    - The column containing the FK to this table is hidden in the widget. Within this column, any newly-added records will automatically receive a value equal to the PK of this record (ensuring that newly-added records properly linked to this record).
    - In the widget, the filter criteria has a filter automatically applied which filters the records to display only those related to this record. The user cannot remove this filter condition. The user is free to add other filter conditions, but those conditions will not persist after navigating away from this Record Page.

- Each widget contains a "View All" link to the right of the title. This link navigates to the Table Page for the widget table pre-filtered to show only the records related to this record. Any ephemeral filter conditions applied to the widget by the user will also be applied within the link to that Table Page.

- The sheet has pagination controls at the bottom. To prevent nested vertical scrolling, the pagination-page-size is a scant `10`! The user can increase it within the pagination UI if needed, but their new setting will not persist. The widget will grow taller to accommodate a larger pagination-page-size, but its `max-height` is `0.9vh` (or similar) to prevent it from being taller than the viewport. This means that nested vertical scrolling will occur if the user sets a large pagination-page-size or has an uncommonly short viewport.

    The small pagination-page-size admittedly limits the utility of the widget -- but does so for the sake of improving usability of the Record Page as a whole. If the user wants to see the "full" results from the widget, they can click the "View All" link (even choosing to open that link in a new browser tab if they like).

- The order of widgets within the Record Page is not defined and also not configurable.

### Longer-term goals for widgets, post-alpha

(This section is subject to further design review and task prioritization, but is presented to justify gaps in functionality of the above specs.)

- There are two types of widgets:

    - **Table widgets** (which are described above, to be implemented first)

    - **Query widgets** (which are more complex and will hopefully be implemented later)
    
        Some example use-cases for query widgets are:

        - Show a patron's currently-checked out books
        - Show all publications of an author, along with the number of items that the library has for that publication.

- The title is stylized differently for the two types of widgets (perhaps via a lock icon or similar) allowing the user to distinguish them.

- Above all widgets, an "Add Query" (or maybe "Add Widget"?) button exists to add a new query widget.

    The button is a link (can be opened in a new tab) to create a new query within the Data Explorer. The link contains URL parameters which specify the id of this table and the id of this record. The Data Explorer then allow the user to build a query from scratch, but the choice of base table is limited only to tables which contain FKs to this table.

    While building the query, the Data Explorer displays the Record Summary of the original record (where the user was before building the query). The user can click on that Record Summary to navigate back to that Record Page. The results of the query the user is building are filtered to show only the items related to that record. That filtering operation is not defined within the query the user is building, but rather performed as part of the `filter` params when fetching the results of the query. The UI which displays the specific Record Summary also allows the user to change the record (using the Record Selector) -- merely for the purpose of previewing their query from the perspective of a different record while building it.
    
    We will need to clarify what happens when the user saves the query. Is the query visible within the top level of the schema? Or is it hidden? Perhaps this is configurable.

- Each **query widget** provides the following options:
    - "Rename"
    - "Edit"
    - "Delete"

- Each **table widget** provides the following options:
    - "Hide"
    - "Edit a copy of this query" -- This is a link similar to the "Add Query" button which directs the user to the Data Explorer, but it also passes the id of the foreign key used in the table widget. The Data Explorer then builds a query to match the behavior of the table widget and allows the user to save it as a new query. The table widget will remain unmodified and visible, leaving the user with two very similar widgets. At this point the user can choose to distinguish between the two by either hiding the table widget or renaming the query widget.

- Above all widgets, a "Show Hidden Queries" dropdown button exists giving the user the capability to un-hide any table widgets widgets they have hidden.

- Each widget is collapsible via a triangle icon to the left of its title. The collapsed/expanded state per-widget is persisted via local storage and will apply to all records within this table.
    
- The default ordering of widgets is not defined, but users *can* re-order all the widgets as as they so choose.

    The mechanism for re-ordering the widgets is subject to further UX experimentation. Drag and drop would seem to be an obvious choice, though the height of each widget (when expanded) would make dragging cumbersome. It may be possible to collapse all widgets when the user initiates a drag, however the user's cursor might jump around on the page if we do this. Another idea is a drop down menu in which the user can re-order the widgets. This menu could potentially contain UI to show/hide the widgets too!

    The user can intermingle table widgets with query widgets. New query widgets are displayed on top. New table widgets are displayed on bottom (which allows for a data structure where the table widgets have optional sorting weights).
