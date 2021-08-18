---
title: API Standards
description: Principles to follow while building our API
published: true
date: 2021-05-28T12:17:44.777Z
tags: 
editor: markdown
dateCreated: 2021-05-26T23:46:24.489Z
---

Mathesar's REST API should be clean, consistent, and generally provide a good developer experience. Although our API supports the Mathesar frontend, it should be treated as its own product and built to support a variety of clients.

All API endpoints should follow the standards below to ensure consistency.

# Standards

Please note that we are assuming that all endpoints are RESTful nd will involve CRUD (create, read, update, or delete) on a resource. This is a deliberate choice so that we try to fit operations into the a RESTful model.

We do want to keep our APIs sensible, so pragmatically, we may eventually need to implement non-CRUD APIs for some things. We will create standards for those when we encounter them.

## Versioning
- All API endpoints should include a version number at the base of the URL (e.g. `/api/v0/tables/`.
- Versions should be integers, not decimal numbers, prefixed with ‘v’.
	- `v0` endpoints are unstable and can change without warning.
	- `v1` endpoints (and onwards) are considered stable. 
- Stable versions should follow these rules:
  - Existing fields/parameters/values should not be removed.
  - New fields/parameters can be added, as long as they do not modify the behavior of existing fields/parameters/values.

## URLs
- A URL identifies a resource.
- URLs should include nouns, not verbs.
- Use plural nouns only for consistency (no singular nouns).
- You shouldn’t need to go deeper than resource/identifier/resource.
- URL v. header:
  - If it changes the logic you write to handle the response, put it in the URL.
  - If it doesn’t change the logic for each response, like OAuth info, put it in the header.
- Specify optional fields in a comma separated list.
- URLs should not include anything other than resource names and IDs.
	- Filters should be in GET query parameters.
  - HTTP verbs should be used for different types of operations

## HTTP Verbs
- Use HTTP verbs (GET, POST, PATCH, PUT, DELETE) to operate on the collections and elements.

| **Verb** | **URL Pattern**         | **Action**                                                         | **Return Status Code** | **Response Data**            |
|----------|-------------------------|--------------------------------------------------------------------|------------------------|------------------------------|
| GET      | /api/v1/resources/      | List all resources                                                 | 200                    | List of resources + metadata |
| GET      | /api/v1/resources/{id}/ | Retrieve single resource with matching ID                          | 200                    | Single resource              |
| POST     | /api/v1/resources/      | Create a new resource with data in request body                    | 201                    | Single resource              |
| PUT      | /api/v1/resources/{id}/ | Replace entire resource with matching ID with data in request body | 200                    | Single resource              |
| PATCH    | /api/v1/resources/{id}/ | Update resource with matching ID with data in request body         | 200                    | Single resource              |
| DELETE   | /api/v1/resources/{id}/ | Delete resource with matching ID                                   | 204                    | *No data*                    |

## Responses

- The portion of the API response describing to a given resource should always contain the same set of keys.
- Keys should not contain values, they should always be a string description of the value.

## Errors
- Error responses should return the appropriate status code and an error message describing the error.
- We should follow the default Django REST Framework error conventions.
  
## Pagination
- We use limit/offset style pagination for all API endpoints.
- All list APIs should include pagination information for consistency, even if there is only one page of results.

# Acknowledgements
Many of these standards were borrowed from the [White House Web API Standards](https://github.com/WhiteHouse/api-standards).