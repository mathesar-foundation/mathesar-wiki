---
title: About Mathesar
description: 
published: true
date: 2023-07-19T23:09:15.197Z
tags: 
editor: markdown
dateCreated: 2021-11-03T00:42:34.804Z
---

> This page is no longer being updated as of 2023-01-27. Please see our **[main website](https://mathesar.org/)** for more up-to-date information about Mathesar.
{.is-warning}

Mathesar is an open source tool that provides an intuitive user interface to databases. Our aim is to make it easy for non-technical users to be able to work with databases without prior knowledge of database concepts. We're heavily inspired by the user experience of [Dabble DB](https://www.youtube.com/watch?v=MCVj5RZOqwY).

Users can either set up a database from scratch or connect to an existing database. They can store, organize, and set up various views of their data. By our beta release, users will also be able to collaborate with other users, see visualizations of their data, and evolve their data model as their needs change.

Mathesar is designed to be self-hosted on your own server.

## Use cases
Mathesar can be used to:
- Publish or explore public datasets
- Run business processes such as:
  - inventory management
  - event planning
  - project and task management
  - expense tracking and accounting
  - customer relationship management
- Provide non-technical users access to existing databases for:
  - data entry
  - custom reporting and querying
- Collect and process data from the public or external collaborators (similar to products like Google Forms)
- Simple data cleaning e.g. consolidating data gathered from different sources into a single format
- Simple data analysis and visualizations
- Automatically generate REST APIs to interact with connected database

Mathesar's goal is to be an infrastructural tool for anyone who works with information and we're looking forward to seeing other use cases people come up with.

## Why build Mathesar?

There are already many tools out there for working with data such as database administration GUIs, spreadsheet software, “low code” platforms, and business intelligence tools. Why do we need another?

**Interoperability and Data Portability**
Data stored using most comparable tools cannot be modified by other software. Mathesar uses a general purpose database (Postgres) with a thriving ecosystem of interoperable tools.

**Approachable User Experience**
Existing tools either limit available features or focus on power users. Mathesar meets users at their technical skill level while also supporting advanced features and encouraging learning.

**Data Integrity and Reuse**
Spreadsheets and low code platforms don’t do much by default to help you make sure data is consistent and this limits reuse potential. Databases are good at this by design.

**Open Source Infrastructure**
Data is valuable and shouldn’t be tied to using a specific proprietary service. The public needs open source, decentralized, and private infrastructure for people to manage their own data.


## Further reading
- [Tool Category Exploration *Report on initial research towards defining Mathesar's scope*](/design/reports/tool-category)
- [Product Concepts *Concepts in Mathesar*](/product/concepts)
{.links-list}