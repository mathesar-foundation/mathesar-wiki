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

### `records.update`

This will be a new API that allows clients to update records based on a query.

Its parameters are as follows:

```ts
/** Same as the `exploration_def` param within `explorations.run` */
interface AnonymousExploration {
  database_id: number;
  schema_oid: number;
  base_table_oid: number;
  initial_columns: InitialColumn[];
  transformations?: QueryInstanceTransformation[];
  display_names?: Record<string, string> | null;
}

interface UpdateParams {
  /** This type will later become a discriminated union of other query types */
  query: {
    type: 'exploration';
    definition: AnonymousExploration;
  };

  /** All cell values in the row, as an array */
  row: unknown[];

  /** Keys are column indexes, values are new values */
  new_values: Record<string, unknown>;
}

interface UpdateReturn {
  updated: number;
}

export const records = {
  update: rpcMethodTypeContainer<UpdateParams, UpdateReturn>,
};
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

