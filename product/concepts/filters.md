---
title: Filters
description: About Filters in Mathesar
published: true
date: 2023-05-11T14:36:53.482Z
tags: 
editor: markdown
dateCreated: 2022-01-26T23:37:01.162Z
---

# About

A **Filter** allows you to reduce the amount of data displayed in a [Table](/en/product/concepts/tables) or a [View](/en/product/concepts/views) based on specified criteria.

## Example
Imagine this table containing movies.

| ID | Title | Release Year | Watched? |
|-|-|-|-|
| 1 | Dante's Peak | 1997 | TRUE |
| 2 | The Bourne Identity | 2002 | TRUE |
| 3 | The Karate Kid | 1984 | TRUE |
| 4 | Full Metal Jacket | 1987 | TRUE |
| 5 | The French Dispatch | 2021 | FALSE |
| 6 | 雨月物語 | 1953 | FALSE |
| 7 | Big Trouble | 2002 | TRUE |

You might want to only see movies you've watched. You could apply the filter `"Watched?" is TRUE` and then you'd only see these rows:

| ID | Title | Release Year | Watched? |
|-|-|-|-|
| 1 | Dante's Peak | 1997 | TRUE |
| 2 | The Bourne Identity | 2002 | TRUE |
| 3 | The Karate Kid | 1984 | TRUE |
| 4 | Full Metal Jacket | 1987 | TRUE |
| 7 | Big Trouble | 2002 | TRUE |

Then you might want to see movies released after 1990 that you've watched, so you'd apply an additional filter of `Release Year > 1990` and see:

| ID | Title | Release Year | Watched? |
|-|-|-|-|
| 1 | Dante's Peak | 1997 | TRUE |
| 2 | The Bourne Identity | 2002 | TRUE |
| 7 | Big Trouble | 2002 | TRUE |

## Filters in Mathesar
You can filter data in a [Table](/en/product/concepts/tables) or a [View](/en/product/concepts/views) in Mathesar using either the "Filters" button or each column's menu.

# Further Reading
- If you're curious, you can look at our [engineering page about Filters](/en/engineering/glossary/filters).

