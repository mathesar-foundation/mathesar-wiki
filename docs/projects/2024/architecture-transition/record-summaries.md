# Record summaries

As part of the 2024 architecture transition (for Mathesar's beta), we're making some changes to the way that record summaries work. This document describes those changes, along with the rationale.

## Motivation

### Short term (for beta)

- We are seeking to improve performance for beta, and record summaries are currently a major performance drag. Brent sees some low-hanging fruit for improving performance by changing the way record summaries are generated.

- The process for generating record summaries currently relies on significant work being performed in the service layer. As part of our larger architectural transition, we are seeking to move more logic from the service layer into the DB layer. Keeping record summaries in the service layer blocks us from making other architectural changes. The record summary logic ideally needs to be moved down into the DB layer to facilitate our other architectural goals.

### Long term (post-beta)

In their current form, record summaries have a number of limitations. Here are some examples of record summaries that we can't generate:

- (A) A record summary for a person, using their nickname when available while falling back to their first name if needed. This requires calling a function like `COALESCE` within the record summary, which we can't do.

- (B) A record summary which formats a date column into string that's more human-readable than ISO format. This requires calling a formatting function.

- (C) Imagine an e-commerce database where products have categories organized in a hierarchically category tree modeled by a `category` table with a self-referential `parent` FK column. One category has title "Computers" (with `parent` being null), while a child category has the title "Laptops" (with `parent` referring to the "Computers" category).  We'd like to summarize the category table such that the laptops record displays as "Computers > Laptops". Each category should show the full path to itself from the root, joined by a string separator.

- (D) Sometimes the only meaningful way to summarize a record is by using aggregate data. For example, imagine a movies database where each movie can have multiple names. One movie has the names "Amélie" and "Le fabuleux destin d'Amélie Poulain" — but the actual movie record may only have an id, and nothing else meaningful. We'd like to summarize it using aggregate data to produce the string "Le fabuleux destin d'Amélie Poulain, aka Amélie".

Currently we allow users to define their own record summaries via a very simplistic templating system which only allows referencing fields directly on the record. Extending this templating system to handle the examples above would require adding tremendous complexity to the templating system.

Sean's idea is to eventually allow users to define their own _query_ which generates record summaries. Perhaps they would author the queries using something like the Data Explorer, or perhaps they would write raw SQL. The query could call functions in order to handle cases like (A) and (B). The query could contain recursive CTEs to handle cases like (C). And the query could contain aggregations to handle cases like (D).

The scope of changes we're currently making to record summaries for Mathesar beta do _not_ allow users to define such queries. However the changes _do_ lay an architectural foundation for eventually moving in that direction. These future considerations do not require any additional work right now. Rather, the future considerations are informing our architectural design by nudging us toward using flexible query-based logic.


## Old record summaries

_This section reviews the behavior of record summaries as of Mathesar 0.1.7 just to provide context to this document. This behavior is specified in more detail within our [old specs document](../../../design/specs/record-summary.md)._

Without any user configuration, records are summarized by their first non-PK column.

Users can customize the behavior by configuring a record summary template like `{First Name} {Last Name}`. In the front end, this template is converted to string like `{817} {819}`, with the numbers representing the Django ids of column objects. That converted template is then persisted in metadata associated with a table.

Any time a _foreign key column_ is referenced (either explicitly in a template or implicitly via the default template), a "transitive summary" is produced by using the record summary for the referenced table.

As an example, to configure the record summary for the Books table so that books are summarized like "Blink, by Malcom Gladwell", we first need to configure the record summary template for the Authors table as `{First Name} {Last Name}` and then configure the record summary template for the Books table as `{Title}, by {Author}`

## New record summaries

_This section describes how we intend for record summaries to work in Mathesar's beta release._

Without any user configuration, records will be summarized by their first _text-like_ column. This is a slight change. For example, if the PK is text, then we use that. If the PK is numeric and the first non-pk column is a numeric FK column, then we keep looking to see if we can find a text column.

Users will still be able to customize the template, but the template DSL will have slightly new syntax. Column references within curly braces will need to be quoted in the same manner as in SQL. So `{first_name} {last_name}` will work if the columns are `first_name` and `last_name`. But if the columns are `First Name` and `Last Name`, then the template will need to be `{"First Name"} {"Last Name"}`. The same quoting and escaping rules apply as with SQL. Any references which fail to parse correctly are interpreted as string literals to be included in the template verbatim. Users should rarely be interacting with the template DSL manually because Mathesar has (and will continue to have) a button to insert a column into the template.

Record summaries will no longer use the transitive templates of other tables referenced via foreign key columns. So from the Books table, putting `{"Author"}` in a template will not show the _summarized_ author (as before). Instead, it will only show the PK value of the author. To show fields in the author's table, we use dot notation within the curly braces.

From the same example above, to configure the record summary for the Books table so that books are summarized like "Blink, by Malcom Gladwell", we would not need to configure the record summary template for the Authors table. We would configure the record summary template for the Books table as `{"Title"}, by {"Author"."First Name"} {"Author"."Last Name"}`.

The UX for inserting things like `{"Author"."First Name"}` into the template is still TBD, but we expect it to function akin to way we add columns to explorations.

From the user's perspective, the change in the transitive behavior has some advantages and some disadvantages. It's slightly more flexible — but also slightly more tedious. Most importantly though: this modification to the transitive behavior helps us achieve our performance goals.

The record summary template will still be persisted in metadata associated with a table. But instead of persisting it as a string, it will be persisted as a parsed syntax tree. For the example above, that tree looks like this:

```json
[
  [2],
  ", by ",
  [10, 2],
  " ",
  [10, 3]
]
```

That means: first include a reference to the column in the base table having attnum 2; then include a string literal, then include a reference to a column that can be found by joining on the FK at column 10 and finding column with attnum 2 in the joined table... and so on.

## Migration path

When upgrading a pre-beta Mathesar installation to the beta version, and pre-existing record summary templates will be discarded. We will warn users about this in the upgrade instructions, giving them notice that they'll need to manually re-configure any record summary templates they've set up.



