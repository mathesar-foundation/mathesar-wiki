---
title: Documentation Strategy
description: 
published: true
date: 2023-04-10T00:00:00.000Z
tags: 
editor: markdown
dateCreated: 2023-04-10T00:00:00.000Z
---

This page describes our various documentation sources and seeks to eliminate gray area between them.

## Docs site

- Source: https://github.com/centerofci/mathesar/tree/master/docs
- Published: https://docs.mathesar.org/
- Scope:
    - **User docs**
    - **Administrator docs** (for people installing/upgrading Mathesar)
- How to edit:
    1. Follow instructions within README to preview docs content locally using mkdocs.
    1. Base your edits on the correct branch:
        - Target `master` if you have an important fix which needs to be published for the currently-released version of Mathesar.
        - Target `develop` if you are adding/updating documentation along with yet-to-be-released changes to the product.
    1. Make a PR against the repo with your changes.
- Notes:
    - The docs site is published from the `master` branch. This is important because we want to ensure that it reflects the latest *released* version of Mathesar so that docs readers who are installing or using Mathesar don't see content before it's actually applicable.

## Markdown near code

- Source: Bespoke `.md` files scattered within https://github.com/centerofci/mathesar/
- Published: *(nowhere, other than the GitHub web interface)*
- Scope:
    - **Developer docs**
    - **Contributor guidelines**
    - **Code standards**
    - **Architectural overviews**
    - **Module documentation**
    - (basically, anything about the *code itself*)
- How to edit:
    1. Make a PR against the `develop` branch.
- Tips:
    - Put documentation close to the code that it documents.
    - Use relative hyperlinks like `[Foo](./bar/foo.md)` to cross-reference other markdown files.
    - Ensure that content is discoverable by linking to it from other places that readers are likely to look.

## Wiki

- Source: https://github.com/centerofci/mathesar-wiki
- Published: https://wiki.mathesar.org
- Scope:
    - ***Public* team docs**
    - **Project planning**
    - **Roles and responsibilities**
    - **Specs**
    - **Meeting notes**
- How to edit (choose any):
    - Make a PR to the repo if your edits warrant review/approval
    - Edit locally and push to `master` for smaller changes (there is no way to preview locally)
    - Edit through the wiki's web interface by logging in

## Other

- Source:
    - https://hackmd.io/team/mathesar
    - https://drive.google.com/drive/u/0/folders/0AJzWWmnmukGHUk9PVA
    - https://github.com/centerofci/mathesar-private-notes
- Scope:
    - ***Private* team docs**

