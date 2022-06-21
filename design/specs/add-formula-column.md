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

[Wireframe link]()

## Scenarios

### Scenario 1 - Add a formula column without clicking outside of the inspector.

On the left hand side of the explorer view, there is a  `Add Column`  button. When user clicks on it, there are two options visible to them. One is `Add direct column` and the other is `Add formula column`. To add a formula column user will need to click on `Add formula column`. 

![](/assets/design/specs/add-formula-column/1.png)

Once the user clicks on `Add formula column` option, the inspector shows formula settings that include `Name` input of the formula and a list of formulas to select from. The list of formulas is described in detail in the component section. 

If the name is left empty by user for the next steps, there is a default name given to the column that is ColumnX. X is the number given to the column. For instance if its the first default named column it will be Column1.

![](/assets/design/specs/add-formula-column/2.png)

Once the user decides on what formula they want, the inspector shows relevant inputs for formula selected. The parameters can be of different data types depending on the selected formula. Parameters of the selected formula are described in scenarios below. 

Before adding the parameters (if they are required), user would be able to see a preview of an empty column. 

![](/assets/design/specs/add-formula-column/3.png)

Once the user adds correct parameter the empty column gets filled with the calculated date and the user is able to preview the filled column. If they are not satisfied by the results they can change the formula selected as well as the parameters before adding the column to the query, this scenario is covered under edit column scenario.

The `Add column` button in the inspector adds the column to the query. This button is only clickable if the column is filled. 

![](/assets/design/specs/add-formula-column/4.png)

Once the generated column is added to query, and user is satisfied by it, user can jump to closing the data explorer. That action will take them to a modal where they are asked to save the query which saved the column to the table permanently. If they do not want to save it they get the option of closing without saving. To cancel the action they get a cross button on the modal.

![](/assets/design/specs/add-formula-column/5.png)

#### Scenario 1.a - Add a random generation type formula column

The random generation type formula generates random numbers or UUID. For random number generation, the user just have to provide upper and lower bound with the decimal flag. There is no column input when it comes to random generation type formulas. Hence, the successful generation of the random generation type column is shown below. 

![](/assets/design/specs/add-formula-column/6.png)

#### Scenario 1.b - Add a text type formula column

The text type formula works on columns with text data type. There can be different parameters depending on what the formula is. For instance, there are `starting index` and `count` here in the example below.

![](/assets/design/specs/add-formula-column/7.png)

#### Scenario 1.c - Add a number type formula column

The number type formula works on columns with number data type. There can be different parameters depending on what the formula is. For instance, there is `comparison sign` here in the example below.

![](/assets/design/specs/add-formula-column/8.png)

#### Scenario 1.d - Add a date & time type formula column

The date/time type formula works on columns with date/time data type. There can be different parameters depending on what the formula is. For instance, there is `precision` here in the example below.

![](/assets/design/specs/add-formula-column/13.png)

#### Scenario 1.e - Add a cumulative type formula column

The cumulative type formula works on columns with any data type. There can be different parameters depending on what the formula is. It basically shows how data in one column is changing with the help of different mathematical equations.

![](/assets/design/specs/add-formula-column/10.png)

#### Scenario 1.f - Add a boolean type formula column

The boolean type formula works on columns with boolean data type. There can be different parameters depending on what the formula is. For instance, there is `condition` here in the example below.

![](/assets/design/specs/add-formula-column/9.png)

#### Scenario 1.g - Add a regular expression type formula column

The regular expression type formula works on columns with any data type. There can be different parameters depending on what the formula is. It basically is to determine if there are any patterns in the data of a column. 

![](/assets/design/specs/add-formula-column/11.png)

#### Scenario 1.h - Add a list type formula column

The list type formula works on columns with list data type. There can be different parameters depending on what the formula is.

![](/assets/design/specs/add-formula-column/12.png)

### Scenario 2 - Adding an errorneous parameter to the formula 

### Scenario 3 - Edit a formula column while adding or after saving the formula column

### Scenario 4 - Click outside the inspector while adding the column

### Scenario 5 - Quit the explorer

## Interactions

### Modal for warning before qutting the explorer

### Column preview while adding the formula

### Parameter inputs

## Components

### Add column button

### The formula selection menu

### Add column button

### Quit explorer button

