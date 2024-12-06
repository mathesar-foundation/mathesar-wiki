# 2024-05-30 maintainer meeting

**Attendees**: Sean, Brent, Anish, Pavish, Ghislaine

## Permissions design review

*Continued from 2024-05-29 meeting.*

- We looked at the newest design, which showed how database roles and login configurations would be handled at the database server level.
- We agreed that DB server roles can be handled without storing nicknames as comments in PostgreSQL, nicknames can be stored in the Django DB.
    - Are nicknames even necessary?
    - No, it's simpler to remove them for now, we can always add them later.
 - How do role assignments work in context of the data model?
     - Roles are mapped per database rather than per server
     - A user can have different roles for different databases on the same server.
     - This seems like it might confuse users.
     - Trade offs:
         - Assigning different roles to the same user in different databases offers more **flexibility**.
         - Having one role per user across all databases on a server offers **simplicity**.
    - Flexibility / offering more control to users managing multiple DBs seems better – let's stick with current approach.
- We reviewed more UX changes around role assignment and login flow.
    - Hard to fully grok UX during meeting.
    - May need to address product questions about how roles are encapsulated before we dive into UX critique.
-  Should users should be allowed to change the database server associated with a configured database?
    - Use case: migrating databases to new servers
    - Adds too much complexity, we don't want this for beta
    - Same applies to changes in hostname and port for database servers, we won't allow editing them for now
- How do we handle DB role information when deleting databases?
    - Users might assume that when they delete a database, all associated data — including user roles, access control information, and passwords — will be deleted automatically.
    - We should ensure that when the user deletes the last database on a server, the system fully clears associated data.
    - We can use full cascade deletion.
        - We could use triggers or foreign key constraints to implement this.
        - Triggers are less visible and harder to maintain, FKs are the more natural way to handle this, can use multi-column FKs, won't obscure the logic.
        - Let's use FKs
            - Also better support within Django
    - We should implement this for the beta.

## CASCADE, IF EXISTS, IF NOT EXISTS

I [Sean] think our codebase has some accidental complexity in how the DB layer and service layer are handling things like `cascade`, `if_exists`, and `if_not_exists`.

For example...

- When creating a schema, we have an `if_not_exists` parameter implemented at the lower levels of code but not implemented at the higher levels of code.
- From the UI, if I attempt to create a schema with a name that already exists, the UI shows the dreaded XHR error 500. From the user's perspective, I think this behavior is mostly fine. The error message should be improved, but the fact that it shows an error is perfectly acceptable.
- To me, this indicates that nobody has ever bumped into this from a user's perspective. And it shows that the lower level complexity is unnecessary for our current product. I don't want to spend time carrying over that complexity through this refactor.

If we can reduce complexity like that while we're wrangling all this code to fit the new RPC patterns, I think it would be a boon for our codebase and also reduce implementation time.

If we can identify some common approaches to these types of SQL options, then I think we can reduce complexity by hard-coding the common approach at the lowest level (i.e. in the final SQL that gets run) and avoiding the need to pass parameters further up the stack.

My proposal:

- We _keep_ parameters for `CASCADE`. I think they may end up being useful in the short term. We also have some inconsistent behavior from a user's perspective here. For example, schemas are dropped with CASCADE whereas rows are not. I think that preserving a cascade parameter would allow us to iron out these inconsistencies by eventually adding UI for it. I'd actually like to expose a cascade parameter at the API layer right now.

- When creating DB objects, we _don't_ use `IF NOT EXISTS`. We just expect that an error will be thrown if we try to create something that already exists. If these errors become problematic for users, then we think about the best way to solve that problem at that point. This change will allow us to stop passing around `if_not_exists` parameters.

- Similarly, when deleting DB objects, we _don't_ use `IF EXISTS`. We just expect that an error will be thrown if we try to delete something that doesn't exist.

### Discussion
Everyone was in agreement that implementing these is additional complexity we don't need right now.

## Exploration association strategy

Since I [Sean] was absent from the last meeting, I'd like to circle back to this topic and make a stronger case for option `A`.

### Discussion
- Explorations are associated with schemas right now, and names need to be unique per schema.
- Do we want to redo this, given that we're not sure about the future of explorations?
- Probably not worth redoing right now. 
- Let's stick with current strategy.
