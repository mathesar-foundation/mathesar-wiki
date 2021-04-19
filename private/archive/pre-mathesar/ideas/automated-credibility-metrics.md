---
title:  Automated Credibility Metrics
description: 
published: true
date: 2021-04-19T20:52:55.870Z
tags: 
editor: markdown
dateCreated: 2021-04-19T20:18:19.529Z
---

Related to [credibility](credibility).

## Problem

It's well known that [_p_-hacking](https://en.wikipedia.org/wiki/Data_dredging)
is a serious problem in modern science.  Another issue is the
[Replication crisis](https://en.wikipedia.org/wiki/Replication_crisis).

## Solution

There should be a standardized resource to determine the credibility of a
paper, without relying on citation numbers alone.
- _p_-hacking can be automatically detected, given an open data set, and the
  set of variables reported in the end (and their significance).  One could
  perhaps develop a metric that could be calculated for how "_p_-hacky" a given
  paper is, and record that metric in some database.
- One could also come up with a way to determine if a paper has ever been
  replicated (or which parts have).
- For papers which are simply analyses of open data sets, the replication could
  be automated?
  
  
## Challenges
- This will probably make many enemies (many)
- Most of these metrics rely on open data backing papers being available.

## Related Projects
There are a number of efforts to try to go beyond citations as the metric.
- [Altmetrics](https://www.altmetric.com/) is a service/site that Amy Brand
  works on which is trying expand beyond just citations.
- James Weis from the CCI Community/MIT recently finished his dissertation on
  ["Optimizing Scientific Innvoation by Learning on Knowledge Graph Dynamics"](https://jw.docsend.com/view/r6rwik6xk3ca9pxv)
  which is an effort to use AI and network science to identify impactful
  work.
- Joi wrote [an article](https://joi.ito.com/weblog/2019/02/04/the-quest-to-topple-science-stymying-academic-paywalls.html) about some of the links between citations,
  academic publishing and openness in Wired.
