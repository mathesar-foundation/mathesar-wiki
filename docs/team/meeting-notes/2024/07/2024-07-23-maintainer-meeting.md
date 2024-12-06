# 2024-07-23 maintainer meeting

## Identifying role that owns Mathesar internal schemas during upgrade
Context:

* Mathesar needs to identify and use the role that owns the `msar`, `__msar`, and `mathesar_types` schemas during upgrade.
* The upgrade process needs to happen for each connected user database.
* We can identify & use the owning role(s) if they are configured in Mathesar.
* There is a chance that the owning roles are removed or we're unable to migrate the schemas in a database due to password change/expiry.

Questions to discuss:

* Our upgrade process is manual & only upgrades the app. The migrations happen during each restart. Should we change this behaviour?
* How about we include a separate upgrade/migrate admin option for each database in the UI?
	* We automatically perform it if we have the roles.
	* We prompt the user to intervene if we aren't able to.
* Can we think of a better way to handle this?
* How much of a priority is this for the beta?

### Discussion
- This is not worth discussing now.
- We will discuss how to handle upgrades as part of our beta planning discussions, this is already tracked in Basecamp.
- Let's focus on finishing permissions implementation first, since we have no bandwidth to implement anything else right now even if we talk about the plan.
- Pavish added a task for this on Basecamp in the beta release project, we'll pick it back up when we have capacity.

### API return value when creating a table without providing a name

**Sean:** 

I've hit a small snag and I'd like opinions on the best approach to dealing with it...

Mathesar 0.1.7 allows users to create a new table without specifying a table name. Mathesar generates one automatically. Personally, I don't actually like this feature. I'd rather Mathesar prompt me for a name because renaming it later requires extra steps. To support this feature, our `tables.add` API supports the ability to auto-generate a table name during creation. But the API only returns the table OID. The front end also needs to know the auto-generated name. Here are the ways I can think of to fix this:

- (A) Bodify the return value of `msar.add_mathesar_table` so that it returns something like `{ "oid": 12345, "name": "foo" }`. A downside here is that the return value would not be consistent with other return values. But this could be a good opportunity to discuss patterns around return values. Brent recent expressed a though/opinion that perhaps functions like this should return everything they can.

- (B) Delegate the automatic name generation to the front end. The API would require a name and would fail if the name already exists. The front end would use what it knows about the existing tables to suggest a good name. This has the benefit of simplifying some DB-layer code. We'd even be able to re-use some front end code that's already in place. A very minor downside is that it would open up a slight possibility of a naming conflict if two users happen to be creating tables close in time to one another.

- (C) Delegate naming to the _user_ by using a modal to prompt the user to enter a name while creating a table. We already do this for schemas, explorations, and columns, so there might be an argument for prompting with tables in order to be consistent. In terms of usability, prompting is the behavior that I personally find the be the smoothest.

I would say that implementation time is similar for the above approaches.

I have a very slight preference for (C), but that's a user-facing change, so perhaps it's not worth considering at the moment. I'm also okay with (A). And (B) is probably my least favorite.

### Discussion
- Sean and Brent prefer (C)
    - API changes would not be less work than UX changes.
- We all agree consistency makes sense, but Brent suggests that consistency the other way (creating shouldn't require names for _anything_)
    - Kriti concurs, since it's also fewer steps for the user.
    - For the best UX, users should be able to get to using Mathesar with their own data in the fewest steps possible.
    - Kriti prefers (A) or (B)
- Doesn't mean we need to make everything consistent right away, just get to consistency eventually.
- Pavish prefers (A)
    - Rest of the team agrees.

**Decision**: Let's go with (A)

- Sean: This is another data point to consider for consistent data values, although we don't have to make a decision now.
    - Pavish would like the entire object returned when creating and patching, but don't need anything returned for deleting.
    - This will involve more queries and joins on the backend, fine for table creation (a few ms), but maybe not for others.
    - Let's kick this can down the road.
