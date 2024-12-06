# Automatic Hint Reflection

## Functions API

Mathesar has an API that describes how a client can assemble Postgres functions into expressions that can later be used, for example, to filter table rows with. We call it the *functions API*. A basic example of such an expression could be: "does the title of this movie start with the same letter as its director's first-name".

For the functions API to not require hardcoding on the client side, and for clients to be able to effortlessly adapt to newly added functions, it declares how those functions can be used. The API uses a system for assigning various types of information to individual functions and types. We're calling it the hint system.

We use it, for example, to describe the signature of the function `starts_with`: it takes two named arguments, one argument is called `base_string` and the other `prefix`, both arguments should be string-like, and the function returns a boolean:

```python
    starts_with_hints = [
        hints.parameter(name='base_string', hints.string_like),
        hints.parameter(name='prefix', hints.string_like),
        hints.returns(hints.boolean),
    ]
```

Here's some hints assigned to Postgres types:

```python
db_types_mapped_to_hints = {
    PostgresType.DECIMAL: [hints.comparable, hints.fractional],
    PostgresType.TIMESTAMP: [hints.comparable, hints.time_related, hints.time_of_day, hints.date],
    PostgresType.DATE: [hints.comparable, hints.time_related, hints.date],
    PostgresType.TIME: [hints.comparable, hints.time_related, hints.time_of_day],
}
```

Above mapping says that:
  - the `DECIMAL` type is comparable (meaning you might be able to ask whether it's larger or smaller than another comparable type), and that it's fractional (as in can represent fractional numbers);
  - the `TIMESTAMP`, `DATE` and `TIME` types are all comparable too, and they're all time-related;
  	- `TIMESTAMP` holds both time-of-day and date information,
    - while `DATE` only holds date information,
    - and `TIME` only holds time-of-day information.

Importantly, hints don't obligate the user of the API to follow them. A user should be able to assemble expressions that are in conflict with what is declared by the hints. The purpose of the hint system is to give hints to the user about how to assemble expressions, but the user should be free to assemble any expression he likes.

We chose for the hint system to be non-authoritative (allow users to ignore it) for two reasons:

- it empowers power-users that might want to use a function or a type in a way contrary to the declared hints;
- and, user developers (users that might also want to define their own Postgres functions or types) will not be obligated to master the hint system just to add a function: they'll be able to gradually start adding hints if/when they find that useful, which will cause the UX for using that function to become more streamlined with every hint added.

A bonus of a non-strict composition system is that you don't have to strive to create very precise signature declarations that cover all use cases, which helps keep the way we declare signatures simple for new-comers.

## The Problem

Currently, the hints are compiled by hand, as seen in the above code sample. That could become cumbersome if the number of functions or types explodes. Also, user developers might find the hint system's learning curve a barrier to declaring their own functions or types (though we're working to minimize that).

We've discussed the possibility to reflect function (and possibly type) properties automatically, which would allow us to also assign (at least some) hints automatically.

The automatic reflection is not essential, but it could be a significant quality-of-life improvement. Its implementation seems too expensive for the core team to take up in the near term. At the same time, it's fairly isolated from the rest of Mathesar, which is good for new contributors.

## Classification
- **Difficulty**: High
- **Skills needed**: PostgreSQL, SQL
- **Length**: *Long (~350 hours)*

## Tasks
- Research what is the intersection between the things that would be useful for Mathesar to automatically reflect and what *can* be automatically reflected;
- Create an accurate picture of what cases the automatic reflection will fully cover and in what cases information (hints) will have to be overridden or supplemented manually;
- Figure out when to reflect and how to cache the reflections so as to minimally burden the wider system with more state;
- Do the implementation.

I would expect the above tasks to be performed (at least somewhat) asynchronously.

## Expected Outcome
An automatic PostgreSQL function (and possibly type) property reflection mechanism tailored to automatically finding useful hints for the hint system.

These automatically generated hints will be exposed through the function and type APIs, alongside manually written hints (if necessary), so that frontends can procedurally generate expression builders and provide useful guidance with minimal prior knowledge.

## Application Tips
I'd say a good candidate would be one that is comfortable taking the time to explore Mathesar needs, as relates to the hint, function and type systems, as well as one that is comfortable investigating the various tid-bits of information that Postgres makes available for reflection. I see this as a very exploratory task that requires the willingness to get to know multiple interesting systems.

## Resources
- [This](https://github.com/mathesar-foundation/mathesar/issues/1038)  is the tracking issue.
- [This](https://github.com/mathesar-foundation/mathesar/pull/1022/) is the PR that will merge the hint system in.
- [This](https://github.com/mathesar-foundation/mathesar/blob/ea3f200e19e4e1138e952ac1976e9f074db6c1c3/db/functions/hints.py) is the current (rudimentary) state of the hint system.
- [This](https://github.com/mathesar-foundation/mathesar/blob/ea3f200e19e4e1138e952ac1976e9f074db6c1c3/db/functions/base.py) is the current (rudimentary) state of the functions system, that uses hints.

## Mentors
- **Primary Mentor**: Dominykas Mostauskis 
- **Backup Mentor**: Brent Moran

See our [Team Members](/team/members) page for Matrix and GitHub handles of mentors.
