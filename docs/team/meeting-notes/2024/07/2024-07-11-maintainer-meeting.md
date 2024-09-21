# 2024-07-11 maintainer meeting
 
 **Attendees**: Brent, Pavish (partial), Anish, Sean
 
## Current work check-in
 - Anyone have any blockers or priorities that need to change?
 - Pavish: I'm implementing a bunch of endpoints in the same PR, heads up to Brent that it's going to be large, but it should be simple to review, not a lot going on.
     - Brent: should probably be fine.
     - Pavish: can split up PR afterwards if it will be a pain to review.

## Upgrading SQL in our development environments

I've [Sean] found myself running this command quite regularly now:

```
docker exec -i mathesar_dev_db bash -c 'psql -U mathesar' < ./db/sql/00_msar.sql
```

I need to run this after pulling the latest changes from our repo. If I don't, then sometimes things are broken. As far as I can tell, I still need to run this even if I restart Docker. Right?

The need to perform this step is not documented anywhere. At the very least, this is a problem for new devs. (Not a big problem right now though.)

But the number of SQL files is growing. We already have a few, and [Process record summaries in DB layer](https://github.com/mathesar-foundation/mathesar/pull/3561) adds `40_record_summaries.sql`.

I think we need a more robust way to upgrade our development environments with the latest SQL. Some kind of script or something?

Comment from Pavish:
- This is a bug/regression. The expected behaviour is for the migrations to happen when the service re-starts which is not working currently. I had a small discussion with Brent on this a while back.
- Here's the issue I opened today for this: https://github.com/mathesar-foundation/mathesar/issues/3674

### Conclusion
- Probably broke during Brent's work.
- We do want the SQL to be upgraded when Docker restarts.
    - Need to switch to psycopg3 etc.
- Anish can work on this. 
    - Not a priority before beta.
    - Can do a 1 line fix to temporary fix it for now.
- Anish is fixing this right now.

## Brent PR review bottleneck

Our current process seems to be that all backend PRs get reviewed by Brent. Can Anish review some too? If so, what is our process for assigning a reviewer?

### Conclusion

- Default to assign Brent to review backend PRs for now. 
    - If Brent gets too overwhelmed with PR review, then he'll delegate to Anish as needed.
- Feel free to assign Anish directly if it's an area of the codebase that you know he has worked on previously. 


## "Not found" behavior in SQL functions

When our SQL functions are subjected to inputs that don't yield any results, some functions return NULL, whereas others raise exceptions. We've discussed this inconsistency a few times already, and thus far we've agreed to postpone any efforts at standardizing these patterns until after beta.

But I'd like to present a bug which I hope will make a compelling case for raising exceptions instead of returning NULL. I think it might be worth it _now_ to use exceptions going forward.

Pavish [encountered a bug](https://github.com/mathesar-foundation/mathesar/pull/3648#pullrequestreview-2163203218) in a PR of mine. The bug went like this:

1. The front end loaded the schemas.
2. Due to an [unrelated bug](https://github.com/mathesar-foundation/mathesar/pull/3666), the loaded schemas had stringified OID values. That bug meant that when attempting to modify a schema, the front end would send an API request that would call `msar.patch_schema` with a stringified OID. Due to function overloading, `msar.patch_schema(sch_name text, patch jsonb)` would get invoked.
3. Then the stringified OID would be passed through `sch_name` into `msar.get_schema_oid`.
4. Due to the pattern of returning NULL instead of raising exceptions, `msar.get_schema_oid` would return NULL and the whole operation would basically short circuit from there.

The really bad part about the above bug is that the API gave no indication of failure! That's bad for users; and it left me with a tricky situation to troubleshoot, costing me time. If that function had raised an exception, I would have caught this bug in my own pre-PR QA instead of during PR review.

I think that erring on the side of failing early is likely to be the safer option in most cases. To be clear: I don't mean _all_ cases. There are inevitably trade-offs here. But I think that raising exceptions has sufficient merit as a pattern to justify its adoption now instead of post-beta.

I did a very rough audit of some of our SQL info functions to see what their behavior is:

| Function                                    | "Not found" behavior |
| --                                          | --    |
| __msar.get_qualified_relation_name          | stringified OID |
| __msar.get_qualified_relation_name_or_null  | NULL  |
| msar.get_attnum                             | NULL  |
| msar.get_cast_function_name                 | Exception |
| msar.get_column_info                        | NULL  |
| msar.get_column_name                        | NULL  |
| msar.get_column_type                        | NULL  |
| msar.get_constraint_name                    | NULL  |
| msar.get_fresh_copy_name                    | Exception |
| msar.get_pk_column                          | NULL  |
| msar.get_relation_namespace_oid             | NULL  |
| msar.get_relation_oid                       | Exception |
| msar.get_schema_name                        | Exception |
| msar.get_schema_oid                         | NULL  |
| msar.get_table                              | NULL  |
| msar.get_table_info                         | NULL  |

I'm proposing that we agree on a standard of raising exceptions. I don't think this means we need to go change all the non-conformant code. But I'd like to document the standard and employ it going forward.

### Discussion

- Brent prefers functions that deal with missing data more gracefully and don't throw exceptions. 
- Sean is concerned that inconsistent exception handling could lead to confusing UI
    - e.g. looking like a table rename succeeded when it didn't.
- General agreement about coding standards being useful to have, but this doesn't seem worth it right now.
- Since there's no quick agreement, let's put this discussion in the parking lot and perhaps revisit post-beta.

------

*At this point, Sean, Brent, and Anish switched to working through an open PR together, that discussion is not recorded in these notes.*
