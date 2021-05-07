---
title: Concepts
description: Glossary of Mathesar terms
published: true
date: 2021-05-07T19:49:45.890Z
tags: 
editor: markdown
dateCreated: 2021-05-07T15:21:44.337Z
---

This page is a reference for concepts related to Mathesar. It is intended to be the primary source of information for how the product is supposed to work.

> This page describes how Mathesar **will** behave. We are still in early development, so most features are not implemented yet.
{.is-warning}

# Database Layer
These concepts relate to the database layer of Mathesar, which is PostgreSQL.

## Databases
At its core, Mathesar provides a friendly user interface to PostgreSQL databases. Mathesar can be configured to provide an interface to multiple databases, but users will only be working with one database at a time.

## Schemas
PostgreSQL schemas are logical groupings (a.k.a. namespaces) of tables, views, and other database objects within databases.

If a user is using Mathesar for a few unrelated applications, we encourage them to have a single database with multiple schemas.

## Tables
PostgreSQL tables are a collection of related data, consisting of columns and rows. All data is stored in tables.

To avoid duplicating data, we encourage users to set up many small tables that are related to each other.

## Views
Views are the result of a stored SQL query on the data stored in tables. Views can involve combining data from multiple tables, filtering, sorting, aggregating (grouping), and so on.

We expect that most users will work with data in views more often than working directly with tables, since users will probably want to see related data from across tables easily.
