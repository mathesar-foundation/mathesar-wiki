# (a) Record Aggregation Formulas

These formulas aggregate the values of a single column across multiple records of the same type. These are used as aggregation types when a multi-record column is added to a query.

# Count
- **Data Type**: Integer
- **Description**: Show a count of all values in the column.
- **Variables Accepted**:
    - **Column**:
        - **Description**: The column to aggregate.
        - **Type** Multiple Record Column Reference
- **Data Editable?**: No

## Example Query
```sql
select movie.title as title, count(actor.name) as num_actors
from movie 
inner join movie_actor_map on movie.id = movie_actor_map.movie_id
inner join actor on movie_actor_map.actor_id = actor.id
group by movie.title;
```

# List
- **Data Type**: List (list item data type depends on the data type of the column being summarized.
- **Description**: Show a list of all values in the column.
- **Variables Accepted**:
    - **Column**:
        - **Description**: The column to aggregate.
        - **Type** Multiple Record Text-Like
- **Data Editable?**: Yes 

## Editing behavior
Data generated using list formulas are editable in two ways:
- **Editing existing items** The user can always edit the contents of an existing item.
    - We are just editing the relevant record in the underlying table.
    - We should make it clear to the user that all instances of the data will be changed, not just in this record.
- **Adding and removing items to a list**: The user can add or remove items from the list. This is only true in the following circumstances:
    - the tables being used to generate the list (including intermediate tables) have no other required fields other than the one the user is editing.
    - we have enough information in the filters being used to generate the list to fill in any required fields other than the one the user is editing in the tables being used to generate the list (including intermediate tables) 

To illustrate editing behavior, let's consider the **Movie Actor** view in [Appendix A](/product/specs/2022-01-views/08-appendix). 

- **Editing existing items**:
    - The user can edit `Brad Pitt` in row 1 to say `William Bradley Pitt` instead.
- **Adding rows**:
    - The user can add `Geena Davis` to the `Meet Joe Black` movie (she's not in that movie but that's beside the point). This will add a new record in **Movie Person Map** to map the existing actor record for Geena Davis to the existing movie record movie record with a `Role` of `Actor` (since we know that from the filter that defines the column).
        - We need to be using autocomplete to select records here (with a record preview) so that the user can select the correct record in case there are two `Geena Davis` records.
        - If there was no filter defined on the column, we would leave the `Role` value blank.
    - The user can add `Anthony Hopkins` to `Meet Joe Black` and this will insert new records in both `Person` and `Movie Person Map` (again with a `Role` of `Actor`).
    
Although the illustration above uses a mapping table, it also applies to other forms of relationships.
    
## Example Query
```sql
select movie.title as title, array_agg(actor.name) as actors
from movie 
inner join movie_actor_map on movie.id = movie_actor_map.movie_id
inner join actor on movie_actor_map.actor_id = actor.id
group by movie.title;
```

# Average
- **Data Type**: Same as the type of column accepted
- **Description**: Show an average of of all values in the column.
- **Variables Accepted**:
    - **Column**:
        - **Description**: The column to aggregate.
        - **Type** Multiple Record Number-Like
- **Data Editable?**: No

# Minimum
- **Data Type**: Same as the type of column accepted
- **Description**: Show the minimum value of all values in the column.
- **Variables Accepted**:
    - **Column**:
        - **Description**: The column to aggregate.
        - **Type** Multiple Record Number-Like
- **Data Editable?**: No

# Maximum
- **Data Type**: Same as the type of column accepted
- **Description**: Show the maximum value of all values in the column.
- **Variables Accepted**:
    - **Column**:
        - **Description**: The column to aggregate.
        - **Type** Multiple Record Number-Like
- **Data Editable?**: No

# Median
- **Data Type**: Same as the type of column accepted
- **Description**: Show the median value of all values in the column.
- **Variables Accepted**:
    - **Column**:
        - **Description**: The column to aggregate.
        - **Type** Multiple Record Number-Like
- **Data Editable?**: No

# Sum
- **Data Type**: Same as the type of column accepted
- **Description**: Show the sum of all values in the column.
- **Variables Accepted**:
    - **Column**:
        - **Description**: The column to aggregate.
        - **Type** Multiple Record Number-Like
- **Data Editable?**: No

# Product
- **Data Type**: Same as the type of column accepted
- **Description**: Show the product of all values in the column.
- **Variables Accepted**:
    - **Column**:
        - **Description**: The column to aggregate.
        - **Type** Multiple Record Number-Like
- **Data Editable?**: No
