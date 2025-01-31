# Worksheets Product Spec

A "worksheet" would be a new user-facing abstraction which would combine the best of the table page and data explorer into a single, powerful tool. It would also lay a strong foundation for building more features in the near future.

This document is designed to:

- Be the highest-level specs document for an initial "MVP" implementation of worksheets.
- Describe — in detail — what the user would be able to do with worksheets.

## Goals

### High level goals

- <details>
    <summary><b>Page Consolidation</b></summary>

    ---

    Worksheets would unify the table page and the data explorer into a single abstraction with (almost) all the features of both.

    Rationale:
    
    - Currently, there are things you can do in the table page but _not_ the data explorer. For example: edit cells, display record summaries, group rows visually, filter/sort via column header cells, modify display options, drag to re-order columns, and more.
    - Likewise there are things you can do in the data explorer but can't do in the table page. For example: view columns from related tables, summarize data, hide columns, save view settings, and more.
    - Many of the above features would be very useful in combination. For example: view columns from related tables _and_ edit cells.

    ---
    </details>


- <details>
    <summary><b>Modular architecture</b></summary>

    ---

    The worksheet system would be split into two polymorphic parts: the "query" and the "display". One worksheet would always have one query and one display, but each part could be swapped out for a different part of the same type.

    Query types could hypothetically be:

    - A simplistic GUI with filtering and sorting akin to the table page
    - An SQL editor
    - An AI query generator with natural language input
    - An elaborate GUI query builder with a rich drag-and-drop interface

    Display types could hypothetically be:

    - A sheet view akin to the table page, where users can perform data entry
    - An interactive scatter plot, allowing you to click on dots to see/edit more fields
    - A calendar view of data, allowing you to input data too
    - A map view displaying GIS data

    The user would be able to **combine any query type with any display type**.

    Rationale:
    
    - This loosely-coupled architecture would pave the road for a future where we can rapidly develop additional query types and display types by building them in isolation.
    - With more query types and display types in the future, multiplicative combinations would make the worksheets system incredibly powerful.

    For the worksheets MVP, we'd would implement two query types **Basic** and **SQL**, plus one display type: **Sheet**.
    
    ---
    </details>

### Query types

- <details>
    <summary><b>Basic Query</b></summary>

    ---

    The Basic Query would be the "easy to use" query option — and the default query type for a new worksheet.
    
    Like the data explorer:

    - You would choose a **base table** and set of **result columns**.
    - You could choose result columns from the base table or any **related tables** (via forward or reverse FKs).

    Unlike the data explorer:

    - There would be **no limit on the number of FK relationships** used to traverse related tables when selecting result columns.
    - **One-to-many data would require aggregation**. For example if your base table is Authors, you could add `"Books".id`, but you'd need to choose an aggregation function like `count` or `array_agg`. If your base is Books, then you'd be able to add the related author's `"First Name"` column in a straightforward manner, without any option to add aggregation.
    - Within the list of result columns, you would be able to **rearrange the columns** after adding them. Note that this is in the _query_, not the display. Imagine a UI similar to our current record summary template builder — it allows your to drag to re-order the columns you've chosen.
    - The user would have the ability to imperatively **add all remaining columns from the base table** via a button or menu option. This action would look at the base table's columns in PostgreSQL and append any missing columns into the query's set of result columns.

    Like the table page:
    
    - It would allow you to perform simple filtering and sorting (on any result column) via a GUI.

    Unlike the table page:

    - There would be no "Group" option. See "Outline view" below for the new feature that would replace that functionality.

    Additionally:

    - You would be able to convert any Basic Query into an SQL Query.
    - You would be able to set aliases for columns to assign names to them within the worksheet. This feature is necessary to disambiguate identically-named columns from related tables.
    - The interface would make it hard (but not impossible) to define a query which lacks the primary key column(s). This is to guide the user towards a query that will allow DML (explained more below). The precise UX is TBD, but here's one way it could work... After the user selects a base table, Mathesar would automatically add the pk (or unique) column(s). If the user later chooses to remove those columns from the query, Mathesar would display a confirmation dialog first in order to explain that DML would not be possible with no identifying columns. However we design the UX, the point is: there would be some additional grease for the idiomatic path (where pk columns are included) and additional friction for the idiosyncratic path (where pk columns are excluded).

    ---
    </details>

