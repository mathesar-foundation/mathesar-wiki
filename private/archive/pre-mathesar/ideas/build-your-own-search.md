---
title: Build Your Own Search
description: 
published: true
date: 2021-04-19T21:19:28.385Z
tags: 
editor: markdown
dateCreated: 2021-04-19T20:18:26.060Z
---

Related to

1. [Accelerate Knowledge, Creativity, and Innovation](../goals/accelerate-innovation)
1. [Innovate Discovery](../goals/innovate-discovery)
1. [Decentralize the Internet](../goals/decentralize-internet)

## Problem

Building a search engine is a difficult and expensive project.  However, a
number of orgs and institutions may be interested in a search engine tailored
to their needs.

## Solution

Provide a tool that allows a team to build a search engine with a minimum
amount of fuss.  The tool should provide:
- A way to define a data model with pertinent info about a given object of
  search (e.g., images)
- A way to scrape data from different sources and feed it via that model into a
  storage database.
- A way to index that data for text searching.
- A GUI to actually search that data
- Some way to deploy the whole thing to the internet.

Ideally, as much as possible should be achievable through a GUI, and there
should be CLI tools covering all functionality as well.

## Challenges

- How many orgs / users really want to build / host an entire search engine?
- Would it be possible to make this general enough to serve a wide variety of
  use cases?

## Thoughts

- We already have a large part of such a project built in the codebase of CC
  Search.
- Maybe this could be more of an "add search to your website" product.
