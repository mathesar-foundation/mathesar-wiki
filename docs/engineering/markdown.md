# Markdown style guide

This page recommends guidelines to follow when writing Markdown in order to keep your content portable, maintainable, consistent, and semantic.

## Indentation

- Use **four spaces** for all indentation.

!!! question "Rationale: 💼 Portability"
    Most Markdown rendering platforms handle other indentation styles with some degree of consistency for _simple_ content, so at first this guideline may appear to be unnecessary. But as content gets more complex, various edge cases tend to crop up which lead to inconsistencies. Maintaining four-space indentation across the board is the best way to ensure your indentation is **always** consistent.

    For example, when some list items are intended by only _two_ spaces:

    - GitHub _nests_ those indented items into into a sub-list
    - MkDocs renders a _flat_ list

!!! tip "Tip: how to handle embedded content with two-space indentation"
    In some cases it can be helpful to keep your _text editor_ set to indent by _two_ spaces (and to manually indent everything by double that amount). For example, if you're authoring content which includes a code block of JSON or TypeScript that has two-space indentation within it, then if you indent that code block within a markdown list the code indentation can get messed up if your text editor is set to indent the markdown by four spaces.
    
## Line breaks

- Do not insert line breaks mid-paragraph.

=== "✅ Good (one long line)"

    ```md
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
    ```

=== "❌ Bad (hard-wrapped lines)"

    ```md
    Lorem ipsum dolor sit amet, consectetur adipiscing elit,
    sed do eiusmod tempor incididunt ut labore et dolore magna
    aliqua. Ut enim ad minim veniam, quis nostrud exercitation
    ullamco laboris nisi ut aliquip ex ea commodo consequat.
    Duis aute irure dolor in reprehenderit in voluptate velit
    esse cillum dolore eu fugiat nulla pariatur.
    ```

!!! question "Rationale: 💼 Portability"
    Markdown rendering platforms have inconsistent behavior for paragraphs containing line breaks.
    
    For example, when a paragraph contains a line break:
    
    - GitHub inserts a `<br>` tag
    - MkDocs ignores the line break

## Blank lines

- Use blank lines between paragraphs, lists, and headings.

=== "✅ Good (with blank lines)"

    ```md
    ## Shopping list

    Here are the things we need to buy at the store:

    - Bread
    - Eggs
    ```

=== "❌ Bad (no blank lines)"

    ```md
    ## Shopping list
    Here are the things we need to buy at the store:
    - Bread
    - Eggs
    ```

!!! question "Rationale: 💼 Portability"
    For example, when a list immediately follows a paragraph:

    - GitHub will render them separately
    - MkDocs will render them together as one paragraph

    Note that when a paragraph or list immediately follows a _heading_, all of the Markdown tools that the Mathesar team currently uses will behave consistently. However there are some more esoteric Markdown rendering platforms that render this sort of content as one paragraph. Sean recommends blank lines as best-practice because it gives your content the best chance of rendering consistently on with other renderers too.

## Headings

- On each page, use one _(and only one)_ level-1 heading (`#`). This should be the page title and should occur before any other content.
- Use level-2 headings (`##`) as the top-most level to separate different content on the page.
- Don't skip nesting levels. For example, If the most recent heading was a level-3 heading, then valid headings which can follow it would be level-2, level-3, or level-4 &mdash; _not_ level-5, because that would be skipping a level-4 heading.

!!! question "Rationale: 📐 Semantics"
    When you follow this rule, the rendered HTML will be styled consistently with other pages and will have a clean structure that other other tools like search engines can understand clearly.

## Ordered lists

- For ordered lists, begin _all_ items with `1.` instead of manually sequencing the numbers.

=== "✅ Good (repeating numbers)"

    ```md
    1. Foo
    1. Bar
    1. Baz
    ```

=== "❌ Bad (sequential numbers)"

    ```md
    1. Foo
    2. Bar
    3. Baz
    ```

!!! question "Rationale: 🛠️ Maintainability"
    Repetitive numbering makes it easier for future editors to insert, remove, and re-order list items.

## Internal hyperlinks

When a Markdown page links to another Markdown page, follow these patterns:

**✅ Good** examples:

| Type | Example |
| - | - |
| Relative child | `[Lorem ipsum](./foo/lorem.md)` |
| Relative ancestor | `[Lorem ipsum](../../lorem.md)` |
| Absolute path | `[Lorem ipsum](/foo/bar/lorem.md)` |
| Index page | `[Lorem ipsum](/foo/bar/lorem/index.md)` |
| Section in current page | `[Lorem ipsum](#lorem-ipsum)` |
| Section in different page | `[Lorem ipsum](./foo/bar.md#lorem-ipsum)` |

**❌ Bad** examples:

| Example | What's wrong |
| - | - |
| `[Lorem ipsum](./foo/lorem)` | missing `.md` extension  |
| `[Lorem ipsum](./some/folder/)` | missing `index.md` file name |
| `[Lorem ipsum][1]` | inconsistent Markdown syntax |

!!! question "Rationale: 🛠️ Maintainability"
    - Following the rules above helps us avoid broken links.
    - MkDocs will detect broken links when building books, but only if the links are absolute and end with `.md`.
    - Using consistent syntax helps us to more easily find-and-replace links when moving pages.

!!! tip "Tip: Custom heading anchors"
    We use the [Attribute Lists](https://python-markdown.github.io/extensions/attr_list/) extension within our MkDocs guides to enable custom named anchors for headings. Use it like this:

    ```md
    ## Section A {:#a}
    
    See [section B](#b) in order to...

    ## Section B {:#b}

    Lorem ipsum dolor sit amet...
    ```

    Giving custom names to your heading anchors is nice because it allows us to change the heading text without breaking the cross-reference. In addition, it allows for shorter URLs.
