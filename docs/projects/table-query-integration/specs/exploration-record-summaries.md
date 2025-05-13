# Exploration Display Improvements

## Front end changes

### Allow custom record summary templates

The "Column" tab of the exploration inspector should have a "Linked Record Summary" section just like the table page. The record summary template should get stored as a column display option.

### Display record summaries

- FK cells should display like they do in (read-only) FK columns in the table page.

- Record summaries should _also_ display for **arrays of primary key values**.

    For example, a query like this is easy to produce with the data explorer:

    ```sql
    WITH e AS (
      SELECT
        customer,
        array_agg(id) AS ids
      FROM emails
      GROUP BY customer
    )
    SELECT
      customers.id AS customer_id,
      customers.full_name AS customer_name,
      e.ids AS emails
    FROM customers
    LEFT JOIN e ON e.customer = customers.id;
    ```

    It shows one row per customer. And it has a column which shows an array of all the associated emails for the given customer.

    In the "emails" column, we'd like to show multiple record summaries for emails records.

    This means that PK array_agg cells will also need configurable record summary templates.


## Backend changes

### `explorations.run`

#### Parameters

- It should accept record summary templates as parameters.

    Example...

    Say our query looks like this:

    ```sql
    SELECT
      barcode,
      movie
    FROM items
    ```

    Since `items.movie` is a FK column, we want to show record summaries there.

    The `explorations.run` API would accept a `linked_record_summary_templates` parameter like this:

    ```json5
    {
      // ...
      "linked_record_summary_templates": [
        {
          "result_column_index": 1, // 👈 specifies the `movie` result column
          "target": {
            "table_oid": 12345,    // 👈 oid of `movies` table
            "key_column_attnum": 1 // 👈 attnum of `movies.id`
          },
          "template": [ 2 ], // 👈 specifies that only `movies.title` is used
          "is_array": false // 👈 indicates the query result column to be scalar
        }
      ]
    }
    ```

#### Return value

- The return value should contain a new `linked_record_summaries` property.

    - This should function similar to `records.list`, but the keys should be column _names_ (not column attnums). The column names should correspond to the names in the exploration result set.

- Within `column_metadata` we need the following new properties added to each column metadata blob:

    - `foreign_key`
        - When the underlying table column has a single-column foreign key constraint, the value here should look like:

            ```json
            {
              "referent_column": {
                "attnum": 1,
                "name": "id",
                "table": {
                  "oid": 18762,
                  "name": "customers"
                }
              }
            }
            ```

        - This is to support the configuration of record summary templates on FK columns.

    - `pk_array`
        - When the column is an aggregation of primary key values, the value here should look like:

            ```json
            {
              "table": {
                "oid": 8715,
                "name": "emails"
              }
            }
            ```

        - This is to support the configuration of record summary templates on PK array columns.

