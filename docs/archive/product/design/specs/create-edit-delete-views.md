# Create, Edit, Delete Views

!!! danger "Danger"
    This spec is outdated and should not be followed.


## Context
A view is a database object based on one or more database tables and contains no data of its own. In the context of Mathesar, the creation and editing of these views is an essential part of the user experience, as it allows users to join and simplify tables into one or represent a subset of the data from a table. For the less technical users, views might be a stepping stone towards analyzing and visualizing their data. For that reason, the design aims to make views easy to discover and edit.

## Prototype
[Prototype for creating, editing, and deleting views](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?page-id=4156%3A34396&node-id=4536%3A41534&viewport=324%2C48%2C0.76&scaling=contain&starting-point-node-id=4536%3A41534)

## User Experience
### Scenarios
#### A user creates a view from scratch.
A user can create a view from scratch by clicking on the 'Add View' button. Since views require a table to be selected, a 'New View' dialog will be presented to the user. From here, they can name the view, select a table and one or multiple columns. 

#### A user creates a view from an open table.
A user might want to create a view to retain applied filters or sorts or add columns from other tables when working on a table. To do so, the user can click on the 'Save as View' button on the table's toolbar, which will automatically create a view and open it.
 
##### Views from filtered tables
A user might want to preserve a particular combination of views, sorts, and groupings as a view, in which case they can create a view after applying the filtering, sorting, or grouping parameters or do so from the view and then proceed to save the view. 
[Prototype for creating a view from the filtered table](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?page-id=4156%3A34396&node-id=4800%3A54681&viewport=324%2C48%2C0.79&scaling=contain&starting-point-node-id=4800%3A54681&show-proto-sidebar=1)

#### A user adds new columns to a view.
Once in the view, a user might want to add additional columns. For this purpose, the same 'Add Column' control used in tables will be available. However, it will display a menu to select columns from available tables in the context of views. 
Available tables will be those that have a foreign key relationship with the already selected tables. Otherwise, they will not be listed. 

#### A user removes columns from a view.
A user can remove columns from a view by selecting the 'Delete Column' option in the column header menu. However, in a view, a column from a table will condition other table relationships. If the user removes the only reference to a table, this might impact the list of different tables from which the user can select columns. 

#### A user deletes a view.
A user can delete a view from the 'View Options' menu in the view toolbar. 
As with other database objects within Mathesar, the system should provide a warning if the view deletion affects other views.

#### A user can see the tables and columns that are referenced in the view.
A user might want to navigate to or modify the tables that are referenced in a view. They should be able to do so by following the 'Go to Referenced Table' option in each column's header menu. 

#### A user can see the query that generated a view.
In views created through complex queries, we might not allow editing. Still, users can see the query that generated them by clicking on the 'Open View Query' in the 'View Options' menu.

## Review Notes
### Using Color to Represent Table Relations
The UI for views should incorporate ways to represent the different tables that make a view. Elements like color could be applied as demonstrated in the prototype. A future document will include more details in the global document once all design issues for this milestone are completed.