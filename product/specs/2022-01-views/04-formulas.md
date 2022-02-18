---
title: 04. Formulas
description: A list of initial formulas supported in Views
published: true
date: 2022-02-18T21:07:17.916Z
tags: 
editor: markdown
dateCreated: 2022-02-04T03:33:53.715Z
---

> Under construction.
{.is-warning}

# List of Formulas

This is a list of view formulas that we should support in the alpha release of Mathesar. To create this list, I've used the [Inventory Use Case](/en/design/reports/inventory-use-case) as a guideline and limited the list to formulas that would be useful in that case.

We will be using the tables in the [Example Schema](/en/product/specs/example-schema) to illustrate different formulas.

## Column Formulas

These formulas will be used to create a new column in a query. See this wireframe for an idea of the user flow.

![view_builder_4.png](/view_builder_4.png)

### Count Related

- **Data Type**: Integer
- **Purpose**: To show a count of related items. We should support relations up to two FKs deep (so that we can handle mapping tables)
- **Variables**
    - Column to use for the relation (e.g. `movie.title` below)
    - Mappings to use for the relationship. This can either be one or two. e.g. 
        - `movie_id`, `movie_actor_map.movie_id`
        - `actor.id`, `movie_actor_map.actor_id`
- **Editable**: Columns of this type are not editable.
- **Example Query**
```sql
select movie.title as title, count(actor.name) as num_actors
from movie 
inner join movie_actor_map on movie.id = movie_actor_map.movie_id
inner join actor on movie_actor_map.actor_id = actor.id
group by movie.title;
```
| title | num_actors |
|-|-|
| Thelma & Louise | 2 |
| Meet Joe Black | 1 |
| Crouching Tiger, Hidden Dragon | 2|
| Crazy Rich Asians | 1 |

### List Related
- **Data Type**: List (list item data type depends on the data type of the column being summarized.
- **Purpose**: To show a list of related items. We should support relations up to two FKs deep (so that we can handle mapping tables)
- **Variables**
    - Column to use for the relation (e.g. `movie.title` below)
    - Mappings to use for the relationship. This can either be one or two. e.g. 
        - `movie_id`, `movie_actor_map.movie_id`
        - `actor.id`, `movie_actor_map.actor_id`
- **Editable**: This field is editable. Editing behavior is as follows:
    - Users can add existing records to the array as long as the tables in question have no other required fields other than the one the user is editing.
        - For example, the user can add `Geena Davis` to the `Meet Joe Black` movie. This will add a new record in `movie_actor_map` to map the existing actor record for Geena Davis to the movie record.
        - If the related record is only one FK away, this will instead populate the FK column.
    - Users can add new records through this mechanism if they don't already exist (with the same caveat about required fields)
        - For example, the user can add `Anthony Hopkins` to `Meet Joe Black` and this will insert new records in both `actor` and `movie_actor_map`
        - If the related record is only one FK away, this will only add a record in a single table.
    - We will autocomplete existing records when the user starts typing.
    
- **Example Query**
```sql
select movie.title as title, array_agg(actor.name) as actors
from movie 
inner join movie_actor_map on movie.id = movie_actor_map.movie_id
inner join actor on movie_actor_map.actor_id = actor.id
group by movie.title;
```
| title | actors |
|-|-|
| Thelma & Louise | Brad Pitt, Geena Davis |
| Meet Joe Black | Brad Pitt |
| Crouching Tiger, Hidden Dragon | Michelle Yeoh, Zhang Ziyi |
| Crazy Rich Asians | Michelle Yeoh |

## Aggregation Formulas

These formulas will be used to create aggregations in queries. See this wireframe for an idea of the user flow.

![view_builder_5.png](/view_builder_5.png)

*TBD*.