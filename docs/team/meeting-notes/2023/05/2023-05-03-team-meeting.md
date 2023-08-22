# 2023-05-03 Team meeting

## Quick Save Functionality: Backend Concerns and Clarifications

- **Added by**: Ghislaine
- **Summary**: Address backend concerns and clarifications for the Quick Save functionality
- **Expected time**: 30 min
- **Priority**: 
- **Required participants:** Backend team (Brent, Mukesh, or Dom)
- **Additional participants:**: *Please replace this with your name if you're interested in participating*

While gathering requirements for the Quick Save functionality, several concerns were raised. We need to address these points to define the product and outline how the functionality should be implemented:

From the conversation with Brent:

1. What terms should we use to accurately describe the functionality and avoid confusion with existing database concepts? For example "Save Point" or "Backup"
3. Should restoration points be created for the whole database or individual tables?
4. How should we handle scenarios where multiple users have access to the same table, and a restoration is performed?
5. Should we create automatic restoration points, or only create them upon user request?

From Sean's previous email:

1. How can we handle the backup and restoration of both data and metadata stored in separate databases?
2. What measures can be taken to ensure atomicity while backing up and restoring data and metadata?
3. How can we handle the fact that oids/attnums do not remain stable through backup/restore operations, and how does this impact our ability to use pg_dump? 


### Notes

- Terminology
    - Ghislaine thinks "backup" is more appropriate terminology
    - 
- Scope
    - Hard to address this feature from a product perspective without knowing the technical limitations
    - Being able to "undo arbitrary edits on a given cell without undoing other edits" is not feasible within the year. We won't focus on any sort of undo.
    - Brent: backup/restore is kind of like "undo" -- just at a higher level
    - Sean: backup/restore is also useful for inspecting and troubleshooting
    - Mukesh: if we're making backups, we need to convey to the user that the process of making a backup can take some time. We don't want to encourage users to make backups super frequently
    - Brent: "big picture backups" should not be our problem. E.g. GCP gives us a system to make and restore filesystem-level backups
    - Brent: I don't think it's worthh it to do something like a button to run pg_dump
    - Brent: Maybe we should have a button which backs up one table
    - Mukesh: Maybe we could have a system for copying a table, allowing users to edit, and then save the whole table back to the database.
        - Brent/Sean: How would we merge conflicts? This would be problematict
    - Brent: Maybe we could use some sort of auditing system. It would require storing massive amounts of data.
    - Ghislaine: If you had all the time in the world to implement "undo", how would you do it? What would the first steps be?
        - Brent: it will involve something like that audit table under the hood
- Data vs metadata
- Sean has thoughts
    - I wish we were building a project that was centered at a low level around preserving the history of the data
    - Allowing users to access that history locally
    - Having local-first data
    - Dolt: MySQL compatible database
    - CR-SQLite: 
        - These have functionality for diffs, logs, merging changes, etc.
- Brent: It would great if we could find another project (e.g. Dolt) to collaborate with so that we can make it someone else's problem

## DB function argument naming

- **Added by**: Brent
- **Summary**: We need to make a decision about arg naming conventions in DB functions.
- **Expected time**: 15 minutes
- **Priority**: High
- **Required participants:**: Backend team, Kriti, Anish
- **Additional participants:**: *Please replace this with your name if you're interested in participating*