- <details>
    <summary><b>SQL Query</b></summary>

    ---

    The SQL Query type would allow users to manually enter SQL into Mathesar.

    You would _not_ be able to convert an SQL query into a Basic query.

    Rationale:

    - Users have upvoted our [SQL roadmap discussion](https://github.com/mathesar-foundation/mathesar/discussions/2277)
    - One user [said](https://github.com/mathesar-foundation/mathesar/discussions/3550#discussioncomment-9185862) _"i would be satisfied if the Data Explorer required you to use raw SQL to construct queries"_ and also gave some [example queries](https://github.com/mathesar-foundation/mathesar/discussions/3532#discussioncomment-9153129).
    - With the worksheets system supporting SQL, we'd have a solid foundation to build other query types later by building things that _generate_ SQL, for example natural language querying via LLM.

    ---
    </details>

### Display types

- <details>
    <summary><b>Sheet Display</b></summary>

    ---

    The Sheet display type would function similar to the sheet interface on the table page, ideally with a minimal amount of regression in functionality. (More of its features are described within separate "goals" below.)

    The Sheet would have the following user-editable configuration:

    - Display options for all columns (mirroring the column metadata we currently have)
    - Customized column widths
    - Record summary configuration for FK columns (described in more detail below)

    ---
    </details>

### Worksheet types

- <details>
    <summary><b>Ephemeral worksheets</b></summary>

    ---

    Similar to explorations, the user should be able to build a worksheet and use all of its features _without_ saving it.

    ---
    </details>

- <details>
    <summary><b>Named worksheets</b></summary>

    ---

    Similar to explorations, the user should be able to **save** a worksheet. 
    
    - Each saved worksheet would:
        - live inside a schema.
        - have a name, unique among all the worksheets within the same schema.
    - All database collaborators would be able to modify the definition of saved worksheets and re-save them.
    - It would not be possible to move the worksheet to a different schema.
    - The worksheet interface would visually indicate the save status to users, making it clear whether the definition of a saved worksheet has been modified since it was last saved.
    - On the Schema page, Mathesar would list Saved Worksheets instead of explorations.

    Unlike explorations:

    - The user would also have the option to save worksheet changes _as a new worksheet_.

    ---
    </details>

- <details>
    <summary><b>Auto-generated default worksheets</b></summary>

    ---

    The Worksheets MVP project would replace the current Table Page with a worksheet interface.
    
    Here is how it would work:

    - The Schema Page would still show a list of tables (as it currently does).
    - Clicking on a table within the list would open the "Default Worksheet" for that table.
    - The default worksheet would begin as an auto-generated worksheet having:
        - A **Basic Query** with:
            - All columns in the table, in the order from PostgreSQL.
            - No filter conditions
            - One sort condition applied on the primary key if possible
        - A **Sheet Display** with default configuration
    - The user would be able to freely modify the auto-generated worksheet, with their changes triggering the "unsaved changes" visual indicator.
    - With any unsaved changes, the user would be able to save the auto-generated worksheet as a new _named worksheet_.
    - With _certain types of unsaved changes_, the user would also be able to save their changes by updating the default worksheet to a _customized default worksheet_. Mathesar would only allow this action when the query:
        - contains all the columns in the base table and no more
        - has no filter conditions
        - has no column aliases

    ---
    </details>

- <details>
    <summary><b>Customized default worksheets</b></summary>

    ---

    Customized default worksheets would be opened by clicking on a table, just like an auto-generated default worksheet. To the user, the two kinds of worksheets would appear identical. But the _customized_ default worksheet would be a _saved_ worksheet. Just, instead of being saved with a name, it would be saved by association to a table.
    
    Customized default worksheets would serve as a metadata container, allowing the worksheet system to entirely replace our current column metadata and replace some of our current table metadata.

    ---
    </details>

### Specific Features

- <details>
    <summary><b>DML</b></summary>

    ---

    Within the some display types, the user should be able to **edit data**.
    
    - For example, with the Sheet display type, the user should be able to add records, delete records, and edit cells.
    - This should be possible regardless of the query type. So for example, the user should be able to query via SQL and then edit cells.
    - The worksheet system will thus need a mechanism to trace down the origins of each cell _regardless of the query type_.
    - Other (future) display types might implement data modification too, for example a calendar view in which people can add/edit events. So the data origin tracing mechanism needs to be general-purpose enough to work with polymorphic queries and displays.
    - Not all cells necessarily need to be editable. The more we can make editable, the better, but some are obviously impossible, and that's okay.

    ---
    </details>

- <details>
    <summary><b>DDL</b></summary>

    ---

    From the Sheet display, we should support the same DDL operations that the table page currently supports. This means the display needs to understand the origin of each column so that it can modify it.

    There are a great deal of UX problems to solve here. For example... How do we communicate the difference between removing a column from the query and dropping the column from an underlying table? Same question for inserting. Subsequent specs will answer UX questions like these.

    This means that, for the worksheets MVP, we would not attempt to build some sort of schema-level UI for DDL operations. Instead, Mathesar's means of DDL would be a worksheet with a Sheet display.

    ---
    </details>

- <details>
    <summary><b>Pagination</b></summary>

    ---

    Control over pagination would be delegated to the _display_ — not the _query_. 
    
    This design has the following implications:
    
    - In order to send a final query to PostgreSQL, the worksheet system would combine the query's definition (potentially raw SQL) with the pagination set in the display. From an implementation perspective, this would be feasible by wrapping the query in a CTE and applying LIMIT/OFFSET outside the CTE.
    - All display types would need to implement their own pagination UI.

    A user would also be free to write their own SQL with LIMIT/OFFSET statements, but the worksheet system would make to attempt to strip them or present them in the UI. The display pagination would be applied on top of any LIMIT/OFFSET present in the user-defined SQL.

    ---
    </details>

- <details>
    <summary><b>Record summaries</b></summary>

    ---

    Like the current table page, the Sheet display would:

    - Be capable of displaying record summaries for FK columns.
    - Allow the user to configure the record summary template.

    Additionally, the Sheet display would also:

    - Allow users to configure the record summary template on a _per-column_ basis, rather than _per-table_. Configuring it _per-table_ would no longer be possible.
    - Allow users to disable record summary display on a per-column basis, displaying the raw values instead.

    Notes:

    - The record summary configuration would be stored inside the Sheet configuration inside the worksheet.
    - Record summary configuration is more than just a display option because it affects what we need to send to PostgreSQL. So, somewhat like pagination, the worksheet system would delegate control over record summaries to the _display_. The display would be responsible for informing the worksheet about the record summaries it needs, and the worksheet would combine that information with the query definition to formulate a full query to send to PostgreSQL
    
    Other changes:

    - With the record summary template being moved to storage per-column instead of per-table, the only place left that we'd need to use per-table record summaries is on the record page. On that page we use the record summary to generate the page title. To allow the user to still configure the template on a per-table basis, we'd add a mechanism to the record page for doing so. And to store this configuration, we'd continue using our the record summary template field in our TableMetadata model.

    ---
    </details>

- <details>
    <summary><b>Query mutation via display</b></summary>

    ---

    The worksheet container would have a mechanism to allow some small query mutations to be performed _via the display_. Only certain query types and certain display types would support query mutation via display. For the worksheets MVP, it would be the Basic Query and the Sheet Display.

    Here are the cases we need to handle for the MVP:

    - Re-ordering query columns via drag-and-drop on column headers in display.
    - Remove query column via context menu in display
    - Add/remove filter/sort conditions via context menu in display

    To reiterate: these features would only be available when the query is a Basic query. With an SQL query, the user would need to manually edit the SQL to accomplish these tasks.

    ---
    </details>

- <details>
    <summary><b>Row grouping</b></summary>

    ---

    The Sheet display would have a "Group" feature similar to the "Group" feature on the current table page.
    
    But it would **differ** in some important ways:

    - **Pagination would be inside groups** (rather than groups inside pagination). The default page size per group would be 20.
    - The list of groups (within the root level or a parent group) would also be paginated, with the default page size again being 20.
    - Groups would be **collapsible**.
    - With multiple grouping columns applied, the groups would be **nested**, allowing them to be collapsed and expanded at multiple levels.
    - With all of the grouping columns being writable via DML, each **group would have its own "Add Record" button**. This would  allow the user to insert a record directly into a group. (Folding groups would not have their own placeholder row though — just a button.)
    - The sorting of groups would be specified per-grouping-column, either ascending (default) or descending.
    - The user would be able to collapse or expand all sibling groups together. This would not affect parents, children, or cousins.
    - Depending on the implementation we choose, it might be necessary to place a cap on the _depth_ of grouping, perhaps setting a maximum of three levels deep.
    - The grouping definition UI would allow the user to re-arrange the grouping columns (similar the re-arranging currently implemented for sorting columns).


    Rationale:

    - The above design would offer a far superior UX to our current Group feature. Much of our current grouping logic would need to be re-implemented for worksheets anyway, so it's worth it to take a fresh look at the overall structure of this feature in order to improve it.

    ---
    </details>

- <details>
    <summary><b>Data exporting</b></summary>

    ---

    Data export functionality would be delegated to the display.

    The Sheet display would offer a data export feature similar to our current table export, but it would not be available when row folding is enabled.

    Other (future) display types might implement their own export capabilities, for example exporting a chart to SVG, PNG, or PDF format.

    ---
    </details>

- <details>
    <summary><b>Resilience against modified objects</b></summary>

    ---

    "Resilience" here means: if the database structure changes outside of Mathesar, nothing breaks inside of Mathesar.

    Currently, Mathesar has the following resilience characteristics:

    > - ✅ Added columns
    >     - Good because Mathesar displays new columns where the user would expect — in the table page
    > - ✅ Dropped columns, with the table page
    > - ❌ Dropped columns, with the data explorer
    >     - Bad because a if a dropped column is referenced within an exploration, the whole exploration breaks, leaving the user no way to recover it.
    > - ❌ Dropped tables, with the data explorer
    >     - Bad for the same reason as dropped columns
    > - ✅ Renamed columns
    > - ✅ Renamed tables
    > - ❌ Column attnum modification
    >     - E.g. if a data migration tool adds a new column instead of changing the type of an existing column, the column won't be included in a record summary template, even if it has the same name as before. This is because we use attnums to reference columns.
    > - ❌ OID modification
    >     - E.g. if a table is exported via pg_dump and re-imported it will get a new OID, breaking URLs to the table, explorations using the table, and table-level metadata.
    
    For Worksheets, the data structures we choose will affect the resilience characteristics. And because those data structures are beyond the scope of this spec, we do not specify the exact resilience characteristics for Worksheets just yet. But it should be a high priority to design the algorithms and data structures so as to **avoid regressions in resilience**. If we can _improve_ resilience too, then great!

    Notable considerations

    - When a new **column is added** to a table:
        - Ephemeral worksheets and named worksheets should remain unaffected, requiring users to manually add the new column before they see its data.
            - In some cases, users might not expect this behavior. For example if they begin with a default worksheet, resize a column, then save a new named worksheet, the named worksheet won't get new columns added to it. Thus, we could employ the following mitigation strategies to help give users the correct expectations. When saving a default worksheet as a named worksheet, the UI would make this "new-column" behavior clear to users. When adding a new column to a table, the UI would also mention this behavior.
        - Auto-generated default worksheets would automatically see the new column when generated.
        - Customized default worksheets are trickier... Since the default worksheet serves as a representation of the table, the new column _must_ display automatically. But a customized worksheet already holds state which lists columns. To solve this source-of-truth problem,  Mathesar would reconcile the worksheet's columns with the PostgreSQL columns before loading a customized default worksheet. If the worksheet is missing a column, then the new column would be added and the customized default worksheet would be updated before it is loaded. The user would see the new column, and all changes would be saved already.

    - When a **column is dropped**:
        - We need to make sure that a customized default worksheet for the table doesn't break!
        - So within a customized default worksheet, the reconciliation process described above for _added_ columns should also be implemented for _dropped_ columns.
        - Plus, we might be able to easily apply the same dropped-column reconciliation logic to _named_ worksheets too. But it could require more consideration. If a dropped column is referenced within a filter condition, it might not be appropriate to automatically remove it.
    
    - Resilience for display configuration
        - The worksheet's _display_ will also need some level of resilience against changes to the worksheet's _query_. For example, if the user has given a column a custom width (in the display), it would be great if we could maintain that customization even in the face of changes to the column's alias and/or ordering index (in the query). We may need to get clever to accomplish this! But that same cleverness may well prove useful in handling other resilience scenarios too.

    ---
    </details>

- <details>
    <summary><b>Query safeguards</b></summary>

    ---

    The worksheets system would (for the time being) restrict user-defined SQL to one SELECT statement. And it would ensure (recursively) that any nested statements are SELECT statements as well. This would prevent the user from executing DDL or DML within worksheets. It would (for better or worse) also prevent users from creating temporary tables for their queries.

    Rationale:

    - Although these safeguards would add extra work for us, it seems prudent to move cautiously with a user-facing SQL editor and be careful not to give users too much power at once. Some Mathesar administrators might be comfortable giving their users the ability to edit data through the UI but wary of giving them the ability to do so via SQL.

    ---
    </details>

## Concessions

To complete the Worksheets MVP, we would sacrifice the following user-facing functionality for the sake of development velocity. We could consider adding these features back in the future.

- <details>
    <summary><b>Abandon URL storage of filter/sort/group/pagination</b></summary>

    ---

    Currently, the Table Page has a nice feature to serialize the filter/sort/group/pagination settings into the URL so that you can bookmark or share a link to a table with it being pre-filtered.
    
    We would not attempt to replicate this functionality within the Worksheets MVP.

    ---
    </details>

- <details>
    <summary><b>Stop aiming to build a whole GUI query builder</b></summary>

    ---

    Currently, the Data Explorer attempts to provide a GUI query builder. However, our user testing has demonstrated that it does a very poor job of striking a balance between power and ease of use. It often falls into an uncanny valley between the two, being underpowered and too difficult to use.

    In the worksheets MVP, the "Basic Query" would offer ease of use, and the "SQL Query" would offer power.

    ---
    </details>

- <details>
    <summary><b>Eliminate the distinction between "viewing" and "editing" explorations</b></summary>

    ---

    Currently, the Data Explorer has separate pages for viewing vs editing a saved exploration.

    In the worksheets MVP, there would be no separate "view" page. It would just be one page where the user can run the worksheet and edit its definition.

    ---
    </details>

- <details>
    <summary><b>Undo/redo in data explorer</b></summary>

    ---

    Currently, the Data Explorer has "Undo" and "Redo" buttons which alter the exploration definition. For simplicity's sake the Worksheets MPV would not have this feature.

    ---
    </details>

- <details>
    <summary><b>Change the way we think of the "Group" feature on table page</b></summary>

    ---

    The "Group" feature currently available on the table page would be replaced by the "Outline View" (described in the Goals section above). This would likely be a net-win but could potentially result in some minor regressions in functionality depending on the final implementation.

    ---
    </details>


## Possible future goals

These hypothetical goals demonstrate exciting features that we could build _on top of_ worksheets later. Although we would _not_ build these features initially, they're listed below in order to delineate scope, encourage robust architectural decisions, and further substantiate the worksheets proposal as a whole.

- <details>
    <summary><b>Improvements for many-to-many data</b></summary>

    ---

    Back in late 2023, conversations about worksheets actually grew out of conversations about improving user flows and experience for many-to-many data! Here is how worksheets could lay a groundwork for such improvements:

    - We could have a new "multi-record" _cell_ type which the Sheet would display whenever it sees a column defined as an `array_agg` of primary key cells. (As currently spec'ed, the user would be able to produce such columns via the Basic query or the SQL query.) The multi-record cell would work as follows:
    - It would allow the user to _view_ by displaying multiple record summaries as pills. Possibly the user could also expand the view to see more details in a modal.
    - It would allow the user to _edit_ by adding or removing records. These edits would result in INSERT/DELETE statements.

    ---
    </details>

- <details>
    <summary><b>Additional display types</b></summary>

    ---

    Each of these additional display types would accept their own special configuration to control the mapping between result columns and the rendering of the display. The worksheet container would present that configuration UI to the user within an inspector panel.

    - **Charts and graphs** — e.g. scatter plot, line chart, bar chart, pie char, etc.
    - **Calendar display** — e.g. where the user would be able to move through months or weeks or days, see events, and edit events too
    - **Map display** — The base map would be set via configuration, possibly with API keys used for lookup of base map tiles (e.g. Mapbox, Google). Then the user could configure geometry to display atop the base map by selecting columns from the result set. There could even be mouse interactions to select geometry for more detailed inspection of other fields not displayed on the map.
    - **Card view** — The user could configure fields displayed on the card, plus the action to take when clicking the card.

    ---
    </details>

- <details>
    <summary><b>Additional query types</b></summary>

    ---

    - **GUI query builder** — Perhaps at some point we'd want to take a second stab at building something like the data explorer's GUI query builder — but better. This could be implemented as a drop-in query type.
    - **AI query** — This would take natural language input, combine it with Mathesar's knowledge of the schema, and use an AI model to generate SQL.

    ---
    </details>

- <details>
    <summary><b>AI-generated worksheets</b></summary>

    ---

    In addition to generating SQL from a natural language prompt, Mathesar could offer a feature to generate and entire _worksheet_ from a natural language prompt. For example:

    > Show me a line chart of the number of checkouts per month over the past year. Use separate lines for checkouts at different library branches.

    ---
    </details>

- <details>
    <summary><b>Reactivity</b></summary>

    ---

    Here's a tricky situation... Let's say you have a query like this:

    ```sql
    SELECT
        "Books".id,
        "Books"."Title" AS title,
        "Books"."Author" AS author,
        "Authors"."First Name" AS author_first_name,
        "Authors"."Last Name" AS author_last_name
    FROM "Books"
    LEFT JOIN "Authors" ON "Authors".id = "Books"."Author"
    ```

    In the Sheet, the `author` column would display record summaries by default, because it's an FK column. And it would allow editing via the record selector. Now let's pretend you _modify_ an `author` cell. What should happen to the `author_first_name` and `author_last_name` cells with the row you just edited?

    Ideally those dependent cells would update too, showing you the latest data. But implementing that auto-updating logic is actually somewhat difficult!

    With arbitrary SQL, the worksheet wouldn't necessarily have unique rows, even if each row did have primary keys to allow editing. We could refresh the _entire sheet_, but that could be problematic if other things have changed too — e.g. many rows inserted by another user that throws off the pagination.

    For the Worksheets MPV, we will not worry about auto-updating any dependent cells. The user will need to **manually click a Refresh button to see dependent cells update.**

    Post-MVP, we could spend more time considering this problem and implementing a solution.

    ---
    </details>

- <details>
    <summary><b>Formulas</b></summary>

    ---

    Within the "Basic Query", we could extend the UI for entering filter conditions and result columns by providing a **GUI _expression_ builder**. This would be _much_ easier to design and build than a fully-fledged GUI _query_ builder because the problem is much narrower in scope. So I think we actually _could_ design and implement something with the right mix of power and ease-of-use. It would allow the user to (for example) add a calculated result column which shows the sum of two fields; or filter on two columns being equal to each other.

    ---
    </details>

- <details>
    <summary><b>Privately-saved worksheets</b></summary>

    ---

    In addition to saving worksheets within the group of collaborators, users might want to save worksheets to their own user account. The main use case here would not be "privacy" per set, but rather that people commonly want to experiment or dabble around without cluttering up the workspace of other users.

    ---
    </details>

- <details>
    <summary><b>Worksheets saved to URL</b></summary>

    ---

    The entire worksheet definition could theoretically be serialized into the URL client-side, as we currently do for the filter/sort/group/pagination params. This would allow ephemeral worksheets to be shared via the URL. 
    
    Since the worksheet definition could become quite large, an alternate approach would be to permanently save every worksheet definition within the internal database every time a worksheet is run. We could index it on its hash. Then on the client we could update the URL with a new hash whenever the worksheet definition is modified. This would allow worksheets to _effectively_ be ephemeral (because the user wouldn't need to bother with naming them or finding a place to save them), and the URL would be kept concise for easy sharing.

    ---
    </details>

- <details>
    <summary><b>Public worksheets</b></summary>

    ---

    We could resurrect our killed "public sharing" feature as follows:

    1. We'd have a model in the internal database called `WorksheetShare` with the following fields:

        - `worksheet` - a reference to a saved worksheet
        - `role` - a reference to a saved role password
        - `slug` - (unique) a small text field used to lookup the share.

    1. When anonymous visit a URL with the slug, the worksheet would be rendered and the user would be given access to it through the corresponding PostgreSQL role.

    This could even allow people to set up anonymously _writable_ worksheets! So we'd need to UI to warn people of the implications here.

    The worksheet _definition_ would not be writable by anonymous users.

    ---
    </details>

- <details>
    <summary><b>Worksheet composition</b></summary>

    ---

    It would be cool to base a worksheet's query on top of the query used in another saved worksheet. This would allow the user to define query pipelines with the ability to view, edit, and reuse each step in isolation.

    To expose this feature in raw SQL, we could have a "magic" schema name, configurable per-database, that would refer to the worksheets stored within the database. It could default simply to `worksheets` for simplicity. And the user could change the configuration to another name in the case that they actually had a real schema with that name.

    ---
    </details>

- <details>
    <summary><b>Save worksheet as pg view</b></summary>

    ---

    Mathesar could save the query as a PostgreSQL view and replace the query definition with simply selecting from the view.

    ---
    </details>

- <details>
    <summary><b>Parameterized worksheets</b></summary>

    ---

    1. A worksheet could define a set of parameters with names and types.
    1. The query would be able to reference parameters in certain places. For example, a Basic query would be able to reference parameters in filter values. A SQL query would ideally be able to reference parameters too, but we'd need to be clever about figuring out a parser-friendly way to do this.
    1. In order to execute, the worksheet would need to have values supplied for these parameters. In building the worksheet, the user could supply sample values to be used.
    1. The worksheet could be embedded into other contexts which can supply parameters, (e.g. the record page)

    ---
    </details>

- <details>
    <summary><b>Configurable record page</b></summary>

    ---

    Using parameterized worksheets, the user could configure any number of worksheets to display on the record page, replacing the current "table widgets" as needed.

    ---
    </details>

- <details>
    <summary><b>SQL editor LSP</b></summary>

    ---

    Supabase has been developing a [PostgreSQL language server](https://github.com/supabase-community/postgres_lsp) that we could plug into our SQL editor to provide a really nice experience for query authoring.

    ---
    </details>


## Subsequent specs to produce

- <details>
    <summary><b>Data structure spec</b></summary>

    ---

    This spec must describe the following data structures:

    - a "Basic Query" instance
    - a "SQL Query" instance
    - a "Sheet" display configuration
    - a whole worksheet instance, including
        - how its contained query and display definitions would be stored
        - how it would be saved to the internal database, along with its name

    It must clearly specify how these data structures reference database objects. Do they use OIDs, names, or some combination thereof. In the display, how would the column display options (e.g. customized width) be associated with columns? Names? Indexes? Something else? (As such, there might be some interdependence between this spec and the Query Analysis Spec.)

    ---
    </details>

- <details>
    <summary><b>Query analysis spec</b></summary>

    ---

    In order to satisfy the DML, DDL, and query safeguard goals, the worksheets system would need a way of analyzing the query — even user-authored SQL — to understand what is happening and trace down the origins of each result column. The query analysis spec needs to answer:

    - How would such analysis be performed?
    - Where in our stack would it run? (And consequently, what language would we use to implement it?)
    - What output would the analysis generate?

    ---
    </details>

- <details>
    <summary><b>UX spec</b></summary>

    ---

    This spec should provide mockups and behavioral descriptions to specify:

    - The worksheet container
    - The Basic query editor
    - The SQL query editor
    - The Sheet display, including inspector

    ---
    </details>

- <details>
    <summary><b>API spec</b></summary>

    ---

    This spec must describe all RPC methods, parameters, and return values required for implementation.

    In particular:

    - Walk through the lifecycle of a worksheet from start to finish, specifying the ways in which API requests are triggered. Under what circumstances might the _query_ part need to trigger API requests? The _display_ part? The worksheet container?
    - Implementing row grouping does not seem straightforward. How will data-fetching and rendering work?

    ---
    </details>

- <details>
    <summary><b>Part interface specs</b></summary>

    ---

    The worksheet container would orchestrate communication between query and display by passing the each part a set of dependencies. Here, we specify what each part needs to be able to do:

    For example, the query part needs to be able to:

    - Statically inform the container whether it supports re-ordering columns. _(The Basic Query would. The SQL Query would not)_.
    - Imperatively receive instructions from the container to re-order its columns.
    - Imperatively send its query definition to the container when changed.
    - _etc..._

    For example, the display part needs to be able to:

    - Reactively know whether the query is capable of re-ordering its columns.
    - _etc..._

    We need to flesh these out, ideally as TypeScript interfaces.

    ---
    </details>



