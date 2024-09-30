# 2024-06-18 maintainer meeting

**Attendees**: Sean, Brent, Anish

## "comment" or "description"

Can we decide on consistent terminology to use in our codebase for PostgreSQL comments/descriptions? Personally, I [Sean] prefer that we stick with "description", because that's how we portray this concept to the user.

### Discussion
- `COMMENT` is a SQL syntax thing; Postgres actually uses "description" in most places as well e.g. in the pg catalog table.
- We're fine with standardizing on "description".
- We'll perform a search through the codebase for occurrences of "comment" and replace them with "description" where applicable.
    - We'll ensure that wherever we are dealing with PostgreSQL object metadata (like functions, tables, columns), we consistently use "description".
    - Be mindful of edge cases in SQLAlchemy or other tools where "comment" is used as a keyword and retain it only when necessary.

## Coexistence of multiple patterns for quoting at the SQL layer
I [Sean] want to revisit our discussion around quoting SQL values. Here's what I'd like to propose:

- In the `msar` schema, names in function arguments should be UNQUOTED. (This should already be satisfied.)
- _And_ in the `msar` schema, names in function _return values_ should be also UNQUOTED. (This is not currently satisfied, but would only require small changes to satisfy.)

Adopting the second standard above would allow us to proceed incrementally with our quoting refactor. And we could simplify some code as we go. This approach is in line with the way I've been structuring my PRs thus far. Basically we could consider the `__msar` namespace deprecated and we could seek to rewrite functions into the `msar` namespace as we go, fully adopting the escape-on-output pattern within the `msar` schema.

Previously we agreed that we didn't want to mix patterns. Indeed **I** was vocal about this. But my opinion here has changed after some time working with the code. The realization I've come to is that we _already_ have multiple patterns in some places. And I've noticed bugs due to it. My proposal seeks to slightly move (and clarify) the boundaries around where each pattern is appropriate. Names in arguments and return values would be exclusively quoted within `__msar` functions. And names in arguments and return values would be exclusively _unquoted_ within the `msar` schema. Then, the more we wean ourselves off the `__msar` schema, the more surmountable the quoting refactor would eventually be.

To bring our SQL into conformance with the second standard above, I would:

- Fix the following functions which currently return quoted values.

    - `msar.get_column_name`
    - `msar.get_column_names`
    - `msar.get_constraint_name`
    - `msar.get_relation_name_or_null`

    For each such function we could either: move it into the `__msar` schema; or we could remove the quoting on the return value (refactoring call sites as needed). We could decide between these two strategies on a per-function basis depending on which strategy appears easiest.
    
- Move the following functions into the `__msar` schema.

    - `msar.get_duplicate_col_defs`
    - `msar.process_col_def_jsonb`
    - `msar.process_con_def_jsonb` 

    This is because they return `__msar.col_def` and `__msar.con_def` types which contain quoted values. These functions are not called from the service layer, so this move seems fine to me. Conveniently, those custom types are already in the `__msar` namespace, as I would expect since they contain quoted values.

- Rename `msar.build_unique_column_name_unquoted` to `msar.build_unique_column_name`

    This is because the fact that the column name is unquoted should be evident from the fact that it's in the `msar` schema.

    It's interesting to note here that this function calls `msar.get_fresh_copy_name`, and it's also is _called by_ `msar.build_unique_fkey_column_name`. Both of those functions already return unquoted names (without making the lack of quoting clear in the function name or documentation). This is great example of the waters being even muddier than I first realized when I raised this topic. Multiple patterns are already here! I'm out to separate the wheat from the chaff.

- Rename `msar.get_fully_qualified_object_name` to `msar.build_qualified_name_sql`

    This makes it clearer that the return value is an SQL fragment (quoted) and not an (unquoted) name.

The above changes are easy enough that I'd like to do them now, in a dedicated PR.

### Discussion
- The team is fine with adopting Sean's proposal.
- No objections to making the changes now since Sean has done the research and knows it's quick.

## Handling PostgreSQL objects that are not found

- This topic came up organically from the previous discussion.
- How do we handle situations where an object (like a table or column) is not found in PostgreSQL? Should the function return `null` or throw an error?
    - Different developers have had different approaches – some functions return `null` when an object isn't found, while others throw an error.
- Pros of returning `null`:
    - More flexibility - batch processes won't fail if one object is missing.
    - Absence of object is not necessarily an error, it might not exist.
- Pros of throwing an error:
    - Cleaner error messages, when a `null` is passed through SQL logic, it can lead to confusing error messages that may not easily trace back to the source of the problem.
    - Explicitly throwing an error provides developers with more direct feedback, making it easier to debug.
- No decision
    - Both approaches have merits depending on the context.
- For now:
    - allow both patterns to coexist
    - remain mindful when consuming functions written by others
- Consistency is important
    - We should adopt a standardized approach to avoid confusion.
    - Should have same behavior across similar functions.
    - We should clearly document `null` or error behavior, perhaps in docstrings or inline documentation.
        - Easier for developers to consume.
    - Function names could also serve as documentation e.g. `get_name_or_null`
- Let's try to adopt these suggestions, but also be okay with embracing some chaos in the short term, can clean up later.