See [this post](https://groups.google.com/a/mathesar.org/g/mathesar-developers/c/jZufTUlAbto) for context.

### Example

Here's the current version of one of our DB functions:
```sql=
CREATE OR REPLACE FUNCTION
msar.rename_table(sch_name text, old_tab_name text, new_tab_name text) RETURNS text AS $$/*
Change a table's name, returning the command executed.

Args:
  sch_name: unquoted schema name where the table lives
  old_tab_name: unquoted, unqualified original table name
  new_tab_name: unquoted, unqualified new table name
*/
DECLARE fullname text;
BEGIN
  fullname := msar.get_fully_qualified_object_name(sch_name, old_tab_name);
  RETURN __msar.rename_table(fullname, quote_ident(new_tab_name));
END;
$$ LANGUAGE plpgsql RETURNS NULL ON NULL INPUT;
```
The result of `\df`
```
Schema |     Name     | Result data type |                 Argument data types                 | Type
--------+--------------+------------------+-----------------------------------------------------+------
 msar   | rename_table | text             | sch_name text, old_tab_name text, new_tab_name text | func
```
The result of `\df+`
```
 Schema |     Name     | Result data type |                 Argument data types                 | Type | Volatility | Parallel |  Owner   | Security | Access privileges | Language |                                        Source code                                         | Description
--------+--------------+------------------+-----------------------------------------------------+------+------------+----------+----------+----------+-------------------+----------+--------------------------------------------------------------------------------------------+-------------
 msar   | rename_table | text             | sch_name text, old_tab_name text, new_tab_name text | func | volatile   | unsafe   | mathesar | invoker  |                   | plpgsql  | /*                                                                                        +|
        |              |                  |                                                     |      |            |          |          |          |                   |          | Change a table's name, returning the command executed.                                    +|
        |              |                  |                                                     |      |            |          |          |          |                   |          |                                                                                           +|
        |              |                  |                                                     |      |            |          |          |          |                   |          | Args:                                                                                     +|
        |              |                  |                                                     |      |            |          |          |          |                   |          |   sch_name: unquoted schema name where the table lives                                    +|
        |              |                  |                                                     |      |            |          |          |          |                   |          |   old_tab_name: unquoted, unqualified original table name                                 +|
        |              |                  |                                                     |      |            |          |          |          |                   |          |   new_tab_name: unquoted, unqualified new table name                                      +|
        |              |                  |                                                     |      |            |          |          |          |                   |          | */                                                                                        +|
        |              |                  |                                                     |      |            |          |          |          |                   |          | DECLARE fullname text;                                                                    +|
        |              |                  |                                                     |      |            |          |          |          |                   |          | BEGIN                                                                                     +|
        |              |                  |                                                     |      |            |          |          |          |                   |          |   fullname := msar.get_fully_qualified_object_name(sch_name, old_tab_name);               +|
        |              |                  |                                                     |      |            |          |          |          |                   |          |   RETURN __msar.rename_table(fullname, quote_ident(new_tab_name));                        +|
        |              |                  |                                                     |      |            |          |          |          |                   |          | END;                                                                                      +|
        |              |                  |                                                     |      |            |          |          |          |                   |          |                                                                                            |
```

The problem with this version is that it 'locks in' the function parameter names. Any change of those names would have to be considered a change of a public API, and would very possibly require manual intervention on the part of users to upgrade (or at least to perform an upgrade that changed any function parameter names).

Now, modified as per option (3) from the linked post:
```sql=
CREATE OR REPLACE FUNCTION
msar.rename_table(text, text, text) RETURNS text AS $$/*
Change a table's name, returning the command executed.
*/
DECLARE
-- Args:
  sch_name TEXT := $1;  -- unquoted schema name where the table lives
  old_tab_name TEXT := $2;  -- unquoted, unqualified original table name
  new_tab_name TEXT := $3;  -- unquoted, unqualified new table name
-- internal variables
fullname text;
BEGIN
  fullname := msar.get_fully_qualified_object_name(sch_name, old_tab_name);
  RETURN __msar.rename_table(fullname, quote_ident(new_tab_name));
END;
$$ LANGUAGE plpgsql RETURNS NULL ON NULL INPUT;
```
The result of `\df`:
```
 Schema |     Name     | Result data type |      Argument data types      | Type
--------+--------------+------------------+-------------------------------+------
 msar   | rename_table | text             | text, text, text              | func
```

The result of `\df+`:
```
                                                                                                                            List of functions
 Schema |     Name     | Result data type |      Argument data types      | Type | Volatility | Parallel |  Owner   | Security | Access privileges | Language |                                        Source code                                         | Description
--------+--------------+------------------+-------------------------------+------+------------+----------+----------+----------+-------------------+----------+--------------------------------------------------------------------------------------------+-------------
 msar   | rename_table | text             | text, text, text              | func | volatile   | unsafe   | mathesar | invoker  |                   | plpgsql  | /*                                                                                        +|
        |              |                  |                               |      |            |          |          |          |                   |          | Change a table's name, returning the command executed.                                    +|
        |              |                  |                               |      |            |          |          |          |                   |          | */                                                                                        +|
        |              |                  |                               |      |            |          |          |          |                   |          | DECLARE                                                                                   +|
        |              |                  |                               |      |            |          |          |          |                   |          | -- Args:                                                                                  +|
        |              |                  |                               |      |            |          |          |          |                   |          |   sch_name TEXT := $1;  -- unquoted schema name where the table lives                     +|
        |              |                  |                               |      |            |          |          |          |                   |          |   old_tab_name TEXT := $2;  -- unquoted, unqualified original table name                  +|
        |              |                  |                               |      |            |          |          |          |                   |          |   new_tab_name TEXT := $3;  -- unquoted, unqualified new table name                       +|
        |              |                  |                               |      |            |          |          |          |                   |          | -- internal variables                                                                     +|
        |              |                  |                               |      |            |          |          |          |                   |          | fullname text;                                                                            +|
        |              |                  |                               |      |            |          |          |          |                   |          | BEGIN                                                                                     +|
        |              |                  |                               |      |            |          |          |          |                   |          |   fullname := msar.get_fully_qualified_object_name(sch_name, old_tab_name);               +|
        |              |                  |                               |      |            |          |          |          |                   |          |   RETURN __msar.rename_table(fullname, quote_ident(new_tab_name));                        +|
        |              |                  |                               |      |            |          |          |          |                   |          | END;                                                                                      +|
        |              |                  |                               |      |            |          |          |          |                   |          |                                                                                            |

```
This avoids the problem above. However, it has some major downsides
- It means the output of `\df` is much less informational
- It makes the function's signature harder to parse in code.
- It adds boilerplate (the `DECLARE` block; this is optional, but recommended)
- We can't name certain variables at all (any pseudotype, e.g., `anyarray`; these can _only_ be function parameters, but can't be declared)



