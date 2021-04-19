---
title: Simple Databases for Everyone
description: a.k.a. Modern version of Dabble DB
published: true
date: 2021-04-19T20:54:30.280Z
tags: 
editor: markdown
dateCreated: 2021-04-19T20:18:32.610Z
---

Related to:  
* [accelerate knowledge, creativity, and innovation in the world](accelerate-innovation.md)
* [decentralize the internet](decentralize-internet.md)

## Problem
Most people want to track and analyze data of one sort or another from simple personal uses such as a book reading log or food inventory to large scale datasets. People often use spreadsheets for this, but spreadsheets are limited – collaboration is hard, and it can be difficult to normalize and connect data between different spreadsheets.

## Solution
Dabble DB (shut down c. 2010) was an interactive GUI that abstracted out databases and made them accessible to lay users. It normalized database schemas behind the scenes, and provided collaboration tools that allowed users to share views and forms to allow others to add or modify data.

The primary feature of Dabble DB was its intuitive UI and simplification of database concepts into terms easily understandable by regular users. This is hard to describe in words, so please watch these demos:  
* [Demo 1](https://www.youtube.com/watch?v=MCVj5RZOqwY)
* [Demo 2](https://www.youtube.com/watch?v=6wZmYMWKLkY)

There isn't a good replacement for Dabble DB on the market, and we're certainly not aware of an open source one.  In fact, we're not aware of any good, open-source tool that allows users to collaborate on tinkering with data.

## Feasibility

### User Flow
Replicating Dabble DB's original user flow (see videos above) is the best place to start.

### Technical Details
- It would be easiest to build this product as a frontend to an existing database (e.g. PostgreSQL), where you can either run it against existing databases or create a new one.
- In the future, perhaps the database connection could be abstracted out and multiple database backends could be supported.

### Potential Roadmap
- Start with replicating DabbleDB UI on top of Postgres
- Future improvements
  - multiple DB backends
  - more ways to input data (through integration with other data ingestion tools)

## Potential Users

- Individuals (for personal uses such as inventory, personal tracking, etc.)
- Companies (for anything you would use Airtable for)
- Small businesses and professionals

### Example Scenario for Company

Perhaps a company wants to put together a database of sales data connecting customers, their locations, what they've bought, what they've spent, store locations, and sales people. Something similar to Dabble DB would allow non-technical users to work together to iteratively develop a data model that serves their needs, and they could easily extend or modify it as their needs (or their understanding) changes.

## Challenges

- There are some solutions (tableau comes to mind) that allow users to accomplish much (though not all) of what we've suggested.
- There are a huge number of different "views" (maps, pie charts, equations, regression models) that people might request of their data.  It seems difficult to be useful without including a large number of those out of the gate.
- Another competitor, Fieldbook, [shut down](https://medium.com/the-fieldbook-blog/what-happened-at-fieldbook-d70bf25b3968) because of a lack of profitability.

### Competitors
- The primary competitor is Airtable
  - Airtable is a SaaS solution, not self-hosted
  - Airtable is not open source
  - Airtable is geared towards work and has a complicated user interface
  - Airtable doesn't support SQL
- Other alternatives are listed on [this Hacker News thread](https://news.ycombinator.com/item?id=15246061)

## Sustainability
- We could offer a paid centralized version so that people wouldn't need to self-host.
- We could offer paid support for the self-hosted version.

## Additional Thoughts

- This seems particularly suited to an open source project with a large number of contributors.  As noted above, there are a huge number of features that might be wanted.  However, a good design of the core pieces would allow a sort of 3rd party plugin ecosystem to implement many of the desired features.
- Perhaps this could somehow work together with BayesDB.
- Maybe we can use some or all of [Apache Superset](https://github.com/apache/superset) for the visualizations?
