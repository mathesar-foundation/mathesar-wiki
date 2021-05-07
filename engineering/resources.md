---
title: Resources
description: Reading and resources that might be of interest.
published: true
date: 2021-05-07T19:04:27.075Z
tags: 
editor: markdown
dateCreated: 2021-04-20T16:30:35.472Z
---

This is a miscellaneous set of reading and resources that may or may not be relevant to Mathesar. **Feel free to add more!**

# Postgres
Information on Postgres related projects and tools.

## Articles
- [Migration Opinions](https://github.com/graphile/migrate#opinions) opinions on writing database migrations in Postgres. Invaluable for long-running production production projects with breaking schema changes.
- [Evaluating PostGraphile For Your Project](https://www.graphile.org/postgraphile/evaluating/): The section on "Schema Driven APIs" here has some great insights.
- [Advice on Indexes in Postgres](https://www.graphile.org/postgraphile/postgresql-indexes/)
- [10 Things I Hate About PostgreSQL](https://rbranson.medium.com/10-things-i-hate-about-postgresql-20dbab8c2791)

## Projects
- The [graphile](https://github.com/graphile) organization on GitHub is full of postgres-related projects written in TypeScript. Clean,  straightforward codebases with very good documentation.

### Introspection + API Generation
- [PostgREST](https://github.com/PostgREST/postgrest) - Introspects, generates, and serves OpenAPI-complaint REST apis from Postgres databases.
- [Postgraphile](https://github.com/graphile/postgraphile) The same thing, but for GraphQL and written in TypeScript. They have really rich documentation that gets into a lot of interesting Postgres best practices and architectural patterns.
	- A package for realtime communication with Postgres `LISTEN / NOTIFY` https://github.com/graphile/graphile-engine/tree/v4/packages/pg-pubsub

