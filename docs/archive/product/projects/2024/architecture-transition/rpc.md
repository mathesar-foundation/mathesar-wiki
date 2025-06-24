# RPC transition

This document lays out plans for our 2024 transition from a REST-based API to one based on JSON-RPC.

It is maintained by Sean and Brent.

## Timeline

We want _most_ (but not all) of our REST endpoints to be fully transitioned to RPC APIs by the **beta release**. Some REST endpoints will likely remain, especially ones like `data_files` that will be difficult (or impossible?) to transition to JSON-RPC.

## JSON-RPC spec

- JSON-RPC is a [spec](https://www.jsonrpc.org/specification) adopted by many libraries.
- You should probably understand this spec before continuing to read this wiki page. Read the spec if needed.
- We'll be using version 2.0 of the spec.
- JSON-RPC is transport agnostic, but we plan on using it exclusively over HTTP for the forseeable future. A time may come when we use it over other transports such as web sockets, but we'll re-evaluate any architectural concerns as needed at that point.

## Libraries

On the backend we'll be using [django-modern-rpc](https://github.com/alorence/django-modern-rpc).

When using this library:

- All requests will be performed using HTTP POST.
- All responses have an HTTP status code of 200, even error responses.

### Alternatives considered

- [json-rpc](https://github.com/pavlov99/json-rpc)
    - This seems to be less actively maintained
    - It doesn't integrate as well with Django auth.

## API Standards

These standards are _preliminary_ and subject to change. We'll need to better document them as they become more solidified with our rollout.

### Use named parameters

The JSON-RPC spec supports both named parameters _and_ positional parameters.

We are enforcing a standard of always using named parameters and never using positional parameters.

### Method namespacing

- Noun first, verb second. (This makes the methods easy to sort.)
- The most common method naming pattern is `noun.verb`, but method names can use arbitrarily deep namespace. It's okay to have a method at the top-level or several levels deep.

### Standard verbs

To ensure that our method names use consistent terminology, use the following verbs within method names:

| ✅ Use      | ❌ Don't use |
| --          | --               |
| **list**    | ~~get all~~, ~~select~~ |
| **get**     | ~~get one~~, ~~fetch~~, ~~return~~ |
| **add**     | ~~create~~, ~~insert~~, ~~make~~, ~~new~~ |
| **patch**   | ~~partial update~~, ~~edit~~, ~~alter~~ |
| **replace** | ~~full update~~, ~~put~~, ~~set~~ |
| **delete**  | ~~remove~~, ~~drop~~ |

### Docstrings

- All API functions must have docstrings.
- Within the docstrings the syntax should be [Google style](https://google.github.io/styleguide/pyguide.html#383-functions-and-methods).

### Id values

For the JSON-RPC `id` parameter, we generate values which are unique only within the scope of a single HTTP request.

### When to batch

The move to JSON-RPC opens up the possibility for the front end to consolidate multiple requests into batches. We need to be cautious of this though. While parallel HTTP requests do incur overhead that can be reduced through batching, we need to be mindful that batching is essentially equivalent to `Promise.all()`. Sometimes batching requests might be possible but not preferable. For example if we can update state in one place of the UI with a fast request while concurrently updating separate UI state from a slow request, then we should issue parallel requests. The front end will need to take this behavior into account and make a case-by-case determinations on when it is appropriate to batch.

## Endpoints 🡆 functions {:#functions}

The table below is a comprehensive list of all REST API endpoints used by the front end as of Mathesar 0.1.6. Sean performed an audit of the codebase to extract this list.

| Endpoint                                                    | HTTP Method | Function                                  |
| --                                                          | --          | --                                        |
| `/api/db/v0/connections/{connectionId}/`                    | DELETE      | `connections.delete`                      |
| `/api/db/v0/connections/{connectionId}/`                    | PATCH       | `connections.patch`                       |
| `/api/db/v0/connections/`                                   | GET         | `connections.list`                        |
| `/api/db/v0/data_files/{id}`                                | GET         | _(keep)_                                  |
| `/api/db/v0/data_files/{id}`                                | PATCH       | _(keep)_                                  |
| `/api/db/v0/data_files/`                                    | POST        | _(keep)_                                  |
| `/api/db/v0/links/`                                         | POST        | `data_modeling.add_link`                  |
| `/api/db/v0/queries/{queryId}/`                             | DELETE      | `explorations.delete`                     |
| `/api/db/v0/queries/{queryId}/`                             | GET         | `explorations.get`                        |
| `/api/db/v0/queries/{queryId}/`                             | PUT         | `explorations.replace`                    |
| `/api/db/v0/queries/{queryId}/results/`                     | GET         | `explorations.run_saved`                  |
| `/api/db/v0/queries/`                                       | GET         | `explorations.list`                       |
| `/api/db/v0/queries/`                                       | POST        | `explorations.add`                        |
| `/api/db/v0/queries/run/`                                   | POST        | `explorations.run`                        |
| `/api/db/v0/schemas/{schemaId}/`                            | DELETE      | `schemas.delete`                          |
| `/api/db/v0/schemas/{schemaId}/`                            | PATCH       | `schemas.patch`                           |
| `/api/db/v0/schemas/`                                       | GET         | `schemas.list`                            |
| `/api/db/v0/schemas/`                                       | POST        | `schemas.add`                             |
| `/api/db/v0/tables/{tableId}/`                              | DELETE      | `tables.delete`                           |
| `/api/db/v0/tables/{tableId}/`                              | GET         | `tables.get`                              |
| `/api/db/v0/tables/{tableId}/`                              | PATCH       | `tables.patch`, `tables.metadata.patch`   |
| `/api/db/v0/tables/{tableId}/columns/{columnId}`            | DELETE      | `columns.delete`                          |
| `/api/db/v0/tables/{tableId}/columns/{columnId}`            | PATCH       | `columns.patch`, `columns.metadata.patch` |
| `/api/db/v0/tables/{tableId}/columns/`                      | GET         | `columns.list`, `columns.metadata.list`   |
| `/api/db/v0/tables/{tableId}/columns/`                      | POST        | `columns.add`                             |
| `/api/db/v0/tables/{tableId}/constraints/{id}`              | DELETE      | `constraints.delete`                      |
| `/api/db/v0/tables/{tableId}/constraints/`                  | GET         | `constraints.list`                        |
| `/api/db/v0/tables/{tableId}/constraints/`                  | POST        | `constraints.add`                         |
| `/api/db/v0/tables/{tableId}/joinable_tables/`              | GET         | `tables.list_joinable`                    |
| `/api/db/v0/tables/{tableId}/move_columns/`                 | POST        | `data_modeling.move_columns`              |
| `/api/db/v0/tables/{tableId}/previews/`                     | POST        | `tables.get_import_preview`               |
| `/api/db/v0/tables/{tableId}/records/{recordPk}/`           | GET         | `records.get`                             |
| `/api/db/v0/tables/{tableId}/records/{recordPk}/`           | PATCH       | `records.patch`                           |
| `/api/db/v0/tables/{tableId}/records/`                      | GET         | `records.list`                            |
| `/api/db/v0/tables/{tableId}/records/`                      | POST        | `records.add`                             |
| `/api/db/v0/tables/{tableId}/settings/{settingsId}/`        | PATCH       | `tables.metadata.patch`                   |
| `/api/db/v0/tables/{tableId}/split_table/`                  | POST        | `data_modeling.split_table`               |
| `/api/db/v0/tables/{tableId}/type_suggestions/`             | GET         | `data_modeling.suggest_types`             |
| `/api/db/v0/tables/`                                        | GET         | `tables.list`, `tables.metadata.list`     |
| `/api/db/v0/tables/`                                        | POST        | `tables.add`                              |
| `/api/ui/v0/connections/{databaseId}/types/`                | GET         | _(remove)_                                |
| `/api/ui/v0/connections/create_from_known_connection/`      | POST        | `connections.add_from_known_connection`   |
| `/api/ui/v0/connections/create_from_scratch/`               | POST        | `connections.add_from_scratch`            |
| `/api/ui/v0/connections/create_with_new_user/`              | POST        | _(remove)_                                |
| `/api/ui/v0/database_roles/{roleId}/`                       | DELETE      | _(remove)_                                |
| `/api/ui/v0/database_roles/`                                | POST        | _(remove)_                                |
| `/api/ui/v0/queries/{queryId}/shares/{shareId}/`            | PATCH       | `shared_explorations.patch`               |
| `/api/ui/v0/queries/{queryId}/shares/{shareId}/regenerate/` | POST        | `shared_explorations.regenerate`          |
| `/api/ui/v0/queries/{queryId}/shares/`                      | GET         | `shared_explorations.list`                |
| `/api/ui/v0/queries/{queryId}/shares/`                      | POST        | `shared_explorations.add`                 |
| `/api/ui/v0/reflect/`                                       | POST        | _(remove)_                                |
| `/api/ui/v0/schema_roles/{roleId}/`                         | DELETE      | _(remove)_                                |
| `/api/ui/v0/schema_roles/`                                  | POST        | _(remove)_                                |
| `/api/ui/v0/tables/{tableId}/records/delete/`               | DELETE      | `records.delete`                          |
| `/api/ui/v0/tables/{tableId}/shares/{shareId}/`             | PATCH       | `shared_tables.patch`                     |
| `/api/ui/v0/tables/{tableId}/shares/{shareId}/regenerate/`  | POST        | `shared_tables.regenerate`                |
| `/api/ui/v0/tables/{tableId}/shares/`                       | GET         | `shared_tables.list`                      |
| `/api/ui/v0/tables/{tableId}/shares/`                       | POST        | `shared_tables.add`                       |
| `/api/ui/v0/users/{userId}/`                                | DELETE      | `users.delete`                            |
| `/api/ui/v0/users/{userId}/`                                | GET         | `users.get`                               |
| `/api/ui/v0/users/{userId}/`                                | PATCH       | `users.patch`                             |
| `/api/ui/v0/users/{userId}/password_reset/`                 | POST        | `users.password.revoke`                   |
| `/api/ui/v0/users/`                                         | GET         | `users.list`                              |
| `/api/ui/v0/users/`                                         | POST        | `users.add`                               |
| `/api/ui/v0/users/password_change/`                         | POST        | `users.password.replace_own`              |

Functions sorted by name (duplicated for ease of reading):

```
columns.add
columns.delete
columns.list
columns.metadata.list
columns.metadata.patch
columns.patch
connections.add_from_known_connection
connections.add_from_scratch
connections.delete
connections.list
connections.patch
constraints.add
constraints.delete
constraints.list
data_modeling.add_link
data_modeling.move_columns
data_modeling.split_table
data_modeling.suggest_types
explorations.add
explorations.delete
explorations.get
explorations.list
explorations.replace
explorations.run_saved
explorations.run
records.add
records.delete
records.get
records.list
records.patch
schemas.add
schemas.delete
schemas.list
schemas.patch
shared_explorations.add
shared_explorations.list
shared_explorations.patch
shared_explorations.regenerate
shared_tables.add
shared_tables.list
shared_tables.patch
shared_tables.regenerate
tables.add
tables.delete
tables.get_import_preview
tables.get
tables.list_joinable
tables.list
tables.metadata.list
tables.metadata.patch
tables.patch
types.list
users.add
users.delete
users.get
users.list
users.password.replace_own
users.password.revoke
users.patch
```

## Plans for the transition process

1. Answer most of the open questions.
1. Agree on roughly 50% of the function names. This will allow us to establish (and agree on) patterns that we can follow as we move forwards.

1. Transition groups of related endpoints together by following these steps for the entire group:

    1. Merge a backend PR which adds the DB functions (if needed) and adds the json-rpc methods.
    1. Merge a front end PR which switches our usage from REST to JSON-RPC for the group of endpoints.
    1. Merge a backend cleanup PR which removes the REST endpoints.

1. For the first group, we'll transition the following endpoints:

    - `/api/ui/v0/connections/create_from_known_connection/`
    - `/api/ui/v0/connections/create_from_scratch/`
    - `/api/ui/v0/connections/create_with_new_user/`

    This will be a proving ground to validate our transition across the entire stack. We'll make sure we fully complete this group of endpoints before moving on.

1. After that validation, we'll continue by transitioning groups of endpoints in parallel. The backend will be free to run wild with merging PRs that add json-rpc methods.

    To track our progress on a per-endpoint basis, we'll likely end up adding more notes to this wiki page or a GitHub ticket.

## Roles

| Role             | Person |
| --               | -- |
| Backend changes  | Brent |
| Frontend changes | Sean |
