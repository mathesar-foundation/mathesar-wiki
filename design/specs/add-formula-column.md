---
title: Listing Views Spec
description: 
published: true
date: 2022-06-20T08:24:04Z
tags: 
editor: markdown
dateCreated: 2022-06-20T08:24:04Z
---

## Context

In addition to data columns, we have formula columns as well. These columns are basically derived from a formula. A formula may or may not use another data column to generate the formula column. The formula can also use parameters of different data types other than columns. 

The formula columns can only be created with Data explorer. For more details, you can check out this [link](https://wiki.mathesar.org/en/product/specs/2022-01-views/04-formulas)

## Scenarios

### Scenario 1 - Add a formula column without clicking outside of the inspector.

![](https://share.balsamiq.com/c/dS6sAay4Re9f2R39zKDDj8.png)

On the left hand side of the explorer view, there is a  `Add Column`  button. When user clicks on it, there are two options visible to them. One is `Add direct column` and the other is `Add formula column`. To add a formula column user will need to click on `Add formula column`. 

Once the user clicks on `Add formula column` option, the inspector shows formula settings that include `Name` input of the formula and a list of formulas to select from. The list of formulas is described in detail in the component section. 

If the name is left empty by user for the next steps, there is a default name given to the column that is ColumnX. X is the number given to the column. For instance if its the first default named column it will be Column1.

Once the user decides on what formula they want, the inspector shows relevant inputs for formula selected. The parameters can be of different data types depending on the selected formula. Parameters of the selected formula are described in scenarios below. 

Before adding the parameters (if they are required), user would be able to see a preview of an empty column. 

Once the user adds correct parameter the empty column gets filled with the calculated date and the user is able to preview the filled column. If they are not satisfied by the results they can change the formula selected as well as the parameters before adding the column to the query, this scenario is covered under edit column scenario.

The `Add column` button in the inspector adds the column to the query. This button is only clickable if the column is filled. 

Once the generated column is added to query, and user is satisfied by it, user can jump to closing the data explorer. That action will take them to a modal where they are asked to save the query which saved the column to the table permanently. If they do not want to save it they get the option of closing without saving. To cancel the action they get a cross button on the modal.


#### Scenario 1.a - Add a random generation type formula column

The random generation type formula generates random numbers or UUID. For random number generation, the user just have to provide upper and lower bound with the decimal flag. There is no column input when it comes to random generation type formulas. Hence, the successful generation of the random generation type column is shown below. 

![](https://share.balsamiq.com/c/2ud3EckJJ5TeEX1SMR1D7Y.png)

#### Scenario 1.b - Add a text type formula column

The text type formula works on columns with text data type. There can be different parameters depending on what the formula is. For instance, there are `starting index` and `count` here in the example below.

![](https://share.balsamiq.com/c/p3ta6G69SiMgL61XYZg24m.png)

#### Scenario 1.c - Add a number type formula column

The number type formula works on columns with number data type. There can be different parameters depending on what the formula is. For instance, there is `comparison sign` here in the example below.

![](https://share.balsamiq.com/c/5si6jjAr1FPZ39bw968N5N.png)

#### Scenario 1.d - Add a date & time type formula column

The date/time type formula works on columns with date/time data type. There can be different parameters depending on what the formula is. For instance, there is `precision` here in the example below.

![](https://share.balsamiq.com/c/bXgh99SMozaUyBNvQHa1g8.png)

#### Scenario 1.e - Add a cumulative type formula column

The cumulative type formula works on columns with any data type. There can be different parameters depending on what the formula is. It basically shows how data in one column is changing with the help of different mathematical equations.

![](https://share.balsamiq.com/c/sqqrcNeq3CVQaUtZiBG9ov.png)

#### Scenario 1.f - Add a boolean type formula column

The boolean type formula works on columns with boolean data type. There can be different parameters depending on what the formula is. For instance, there is `condition` here in the example below.

![](https://share.balsamiq.com/c/nBHVJCNiZ2PgJMrn1wdGcL.png)

#### Scenario 1.g - Add a regular expression type formula column

The regular expression type formula works on columns with any data type. There can be different parameters depending on what the formula is. It basically is to determine if there are any patterns in the data of a column. 

![](/https://share.balsamiq.com/c/dNYLKaCt4oJAgZ9qE7rFy4.png)

#### Scenario 1.h - Add a list type formula column

The list type formula works on columns with list data type. There can be different parameters depending on what the formula is.

![](https://share.balsamiq.com/c/wnDL3cvcR9R3cgPwR3Co2.png)

### Scenario 2 - Adding an erroneous parameter to the formula 

Parameters of different formulas accept columns of different data types and values of different data types. The erroneous parameter here means the data type of the entered value or column is incompatible with the formula. 

For instance, the length formula expects a list value or a list type column as an input to the parameter `List` but it gets a text type column which is movieNames and hence throws an error and the user is not able to see a filled column.

![](https://share.balsamiq.com/c/p2oHazbJvtdHNADo1nBB4p.png)

### Scenario 3 - Edit a formula column 

#### Scenario 3.a - Edit a formula before adding the column

Before adding the column, user can edit the formula with no constraints. 

Case 1 - Edit parameters before adding column.
Parameters can be easily edited at this point. To not run into errors, the users would just have to take care of the data type compatibility.

Case 2 - Change the formula before adding the column
This can also be easily done. The user just have to select another formula from the selection list. Then they will be able to see the parameters relevant to the selected formula and they will be empty. 

#### Scenario 3.b - Edit a formula after adding the column

Users can only change the parameters after adding the column to the query. Again users might run into errors if they enter incompatible values/columns. More details TDB. 

### Scenario 4 - Click outside the inspector

#### Scenario 4.a - Clicks outside before adding name or selecting formula

If the users click outside the inspector before even touching the formula settings that is adding name or selecting formula, there won't be any empty column added. And there would be absolutely no change in the explorer.

#### Scenario 4.b - Clicks outside after adding name or selecting formula

If there is any activity in the formula settings that is if the name of the column is added or the formula is selected, an empty column will be added. 

Once users click outside, they will see a warning on the column so users know there is something left to do with the formula column. 

![](https://share.balsamiq.com/c/79ZrfbdaMgz8rfuHN3bRDY.png)

#### Scenario 4.c - Clicks outside after successfully adding the formula

If the formula and its parameters are added successfully and the preview column is filled. When the user clicks outside the preview is still visible. The user will get the inspector view of formula back if they click on the column. 

![](https://share.balsamiq.com/c/dS6sAay4Re9f2R39zKDDj8.png)

#### Scenario 4.d - Clicks outside after adding erroneous parameters

If the users have added erroneous parameters then they click outside the inspector, the parameter values will be lost and they will see a similar empty column preview with a warning. 

![](https://share.balsamiq.com/c/p2oHazbJvtdHNADo1nBB4p.png)

### Scenario 5 - Quit the explorer

#### Scenario 5.a - Quits the explorer before adding the column

Case 1 - The preview column is empty
If the preview column is empty, there won't be any save changes warning modal. Since there are no significant changes and there is nothing to be saved. The modal would only have a warning about whether to close the explorer or not.
![](https://share.balsamiq.com/c/ffSKeCLi8D3DXfkRN8qrV1.png)

Case 2 - The preview column is filled
If the preview column is filled but not yet added to the query, the user will be asked in the modal if they want it to save it to the query directly or just close the explorer without saving anything.
![](https://share.balsamiq.com/c/79ZrfbdaMgz8rfuHN3bRDY.png)

#### Scenario 5.b - Quits the explorer after adding the column
If the column is added and the user quits the explorer after adding the column to the query. The user would see a modal whch asks them to whether save the query or close without saving.
![](https://share.balsamiq.com/c/79ZrfbdaMgz8rfuHN3bRDY.png)

## Interactions

### Modal for warning before qutting the explorer

The modals are for warning the users about the consequences of closing the data explorer. There is no action for saving query in the data explorer view. The modal provides the action of saving the column if there are significant changes that is there a filled preview column. If there are no significant changes there is only warning of closing the data explorer.

![](https://share.balsamiq.com/c/5Y3TjZ551mZdf5Q4cpBCNi.png)

### Column preview while adding the formula

The column preview is necessary for the user to see the reflected changes when they interact with the formula settings. The different states of the column preview can be seen below. 

1. Active empty column preview (Green highlight) - Users will see the active empty column preview when they are interacting with the formula settings in the inspector.

2. Inactive empty column with a warning (Yellow highlight) - Users will see the inactive column preview with a warning when the user has click outside the inspector. 

3. Erroneous empty column (Red highlight) - Users will see erroneous column when there are errors in formula settings inputs.

![](https://share.balsamiq.com/c/bhzoPkNR4MtQnpb4mB2hws.png)

### Parameter inputs

The parameters have two kinds of inputs that are values and column names. A parameter can accept both or either. But the parameter that accepts both have a prefix that the user needs to select for distinguishing what type of input they have chosen. There is a painless dropdown to do so as seen below.

![](https://share.balsamiq.com/c/4nmcRjLxr3mHpngZxFDZfx.png)

### Error messages

## Components

### Add column button

The user can only add formula column through data explorer. But the user can add two types of column through the data explorer so on clicking the `Add column` button the user sees a drop down to select from. The dropdown consists of - 
1. Add direct column - The column that has direct data.
2. Add formula column -  The column which is generated using a formula.

![](https://share.balsamiq.com/c/iwXpHctgMSRNcYQjeY7MBe.png)

### The formula selection menu

The formula selection menu is quite long since there are a lot of formula to choose from. To reduce the strain, the dropdown is divided into categories of formulas that are text, number, random generator and so on. There is search option where user can search the category or the formula name to directly use a formula. There is a recent section where the user can see their last three used formulas to quickly jump on that.

![](https://share.balsamiq.com/c/svLZHynK3NqVkjofBmqgMj.png)

### Add column to the query button

There are two add column buttons in the view. This button exists in formula settings column. This will add the column to the query. Once the user is satisfied with the column preview, the user can go ahead and add the column to the query and further save it if they want.

### Quit explorer button

Quit explorer lets the user to quit the data explorer view. The action is followed by a modal and those are explained in the [warning modal section](#modal-for-warning-before-qutting-the-explorer).

