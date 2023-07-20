---
title: Adding, Update and Deleting Records
description: 
published: true
date: 2023-05-11T14:31:37.390Z
tags: 
editor: markdown
dateCreated: 2021-06-28T17:47:57.446Z
---

# Figma Prototype
<iframe style="border: 1px solid rgba(0, 0, 0, 0.1);" width="800" height="450" src="https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Fproto%2FUaf1ntcldzK2U41Jhw6vS2%2FMathesar-MVP%3Fpage-id%3D1064%253A0%26node-id%3D1066%253A0%26scaling%3Dscale-down-width" allowfullscreen></iframe>

# Context
Adding records will be an essential part of an inventory system as users will have to update their inventory to reflect changes. For example, if users added a new item to their list, we should allow them to update their inventory by adding records to the relevant database table.

# User Experience
The user experience for adding, editing, and deleting records should make table modifications seamless, intuitive, and visual. For example, users should do so without following any specific data entry order and across multiple records at once when adding and editing records. Errors, if present, shouldn't block the user from performing other actions and should be easily corrected from the UI.

## Scenario: Adding a Record
### User opens a table
The user starts adding a record by opening the table in which they wish to add the record. They must have write permissions to insert the record.

An empty row should be placed at the bottom of every table so that users can easily add rows.

#### Review Notes
- 

![](/assets/design/specs/add-update-delete-records/PTp51fp.png)


#### When the last row is not visible
The user can trigger the add row action from the top menu options. The table should then scroll to where the new row is positioned.
 
![](/assets/design/specs/add-update-delete-records/XK61ZO6.png =160x)

### user selects any new row cell
Users can select a cell and start editing its contents by double-click or on key-down on the selected cell. The user could also paste clipboard data into a selected cell. 

![](/assets/design/specs/add-update-delete-records/6KnTJfR.png)

- The new row is the last row of a table
- Once they start to edit the new row, the row number is assigned, and an asterisk is used to represent the unsaved state
- Another new row is added to the bottom once the existing one is assigned a row number

### user enters data into each field
Once a cell is in edit mode, the user can modify its content as needed. The content has to be valid for each specific data type. However, users are allowed to enter any value and change the data type before saving. 

![](/assets/design/specs/add-update-delete-records/IqIKvbi.png)

- The user can fill out the columns in any order, as long as they complete all required columns before saving.
- If multiple rows are added, users can fill out columns on more than one. However, all would have to be error-free for the save action to work
- Only one column at the time can be filled (multiple select is not possible)

### User enters an invalid value
The user enters invalid data, and as a response, the system shows a visual indicator for the affected table cell. The visual indication will remain until the error is resolved. The user can hover over the affected cell to display an explanation of why it is failing. 

![](/assets/design/specs/add-update-delete-records/6EjAxO9.png)

Attempting to save a table with errors will result in a dialog asking the user to fix the errors before continuing to the save step.

![](/assets/design/specs/add-update-delete-records/kETg4x2.png =400x)


### user saves the new record
Once the table is free of errors, the user can click the save button to save the record. After this, the user will see the record added to the table.
![](/assets/design/specs/add-update-delete-records/vzJIXPL.png)

#### If the edited cell column is affected by a filter, sort, or group condition.
If the value of the edited cell is affected by a table display property, the row should move to its new position on save and not after edit. 


## Scenario: Updating a Record

### user selects a cell from an existing record
Users can do table modifications on existing records by enabling edit mode on any cell. 

![](/assets/design/specs/add-update-delete-records/UJE4o2J.png)

## Scenario: Deleting a Record

### User selects a row
Users can select rows by a single click on any table cell or by clicking on a row number indicator.

![](/assets/design/specs/add-update-delete-records/mDe3Vpr.png)

### User deletes a selected row
Deleting a row or multiple rows can be done from the 'Delete' dropdown menu. 

![](/assets/design/specs/add-update-delete-records/i9t1LFe.png =140x)

### user deletes multiple rows
To select multiple rows, users must select them from the number indicators rather than at the table cell level while pressing the shift key or command key for multi-selection.

![](/assets/design/specs/add-update-delete-records/ZC0uhJp.png)

## Interactions

### Save Status Indicators
Any changes to a table should trigger the save status to change. This is represented visually at the modified table object level and the table itself. Users can't save changes individually. And instead, they can be saved in batches. 

![](/assets/design/specs/add-update-delete-records/3LD4REZ.png)

![](/assets/design/specs/add-update-delete-records/Tif1Pcx.png)



### Selecting rows
Users can select entire rows if they wish to copy their contents, delete them, or perform other row-level actions. 

![](/assets/design/specs/add-update-delete-records/GXqOHol.png)

However, any selected cell will automatically set the row and columns to which it belongs as selected. The system will target any row or column action level actions to the current selection.

![](/assets/design/specs/add-update-delete-records/WaEWViQ.png)

## Implementation Notes
- The table toolbar component introduced for the design of this feature could also be used to trigger the table properties panel discussed on the previous [feature specs](/design/specs/filter-sort-group)

## Additional Review Notes

### Accessing new record row
Access to the new record row control is provided via the table's toolbar and table navigation controls.

![](/assets/design/specs/add-update-delete-records/sbz7eIR.png =340x)

#### Last row visible
When the last row is visible, users can simply click on the new record row and activate it. 

