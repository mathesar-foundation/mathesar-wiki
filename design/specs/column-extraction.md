---
title: Column Extraction
description: 
published: true
date: 2022-07-22T11:12:59.313Z
tags: 
editor: markdown
dateCreated: 2022-07-22T11:12:59.313Z
---

# Context
Tables must be split into smaller tables during the normalization process to ensure data integrity. To make this process easier, the product should include capabilities that allow users to restructure data by splitting, merging, and combining existing tables.
Initially, just table splitting will be implemented, so that a user can select columns from an existing table and create a new one.

# Splitting a Table by Extracting Columns
To create a new table from an existing one, select the columns to include in the new table. These columns must not be primary keys for the parent table (although they can be foreign keys to another table). Once selected, the inspector panel should display a list of possible 'Selection Actions,' with the 'New Table from Columns' option allowing the user to extract the columns into a new table.

## Selecting Columns
Columns must be given a new interaction in order to be selected. A column header can be selected by clicking on it, as in spreadsheet applications. Multi-selection is also possible by holding down the shift key and clicking on multiple column headers. Clearing the selection is as simple as clicking anywhere outside of the selection target or on a selected column once more.

## Selection Actions
Depending on a particular selection, the inspector panel will display actions that can be performed on the selection, as described above with columns. These selection actions will be determined by the type and number of items chosen.

# User Flow

1. **The user imports a table from a file**

    This user flow assumes that the starting point is an imported table containing columns that can be extracted and turned into entities. A column that may be transformed into a table or entity will usually include other columns that are attributes for that entity. If the database is not normalized, the entity to be extracted might include duplicated values. For example, consider a table of publications with multiple entries for the same publisher in the publisher column.

2. **The user selects the columns (attributes) for the new entity**

    The user chooses all the columns that will be attributes for the new object. For example, in the instance of the publisher, there could be columns for 'Publisher Name' and 'Publisher Id.' Including all the attributes is very important since columns cannot be moved after the fact.

     <img width="1512" alt="image" src="https://user-images.githubusercontent.com/845767/177544077-9f074830-ce64-4ed9-80bc-53de53977f9c.png">


3. **The user clicks on the 'Extract Columns' option**

    The user can choose to keep copies of the columns in the table if needed. By default the extracted columns are deleted.

4. **The user inspects the new foreign key column (link)**

    The new foreign key column will contain links to the new records that have been created. Additionally, when selected, the inspector panel will display the link properties.

    <img width="1469" alt="image" src="https://user-images.githubusercontent.com/845767/177546415-23b11ded-8987-4e69-ab1a-1decb9e773d3.png">


5. **The user navigates to the new table**

    The new table will be listed in the list of tables for the current schema. The user can modify the table, add new columns or rename it if needed.

    <img width="874" alt="image" src="https://user-images.githubusercontent.com/845767/177550009-30fcae81-2ae9-4539-ad85-5a0d1289790b.png">

# Unresolved Design Problems

## Extracting a foreign key column to create a mapping table
If a user had a foreign key referencing a publisher in a publications table and wanted to link to more than one publisher, could they select both the table's primary key and that foreign key and create a new table from both? Should there be a special action that does this without adding a foreign key in place of the columns?

## Suggesting columns to be extracted
Offering suggestions for columns that can be extracted into new tables would improve the feature's discoverability and provide users with a clear path to a better data model.

## UI for Inspector Panels
The inspector's UI is still in its early stages and should not be implemented without additional design work.

## Specify the table's name and foreign key column name
WIP
## Multiple column actions
WIP
## Allow Duplicates
WIP
## Selection
WIP
### Column vs. Cell Selection
WIP
### Row and Column Selection Consistency
WIP
## Inspector Modes
WIP
### Column
WIP
### Cell
WIP
### Row
WIP
## Keyboard Modifiers
WIP
### Touch-only devices
WIP
### Visual Cues
WIP
## Reordering Columns
WIP
## Cell-Only Selection
WIP