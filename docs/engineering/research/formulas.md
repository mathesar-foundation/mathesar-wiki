# Formulas research

This is a report which details some research that Sean did in 2023-06 to vet the feasibility of implementing Mathesar formulas using PostgreSQL generated columns.

## Postgres generated columns

### Docs

- https://www.postgresql.org/docs/current/ddl-generated-columns.html

### Vis à vis Mathesar

- To build Mathesar formulas, we _could_ leverage Postgres generated columns, but I'm not sure we _should_.

- From our perspective: a proper implementation seems challenging but still surmountable. The hardest parts would appear to be:
    - Providing graceful support for **updating** formula definitions while also preserving oid-attnum references to the column (e.g. in data explorer and other metadata). _(See "Updating a formula" below.)_
    - Security concerns:
        - It's not like we can just escape user input for this like we normally would. How do we guard against SQL injection? It seems like we'd need a library which can parse the user input as a Postgres SQL expression to validate it. I imagine most libraries will be tailored towards parsing _queries_ (not _expressions_), so we might need to employ a hack like using a query parser to parse and validate `f"SELECT {expr};"`
        - Do any _valid_ expressions exist which might pose additional security concerns? For example, is it possible for a user to enter an expression which takes too much time to compute? That could be a denial-of-service concern for a Mathesar SaaS provider. One such expression might be a RegEx comparison. Postgres [says](https://www.postgresql.org/docs/current/functions-matching.html):

            > While most regular-expression searches can be executed very quickly, regular expressions can be contrived that take arbitrary amounts of time and memory to process. Be wary of accepting regular-expression search patterns from hostile sources. If you must do so, it is advisable to impose a statement timeout.

- From a user's perspective:
    - The lack of composition seems like it might be a deal-breaker, especially given that our competitors support it. I don't see any ways around it.

        As a potential next step, it might be interesting to explore the possibility of using triggers instead of generated columns. I can imagine it being a whole lot more work, but maybe giving us the capability of supporting composition.

    - Our competitors support relative time in formulas. This would also be a strike against Mathesar if we use generated columns for formulas. I can imagine a future version of the Data Explorer that would allow users to perform such computations though, so it might not be a deal-breaker from a product design standpoint.

    - Frequent formula definition updates could lead the user to bump into the 1600 column limit described below. My guess is that this would be quite rare though.

- We might consider some small changes to Mathesar that would allow it to play well with generated columns _defined outside Mathesar_:

    - The API should tell the front end when a column is generated, ideally showing the formula definition too.
    - The front end should disallow editing within generated columns, in a manner similar to pk columns
    - When a user updates a table cell, the front end should update the _entire row_ with the API PATCH response. (Currently it only updates the cell edited.)

### Behavior

- ✅ **Defining a formula**

    - Works. Example:

        ```sql
        drop table if exists formulas;
        create table formulas (
          id serial primary key,
          a integer,
          b integer,
          c integer generated always as (a + b) stored
        );
        insert into formulas (a, b) values 
        (1, 7),
        (5, 11);
        select * from formulas;
        ```

    - Generated columns must be materialized. From their [docs](https://www.postgresql.org/docs/current/ddl-generated-columns.html)

        > PostgreSQL currently implements only stored generated columns

- ❌ **Relative time in formulas**

    - This is not possible

        ```sql
        drop table if exists formulas;
        create table formulas (
          id serial primary key,
          a integer,
          b integer generated always as (a + now()::date) stored
        );
        ```

        > ERROR: generation expression is not immutable

- ⚖️ **Inspecting a formula**

    - Formulas can be inspected, although we have no way of recovering the formula definition _exactly_ as the user entered it.

    - This query will show the formula in the `expr` column:

        ```sql
        select
          tbl.oid as table_oid,
          col.attnum as column_attnum,
          tbl.relname as table_name,
          col.attname as column_name,
          def.adbin as expr_raw,
          pg_get_expr(def.adbin, tbl.oid) as expr,
          pg_get_expr(def.adbin, tbl.oid, true) as expr_pretty
        from pg_catalog.pg_attribute col
        join pg_catalog.pg_class tbl on
          tbl.oid = col.attrelid
        join pg_catalog.pg_attrdef def on
          def.adrelid = col.attrelid and
          def. adnum = col.attnum
        where
          col.attgenerated = 's';
        ```

    - A formula entered as `a + b` will display as `a + b`. Good.

    - Columns are quoted with double quotes only when needed. That's nice.

    - A formula entered as

        `CoAlEsCe(a + 0   + /* HI */ b * (1+(1-1)), char_length('BAR'))`

        ...will display as...

        `COALESCE(((a + 0) + (b * (1 + (1 - 1)))), char_length('BAR'::text))`

    - The `expr_raw` column in the above table gives us a window into what's happening here. Postgres stores an AST of the formula, and then renders that AST to a string via `pg_get_expr`.


- ❌ **Updating a formula**

    - This is not supported.

    - The closest thing would be dropping and adding a new column like so:

        ```sql
        start transaction;
        alter table formulas drop column c;
        alter table formulas add column c integer generated always as (a - b) stored;
        commit;
        ```

    - The drop/add approach is fine for queries which reference the column by name (e.g SQL outside Mathesar), but it would break anything referencing the column by oid-attnum (e.g. Explorations). We could conceivably seek to repair those dangling references if the formula is updated via drop/add _through Mathesar_ though.

    - Postgres [says](https://www.postgresql.org/docs/current/limits.html) that tables can have no more than 1600 columns _ever_, including columns that have been dropped. Additionally, some column types contribute more heavily to the count, further reducing this limit. I'm not sure if this limit is a practical concern for our users though.


- ✅ **Renaming a referenced column**

    - This works fine

        ```sql
        alter table formulas rename column a to foo;
        ```

    - Inspecting the formula shows the column's new name afterwards.

- ⚖️ **Deleting a referenced column**

    - It's _possible_ to delete a referenced column, but the resulting behavior may catch users off guard

        ```sql
        alter table formulas drop column a;
        ```

    - The generated column is silently dropped too!
    - I couldn't find a way to define a generated column that protect it against being dropped with this cascade-like behavior.
    - This behavior could be a problem for users. Say a user spend a bunch of time crafting a formula and then decides to swap out one column for another in the formula by deleting the old column first. Ooops!
    - In theory, we could guard against this at the application layer by making it clear that the column has "dependents" and warning the user that dependent generated columns will be automatically dropped too. But pg doesn't seem to offer a clear way to identify them. A quick and dirty way would be to search the stringified AST for occurrences of strings like `:varattno 3` (for column with attnum 3). It seems like that might do the trick. Performance wise, we would only need to search the generated columns within one table, so the fact that `pg_attrdef.adbin` is not indexed doesn't worry me.

- ⚖️ **Type safety**

    - Postgres does a good jod at disallowing formulas to be defined in ways that would lead to type problems.

    - You can't change a column's type once it is referenced in a generated column.

        ```sql
        alter table formulas alter column a type text;
        ```

        > ERROR: cannot alter type of a column used by a generated column Detail: Column "a" is used by generated column "c".

        From a data integrity perspective, this is good. From a UX perspective, we may need to consider what additional features we'd need to build to allow users to change things more easily.

- ❌ **Composition**

    - Generated columns cannot reference other generated columns

        ```sql
        drop table if exists formulas;
        create table formulas (
          id serial primary key,
          a integer,
          b integer,
          c integer generated always as (a + b) stored,
          d integer generated always as (c * 2) stored
        );
        insert into formulas (a, b) values 
        (1, 7),
        (5, 11);
        ```

        > ERROR: cannot use generated column "c" in column generation expression

    - It's interesting to note that SQLite does [not](https://www.sqlite.org/gencol.html) have this limitation:

        > The expression of a generated column can refer to any of the other declared columns in the table, including other generated columns, as long as the expression does not directly or indirectly refer back to itself. 


## Competing products

### NocoDB

- **Docs**: https://docs.nocodb.com/setup-and-usages/formulas/

- **Implementation**

    - Formula columns are _virtual_, not _stored_. That is, they are computed on the fly when the table results are displayed.

    - Formulas are implemented at the _application layer_, not the _database layer_. This means the formula definition is stored in application-specific metadata, and the formula column is not visible within the underlying database. If I update a referenced value outside NocoDB, then the result of the formula that NocoDB displays _will_ update, but only due to the virtual nature of the formula. The source data is read/write accessible outside NocoDB, but not the computed data.

    - NocoDB has its own special formula syntax and functions.

- **Syntax**: `a + b` or `{a} + {b}`

- **Editing**: Single line. No syntax highlighting. Squiggly underlines for syntax error in some cases.

- **Functions** generally try to mimic spreadsheets

- **Updating the formula definition**

    Works, but my syntax is not preserved exactly as I entered it.

- **Relative time in formulas**

    Works

- **Rename a referenced column**

    Some bugs here. The formula re-calculates successfully, but still displays the definition in terms of the old column name. Attempting to edit the formula definition results in an error if the rename is not manually propagated into the formula definition.

- **Delete referenced column**

    Formula returns `ERR`

- **Update source data outside application**

    Works because formula columns are virtual, not stored.

- **Define formula in terms of a column whose name includes a formula token**

    Impossible or too hard to figure out.

    I made a column named `d}` and tried to base a formula on it. I couldn't figure out how to do it.

- **Composition**

    Works

- **Circular references**

    Prevented validation during formula definition

- **Type problems**

    I end up with vague errors such as "Invalid formula" during formula definition.

- **Sorting on formula columns**

    Works

- **UX notes**

    - Hovering the column header shows the formula definition

        ![image](/assets/engineering/research/formulas/b7a53348-4811-42f6-a562-f6d31b955af6)

    - I kept wanted to double-click the _cell_ to edit the formula. Instead, I need to click the column header, then select "edit" from the menu

### Baserow

- **Docs**: https://baserow.io/docs/tutorials%2Funderstanding-baserow-formulas

- For much of what is relevant to Mathesar, Baserow behaves in a very similar manner to NocoDB. Their technical approach and limitations are basically the same.

- Their formula syntax is a bit different though.

- Their formula editor has better UX, and overall the experience has fewer bugs.

- Unlike NocoDB (and Mathesar), Baserow does not support working with pre-existing databases. You _import_ your data into Baserow, and work with it there. Given that product design, it makes sense why they've implemented formulas in the application layer (at least, it makes more sense than NocoDB).


### Others

- **APITable** - I played with this a bit, only from the UI (not looking at the DB layer). Their approach is similar to NocoDB.
- **Retool database** - I looked at this because they seem to be adhering to Postgres idioms more so than our other competitors. Unfortunately they do not support formulas.
- **undb** - They do not support formulas.

