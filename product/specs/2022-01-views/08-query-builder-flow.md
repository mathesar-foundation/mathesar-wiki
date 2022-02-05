---
title: 08. Query Builder Flow
description: 
published: true
date: 2022-02-05T23:04:47.283Z
tags: 
editor: markdown
dateCreated: 2022-02-05T23:04:47.283Z
---

> This page is still being written so the information below is incomplete.
{.is-warning}

This page describes the workflow to build a query, to be used during View Creation. 

## Example
To make the flow easier to understand, we'll use the following example schema. Each object below represents a table and an arrow represents a foreign key relationship. The direction represents where the foreign key column is defined.

> We'll use this formatting to follow each step below using this example.
{.is-info}


![movie_schema.png](/assets/product/specs/2022-01-views/08-query-builder-flow/movie_schema.png)

## Flow

### Step 1: Selecting the First Column

In this step, we will ask the user to select the first column to start the query. This first column will be used as the main reference column for the rest of the View. 

There are no restrictions at this point, we'll show the user every column from every table.

> Let's assume the user picks the **title** column from the **Movie** table here.
{.is-info}

### Step 2: Selecting the Second Column

