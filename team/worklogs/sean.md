---
title: Sean's work log
description: 
published: true
date: 2023-07-07T00:00:00.000Z
tags: 
editor: markdown
dateCreated: 2023-07-07T00:00:00.000Z
---

## TODO

### Soon

- Probably will dig into some of the backlog work below if nothing more pressing comes up while I'm waiting on Pavish/Rajat

### Paused

- [Frontend-fixes](../../projects/2023-07-frontend-fixes.md)
    - [Refactor CellSelection data structure and store](https://github.com/centerofci/mathesar/pull/3037)
        - Awaiting preliminary review by Pavish and Rajat before I continue further work

### Backlog

- Resolve [front end code standard prohibiting usage of events on components](https://github.com/centerofci/mathesar-wiki/pull/93)
- PR to add docs on running front end in prod mode
- PR to add docs on loading sample data

--------------------------------------------------------------------------------

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

