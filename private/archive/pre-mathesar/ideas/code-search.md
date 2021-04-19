---
title: Code Search Engine
description: 
published: true
date: 2021-04-19T21:17:52.345Z
tags: 
editor: markdown
dateCreated: 2021-04-19T20:18:29.329Z
---

Related to [Innovate discovery](../goals/innovate-discovery)

## Problem

Current tools for searching open-source code online are subpar.  For instance,
We should be able to search "reverse dictionary python" and end up at some
python recipe for reversing dictionaries.  Current code search tools have no
understanding whatsoever (to my knowledge) of the logic of the code.

## Solution

A better code search tool.  It should have all features for finding code
included in your average IDE, but scaled over, e.g., github.  For example, it
should be able to tell the difference between the definition of a function and
its use.  Even better would be translation of "human logic" into code that
implements that logic.

## Challenges
- Translating human logic into searching for code doesn't seem fundamentally
  more difficult than just generating the code.
  
## Thoughts
- This could bring a pretty big benefit to the FOSS community if done well,
  since it would increase interaction and sharing between different projects'
  codebases.
