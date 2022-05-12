---
title: List Data Type
description: 
published: false
date: 2022-04-10 18:02:53
tags: 
editor: markdown
dateCreated: 2022-04-06 18:02:58
---

# Context

This document specifies the design of List data type within the Mathesar application. List data type can include one or more items that are in the same basic data type (e.g., Number). It can be generated via user input as well as data aggregation. This spec focuses on List data generated via user input. 

Mathesar aims to support all basic data types in List format. Users will be able to view data that is currently in Mathesar List data type, edit and filter List data, create new columns in List data type, and convert existing data in the table into List data type. The goal of the design in general is to help non-technical understand List data type and maintain List data integrity.

Mathesar List data type is similar to [PostgreSQL "Arrays" concept](https://www.postgresql.org/docs/current/arrays.html). However, Mathesar List data type is only supporting single dimensional Array/List currently.

Read [Design for List data type](https://github.com/centerofci/mathesar/issues/978) for a more in-depth explanation of this feature.

Read [Design for visual query builder](https://github.com/centerofci/mathesar/issues/1065) for List data generated via aggregation and mapping table (beyond the scope of this spec).

# Scenarios

## 1. Working with Existing List Data

Users will be able to view, filter, and edit existing List data. This scenario assumes no List item data type change (e.g., converting a Number item to a Text item) during the edit. 

### 1.1 Viewing Existing List Data

Existing Mathesar List data distinguishes itself from other data type through four unique ways: 

1. Column header data type icon.
2. Data type description in the column header menu, as well as the `Single` and `List` options in Data Type Options.
3. Tooltip information when hovering on the column header data type icon. 
4. Each List item is tag-like and has a light background shade. When List is too long to be displayed in a single cell, tags such as `+2 items` (meaning 2 more items are not currently showing) will be used.

---
Wireframes

[Viewing Existing List Data](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?node-id=7317%3A80859&viewport=911%2C317%2C0.16&scaling=min-zoom&starting-point-node-id=7379%3A82626&show-proto-sidebar=1)

---

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

Users are able to utilize multiple filters through the `Add Filter` feature. 

---
Wireframes

[Filtering Existing List Data](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?node-id=7317%3A80859&viewport=911%2C317%2C0.16&scaling=min-zoom&starting-point-node-id=7379%3A82944&show-proto-sidebar=1)

---

### 1.3 Editing Existing List Data

Users can single-click a List data cell or click the `+? items` button to expand the selected the data cell and enter editing mode. A darker background shade is used for the cell that is currently selected. Under cell editing mode, users can again single-click the item that they wish to edit to finish the edit without compromising the data structure. The item being edited has a visually prominent highlight color.

To add a new List item in the cell, users can simply single-click the white space within the cell when under editing mode. A new item placeholder will show up. A preset Null value will be entered automatically if users have allowed and configured it.

---
Wireframes

[Editing Existing List Data](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?node-id=7317%3A80859&viewport=763%2C-546%2C0.24&scaling=min-zoom&starting-point-node-id=8835%3A92418&show-proto-sidebar=1)

---

### 1.4 Editing Existing List Data – Item Type Warning

While editing List data items, if Mathesar detected that users were entering a potentially non-conforming item type (e.g., entering a number into a List of Text items), a warning modal would show up to inform users. 

If Mathesar couldn't conform the new item to the existing List item data type, a serious warning would show up before converting all List data item in the column to Text.

---
Wireframes

[Item Type Warning](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?node-id=7317%3A80859&viewport=-74%2C-2747%2C0.51&scaling=min-zoom&starting-point-node-id=8835%3A92081&show-proto-sidebar=1)

[All Column Item Change Warning](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?node-id=7317%3A80859&viewport=-74%2C-2747%2C0.51&scaling=min-zoom&starting-point-node-id=8268%3A90982&show-proto-sidebar=1)

---

## 2. Converting Existing List Data to a Different Type

### 2.1 Converting List Items to a Different Type

Users can keep the List data structure and convert the List item data type only. As with all data entries, all List items can be converted into Text items. Mathesar will check whether the item format comforms to the destination data type requirement for all other conversions. Users will be warned about potential data loss as required. The conversion between different data types has been explored and will be detailed in a separate spec. The wireframe example is demonstrating changing List items from Number to Text.

---
Wireframes

[Converting List Items](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?node-id=7317%3A80859&viewport=495%2C-515%2C0.14&scaling=min-zoom&starting-point-node-id=8835%3A92812&show-proto-sidebar=1)

---

## 3. Creating a New Column in List Data Type

### 3.1 Creating a New Column

After adding a new column, users can change the column data type from `Single` to `List` in the data type menu. Tooltip is provided in the data type menu for users to differentiate `Single` and `List` options.

---
Wireframes

[Creating a New List Column](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?node-id=7317%3A80859&viewport=-296%2C-397%2C0.29&scaling=min-zoom&starting-point-node-id=8836%3A92137&show-proto-sidebar=1)

---

## 4. Converting Existing Non-List Data to List Data

### 4.1 Converting Correctly Formatted Non-List to List

When users change the column data type from `Single` to `List` in the data type menu, correctly formatted non-List data can be converted to List conveniently. Tooltip is provided in the data type menu for users to understand what format Mathesar is expecting.

---
Wireframes

[Converting Correctly Formatted Non-List to List](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?node-id=7317%3A80859&viewport=-447%2C-678%2C0.29&scaling=min-zoom&starting-point-node-id=8836%3A93044&show-proto-sidebar=1)

---

### 4.2 Converting Incorrectly Formatted Non-List to List

Incorrectly formatted non-List data cannot be converted to List, or they may be converted with data loss. When users attempt to convert incorrectly formatted non-List data, a warning modal would be displayed.

---
Wireframes

[Converting Incorrectly Formatted Non-List to List](https://www.figma.com/proto/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?node-id=7317%3A80859&viewport=-447%2C-678%2C0.29&scaling=min-zoom&starting-point-node-id=8848%3A92359&show-proto-sidebar=1)

---

## 5. Other Considerations

The List data type design exploration above has assumed that Mathesar can convert non-List data to List if the data is following a certain format. In the prototype above, a comma delimiter format is used to illustrate the idea. The methods for converting between basic data types are indispensable when design for List item data type conversion. The currently staging product included some examples, but most data type conversions would result in errors (understandably, though, it would be impossible to convert an alphabetical Text into a Number). How to inform users what conversion is possible vs. impossible is a critical piece of the user experience for data types. 

---
Wireframes

[Converting Between Basic Data Types](https://www.figma.com/file/Uaf1ntcldzK2U41Jhw6vS2/Mathesar-MVP?node-id=8399%3A89327)
