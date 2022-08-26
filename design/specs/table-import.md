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

## Navigating to the Data Import page

Data import navigation link will be found on the active schema page. Once clicked the user will be taken to select upload method screen.

## Importing data into a new table

### Selecting upload method
![](https://share.balsamiq.com/c/uhmhbecvbb8cji2LVGFRWo.png)

First step for the import is selecting the upload method. On the select upload method screen there are three action cards that will take user to a respective method mentioned in the [uploading the data file section](#uploading-the-data-file)

### Uploading the Data File
There are three methods for uploading the data file -

#### Drag & Drop or Browse
![](https://share.balsamiq.com/c/Lhu3yxutZVoXivwcKPtT1.png)

Once the user selects this upload method, the user gets clickable area where the user can drag & drop a local file or click on it for browsing the file locally. The user can go back to the select upload method screen by `Select another upload method` button.

#### URI
![](https://share.balsamiq.com/c/r7fmqfwG2hmjTTbwvMRehr.png)

Once the user selects this upload method, the user gets an input text block for URI where they can paste valid URI and click on continue to upload the file. The user can go back to the select upload method screen by `Select another upload method` button.

#### Copy & paste data
![](https://share.balsamiq.com/c/uC1C6dxPCze6oiHHTAkAvt.png)

Once the user selects this upload method, the user gets a textarea to paste data for the table. Once the data is valid, the user can upload by clicking on the continue button. The user can go back to the select upload method screen by `Select another upload method` button.

### Processing Uploaded File
![](https://share.balsamiq.com/c/9d1wf4y7cgBUawWbdcoThs.png)

This is the stage where the uploaded file is processed. The user sees the progress and updates related to the import here. 

#### Status Indicators

On the processing screen there is a progress bar which indicates where the upload and import process is. There will also be small messages below the progress bar to keep user informed about the process/status.

The user can also cancel the import by clicking on the cancel button. But the user will have to confirm the cancellation by the modal in [Abandon scenario](#abandoning-the-file-processing-step)

### Errors 
![](https://share.balsamiq.com/c/asGm1LMUCEvjCd1jBdcDEA.png)

If there is any error in the import, the user will see the data import screen again. And there will be a error message at the top of the screen.

### Confirmating the uploaded table
![](https://share.balsamiq.com/c/g1YFz8wYRm71tQ5W6skCX7.png)

#### Components

##### Table name
The user can rename the table on the confirmation stage. 

##### Use first row as header
This is a check box. If checked, the user can use the first row as the header.

##### Table summary
There is a small table summary above the table. 

##### Table 
The table's first row are headers. This row has checkbox which is when checked the column is included in the table. The second row has the data type of the column. 

##### Table height
Since multiple scrolls on the screen is a bad UX. I propose limiting table's height to a certain percentage of the screen height. The percentage might be more clearer when we include styling part here. But as far as I think 25-35% of screen height for the table would suffice. 

#### Changing data type
![](https://share.balsamiq.com/c/agFL3gk3gc7pkgjc2GUcw3.png)

When the settings beside the data types is clicked, the user is presented with a choice of compatible data types. The compatible data types will be similar to the table view. The data options will not be available at this point. 

### Abandoning the import 
The user can abandon import process at ceratin points in the journey.

#### Abandoning the import at processing stage
![](https://share.balsamiq.com/c/8WvP45gNpqAm3UYUM1r3m2.png)

If the user abandons the import at the processing stage, the user will be given a warning in form of modal to notify that if they abandon this they will lose the file.

#### Abandoning the import at confirmation stage
![](https://share.balsamiq.com/c/6XqnBjSAk2FUAK8DyexoU5.png)

If the user abandons the import at the confirmation stage, the user will be given a warning in form of modal to notify that if they want to abandon it or not.

### Uncomfirmed table on the schema page
![](https://share.balsamiq.com/c/vr3pvTp1cUsMJw7gb8xNKY.png)