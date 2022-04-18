---
title: List Data Type
description: 
published: false
date: 2022-04-10 18:02:53
tags: 
editor: markdown
dateCreated: 2022-04-06 18:02:58
---

## Context

This document specifies the design of List data type within the Mathesar application. List data type can include one or more items that are in the same basic data type (e.g., Number), separated by a comma delimiter if more than one item is present. Mathesar aims to support all basic data types in List format. Users will be able to view data that is currently in Mathesar List data type, edit and filter List data, create new columns in List data type, and convert existing data into List data type. 

The goal of the design in general is to help non-technical understand List data type and maintain List data integrity. Aggregating data into Lists via mapping tables is not beyond the scope of this spec and should be designed in visually different ways to communicate the affordance.

Mathesar List data type is similar to [PostgreSQL "Arrays" concept](https://www.postgresql.org/docs/current/arrays.html). However, Mathesar List data type is only supporting single dimensional Array/List currently.

Read [Design for List data type](https://github.com/centerofci/mathesar/issues/978) for a more in-depth explanation of this feature.

Read [Design for visual query builder](https://github.com/centerofci/mathesar/issues/1065) for mapping table details.

## Scenarios

## 1. Working with Existing List Data

Users will be able to view, filter, and edit existing List data. This scenario assumes no List item data type change (e.g., converting a Number item to a Text item) during the edit. 

### 1.1 Viewing Existing List Data

Existing Mathesar List data distinguishes itself from other data type through four unique ways: 

1. Column header data type icon.
2. Data type icon and description in the column header menu. `Allow List` option is required to be turned on for List data type.
3. Tooltip information when hovering on the column header data type icon. 
4. Items in a single cell is separated by comma delimiters and a `show all` option is present. Users can use `show all` function to expand the List and view all List items.

---
Wireframes

[Viewing Existing List Data](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?node-id=7317%3A80859&viewport=306%2C48%2C0.59&scaling=min-zoom&starting-point-node-id=7379%3A82626&show-proto-sidebar=1)

### 1.2 Filtering Existing List Data

The following filters are available for List data:

1. is empty
2. is not empty
3. contains `<LIST ITEM DATA TYPE>`
4. number of items greater than `<NUMBER>`
5. number of items greater than or equal to `<NUMBER>`
6. number of items equal to `<NUMBER>`
7. number of items lesser than `<NUMBER>`
8. number of items lesser than or equal to `<NUMBER>`

Users are able to utilize multiple filters through the `Add Filter` feature. By default, the relationship between filters is set to `difference`. Users can enable the `Union` toggle to include data cells that appear in any of the filters.

---
Wireframes

[Filtering Existing List Data](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?node-id=7317%3A80859&viewport=306%2C48%2C0.19&scaling=min-zoom&starting-point-node-id=7379%3A82944&show-proto-sidebar=1)

### 1.3 Editing Existing List Data

Users can single-click a List data cell or click the `show all` button to expand the selected the data cell and enter editing mode. A background shade is added to each List item, not the delimiters, to highlight the nature of List data type. Under cell editing mode, users can again single-click the item that they wish to edit to finish the edit without compromising the data structure.

To add a new List item in the cell, users can simply single-click the white space within the cell when under editing mode. A new item placeholder and a new delimiter will show up. A preset Null value will be entered automatically if users have allowed and configured it.

---
Wireframes

[Editing Existing List Data](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?node-id=7317%3A80859&viewport=306%2C48%2C0.24&scaling=min-zoom&starting-point-node-id=7809%3A84002&show-proto-sidebar=1)

### 1.4 Editing Existing List Data – Item Type Warning

While editing List data items, if Mathesar detected that users were entering a potentially non-conforming item type (e.g., entering a number into a List of Text items), a warning modal would show up to inform users. 

If Mathesar couldn't conform the new item to the existing List item data type, a serious warning would show up before converting all List data item in the column to Text.

---
Wireframes

[Item Type Warning](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?node-id=7317%3A80859&viewport=306%2C48%2C0.22&scaling=min-zoom&starting-point-node-id=8268%3A90606&show-proto-sidebar=1)

[All Column Item Change Warning](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?node-id=7317%3A80859&viewport=306%2C48%2C0.4&scaling=min-zoom&starting-point-node-id=8268%3A90982&show-proto-sidebar=1)

## 2. Converting Existing List Data to a Different Type

Users can perform numerous data type operations to List data. There are two main categories of conversion:

1. Converting List data to a basic data type as a whole.
2. Converting List items to a different basic data type.

### 2.1. Converting List Data to a Basic Type by Turning Off `Allow List`

By default, the `Allow List` toggle in the column header menu would be turned on. While users are editing data cells, if Mathesar detects a comma delimiter and a data structure that resembles a List, Mathesar can make automatically inference and convert the column into a List data type. Users can still maintain the same basic data type for each List item, and the common basic data type settings, such as formatting and setting up Null values, are still available for List items.

Users can convert the entire List back to a basic type by simply turning off the `Allow List` toggle. While the toggle is turned off, the column will not automatically and cannot be converted to a List data type. In this case, users' comma delimiter formatted data can only be recognized as Text by Mathesar.

---
Wireframes

[Turning Off `Allow List`](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?node-id=7317%3A80859&viewport=306%2C48%2C0.34&scaling=min-zoom&starting-point-node-id=8268%3A91375&show-proto-sidebar=1)

### 2.2 Converting List Items to a Different Type

Users can keep the List data structure and convert the List item data type only. As with all data entries, all List items can be converted into Text items. Mathesar will check whether the item format comforms to the destination data type requirement for all other conversions. Users will be warned about potential data loss as required. The conversion between different data types has been explored and will be detailed in a separate spec. The wireframe example is demonstrating changing List items from Number to Text.

---
Wireframes

[Converting List Items](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?node-id=7317%3A80859&viewport=306%2C48%2C0.26&scaling=min-zoom&starting-point-node-id=8268%3A91011&show-proto-sidebar=1)

## 3. Creating a New Column in List Data Type

Since Mathesar aims to support all basic data types in List format as well as detect List data structure automatically, List data capability comes with every new column added. Users can opt out this feature by turning off `Allow List`.

### 3.1 Creating a New Column

As noted earlier, List data capability comes with every new column and `Allow List` is automatically turned on. When allowing List, Mathesar will automatically convert the column into List as it detects the List data structure. List item type will remain the same as the current setting. Tooltip information is provided.

---
Wireframes

[Creating a New List Column](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?node-id=7317%3A80859&viewport=306%2C48%2C0.82&scaling=min-zoom&starting-point-node-id=7923%3A86825&show-proto-sidebar=1)

### 3.2 Empty List Data Column Options

When a column is empty, Mathesar column data type settings follow basic data type settings. Please refer to basic data type design and menu options. 

---
Wireframes

[Basic Data Type Menu](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?node-id=4260%3A37440&viewport=306%2C48%2C0.06&scaling=min-zoom&starting-point-node-id=4270%3A39549&show-proto-sidebar=1)

## 4. Converting Existing Non-List Data to List Data

Existing non-List data that follows List comma delimiter format will be in Text data type if `Allow List` has been turned off. Users can simply convert the non-List data into List data by turning on `Allow List`.

### 4.1 Converting Correctly Formatted Non-List to List

Correctly formatted Lists can be in non-List data types only when `Allow List` is turned off. As mentioned above, users can convert non-List data that follows List comma delimiter format by simply turning on `Allow List`. Mathesar can automatically parse the data into List and make inference for the List item data type. Users can change List item data type by following 2.2.

---
Wireframes

[Converting Correctly Formatted Non-List to List](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?node-id=7317%3A80859&viewport=306%2C48%2C0.28&scaling=min-zoom&starting-point-node-id=8398%3A88843&show-proto-sidebar=1)

### 4.2 Converting Incorrectly Formatted Non-List to List

Incorrectly formatted data cannot be automatically turned into List even when `Allow List` is turned on. However, this scenario will only happen when no comma is detected in one or more cells of the column (see 4.3). Users are informed in the following two ways:

1. Tooltip will show up as soon as users hover over the information icon next to `Allow List` option. The tooltip aims to concisely convey the correct format of List data and point users to relevant help pages for details.
2. When users turn on `Allow List` and Mathesar is unable to detect a correct List data format, a warning modal will show up. The warning should only show up when Mathesar detects certain List conversion intents from the users. For example, if users only have a single number in each cell, turning on `Allow List` is just to enable this feature and clearly the data is not yet in List format.

---
Wireframes

[Converting Incorrectly Formatted Non-List to List](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?node-id=7317%3A80859&viewport=306%2C48%2C0.37&scaling=min-zoom&starting-point-node-id=8399%3A90654&show-proto-sidebar=1)

### 4.3 Converting Partially Correctly Formatted Non-List to List

If Mathesar uses comma delimiter to detect List, Mathesar can still successfully parse Text data type as long as a comma is present. In this case, if the resulting List items are inferred as an incorrect basic data type due to the data error (e.g., Mathesar is not successful in inferring Number due to a data error), users can quickly realize something is wrong. Unfortunately, users still need to locate the errors by themselves.

## 5. Other Considerations

The List data type design exploration above has assumed a fair amount of background processing capability in Mathesar. For example, the `Allow List` option can simplify users' decision-making process by detecting the existence of a List in the background constantly, as users are actively editing data. 

In addition, each List item is in a basic Mathesar data type and the conversions between basic data types should be explored in detail. See the following prototype for example design exploration.

---
Wireframes

[Converting Between Basic Data Types](https://www.figma.com/file/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?node-id=8399%3A89327)