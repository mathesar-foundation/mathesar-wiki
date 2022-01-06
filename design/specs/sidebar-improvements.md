---
title: Sidebar Improvements
description: 
published: true
date: 
tags: 
editor: markdown
dateCreated: 
---

## Context

The `Left Sidebar` component's main purpose is to give users access to the list of database objects. The sidebar supports the addition of [various sections](#sidebar-sections), where additional functionality can be displayed.

## Prototype

### Link

[Prototype Link](https://mathesar-prototype.netlify.app/)

### Videos

- All Scenarios:

## User Experience

When in the `Explorer` section, the' Left Sidebar' should allow for quick navigation objects. Users should be able to retrieve objects and open them quickly. Additionally, it should make the [status of objects](#status-of-objects) listed visible.

## Scenario 1: Opening the Sidebar

### Scenario 1a: Via opening a schema

#### Steps for 1a

1. A user opens a schema.
2. The sidebar is open by default with the `Explorer` section active.

### Scenario 1b: Via sidebar navigation bar

#### Steps for 1b

1. A user is in the schema view.
2. The user clicks on any navigation item from the sidebar navigation bar.
3. The selected sidebar section opens.

## Scenario 2: Closing the Sidebar

### Scenario 2a: Via sidebar navigation bar

#### Steps for 2a

1. A user is in the schema view.
2. The user clicks on a currently selected navigation item.
3. The sidebar closes.

## Scenario 3: Navigating to Another Section

### Scenario 3a: Via sidebar navigation bar

#### Steps for 3a

1. A user is in the schema view.
2. The user clicks on any navigatiom item that is not currently selected.
3. The sidebar closes.

## Components

### Sidebar Sections

The `Left Sidebar` component, can support multiple sections. At the time of writing this spec, only the `Explorer` section is planned to be implemented.

### Explorer Section

The `Explorer` section contains the list of database objects for a currently open schema.

## Interactions

### Status of Objects

Items listed in the `Explorer` sidebar are styled differently according to their status.

- Open/Active
- Unsaved Changes
- Error
