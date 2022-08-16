---
title: Add Table from Import/URI/Data paste Specs
description: 
published: true
date: 2021-08-18T13:45:20.499Z
tags: 
editor: markdown
dateCreated: 2022-08-10T21:03:22.324Z
---

# Context
Adding a new table from a file import allows users to input data into Mathesar without populating tables manually. This feature is also convenient for users who need to import data for testing Mathesar's functionality.

While data file import is a baseline feature for most applications in this category, additional functionality will be implemented in the future to enhance the data import process, such as automatic type detection, data cleansing, error detection, and others.

# User Experience

## Navigating to the Data Import page

![](https://share.balsamiq.com/c/p3dqSXr66qa6EnPyykqpyZ.png)

Data import navigation link will be found on the active schema page. Since we are only allowing users to import tables for now, positioning it with the existing tables/ active schema view made sense. 

## Importing data into a new table

![](https://share.balsamiq.com/c/w2AbsJLMY5Qwt4aGDuozLN.png)

### Defining the New Table

When the user jumps to the upload view. They see a name input which can be added or not added. If not added by user the table will be given a default name and that can also be changed in the confirmation view.

### Uploading the Data File

#### File Upload Methods

There are three main blocks that specifies three ways to upload the file/data for import. Each block has some important description with it. Each active way is highlighted when in use.

##### Local File

The local file on the disk can be uploaded by dragging to the block or clicking on the block. Once the user drag the file to the block or select the file from their local machine, they can see the processing view.

##### URI

User can paste a URI in this block. If the URI is valid, the user would be able to click on the continue button to move to the processing import view.

##### Paste

User can paste data directly here in this block. If the data pasted here is valid, the user would be able to click on the continue button to move to the processing import view.


#### Import Options

There are a few flags that user will find helpful for the import process. And they are present on the upload view itself. 

##### Data Type Inference

This is a checkbox input. So when the checkbox is checked, the data type inference will not happen while the import process. This would make the import process faster and in some cases, the process possible too. The user would then have to select the data types in the confirmation stage. 

If not checked, the data type will be detected and this might take a longer time and sometimes the import might not even happen. The user can still change the data types in the confirmation stage.

##### Skip Warnings

This is again a checkbox, if checked he user would not be notified with any warnings related to the import process. This way when there are situations, the defaults will be considered and the user won't be informed about it.

##### Automatic Delimiter Overwrite

This is an input field where user can enter a deliminator used in their file. The default is taken as a comma(,). 

### Processing Uploaded File

This is the stage where the uploaded file is processed. The user sees the progress, warnings and errors related to the file here. 

#### Status Indicators

On the processing screen there is a progress bar which indicates where the upload and import process is. There will also be small messages below the progress bar to keep user informed about the process/status.

#### File Processing Errors and Troubleshooting

![](https://share.balsamiq.com/c/mo3WasYJpME3uCDc9dmuaW.png)

##### Invalid file type 

The user cannot upload files other than CSV/TSV. They will have to reupload it in such case.

##### Invalid header

When there are invalid headers. User will get an option of ignoring the headers.

There might also be a case where they have to reupload the file so then we wont be showing ignore headers modal to them.

##### Missing row data

When the row data is missing, the message consists of row number. The user might get the option of skipping that row and move forward.

In some cases the user might have to upload the file again.

##### File too large

The data inference of some files might take too long so there is an option for users to skip it.

But sometimes the memory just runs out so the user would have to reupload a new file.

##### File is corrupt

No particular insightful messages. User will have to reupload new valid file.

##### Date type error (Format errors)

Q - Not very sure about this.

##### Invalid data paste

##### Invalid input in the confirmation state of a record
Q - Is there an validation for data input in the table confirmation

As much as I have seen it in staging. The iput validation will be similar as table view. And if the user confirms the table with erroneous records, the values will be set to null.

#### Abandoning the File Processing Step

![](https://share.balsamiq.com/c/m6Ui2naMGZXijJgjcaF15f.png)

Since technically background/parallel imports are difficult, we wont be supporting in the user journey as well. When the user tries to move away there is a warning modal that warns them that they would lose the progress and they would land to the first screen if they land back to the import. 

### Confirming Imported Data

![](https://share.balsamiq.com/c/ds5qgkUM5bhGBWvkucdWnT.png)

When the import is successful, the user lands on the active confirmation view.

#### Go back button

 This will take them to import screen. So before that there will be a warning modal which is listed in [Behavior section]. If the table gets confirmed it is added to the schema or else its discarded.

#### Selected file section

This consists of the file the user uploaded. They can access it from here when they click on it. If the reupload button is selected it has a similar behavior like go back button.

#### Table name

The input has a default name that can be changed by user there itself.

#### Import Summary (Total Records, Columns)

This has a small summary like number of rows, records etc. The missing data link will take them to the first row that has missing data(Not sure that is possible technically TBD). Similarly the duplicate column link takes the user to the first duplicate column(Not sure that is possible technically TBD).

#### Options

- Use headers - This will use the first row as headers if selected or else there will be default column names. This will remove duplicate column scenario.
- Set missing data as null - This will set missing data as null and remove missing data scenario.

#### Verifying and Updating Data Types

This is similar to the data options menu for the table view. But there are small differences to remove Cognitive load on user -

1. Removal of options like filtering, sorting etc since it might not be that useful to user at this point.
2. Removal of options which are related to adding new data like set default value. Since we are not allowing user to add data at this stage keeping these options can be avoided. However all the options related to the data type and data format will be intact since this might be a deciding factor. 

Q - Are we allowing user to add column or a record at this stage? If not are we gonna do that in future?

##### Allowed Data Type Changes

The data type changes behavior will be similar to that of table data type changes. User will be able to switch to compatible data types so they do not lose the data.

##### Revert Data Type Change

User can change the data types to the other compatible ones at any moment in the confirmation stage. 

#### Exclude Columns from Import

Each column has a checkmark on the side. If selected the table will have the column or else it will be excluded from the table. 

The duplicate columns will be unselected by default. To select them, the user will have to rename them. Until then the checkbox will be grayed out. 

#### Abandoning the Confirmation Step

![](https://share.balsamiq.com/c/ajPCXuhshEjRMvJXMLb5Xu.png)

Handling unconfirmed table in different scenarios might be difficult so the solution I propose for it is blocking the user to navigate away before confirming or dumping the import.

## UI Components

### File Upload Method Selector

![](https://share.balsamiq.com/c/jyszUUBfSvoCqd6qWQcz3G.png)

To select the method to upload the file there will be vertical tabs to select the method. There will be a rectangular space attached to the tabs. This space will be dedicated to the upload method selected. 
- For drag and drop, the user would have to drag and drop the file to the rectangular space or click the button to open file browser.
- For URI, paste the URI in the input box. Once the URI is valid the user can click on continue.
- For paste data, paste the data into the text area. Once the data is valid the user can click on continue.

### Preview Table height

Since multiple scrolls on the screen is a bad UX. I propose limiting table's height to a certain percentage of the screen height. The percentage might be more clearer when we include styling part here. But as far as I think 25-35% of screen height for the table would suffice. 