### Notes

- We havn't yet released any code that causes a problems
- If you have named parameters in postgres functions, you cannot update them. You have to drop them and re-create them. Functions can have dependencies. You cannot easily drop functions with dependencies.
- Brent: Are we tracking dependencies of functions?
    - Mukesh: I don't think so
- We really want to avoid dropping functions
- Mukesh: The problem happens when you upgrade the types. I think we should consider better ways to do upgrades.
- Mukesh: can we drop the functions and re-build them during upgrades?
    - Brent: this can be problematic if, for example, the user has views that depend on the function
- Sean: We should consider the DB functions as a "public API". Sometimes this API has breaking changes. We'll never be able to avoid that. From a UX perspective, the named function parameters improve UX, so I'd be inclined to allow them. We should just minimize the breaking changes, and be clear in the release notes when we make them.
- **Decision** we'll keep the named parameters
- For the time being, we won't change the parameter names. If we want to change a parameter name, we'll discuss how to do that later. We could add a `--force` flag to the python layer install which drops the functions with CASCADE.
- The 0.1.2 release will have a bunch of new functions
- We'll have docs for developers to help them upgrade their functions from develop to develop

### Action items for Brent

- add documentation to Sean's dev docs PR for recovery when there's a function parameter naming issue
- Add documentation to the effect of 'changing function parameter names is a breaking change'
- Either automate checking for parameter name changes in CI for PRs, or document that this should be checked for backend PRs
- Double-check that we don't already have this problem (i.e., the current develop branch doesn't change any parameter names compared to 0.1.1).

