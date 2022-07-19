---
title: Record Page
description: 
published: true
date: 2022-07-19T17:50:20.851Z
tags: 
editor: markdown
dateCreated: 2022-07-18T13:41:06.809Z
---

# Record Page

## Context

The record page is a view that shows a single record from a table and offers functionality to let users read and update data in tables. As an additional feature, the record pages allow users to integrate queries for displaying linked records from other tables.

## Structure of the record page
> Not the final layout, but just an outline of what will be included on the record page, so take that into consideration when reading.
{.is-warning}

![image](https://user-images.githubusercontent.com/845767/179816131-71132b6e-c36d-4265-800a-02f6ae4d42c5.png)

### A.Record-Level Navigation 

The buttons for navigating to different records in the table will be located in the Record-Level Navigation. Users will also be able to search for a specific one using the record selector feature.

### B.Record Toolbar 

The record toolbar displays the [record summary](#record-summary) for the currently active record. The record toolbar label will also toggle a menu with record-related operations such as duplicate, delete, among others. Some action buttons will be located in the toolbar, similar to the toolbar in tables, however there is no definition of which actions will be provided at this time.

Once the entire flow is specified, this design is likely to change.

### C.Record Fields 

The record fields will be shown as a collection of input controls. As with tables, the input fields may be interacted with by users to modify the data. The fields will be presented in the same format and order as in tables. 

### D.Links to Record and Queries 

The record page will also have a section with links to the selected record. This work is currently being defined, and it is likely to change. However, the aim is to add a default query for the tables with connected records and present them as tables or visualizations that the user can edit.

Custom embedded queries created by users with Data Explorer will be used to define the tables' fields and options.

## Navigating to the record page

The navigation to and from records is an important factor to consider when designing the record page as it is intended to be integrated into various user flows.

### From the schema view via record selector
From the schema view, users may access the record page by selecting the 'record search' option from any of the tables provided. This will launch the record selector, allowing the user to go to a certain record.

![image](/assets/design/specs/record-page/179518507-ff971ee7-fc09-4c65-aaf0-df8a73743998.png)

> This is contingent on the new design for the listed tables, which will contain buttons for searching and adding entries right from the list item.
{.is-info}


### From the table page

Clicking on the primary key cell link in the table will take the user to a specific record.

![image](/assets/design/specs/record-page/179518645-c6892e7c-91c5-43a3-a940-b1977ad38d84.png)

### From the record page

The user can access other records from the record page by utilizing the record navigation controls at the top of the page. There is also a 'go to record' option in the record navigation controls, which opens the record selector component.


## Related Features

### Record Summary
Record summaries are strings that represent a record's data. They are specified by users and can include variable values from the record's fields, or include symbols and text characters. 
[Record Summary Spec](design/specs/record-summary)