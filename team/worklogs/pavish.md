---
title: Pavish's work log
description: 
published: true
date: 2023-07-20T11:33:23.341Z
tags: 
editor: markdown
dateCreated: 2023-07-07T17:01:46.847Z
---

## Actively working on
* Get the initial PRs merged.
  - [Shareable links frontend - shared table consumer view](https://github.com/centerofci/mathesar/pull/3093)
	- [Shareable links backend - Models, APIs, bypass auth for table requests](https://github.com/centerofci/mathesar/pull/3092)
* Implement query sharing

## 2023-07-25
* Pondered a bit on how to handle related entities in shared pages, mainly filtering linked records and the record selector
* Discussions

## 2023-07-24
* Started and completed implementing a workaround for seperating app context of shared routes and normal authenticated routes on the frontend
* Split the [large Shared tables PR](https://github.com/centerofci/mathesar/pull/3061) into two, and requested review for both
	- [Shareable links frontend - shared table consumer view](https://github.com/centerofci/mathesar/pull/3093)
	- [Shareable links backend - Models, APIs, bypass auth for table requests](https://github.com/centerofci/mathesar/pull/3092)

## 2023-07-21
* Pondered on how to separate context on frontend for shared routes and normal authenticated routes
* Community Team event

## 2023-07-20
* Reviewed [Auto-focus input when editing number/money cells](https://github.com/centerofci/mathesar/pull/2975)
* Reviewed [Improve cell focus behavior](https://github.com/centerofci/mathesar/pull/2989)
* Got end-to-end flow working for viewing shared tables
* Comms and discussions

## 2023-07-19
* Reviewed installation improvements project and raised some questions.
* Responded to barriers to adoption email
* Weekly meeting
* Continued work on Shared tables:
	- Frontend work on displaying the shared page

## 2023-07-18
* Raised [draft PR](https://github.com/centerofci/mathesar/pull/3061) with models, APIs, and access control for shares
* Needed to figure out if I might hit snags while building frontend, so decided to work on a minimal frontend simultaneously:
	- Added view for page when user views shared entity
  - Added auth bypass for tables, columns, and constraints
  - Work on figuring out passing slug in request header

## 2023-07-17
* Continued work on implementing APIs for Shares
* Work on figuring out auth bypass for tables
* Reviewed approach in [Refactor CellSelection data structure and store](https://github.com/centerofci/mathesar/pull/3037)

## 2023-07-14
* Continued work on implementing APIs for Shares
* Had to fight with the framework for simplifying access control
	- Got to read up on a bunch of DRF and drf-access-policy internals
* Continued thinking on auth bypass & access control for table requests

## 2023-07-13
* Go through backend codebase to understand access controls
* Put some more thought on access control for bypassing table requests

## 2023-07-12
* Write up Shares implementation project
* Update product spec with API structure details
* Continued work on implementing APIs for Shares

## 2023-07-11
* Installation planning meeting
* Chat with Kriti on shareable links API structure
* Work on figuring out API structure needed for shareable links

## 2023-07-10
* Started work on models and APIs needed for shareable links project

## 2023-07-07
* Core team event

## 2023-07-06
* Frontend team meeting
* Weekly meeting
* 1:1 with Kriti
* Installation planning meeting
* Prepped for frontend team meeting
