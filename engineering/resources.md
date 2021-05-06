---
title: Resources
description: Reading and resources that might be of interest.
published: true
date: 2021-05-06T18:10:04.473Z
tags: 
editor: markdown
dateCreated: 2021-04-20T16:30:35.472Z
---

This is a miscellaneous set of reading and resources that may or may not be relevant to Mathesar. **Feel free to add more!**

# Product

* [Speed is the killer feature](https://bdickason.com/posts/speed-is-the-killer-feature/)
* ["Early Work" by Paul Graham](http://paulgraham.com/early.html)

## Post-mortems of related products
* [RethinkDB: why we failed](https://www.defmacro.org/2017/01/18/why-rethinkdb-failed.html)
	* Related [Hacker News discussion](https://news.ycombinator.com/item?id=26443406)
* [What Happened at Fieldbook](https://medium.com/the-fieldbook-blog/what-happened-at-fieldbook-d70bf25b3968)

## Dabble DB
- [DabbleDB pre-beta demo](https://www.youtube.com/watch?v=6wZmYMWKLkY)
- [DabbleDB product demo](https://www.youtube.com/watch?v=MCVj5RZOqwY)
- [Old Computer World review of database builder applications, including Dabble DB](https://www.computerworld.com/article/2535560/enterprise-applications-review-4-online-databases-let-you-structure-and-share-your-data.html?page=6): useful because it articulates what was special about Dabble DB.
- [Twitter's announcement of DabbleDB acquisition](https://blog.twitter.com/en_us/a/2010/more-than-dabbling.html)

# Technology

## Postgres
Information on Postgres related projects and tools.

### Articles
- [Migration Opinions](https://github.com/graphile/migrate#opinions) opinions on writing database migrations in Postgres. Invaluable for long-running production production projects with breaking schema changes.
- [Evaluating PostGraphile For Your Project](https://www.graphile.org/postgraphile/evaluating/): The section on "Schema Driven APIs" here has some great insights.
- [Advice on Indexes in Postgres](https://www.graphile.org/postgraphile/postgresql-indexes/)
- [10 Things I Hate About PostgreSQL](https://rbranson.medium.com/10-things-i-hate-about-postgresql-20dbab8c2791)

### Projects
- The [graphile](https://github.com/graphile) organization on GitHub is full of postgres-related projects written in TypeScript. Clean,  straightforward codebases with very good documentation.

#### Introspection + API Generation
- [PostgREST](https://github.com/PostgREST/postgrest) - Introspects, generates, and serves OpenAPI-complaint REST apis from Postgres databases.
- [Postgraphile](https://github.com/graphile/postgraphile) The same thing, but for GraphQL and written in TypeScript. They have really rich documentation that gets into a lot of interesting Postgres best practices and architectural patterns.
	- A package for realtime communication with Postgres `LISTEN / NOTIFY` https://github.com/graphile/graphile-engine/tree/v4/packages/pg-pubsub

