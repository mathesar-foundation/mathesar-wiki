<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [Mathesar Wiki](#mathesar-wiki)
  - [Preview your edits locally](#preview-your-edits-locally)
  - [Contribution process](#contribution-process)
  - [Reference](#reference)
  - [See also](#see-also)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Mathesar Wiki

This repository holds the source content for Mathesar's wiki, as published to:

https://wiki.mathesar.org/

## Preview your edits locally

1. Install requirements

    ```
    pip install -r requirements.txt
    ```

1. Start MkDocs

    ```
    mkdocs serve -a localhost:9000
    ```

1. Preview the docs at http://localhost:9000

1. Keep mkdocs running while you edit and your local preview will refresh automatically.

## Contribution process

- Core team members are encouraged to push small commits directly to `master`.

- Community contributors may suggest changes by opening PRs.

## Reference

- Our docs run on a distribution of [`mkdocs`](https://www.mkdocs.org/) called [`mkdocs-material`](https://squidfunk.github.io/mkdocs-material/). For basics of doc writing, see the [Writing your docs](https://www.mkdocs.org/user-guide/writing-your-docs/) section of `mkdocs` user guide.

- For some customization basics, see [Customization](https://squidfunk.github.io/mkdocs-material/customization/) section of `mkdocs-material`'s Getting started guide. To learn about some of `mkdocs-material`'s features (annotations, code blocks, content tabs, etc.), see its [Reference](https://squidfunk.github.io/mkdocs-material/reference/).

- For page redirects, we use [`mkdocs-redirects`](https://github.com/mkdocs/mkdocs-redirects).

- We use the [awesome-pages plugin](https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin) for some additional control over the navigation system.

- We use the [mkdocs-htmlproofer-plugin](https://github.com/manuzhang/mkdocs-htmlproofer-plugin) to validate internal hyperlinks.

## See also

- The [source content for Mathesar's _documentation_](https://github.com/centerofci/mathesar/tree/develop/docs), which also utilizes MkDocs.

- [Mathesar's homepage](https://mathesar.org/)

- [Mathesar's main source code repository](https://github.com/centerofci/mathesar)
