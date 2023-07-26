---
title: Sean's work log
description: 
published: true
date: 2023-07-20T16:13:14.279Z
tags: 
editor: markdown
dateCreated: 2023-07-07T18:46:25.644Z
---

## TODO

### Active

- [Make column type inference optional](https://github.com/centerofci/mathesar/issues/2358)

### Paused

- [Frontend-fixes project](../../projects/2023-07-frontend-fixes.md)
    - [Refactor CellSelection data structure and store](https://github.com/centerofci/mathesar/pull/3037)
        (Paused while I focus my time on optional inference)

### Backlog

- Resolve [front end code standard prohibiting usage of events on components](https://github.com/centerofci/mathesar-wiki/pull/93)
- PR to add docs on running front end in prod mode
- PR to add docs on loading sample data

--------------------------------------------------------------------------------

## 2023-07-25 Tuesday

- [Chat](https://matrix.to/#/!UnujZDUxGuMrYdvgTU:matrix.mathesar.org/$f5v5Bd_KRNHHVUN4HF-MK9AeV-qDo4uEeXcyYvHabr4?via=matrix.mathesar.org&via=matrix.org) about next steps for Rajat's [i18n PR](https://github.com/centerofci/mathesar/pull/3087).
- Review Pavish's [Shareable links frontend PR](https://github.com/centerofci/mathesar/pull/3093#pullrequestreview-1546069582)
- Push some more commits to my [optional inference PR](https://github.com/centerofci/mathesar/pull/3050)
- Read and respond to product strategy documents in preparation for Wednesday's meeting

## 2023-07-24 Monday

- Open ticket: [Discussion about active cell height design and regression](https://github.com/centerofci/mathesar/issues/3091)
- Review [Use Truncate component in Record Selector table cells](https://github.com/centerofci/mathesar/pull/3077/), pushing some additional commits and merging
- Begin [discussion](https://groups.google.com/a/mathesar.org/g/mathesar-developers/c/45M2ZxoN-Qg) about i18n project workflow
- Open PR to [Copy formatted cell values to clipboard instead of raw values](https://github.com/centerofci/mathesar/pull/3094)
- A small amount of work on optional inference

## 2023-07-21 Friday

- Respond to Ghislaine's ticket [Change in Behaviour of Sorting, Filtering, Grouping and Copy-Paste for Linked Records](https://github.com/centerofci/mathesar/issues/3080)
    - Create ticket: [Copying FK cells should copy the record summary instead of the PK value](https://github.com/centerofci/mathesar/issues/3085)
    - Create ticket: [Behavior when sorting FK columns may be confusing to users](https://github.com/centerofci/mathesar/issues/3084)
- Send weekly project update emails for frontend fixes project and my work within the backend fixes project
- Team meeting
- Continued work on optional inference, pushing some more commits to my [draft PR](https://github.com/centerofci/mathesar/pull/3050)

## 2023-07-20 Thursday

- Meet with Brent and Aritra about summarization functions
- Chat about wiki sync problems
- Create PR with [1 hour quick stab at migration to mkdocs](https://github.com/centerofci/mathesar-wiki/pull/99)
- Create issue [Migrate wiki to MkDocs](https://github.com/centerofci/mathesar/issues/3079)
- Continue working on [Make column type inference optional](https://github.com/centerofci/mathesar/issues/2358)

## 2023-07-19 Wednesday

- Team meeting
- Matrix chat with Kriti about some product design process stuff
- Help triage [Support for column descriptions/comments](https://github.com/centerofci/mathesar/issues/3069)
- Create ticket [Help users understand the connection between descriptions and PostgreSQL comments](https://github.com/centerofci/mathesar/issues/3071)
- Several other smaller discussions
- Push more commits to my draft [CellSelection PR](https://github.com/centerofci/mathesar/pull/3037), beginning to integrate new CellSelection code into TabularData class

## 2023-07-18 Tuesday

- Chat with Rajat about cell selection PR
- Help answer questions for community contributor working on [Use Truncate component in Record Selector table cells](https://github.com/centerofci/mathesar/issues/2345)
- Push more commits to my draft [CellSelection PR](https://github.com/centerofci/mathesar/pull/3037), filling in logic within the scaffolding

## 2023-07-17 Monday

- Open draft PR to [Make column type inference optional](https://github.com/centerofci/mathesar/pull/3050) and begin a discussion soliciting feedback from others
- Open ticket [Gracefully recover from failed type inference during import](https://github.com/centerofci/mathesar/issues/3051)
- Discuss [Refactor CellSelection data structure and store](https://github.com/centerofci/mathesar/pull/3037) with Pavish
- Address review feedback in [Clean up import docs](https://github.com/centerofci/mathesar/pull/3042) and merge
- Review [Scroll sheet all the way down when clicking the New Record button](https://github.com/centerofci/mathesar/pull/3045), adding another commit and merging

## 2023-07-14 Friday

- Send [project update email](https://groups.google.com/a/mathesar.org/g/mathesar-developers/c/GJIzUwk3Zs8)
- Review [Date Input closes now on tab](https://github.com/centerofci/mathesar/pull/3038)
- Call with Dom to discuss type inference issues and brainstorm solutions
- Open PR with [Small clean up to import help text code](https://github.com/centerofci/mathesar/pull/3041)
- Open PR to [Clean up import docs](https://github.com/centerofci/mathesar/pull/3042)
- Some progress to [Make column type inference optional](https://github.com/centerofci/mathesar/issues/2358)

## 2023-07-13 Thursday

- GSoC project meeting with Aritra
- Continued work on cell selection refactor
- Add some more content to my "Querydown for Mathesar devs" Gist, explaining [why I think "mandatory aggregation" is important](https://gist.github.com/seancolsen/42d5f3873e644e3905eaac0b69f876ac#why-i-think-mandatory-aggregation-is-important), with an example using the Data Explorer
- Minor [updates](https://github.com/centerofci/mathesar-wiki/commit/11b9cb8266b72d86718953eceb3ce44843e6c1ca) to [frontend fixes](../../projects/2023-07-frontend-fixes.md) project description

## 2023-07-12 Wednesday

- Open draft PR with scaffolding to [Refactor CellSelection data structure and store](https://github.com/centerofci/mathesar/pull/3037), and write a summary requesting Pavish and Rajat review the approach.

## 2023-07-11 Tuesday

- Re-review [Updated frontend to send a single bulk delete request instead of one request for each record](https://github.com/centerofci/mathesar/pull/2985)
- Re-review [Added margin between breadcrumb selector and bottom of the veiwport](https://github.com/centerofci/mathesar/pull/3014)
- Start discussion about [graceful fallback behavior for all unsupported Postgres data types](https://github.com/centerofci/mathesar/issues/3024)
- Review Varsha's [Sample schema file for API Documentation](https://groups.google.com/a/mathesar.org/g/mathesar-developers/c/invt1JTg7hk)
- Installation planning meeting
- Some progress writing code for [SheetSelection refactor](https://github.com/centerofci/mathesar/issues/1732)

## 2023-07-10 Monday

- Mark Usability Improvements project as "cut short" so that it can be closed
- Add [2023-07 frontend fixes](https://github.com/centerofci/mathesar-wiki/blob/master/projects/2023-07-frontend-fixes.md) project page
- Respond to comment on [Date input should close date picker when losing focus via Tab or Shift+Tab](https://github.com/centerofci/mathesar/issues/1769), posting clearer steps to reproduce.
- Review [Added margin between breadcrumb selector and bottom of the veiwport](https://github.com/centerofci/mathesar/pull/3014)
- Open ticket [Time cell not saved after pressing Tab key](https://github.com/centerofci/mathesar/issues/3018)
- Open ticket [Confusing timezone issue when editing Time cells](https://github.com/centerofci/mathesar/issues/3019)
- Review [Add Peak Time aggregation function](https://github.com/centerofci/mathesar/pull/2981)
- Review [Add Peak Day of Week aggregation function](https://github.com/centerofci/mathesar/pull/3004)
- Review [Add Peak Month aggregation function](https://github.com/centerofci/mathesar/pull/3006)
- Review [Updated frontend to send a single bulk delete request instead of one request for each record](https://github.com/centerofci/mathesar/pull/2985)

## 2023-07-07 Friday

- Team event
- Catch up with some email discussions from the past week
- Re-review [Publicly Sharable Links spec](https://wiki.mathesar.org/en/product/specs/publicly-shareable-links)
- Begin mapping out some thoughts for the SheetSelection refactor RFC

## 2023-07-06 Thursday

- Many meetings:
    - Front end team meeting
    - Core team meeting
    - List data types meeting
    - Installation planning meeting
    - 1/1 with Kriti
- Some work organizing info for upcoming project
- Some work planning Friday's team event
- Review/merge small community dev docs pr [Fix typo error in DEVELOPER_GUIDE.md](https://github.com/centerofci/mathesar/pull/2999)

