---
title: Import Status
description: 
published: true
date: 2021-07-16T16:56:42.165Z
tags: 
editor: markdown
dateCreated: 2021-07-08T12:22:29.972Z
---

# Context
The initial design for [Add Table from File Import](https://wiki.mathesar.org/en/design/specs/table-import) defined all the steps needed to import a file, preview its content, make adjustments and save it as a table within Mathesar. However, certain aspects of the upload process and status lack definition for implementation as reported on the issue [#296](https://github.com/centerofci/mathesar/issues/296) on Github. This spec looks to address those gaps in the design.

# Prototype
[Import Status Indicator](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?page-id=2306%3A11983&node-id=2306%3A11984&viewport=556%2C470%2C0.5827216506004333&scaling=contain)

# User Experience
## User Starts Import from File
The user wants to add a table to an existing schema. From the data explorer view, they click on add table and choose the 'Import from File' method.

## User Uploads a File
The first step to creating a table from file import is to upload a valid file. The user selects a locally stored file, and the upload process begins. Once the file is ready to be imported, the user clicks on the 'Import' action. 
This action triggers a new state that persists while the file is being processed. Processing might take longer if the file contains many rows, as the resulting import will have gone through the type inference process.

## User Navigates to Another Tab
Given that a file might take a long time to process, a user could navigate away to continue work on another table or view. They might also want to import an additional table. In this case, the user needs the following:

- A way to know the status of their imports
- A way to navigate back to the corresponding import tab
- A way to respond to errors or cancel an import from anywhere in the app

## User Expands the Import Status Details
The user at any time can expand the file import component that shows active imports. Once expanded, they should be able to see all the files that are actively being processed. 

## User Navigates to a Tab Where a File Is Being Imported
By clicking on any of the files, the user can navigate back to the tab with the import in progress. From this view, a user might cancel the operation and go back to the previous step. 

# Review Notes

## Global Notifications
Global notifications are needed to help users keep track of ongoing operations and navigate back to the particular pages. The location of these notifications should be a permanent one that is always visible to users, especially in scenarios such as moving from one database or schema to another.

## Notification States
The content and layout of these notifications might change dynamically according to the number or type of operations. In a single operation, the notification might show specific details, such as the file's name being imported. Once more operations of the same type are added, it might change to offer a total count rather than details.

When operations are of a distinct type, the design might reduce the notification to only showing the number of operations, and users will find the actual type information in the dropdown.

### Scenarios

[Component Examples in Figma](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?page-id=2798%3A18566&node-id=2798%3A18763&viewport=1285%2C9%2C0.47174111008644104&scaling=min-zoom&starting-point-node-id=2798%3A18763)

#### If a single job is in progress
A single job in progress, such as importing a file, can be described with details such as job type and file name in the notification widget.

#### If multiple jobs of the same type are in progress
Various jobs of the same kind might run concurrently, in which case a total count replaces details such as file names. The user can find the file names under the expanded dropdown.

#### If multiple jobs of different types are in progress
If the jobs in progress are of different types, the job type is replaced by the general term jobs rather than the job-specific verbs.

#### If multiple jobs are in progress with some finished
If some jobs are finished, but some are still in progress, the status indicator will show the status of those in progress only.

#### If all jobs are finished
If all of the jobs are finished, the status indicator will change to indicate that all jobs are finished.

#### If any of the jobs failed
If any of the jobs running fails, the status indicator will change to indicate an error requiring attention.

