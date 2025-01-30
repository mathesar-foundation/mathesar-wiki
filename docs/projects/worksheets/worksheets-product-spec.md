# Worksheets Product Spec

A "worksheet" would be a new user-facing abstraction which would combine the best of the table page and data explorer into a single, powerful tool. It would also lay a strong foundation for building more features in the near future.

This document serves as the highest-level specs document for an initial "MVP" implementation of worksheets.

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
    <summary><b>❌Basic Query</b></summary>

    ---

    The Basic Query would be the "easy to use" query option — and the default query type for a new worksheet.
    
    Like the data explorer:

    - You would choose a **base table** and set of **result columns**.
    - You could choose result columns from the base table or any tables related through forward or reverse FK relationships.

    Unlike the data explorer:

    - There would be no limit on the number of FK relationships used to traverse related tables when selecting result columns.
    - Aggregation would be mandatorily applied to any columns selected through reverse FK relationships. For example if your base table is Authors, you could add `"Books".id`, but you'd need to choose an aggregation function like `count` or `array_agg`. Or if your base is Books, then you'd be able to add the related author's `"First Name"` column in a straightforward manner, without any option to add aggregation.
    - You would be able to rearrange the result columns after adding them. Note that this is in the _query_, not the display. Imagine a UI similar to our current record summary template builder — it allows your to drag to re-order the columns you've chosen.
    - There would be an easy mechanism to _add all columns within the base table_. This would not be the same as `SELECT *`. Instead, all columns would be added sequentially into the query definition using the order in which they occur in PostgreSQL. This way, the user would be free to remove and rearrange columns at will.

    Like the table page:
    
    - It would allow you to perform simple filtering and sorting (on any result column) via a GUI.

    Unlike the table page:

    - There would be no "Group" option. See "Outline view" below for the new feature that would replace that functionality.

    Additionally:

    - You would be able to convert a Basic Query into an SQL Query.

    TODO:

    - aliases (important for related data)
    - mandatory pks

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

    Control over pagination would be delegated to the _display_ — not the _query_. This means that in order to send a query to PostgreSQL, the worksheet system would need to combine the query's definition with the pagination set in the display — and it would need to be able to do it for all query types (including SQL). It also means that all display types would need to implement their own pagination UI.

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
    <summary><b>Query editing via display</b></summary>

    ---

    The worksheet container would have a mechanism to allow some small query mutations to be performed _via the display_. Only certain query types and certain display types would support query editing via display. For the worksheets MVP, it would be the Basic Query and the Sheet Display.

    Here are the cases we need to handle for the MVP:

    - Re-ordering query columns via drag-and-drop on column headers in display.
    - Remove query column via context menu in display
    - Add/remove filter/sort conditions via context menu in display

    And during implementation we should consider the following future possibilities while making architectural decisions:

    - a calendar display which sets filters in order to return only the records relevant within the current time window
    - a map display which sets similar filters
    ---
    </details>

- <details>
    <summary><b>Ephemeral worksheets</b></summary>

    ---

    Similar to explorations, the user should be able to build a worksheet and use all of its features _without_ saving it.

    ---
    </details>

