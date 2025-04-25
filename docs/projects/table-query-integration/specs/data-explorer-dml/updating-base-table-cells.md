# Updating Base Table Cells

## UX

The UX for updating base table cells should mirror the current table page UX as closely as possible.

If a user creates an exploration which shows all the columns in a base table, the experience of updating cells should ideally be indistinguishable from the corresponding table page. And this should hold true regardless of data type or constraints.

For the purpose of this spec, only the columns in the base table will allow DML. Any columns outside the base table will not allow DML for now. (DML on related data is handled in subsequent specs.)

## Record identification

Let's start with an example in our movie_rentals data set...

Say I build an exploration of movies, adding **only the movie title** — just one column! Should I be able to update cells in that column? The answer is: _it depends_! Let's walk through some more detailed scenarios within this example:

- If I choose the movie "12 Rounds" and change its title to "Twelve Rounds", Mathesar will run SQL like this:

    ```sql
    UPDATE movies SET title = 'Twelve Rounds' WHERE title = '12 Rounds';
    ```

    That will work because our data set happens to have only one movie titled "12 Rounds". Mathesar will check to make sure only one record is updated before committing the transaction.

- But our data set has _multiple_ movies titled "12 Angry Men". What happens if I find one of those cells and try changing it to "Twelve Angry Men"? Again Mathesar will run the same sort of SQL, but this it will roll back the transaction because multiple records would have been updated. Mathesar will show an error like this to the user:

    > Unable to uniquely identify a record to update.
    >
    > Consider adding the `movies` ⏵ `id` column to your query in order to uniquely identify `movies` records.

- Basically: Mathesar will use all the available (relevant) columns it has from the result set when making updates. And if more than one row is found, Mathesar will roll back, showing an error.

- In the future, there are many potential improvements we could make to this record identification process. For example:

    - We could provide more information in the error, showing _which_ records were found.
    - We could provide a means to update some or all of the found records in the case where multiple were found.
    - We could provide a button to automatically add the PK column.
    - We could provide a means to utilize "hidden" columns for the record identification process.
    - We could automatically add such hidden columns in some cases.

    But for now, we will be building the _minimum viable_ record identification process. We can improve it incrementally after giving some attention to other DML issues first.

## APIs

### `records.update_where`

This will be a new API that allows clients to update records based on a set of conditions.

#### Parameters

```json5
{
  "database_id": 1,
  "table_oid": 12876,
  "set": {
    "2": "foo", // 👈 Maps column attnums to their new values
    "3": 123
  },
  "where": { // 👈 Takes the same form as filter params in records.list
    "type": "and",
    "args": [
      {
        "type": "equal",
        "args": [
          {
            "type": "attnum",
            "value": 1
          },
          {
            "type": "literal",
            "value": 1
          }
        ]
      },
      {
        "type": "equal",
        "args": [
          {
            "type": "attnum",
            "value": 2
          },
          {
            "type": "literal",
            "value": "bar"
          }
        ]
      },
      {
        "type": "equal",
        "args": [
          {
            "type": "attnum",
            "value": 2
          },
          {
            "type": "literal",
            "value": 0
          }
        ]
      }
    ]
  }
}
```

#### Behavior and return value

In the DB layer, Mathesar starts a transaction and tries to perform the update — checking to see _how many records were updated_.

- If a PostgreSQL error is encountered, the transaction is aborted, and the API returns an **error** response with the content of the PostgreSQL error.

- If **zero** records were updated (i.e. no records matched), then the API returns a **success** response with the following value:

    ```json
    {
      "updated": 0
    }
    ```

- If **one** record was updated, then the API returns a success response with the following value:

    ```json
    {
      "updated": 1
    }
    ```

- If **multiple records** were updated, then Mathesar **rolls back the transaction**! It returns an **error** response which looks just like the response from `records.list` with the filtering conditions applied, a `limit` of 100, and an `offset` of 0.

### `explorations.run`

We need some changes to this API's return value in order to give the front end the information it needs to call `records.update_where`.

Within `column_metadata` we need the following new properties added to each column metadata blob:

- `input_column_attnum`
    - We already have the column name. But we'll need the attnum too.

- `join_path`
    - This one takes a little explaining. Buckle up...

    - Although we're in the "Updating _base table_ cells" spec, we'd like this property to be general-purpose enough to help us with future DML work too. So it needs to be set up in a robust manner that handles columns in related tables.

    - Consider this example:

        ```sql
        DROP TABLE IF EXISTS categories;
        CREATE TABLE categories (
          id int primary key generated by default as identity,
          name TEXT,
          parent INT REFERENCES categories(id)
        );
        INSERT INTO categories (id, parent, name) VALUES
        ( 1,  NULL, 'Tools'),
        ( 2,  1   , 'Power tools'),
        ( 3,  1   , 'Hand tools'),
        ( 4,  2   , 'Drills'),
        ( 5,  3   , 'Screwdrivers'),
        ( 6,  3   , 'Wrenches');
        SELECT setval('categories_id_seq', (SELECT max(id) FROM categories));
        ```

        ```sql
        select
          base.id as id,
          base.name, as name
          parent.name as parent_name
        from categories base
        left join categories parent on parent.id = base.parent
        ```

        Here we have the `categories.name` column in the query twice, but not with the same values! The result column aliased as "name" is from the base table whereas the result column aliased as "parent_name" is not from the base table. We need a mechanism to distinguish between these sorts of columns. And we need a mechanism to tie "id" and "name" together while putting "parent_name" into a different bucket, so-to-speak. That's where `join_path` comes in.

    - The `join_path` property should serve to group result columns together which originated from the same relational source. Not necessarily the same ultimate _table_ — but the same path through the query plan to _get_ to that table.

    - As far as the front end is concerned, `join_path` could be structured as a string, array, object, or even a number. The front end just needs a way to _compare_ the `join_path` values for different columns in the result set. It needs to be able to answer the question: _"when I want to update a cell, what other result columns share the same join path with that cell?"_

We need something else too, but it will depend on how we choose to set up the `join_path` property... The front end needs a mechanism to determine which columns are from the base table.

- If we choose some sort of hash or counter for `join_path`, then we'll likely want a new property alongside `column_metadata` which specifies the `join_path` value of the base table, such as `base_table_join_path`.
- If we choose a string or array with a known, deterministic structure, then the front end could potentially look for the columns that have `join_path` value matching the statically-known join path of the base table.
- Alternatively, we could add something like a `in_base_table` property to every column's metadata. But the `join_path` already gives us something very similar, so it would be good to leverage that if possible.

