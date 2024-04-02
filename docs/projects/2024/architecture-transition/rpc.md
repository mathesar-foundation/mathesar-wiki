# RPC transition plan

This document lays out plans for our 2024 transition from a REST-based API to one based on JSON-RPC.

It is maintained by Sean and Brent.

## Timeline

We want to be fully transitioned to RPC APIs by the **beta release**. Ideally we would not have any REST-based APIs at that point.

## JSON-RPC

### JSON-RPC _spec_

- JSON-RPC is a [spec](https://www.jsonrpc.org/specification) adopted by many libraries.
- You should probably understand this spec before continuing to read this wiki page. Read the spec if needed.
- We'll be using version 2.0 of the spec.

### json-rpc _library_

- We'll be using the [json-rpc](https://github.com/pavlov99/json-rpc) python package, which [integrates with Django](https://json-rpc.readthedocs.io/en/latest/django_integration.html) nicely.
- JSON-RPC is transport agnostic, but we plan on using it exclusively over HTTP for the forseeable future. A time may come when we use it over other transports such as web sockets, but we'll re-evaluate any architectural concerns as needed at that point.
- All requests will be performed using HTTP POST.

### Terminology

- The [spec](https://www.jsonrpc.org/specification) and the [library](https://github.com/pavlov99/json-rpc) are different things (with annoyingly similar names). Wherever possible, we should attempt to disambiguate these things by explicitly saying "JSON-RPC spec" or "json-rpc library".

## Open questions

### Special characters in method names

When using the json-rpc library, what characters are we permitted to use within method names (for the purpose of namespacing)? For example, can we have a method named `schema.add`?

### Docstring syntax

What syntax do want want to adopt within the docstring for each function? Do we want it to be machine parsable?

### TypeScript types

Would it feasible for us to write custom tooling that generates TypeScript types from the introspection capabilities built in to the json-rpc library?

### File uploads

How will we deal with file uploads in `data_files`? Are our needs compatible with JSON-RPC in this case?

### Id values

- The JSON-RPC spec requires that all request objects have `id` parameters (unless they're "notification" request objects, which we probably won't use).
- The id parameter must be a number or string.
- The id parameters are important in the following cases:
    - when sending a batch request — because response objects can be returned in any order within the batch response
    - when using the JSON-RPC spec over a channel like web sockets — because (even non-batched) responses are not issued directly to requests and thus might arrive out of order
- However, when sending a non-batch request over HTTP, the spec does not clearly indicate the purpose of the id parameter — likely because the spec is transport agnostic and does not assume that the transport is necessarily capable of matching responses directly to requests.
- For our purpose, we need to decide what meaning (or lack thereof) the id parameter would have for non-batched HTTP requests. We essentially have two approaches:

    - **Fixed ids**: The client generates id values uniquely scoped to each HTTP request. For a non-batched request, the client uses an id of `0`. For batched requests, the client uses id values `0`, `1`, `2`... and so on.

    - **Sequential ids**: The client generates sequential id values which increment for subsequent requests. The counter is reset when the page is reloaded.

    We could potentially formulate other approaches too, e.g. stringified UUIDs.

- Sean and Brent discussed this.
    - Brent's inclination was to use sequential ids, but he didn't feel strongly about it. His rationale was that maybe someday this decision would come in handy, but he didn't have a clear use case for it in the forseeable future.
    - Sean didn't have an opinion during the call.
    - Upon reflection, Sean formed an opinion leaning towards fixed ids because they would be simpler to implement on the front end. With fixed ids, the front end's request machinery would be stateless. With sequential ids, it would be stateful, adding a small amount of complexity.

### Standard verbs

We'd like to use consistent terminology in our method names. What verbs do we want to use for the following concepts?

- list, get all, select
- get, get one, fetch, return
- create, add, insert, make, new
- partial update, edit, patch, alter
- full update, replace, put, set
- delete, remove, drop

SQL uses different terms for DDL operations (e.g. `CREATE`, `ALTER`, `DROP`) from DML operations (e.g. `INSERT`, `UPDATE`, `DELETE`). Do we want to maintain such a distinction within our API layer?

### Response structure

What general rules-of-thumb should we adopt as we decide the response schema for each method?

### Error structure

What will our error responses look like?

What HTTP status code does the json-rpc library use when returning errors? In what cases will the HTTP status code be meaningful to us, if any?

### Casing transformation

We use snake_case for Python variables and camelCase for JavaScript variables. This case transformation is currently implemented on a ad-hoc basis throughout many of the outermost leaves of the frontend codebase. [Example](https://github.com/mathesar-foundation/mathesar/blob/4f498843480060e59e5378c0238a4981d8cbc91c/mathesar_ui/src/stores/abstract-types/type-configs/money.ts#L104-L109).

If we were starting from scratch, Sean would have a preference for moving this case transformation into an automated step that would happen somewhere like middleware. Being that we're _kind of_ starting from scratch with this new RPC API, is it worth considering adopting a case transformation step like this? Sean thinks it's _probably not_.

## API Standards

These standards are _preliminary_ and subject to change. We'll need to better document them as they become more solidified with our rollout.

### Use named parameters

The JSON-RPC spec supports both named parameters _and_ positional parameters.

We are enforcing a standard of always using named parameters and never using positional parameters.

### Method namespacing

- Noun first, verb second. (This makes the methods easy to sort.)
- _(More specific guidelines will follow after some of the open questions are resolved)_

### When to batch

The move to JSON-RPC opens up the possibility for the front end to consolidate multiple requests into batches. We need to be cautious of this though. While parallel HTTP requests do incur overhead that can be reduced through batching, we need to be mindful that batching is essentially equivalent to `Promise.all()`. Sometimes batching requests might be possible but not preferable. For example if we can update state in one place of the UI with a fast request while concurrently updating separate UI state from a slow request, then we should issue parallel requests. The front end will need to take this behavior into account and make a case-by-case determinations on when it is appropriate to batch.

## Endpoints 🡆 functions

The table below is a comprehensive list of all REST API endpoints used by the front end as of Mathesar 0.1.6. Sean performed an audit of the codebase to extract this list.

**TODO**: fill out the function names in this table.

| Endpoint                                                    | HTTP Method | Function  |
| --                                                          | --          | --        |
| `/api/db/v0/connections/{connectionId}/`                    | DELETE      |           |
| `/api/db/v0/connections/{connectionId}/`                    | PATCH       |           |
| `/api/db/v0/connections/`                                   | GET         |           |
| `/api/db/v0/data_files/{id}`                                | GET         |           |
| `/api/db/v0/data_files/{id}`                                | PATCH       |           |
| `/api/db/v0/data_files/`                                    | POST        |           |
| `/api/db/v0/links/`                                         | POST        |           |
| `/api/db/v0/queries/{queryId}/`                             | DELETE      |           |
| `/api/db/v0/queries/{queryId}/`                             | GET         |           |
| `/api/db/v0/queries/{queryId}/`                             | PUT         |           |
| `/api/db/v0/queries/{queryId}/results/`                     | GET         |           |
| `/api/db/v0/queries/`                                       | GET         |           |
| `/api/db/v0/queries/`                                       | POST        |           |
| `/api/db/v0/queries/run/`                                   | POST        |           |
| `/api/db/v0/schemas/{schemaId}/`                            | DELETE      |           |
| `/api/db/v0/schemas/{schemaId}/`                            | GET         |           |
| `/api/db/v0/schemas/{schemaId}/`                            | PATCH       |           |
| `/api/db/v0/schemas/`                                       | GET         |           |
| `/api/db/v0/schemas/`                                       | POST        |           |
| `/api/db/v0/tables/{tableId}/`                              | DELETE      |           |
| `/api/db/v0/tables/{tableId}/`                              | GET         |           |
| `/api/db/v0/tables/{tableId}/`                              | PATCH       |           |
| `/api/db/v0/tables/{tableId}/columns/{columnId}`            | DELETE      |           |
| `/api/db/v0/tables/{tableId}/columns/{columnId}`            | PATCH       |           |
| `/api/db/v0/tables/{tableId}/columns/`                      | GET         |           |
| `/api/db/v0/tables/{tableId}/columns/`                      | POST        |           |
| `/api/db/v0/tables/{tableId}/constraints/{id}`              | DELETE      |           |
| `/api/db/v0/tables/{tableId}/constraints/`                  | GET         |           |
| `/api/db/v0/tables/{tableId}/constraints/`                  | POST        |           |
| `/api/db/v0/tables/{tableId}/joinable_tables/`              | GET         |           |
| `/api/db/v0/tables/{tableId}/move_columns/`                 | POST        |           |
| `/api/db/v0/tables/{tableId}/previews/`                     | POST        |           |
| `/api/db/v0/tables/{tableId}/records/{recordPk}/`           | GET         |           |
| `/api/db/v0/tables/{tableId}/records/{recordPk}/`           | PATCH       |           |
| `/api/db/v0/tables/{tableId}/records/`                      | GET         |           |
| `/api/db/v0/tables/{tableId}/records/`                      | POST        |           |
| `/api/db/v0/tables/{tableId}/settings/{settingsId}/`        | PATCH       |           |
| `/api/db/v0/tables/{tableId}/split_table/`                  | POST        |           |
| `/api/db/v0/tables/{tableId}/type_suggestions/`             | GET         |           |
| `/api/db/v0/tables/`                                        | GET         |           |
| `/api/db/v0/tables/`                                        | POST        |           |
| `/api/ui/v0/connections/{databaseId}/types/`                | GET         |           |
| `/api/ui/v0/connections/create_from_known_connection/`      | POST        |           |
| `/api/ui/v0/connections/create_from_scratch/`               | POST        |           |
| `/api/ui/v0/connections/create_with_new_user/`              | POST        |           |
| `/api/ui/v0/database_roles/{roleId}/`                       | DELETE      |           |
| `/api/ui/v0/database_roles/`                                | POST        |           |
| `/api/ui/v0/queries/{queryId}/shares/{shareId}/`            | PATCH       |           |
| `/api/ui/v0/queries/{queryId}/shares/{shareId}/regenerate/` | POST        |           |
| `/api/ui/v0/queries/{queryId}/shares/`                      | GET         |           |
| `/api/ui/v0/queries/{queryId}/shares/`                      | POST        |           |
| `/api/ui/v0/reflect/`                                       | POST        | _(none)_  |
| `/api/ui/v0/schema_roles/{roleId}/`                         | DELETE      | _(none)_  |
| `/api/ui/v0/schema_roles/`                                  | POST        | _(none)_  |
| `/api/ui/v0/tables/{tableId}/records/delete/`               | DELETE      |           |
| `/api/ui/v0/tables/{tableId}/shares/{shareId}/`             | PATCH       |           |
| `/api/ui/v0/tables/{tableId}/shares/{shareId}/regenerate/`  | POST        |           |
| `/api/ui/v0/tables/{tableId}/shares/`                       | GET         |           |
| `/api/ui/v0/tables/{tableId}/shares/`                       | POST        |           |
| `/api/ui/v0/users/{userId}/`                                | DELETE      |           |
| `/api/ui/v0/users/{userId}/`                                | GET         |           |
| `/api/ui/v0/users/{userId}/`                                | PATCH       |           |
| `/api/ui/v0/users/{userId}/password_reset/`                 | POST        |           |
| `/api/ui/v0/users/`                                         | GET         |           |
| `/api/ui/v0/users/`                                         | POST        |           |
| `/api/ui/v0/users/password_change/`                         | POST        |           |

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