- <details>
    <summary><b>Savable worksheets</b></summary>

    ---

    Similar to explorations, the user should be able to save a worksheet. 
    
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
    <summary><b>Default worksheets</b></summary>

    ---

    The Worksheets MVP project would replace the current Table Page with a worksheet interface.
    
    Here is how it would work:

    - The Schema Page would still show a list of tables (as it currently does).
    - Clicking on a table within the list would open the "Default Worksheet" for that table.
    - The Default worksheet would either be:
        - An _auto-generated_ default worksheet, or
        - A _customized_ default worksheet
    - An auto-generated default worksheets would have:
        - A **Basic Query** with:
            - All columns in the table, in the order from PostgreSQL.
            - No filter conditions
            - One sort condition applied on the primary key if possible
        - A **Sheet Display** with default configuration
    - The user would be able to freely modify the auto-generated worksheet, with their changes triggering the "unsaved changes" visual indicator.
    - With any unsaved changes, the user would be able to save the auto-generated worksheet as a new named worksheet.
    - With _certain types of unsaved changes_, the user would also be able to save their changes by _updating the default worksheet_. Mathesar would only allow this action when:
        - The query is not missing any columns from the base table, and
        - The query doesn't have any extra columns not present in the base table, and
        - THe query doesn't have filter conditions
    - Customized default worksheets would serve as a metadata container, allowing the worksheet system to entirely replace our current column metadata and replace some of our current table metadata.

    This means there would be four kinds of worksheets:

    - Ephemeral worksheets (built from scratch and not saved)
    - Named worksheets (saved with a name)
    - Auto-generated default worksheets (representing a table, unsaved)
    - Customized default worksheets (saved, but associated with a table instead of a name)

    When a new column is added to a table:

    - Ephemeral worksheets and named worksheets would be unaffected. Users would need to manually add the new column to see its data.
        - In some cases, users might not expect this behavior. For example if they begin with a default worksheet, resize a column, then save a new named worksheet, the named worksheet won't get new columns added to it. Thus, we would employ the following mitigation strategies to help give users the correct expectations. When saving a default worksheet as a named worksheet, the UI would make this "new-column" behavior clear to users. When adding a new column to a table, the UI would also mention this behavior.
    - Auto-generated default worksheets would automatically see the new column when generated.
    - Customized default worksheets are trickier... Since the default worksheet serves as a representation of the table, the new column _must_ display automatically. But a customized worksheet already holds state which lists columns. To solve this source-of-truth problem,  Mathesar would reconcile the worksheet's columns with the PostgreSQL columns before loading a customized default worksheet. If the worksheet is missing a column, then the new column would be added and the customized default worksheet would be updated before it is loaded. The user would see the new column, and all changes would be saved already.

    ---
    </details>

- <details>
    <summary><b>❌Partial resilience against deleted objects</b></summary>

    ---

    TODO

    Rationale:

    ---
    </details>

- <details>
    <summary><b>❌Resilience against renamed objects</b></summary>

    ---

    TODO

    Rationale:

    ---
    </details>

- <details>
    <summary><b>❌Outline view</b></summary>

    ---

    TODO

    Rationale:

    ---
    </details>

- <details>
    <summary><b>❌Query safeguards</b></summary>

    ---

    TODO

    Rationale:

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
    <summary><b>❌UNDO/REDO in data explorer</b></summary>

    ---

    TODO

    ---
    </details>

- <details>
    <summary><b>Change the way we think of the "Group" feature on table page</b></summary>

    ---

    The "Group" feature currently available on the table page would be replaced by the "Outline View" (described in the Goals section above). This would likely be a net-win but could potentially result in some minor regressions in functionality depending on the final implementation.

    ---
    </details>


## Possible future goals

These hypothetical goals demonstrate exciting features that we could build _on top of_ worksheets later. Although we would _not_ build these features initially, they're listed below in order to delineate scope, encourage resilient architectural decisions, and further substantiate the worksheets proposal as a whole.

- <details>
    <summary><b>❌Improvements for many-to-many data</b></summary>

    ---

    TODO

    - Allow users to display multiple record summaries in a single cell when the cell is an `array_agg` of primary key cells.

    Rationale:

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

- <details>
    <summary><b>❌Reactivity</b></summary>

    ---

    TODO

    Rationale:

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

    Must specify how these data structures reference database objects. Do they use OIDs, names, or some combination thereof. In the display, how would the column display options (e.g. customized width) be associated with columns? Names? Indexes? Both?

    ---
    </details>

- <details>
    <summary><b>❌Query introspection spec</b></summary>

    ---

    In order to satisfy the DML and DDL goals, 
    

    ---
    </details>

- <details>
    <summary><b>❌Pagination algorithm spec</b></summary>

    ---

    In order to 
    

    ---
    </details>

- <details>
    <summary><b>API spec</b></summary>

    ---

    This spec must describe all RPC methods, parameters, and return values required for implementation.

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