<iframe style="border: 2px solid rgba(0, 0, 0, 0.1);" width="800" height="450" src="https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Fproto%2FUaf1ntcldzK2U41Jhw6vS2%2FMathesar-MVP%3Fpage-id%3D1064%253A0%26node-id%3D1066%253A0%26viewport%3D-3518%252C558%252C0.6873981952667236%26scaling%3Dscale-down-width" allowfullscreen></iframe>

#### Last row not visible
When the number of rows exceeds the visible portion of the table, a user can navigate to the bottom of the page by using the page navigation control.

![](/assets/design/specs/add-update-delete-records/GmtmLaj.png =140x)

<iframe style="border: 2px solid rgba(0, 0, 0, 0.1);" width="800" height="450" src="https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Fproto%2FUaf1ntcldzK2U41Jhw6vS2%2FMathesar-MVP%3Fpage-id%3D1064%253A0%26node-id%3D1246%253A157%26viewport%3D-3518%252C558%252C0.6873981952667236%26scaling%3Dscale-down-width" allowfullscreen></iframe>

### Order and Filter Independence
If a row's position or visibility is affected, a notice will be displayed when the user hovers over the row.

![](/assets/design/specs/add-update-delete-records/wvKnuSQ.png)

### Required Fields
If a record has required fields, the system won't save the new record until all the necessary fields are filled.

![](/assets/design/specs/add-update-delete-records/cwG5AQ7.png =240x)

<iframe style="border: 2px solid rgba(0, 0, 0, 0.1);" width="800" height="450" src="https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Fproto%2FUaf1ntcldzK2U41Jhw6vS2%2FMathesar-MVP%3Fpage-id%3D1064%253A0%26node-id%3D1345%253A2113%26viewport%3D-3518%252C558%252C0.6873981952667236%26scaling%3Dscale-down-width" allowfullscreen></iframe>

### Save Status
The saved status is displayed on the table toolbar and changes based on the save status of all modified rows.

![](/assets/design/specs/add-update-delete-records/3RYqaUH.png =240x)

### Disabled State while Syncing Changes
While saving is in the process, the system will block the affected rows from editing.

<iframe style="border: 2px solid rgba(0, 0, 0, 0.1);" width="800" height="450" src="https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Fproto%2FUaf1ntcldzK2U41Jhw6vS2%2FMathesar-MVP%3Fpage-id%3D1064%253A0%26node-id%3D1345%253A2844%26viewport%3D-3518%252C558%252C0.6873981952667236%26scaling%3Dscale-down-width" allowfullscreen></iframe>

### Contextual Menu
Opening a menu on right-click was discussed and will be considered for a future iteration.

![](/assets/design/specs/add-update-delete-records/sbz7eIR.png =340x)

#### Last row visible
When the last row is visible, users can simply click on the new record row and activate it. 

<iframe style="border: 2px solid rgba(0, 0, 0, 0.1);" width="800" height="450" src="https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Fproto%2FUaf1ntcldzK2U41Jhw6vS2%2FMathesar-MVP%3Fpage-id%3D1064%253A0%26node-id%3D1066%253A0%26viewport%3D-3518%252C558%252C0.6873981952667236%26scaling%3Dscale-down-width" allowfullscreen></iframe>

#### Last row not visible
When the number of rows exceed the visible portion of the table, a user can navigate to the bottom of the page by using the page navigation control.

![](/assets/design/specs/add-update-delete-records/GmtmLaj.png =140x)

<iframe style="border: 2px solid rgba(0, 0, 0, 0.1);" width="800" height="450" src="https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Fproto%2FUaf1ntcldzK2U41Jhw6vS2%2FMathesar-MVP%3Fpage-id%3D1064%253A0%26node-id%3D1246%253A157%26viewport%3D-3518%252C558%252C0.6873981952667236%26scaling%3Dscale-down-width" allowfullscreen></iframe>

### Order and Filter Independence
In the case that a row's position or visibility is affected, a notice will be displayed when the user hovers over the row.

![](/assets/design/specs/add-update-delete-records/wvKnuSQ.png)

### Required Fields
If a record has required fields, the new record won't be saved until all required fields are filled.

![](/assets/design/specs/add-update-delete-records/cwG5AQ7.png =240x)

<iframe style="border: 2px solid rgba(0, 0, 0, 0.1);" width="800" height="450" src="https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Fproto%2FUaf1ntcldzK2U41Jhw6vS2%2FMathesar-MVP%3Fpage-id%3D1064%253A0%26node-id%3D1345%253A2113%26viewport%3D-3518%252C558%252C0.6873981952667236%26scaling%3Dscale-down-width" allowfullscreen></iframe>

### Save Status
The save status is displayed on the table toolbar and changes based on the save status of all modified rows.

![](/assets/design/specs/add-update-delete-records/3RYqaUH.png =240x)

### Disabled State while Syncing Changes
While saving is in process the affected rows will be blocked from editing.

<iframe style="border: 2px solid rgba(0, 0, 0, 0.1);" width="800" height="450" src="https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Fproto%2FUaf1ntcldzK2U41Jhw6vS2%2FMathesar-MVP%3Fpage-id%3D1064%253A0%26node-id%3D1345%253A2844%26viewport%3D-3518%252C558%252C0.6873981952667236%26scaling%3Dscale-down-width" allowfullscreen></iframe>

### Contextual Menu
Opening a menu on right-click was discussed and will be considered for a future iteration.
