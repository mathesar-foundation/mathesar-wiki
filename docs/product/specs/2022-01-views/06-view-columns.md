# 06. View Columns

Here is the information we should show in View Columns. We don't necessarily have to use the abstractions below, there might be a better way to show the data necessary.

If we end up having a column menu in [the Query Builder](/product/specs/2022-01-views/03-the-query-builder), we can probably reuse it here.

## Data Type
This is the final data type of the content of the column after any computations etc. are applied.
- **Allowed values**: same as Table data types.
- **Required**. Data type should always be set, at the very least, we can treat unknown data types as text.

## Sources
This is the set of source columns that are used to generate the data in the current View column.
- **Allowed values**: References to other Table columns or columns in the same View.
    - We should also depict relationships used to get to the source and any filters applied to the source.
- **Optional**: This could be empty for purely calculated columns (e.g. using the Postgres `random()` function and putting the output in a column)

Using Element's UI as an example (Matrix channel names stand in for data sources here), here's how Sources might be represented:

![screen_shot_2022-01-20_at_4.21.05_pm.png](/assets/product/specs/2022-01-views/06-view-columns/screen_shot_2022-01-20_at_4.21.05_pm.png)

## Formula
This is the formula used to generate data in for this column.
- **Allowed values**: List of pre-defined formulas, see [04. Formulas](/product/specs/2022-01-views/04-formulas)
- **Optional**: Columns that are direct copies of other columns from tables or views won't have a formula.

We should allow users to use a pre-set set of formulas or (in the future) enter a custom formula using whatever functions are installed on their Postgres database.

Using Element's UI as an example (Matrix channel names stand in for data sources here), here's how a Formula might be represented. Note that Sources are used within the Formula.
![screen_shot_2022-01-20_at_4.23.21_pm.png](/assets/product/specs/2022-01-views/06-view-columns/screen_shot_2022-01-20_at_4.23.21_pm.png)

Details about creating formulas are in [04. Formulas](/product/specs/2022-01-views/04-formulas).

## Link
This notes whether a column is a join column. This is a column used to match the same values across multiple tables to create the View. These columns have multiple Sources but no Formula.
- **Allowed values**: True or False.
- **Required**: This must be set for all columns.

In [this example View](https://www.w3resource.com/sql/creating-views/create-view-with-join.php), the `agent_code` and `cust_code` columns are Links.
