---
title: Design Review Guidelines
description: Guidelines for working with design specs
published: true
date: 2021-10-23T19:09:21.178Z
tags: 
editor: markdown
dateCreated: 2021-05-28T21:02:49.613Z
---

The design team creates design specs to describe the design solutions related to the Mathesar product. Whether small or large, all design issues need to be accompanied by a spec containing the solution details and information relevant to its implementation. Every spec goes through a review process so that the team can discuss it and ask questions.

The spec creation begins when a design issue is started and finalizes when the spec is approved and merged. When a design issue is ready for review, a spec is created, and a PR is opened.

Finalizing a design spec means, in most cases, that the design issue has also been solved. If this is not the case, the reason and additional requirements must be communicated in the design issue and the spec.

## Review Process

### Authors

- Clone the [Mathesar Wiki Repo](https://github.com/centerofci/mathesar-wiki) and create a new page under the [Design Specs](/design/specs) directory. Additionally, create a link to it from the top-level [Documents](/design/specs) page.
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

## Advice for Reviewers

- Describe the problem with the design but don't assume a specific design solution
- Strive to think from the user's perspective, not your own
- If you find inconsistencies in the design, describe what you expected to encounter instead
- Adapt your feedback to the design's fidelity level
  - e.g. pointing out alignment issues on wireframes is not useful because they are not meant to be high-fidelity
- Avoid ambiguity, try to articulate problems clearly and concisely
  - Use descriptive words such as "clear", "helpful", "obvious", "confusing", "complex", rather than "bad", "wrong", "off", etc.
- Think backwards from the end-goal
- Don't highlight only negative aspects of the design. Positive feedback provides valuable information.
