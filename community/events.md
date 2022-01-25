---
title: Community Events
description: Notes about community events
published: true
date: 2022-01-25T21:41:39.097Z
tags: 
editor: markdown
dateCreated: 2022-01-25T21:41:39.097Z
---

## 2022-01-22 Code for Japan Social Hack Day

*Brent, Joi, Mukesh, and Pavish represented Mathesar at the January 2022 iteration of [Code for Japan's Social Hack Day](https://hackday.code4japan.org/). Notes from them have been combined below.*

### Use Cases
- Mathesar has applicability in "sometimes available DBA" situations. The example use case was tracking disaster supplies. During non-disaster times, it's likely a DBA could manage the DB and set things up. However, in a disaster it might become necessary for a non-expert to both work with the data and potentially modify the data model. We've previously been mostly considering scenarios where the DB management would be through Mathesar except when some functionality wasn't available, using psql as a fallback. I thought the scenario of a "real" DBA managing the database how they want (e.g., through psql) under normal conditions, but the users being empowered to take control of the DB through Mathesar in an emergency quite compelling.
- Real life usecases of participants which Mathesar can help solve:
    - Mapping disater recovery stockpiles
    - Conducting public surveys and sharing datasets
- Listing public restrooms
- [Listing Sake related places](https://github.com/Code-for-SAKE/Sakepedia-Nuxt), they have their own storage based our of MongoDB.

### Feature Requests
- We came across a scenario where the ability to import a database scheme that enforces some data model would be quite useful. I.e., you would be able to distribute a data model for individual admins to import into their installation and use. It might be worth setting up a user flow for that.
- Being able to export and import schemas
- Being able to create users that own a specific set of rows, essentially using Mathesar as a user login & data access portal for higher level applications
- Being able to detect and maintain consistent Japanese language encoding
- Maintain data format
- Granular permissioning

### Action Items
- :white_check_mark: Set up a bridge between the new `#proj-mathesar` channel in the Code for Japan Slack and our Matrix server.
- :white_check_mark: Set up a section in our wiki for notes on events
- Set up a team email address for people to contac us

### Other Notes
- People found Mathesar really hard to pronounce
- We had new contributors who helped & expressed interest in translating our wiki. The [About](/en/product/about) page is already translated to Japanese, [see here](/ja/product/about).
