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

![](/assets/design/specs/add-formula-column/dS6sAay4Re9f2R39zKDDj8.png)

To add a column, the left hand side of the explorer view has an `Add Column` button. Once that is clicked, there are two options visible. Those are - `Add direct column` and `Add formula column`. 

After selecting `Add formula column`, an empty placeholder column is visible. The column also has a default name that is `formulaColumnX`. X indicates serial number of formula column with a default name.

The inspector on the right hand side shows a name input for the user to give a relevant name to the column. There is a formula selection dropdown for the user to select from. A detailed description of the selection menu can be found in [components section](#components)

Once the formula is selected, the formula settings will then be visible. If the user inputs valid parameters, they will be able to see results in the formula column. Invalid parameters are described in [this scenario](#scenarios-2b---the-formula-is-configured-incorrectly-and-returns-an-invalid-output).

If the user is satisfied with the result, they can save the query. 


#### Scenario 1.a - Add a random generation type formula column

The random generation type formula generates random numbers or UUID. For random number generation, the user just have to provide upper and lower bound with the decimal flag. There is no column input when it comes to random generation type formulas. Hence, the successful generation of the random generation type column is shown below. 

![](/assets/design/specs/add-formula-column/2ud3EckJJ5TeEX1SMR1D7Y.png)

#### Scenario 1.b - Add a text type formula column

The text type formula works on columns with text data type. There can be different parameters depending on what the formula is. For instance, there are `starting index` and `count` here in the example below.

![](/assets/design/specs/add-formula-column/p3ta6G69SiMgL61XYZg24m.png)

#### Scenario 1.c - Add a number type formula column

The number type formula works on columns with number data type. There can be different parameters depending on what the formula is. For instance, there is `comparison sign` here in the example below.

![](/assets/design/specs/add-formula-column/5si6jjAr1FPZ39bw968N5N.png)

#### Scenario 1.d - Add a date & time type formula column

The date/time type formula works on columns with date/time data type. There can be different parameters depending on what the formula is. For instance, there is `precision` here in the example below.

![](/assets/design/specs/add-formula-column/bXgh99SMozaUyBNvQHa1g8.png)

#### Scenario 1.e - Add a cumulative type formula column

The cumulative type formula works on columns with any data type. There can be different parameters depending on what the formula is. It basically shows how data in one column is changing with the help of different mathematical equations.

![](/assets/design/specs/add-formula-column/sqqrcNeq3CVQaUtZiBG9ov.png)

#### Scenario 1.f - Add a boolean type formula column

The boolean type formula works on columns with boolean data type. There can be different parameters depending on what the formula is. For instance, there is `condition` here in the example below.

![](/assets/design/specs/add-formula-column/nBHVJCNiZ2PgJMrn1wdGcL.png)

#### Scenario 1.g - Add a regular expression type formula column

The regular expression type formula works on columns with any data type. There can be different parameters depending on what the formula is. It basically is to determine if there are any patterns in the data of a column. 

![](/https://share.balsamiq.com/c/dNYLKaCt4oJAgZ9qE7rFy4.png)

#### Scenario 1.h - Add a list type formula column

The list type formula works on columns with list data type. There can be different parameters depending on what the formula is.

![](/assets/design/specs/add-formula-column/wnDL3cvcR9R3cgPwR3Co2.png)

### Scenario 2 - The formula column result is empty or erroneous

![](/assets/design/specs/add-formula-column/j2UsBsrGYshUtfTS6jcEQt.png)

#### Scenarios 2.a - The formula is configured correctly but returns no values

Whenever the user adds valid input there is a temporary feedback message below the input which says `Valid Input`. This is to notify them that there is nothing wrong in the formula configuration if they don't see desired column values.

#### Scenarios 2.b - The formula is configured incorrectly and returns an invalid output

If the formula parameters input are invalid, there is a temporary feedback message below the input which says `Invalid Input`. This is to notify them that the inputs are wrong and hence they might not see the desired column

#### Scenarios 2.c - The formula is configured correctly but a column referenced in the parameters is missing

When formula is configured correctly at first but if the column or the table which had that column gets deleted, the column data is retained but there is warning with an hoverable info message.

#### Scenario 2.d -  The formula is configured correctly but a column referenced in the parameters has a new invalid data type

When formula is configured correctly at first but if the column data type is changed to an incompatible one, the column data is retained but there is warning with an hoverable info message.

### Scenario 3 - Edit a formula column 

The formula can be edited anytime user wants. So there can be two scenarios on how users goes about changing the formula.

Case 1 - The user changes the parameters.
So here, user will be only given options for compatible columns. And if they want it to change it to a value, they can even do that. But an invalid value will again show `Error` in the column. 

Case 2 - The user changes the selected formula.
Once the user selects a different formula parameter values are not retained and they see empty parameters and an empty column again. To see the value they will have to add compatible params again.

### Scenario 4 - User clicks outside the inspector before saving

The outcome of this scenario is dependent on future Navigation so will be updated then.

### Scenario 5 - User closes the explorer without saving the query

The outcome of this scenario is dependent on future Navigation so will be updated then.

## Interactions

### Parameter inputs

The parameters have two kinds of inputs that are values and column names. A parameter can accept both or either. But the parameter that accepts both have a prefix that the user needs to select for distinguishing what type of input they have chosen. The columns list consists of columns with compatible data type only. User wont't be able to select a column that is not compatible. There is a painless dropdown to do so as seen below.

![](/assets/design/specs/add-formula-column/4nmcRjLxr3mHpngZxFDZfx.png)

## Components

### Add column button

The user can only add formula column through data explorer. But the user can add two types of column through the data explorer so on clicking the `Add column` button the user sees a drop down to select from. The dropdown consists of - 
1. Add direct column - The column that has direct data.
2. Add formula column -  The column which is generated using a formula.

![](/assets/design/specs/add-formula-column/iwXpHctgMSRNcYQjeY7MBe.png)

### The formula selection menu

The formula selection menu is quite long since there are a lot of formula to choose from. To reduce the strain, the dropdown is divided into categories of formulas that are text, number, random generator and so on. There is search option where user can search the category or the formula name to directly use a formula. There is a recent section where the user can see their last three used formulas to quickly jump on that.

![](/assets/design/specs/add-formula-column/svLZHynK3NqVkjofBmqgMj.png)

## Future work 

The Data Explorer save and close actions are dependent on other flows that are still being defined. This is likely to be a part of future Navigation updates where there will be a special navigation scenario for abandoning a view when changes are unsaved.

