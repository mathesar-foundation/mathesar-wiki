# Resources

This is a miscellaneous set of reading and resources that may or may not be relevant to Mathesar. **Feel free to add more!**

# APIs
- [Best practices for REST API design - Stack Overflow Blog](https://stackoverflow.blog/2020/03/02/best-practices-for-rest-api-design/)

# Deployment

- [Best Practices Around Production Ready Web Apps with Docker Compose](https://nickjanetakis.com/blog/best-practices-around-production-ready-web-apps-with-docker-compose)

# Licensing
- [Maintaining Permissive-Licensed Files in a GPL-Licensed Project: Guidelines for Developers](https://softwarefreedom.org/resources/2007/gpl-non-gpl-collaboration.html)

# Postgres
Information on Postgres related projects and tools.

## Articles
- [Migration Opinions](https://github.com/graphile/migrate#opinions) opinions on writing database migrations in Postgres. Invaluable for long-running production production projects with breaking schema changes.
- [Evaluating PostGraphile For Your Project](https://www.graphile.org/postgraphile/evaluating/): The section on "Schema Driven APIs" here has some great insights.
- [Advice on Indexes in Postgres](https://www.graphile.org/postgraphile/postgresql-indexes/)
- [10 Things I Hate About PostgreSQL](https://rbranson.medium.com/10-things-i-hate-about-postgresql-20dbab8c2791)

### Primary Keys
- [UUID, serial or identity columns for PostgreSQL auto-generated primary keys?](https://www.cybertec-postgresql.com/en/uuid-serial-or-identity-columns-for-postgresql-auto-generated-primary-keys/)
- [Sequential UUID Generators](https://www.2ndquadrant.com/en/blog/sequential-uuid-generators/)

## Projects
- The [graphile](https://github.com/graphile) organization on GitHub is full of postgres-related projects written in TypeScript. Clean,  straightforward codebases with very good documentation.

### Introspection + API Generation
- [PostgREST](https://github.com/PostgREST/postgrest) - Introspects, generates, and serves OpenAPI-complaint REST apis from Postgres databases.
- [Postgraphile](https://github.com/graphile/postgraphile) The same thing, but for GraphQL and written in TypeScript. They have really rich documentation that gets into a lot of interesting Postgres best practices and architectural patterns.
	- A package for realtime communication with Postgres `LISTEN / NOTIFY` https://github.com/graphile/graphile-engine/tree/v4/packages/pg-pubsub

