---
title: Design Review Guidelines
description: Guidelines for working with design specs
published: true
date: 2021-10-23T19:09:21.178Z
tags: 
editor: markdown
dateCreated: 2021-05-28T21:02:49.613Z
---

The design team creates specs to describe the design solutions related to the Mathesar product. Whether small or large, all design issues should be accompanied by a spec containing the solution details and information relevant to its implementation. Every spec goes through a review process so that the team can discuss it and ask questions.

The spec creation process begins when a design issue is started and finalizes when the spec is approved and merged. When a design issue is ready for review, a spec is created, and a PR is opened. Finalizing a design spec means, in most cases, that the design issue has also been solved. If this is not the case, the reason and additional requirements must be communicated in the design issue and the spec.

## Review Process

### Authors

- Clone the [Mathesar Wiki Repo](https://github.com/centerofci/mathesar-wiki) and create a new page under the [Design Specs](/design/specs) directory. Additionally, create a link to it from the top-level [Documents](/design/specs) page.
  - Please follow the format of the most recent spec. Spec formats may change over time.
- Add the [spec content](##spec-content) to the page. Make sure the page date is updated as well.
- Once you think the spec is ready for review, create a PR that includes:
  - a link to the referenced design issue from the [Mathesar Repo](https://github.com/centerofci/mathesar)
  - an expected timeline for the review, if any.
- Be sure to include the specific feedback you are seeking.
- Assign the required reviewers by their GitHub username.
  - Always request a review from the Mathesar members with Product or Design roles (see [Team](/team) for handles). If the issue is related to implementation, request a review from members with Engineering roles as well.
- Please post the GitHub PR link to `#design-review:matrix.mathesar.org`.
- If the reviewers request changes or have questions, please make the changes and re-request the review.
- Once everyone has had a chance to review (or the timeline expires) and you're satisfied with the feedback, update the spec and ensure that it all fits together nicely.

### Reviewers

- Check for outstanding [design spec review requests](https://github.com/centerofci/mathesar-wiki/pulls?q=is%3Aopen) at least once a day.
- Comment on the GitHub PR with feedback. Please follow the general advice above.
Once you're done reviewing the document, approve the changes or unassign yourself from the PR if you don't have any feedback.
- Request changes explicitly if you want them included in the spec before it is finalized.
- By sharing feedback, you actively participate in the UX process; make sure you read the context documents and are clear on the user's needs. If needed, ask questions, don't make assumptions.

#### Advice for Reviewers

- Describe the problem with the design but don't assume a specific design solution
- Strive to think from the user's perspective, not your own
- If you find inconsistencies in the design, describe what you expected to encounter instead
- Adapt your feedback to the design's fidelity level
  - e.g., pointing out alignment issues on wireframes is not useful because they are not meant to be high-fidelity
- Avoid ambiguity, try to articulate problems clearly and concisely
  - Use descriptive words such as "clear", "helpful", "obvious", "confusing", "complex", rather than "bad", "wrong", "off", etc.
- Think backward from the end-goal
- Don't highlight only the negative aspects of the design. Positive feedback provides valuable information.

## Spec Content

The spec content will depend on the particular design problem being addressed. However, it is recommended that you include the following parts:

- An overview or summary of the problem.
  - Assume the person looking at the spec didn't read the related issue.
- User Scenarios.
  - Go from simplest to complex so that new details are added incrementally, for example, 'User opens a table' to 'User opens multiple tables at once.
- A link to a prototype or wireframes or any artifact used to demonstrate the design solution.
  - Including video walkthroughs for prototypes or wireframes can help the team better understand the proposed solution.
