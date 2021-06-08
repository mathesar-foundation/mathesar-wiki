---
title: Product Principles
description: 
published: true
date: 2021-06-08T11:00:24.020Z
tags: 
editor: markdown
dateCreated: 2021-06-08T11:00:24.020Z
---

> See also [Design Principles](/design/design-principles)
{.is-info}

# Product

These principles apply to _what_ Mathesar is.

- Mathesar should be able to work as a frontend to existing databases without altering data, even if not all features are available.
- Mathesar is built in a modular way, so that:
	- Our database helper library should be able to be used independently of using Mathesar.
  - Mathesar's backend should support building custom frontend/mobile clients (all actions should be available via API, and should be well documented)
  - Mathesar should support plugins for custom data types, views, data manipulations, etc.
- Mathesar's frontend should have an intuitive, user-friendly, and delightful user interface.

# Process

These principles apply to _how_ we build Mathesar.

- Documentation is meant to be descriptive, not prescriptive.
  - Our aim is to write down what we need to make things easier for ourselves.
  - Avoid rabbit holes (defining/planning out too far into the future), keep focus on getting a product out.
- Iterate, don't try to get things perfect.
  - We are trying to make something that we can put in front of users _quickly_.
  - We might have to change or throw away stuff later, that is absolutely fine.
- Keep implementation simple.
  - Try to minimize assumptions about users, we cannot know what users want ahead of time.
  - Given two options, if both rely on assumptions about users, choose the one that's simpler to implement.