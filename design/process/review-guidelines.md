---
title: Design Review Guidelines
description: Guidelines for Reviewers of Design
published: true
date: 2021-07-01T20:24:40.771Z
tags: 
editor: markdown
dateCreated: 2021-05-28T21:02:49.613Z
---

# Design Review Guidelines
## General Advice
- Describe the problem with the design but don't assume a specific design solution
- Strive to think from the user's perspective, not your own
- If you find inconsistencies in the design, describe what you expected to encounter instead
- Adapt your feedback to the design's fidelity level
    - e.g. pointing out alignment issues on wireframes is not useful because they are not meant to be high-fidelity
- Avoid ambiguity, try to articulate problems clearly and concisely
    - Use descriptive words such as "clear", "helpful", "obvious", "confusing", "complex", rather than "bad", "wrong", "off", etc.
- Think backwards from the end-goal
- Don't highlight only negative aspects of the design. Positive feedback provides valuable information.


## Review Process
Please follow these guidelines when reviewing designs.

### Authors
- Write your design spec on the wiki under the [Documents]((/design/process/documents) folder and link to it from the [Documents]((/design/process/documents) page.
  - Please follow the format of the most recent spec. Spec formats may change over time.
- Once you think the spec is ready for review, create a GitHub Discussion that includes:
  - the design document and all related resources such as wireframes, prototypes, etc. 
  - an expected timeline for the review, if any.
- Be sure to include the specific feedback you are seeking.
- Tag the required reviewers by their GitHub username.
  - Always tag the Mathesar members with Product or Design roles (see [Team](/team) for handles). If the issue is related to implementation, tag the members with Engineering roles as well.
- Please post the GitHub discussion link to `#design-review:matrix.mathesar.org`. 
- If the reviewers request changes or have questions, please make the changes and re-request the review by posting on the GitHub Discussion and tagging reviewers.
  - Make sure to summarize your changes in your comment.
- Once everyone has had a chance to review (or the timeline expires) and you're satisfied with the feedback, update the document and ensure that it all fits together well.

[Here's an example review request for reference](https://github.com/centerofci/mathesar/discussions/305).

### Reviewers
- Check for outstanding design review requests at least once a day.
- Comment on the GitHub Discussion with feedback. Please follow the general advice above.
- Once you're done reviewing the document, if you don't have any feedback, post on the discussion and say you're done reviewing.
- Specify explicitly if you want another look at the design spec before it is finalized.
- By sharing feedback, you actively participate in the UX process; make sure you read the context documents and are clear on the user's needs. If needed, ask questions, don't make assumptions.
