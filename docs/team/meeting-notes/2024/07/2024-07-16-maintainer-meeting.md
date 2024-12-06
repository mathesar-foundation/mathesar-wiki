# 2024-07-16 maintainer meeting
 
 **Attendees**: Brent, Pavish, Anish, Sean.
 
## Breaking changes to develop branch

This was an impromptu agenda item. Notes below:

- Using separate branches for our work has been slightly inconvenient. Sometimes we need to base work off open PRs which target two separate branches. This gets tricky. Also our GH actions currently don't auto-close issues unless the PR is merged into `develop`.

- We decided to rename `rpc_frontend` to `beta` for now. This will allow us to target that branch with other PRs that break things (e.g. Anish wants to make a back-end PR that breaks the Explorations model).

- Do we need the `beta` branch at all though?

- We could use `develop` instead for all our work instead. But we'd need to send an email to the developers mailing list (or perhaps some other list?) notifying Mathesar users that they would no longer be able to run production installations off the `develop` branch.

- We agreed that it's important for us to be able to run a stable version of Mathesar. And we also agreed that we could use `master` for that purpuos (instead of `develop`).

- We'd like to get Kriti's opinion on potentially merging `beta` into `develop`.

## Filter formatting for record retrieval

The current format of the filtering param for records is a bit clumsy and has features we don't need. An example is:
```
filter={
  "and": [
    {
      "lesser": [
        {
          "column_id": [
            7
          ]
        },
        {
          "literal": [
            "500"
          ]
        }
      ]
    },
    {
      "greater": [
        {
          "column_id": [
            5
          ]
        },
        {
          "literal": [
            "2000"
          ]
        }
      ]
    }
  ]
}
```
I'm [Brent] going to start working on filtering in the database for record retrieval, and I think it would be simpler (and easier for implementation) to simplify that to something like:
```
filter=[
  {
    "method": "lesser",
    "column_attnum": 7,
    "value": 500
  },
  {
    "method": "greater",
    "column_attnum": 5,
    "value": 2000
  }
]
```

### Questions to discuss
* Does this form have enough power?
    * Do we have filters that need multiple columns as input?
        * No
    * Do we have filters that need multiple values as input?
        * No
    * Do we ever combine filters with any logic other than `and`?
        * Yes, we use `or`.
    * Do we have preproc on any filter functions?
        * No
* Is this worth doing for beta?
    * For the back end, YES. It will save time. But, I'd like to hear the front end perspective on it.

### Pavish's comments:
> Do we have filters that need multiple columns as input?
>
> Do we have filters that need multiple values as input?

Not at the moment.

> Do we ever combine filters with any logic other than `and`?

Yes. We have `and` and `or` at the highest level. We do not have nesting yet.

### Conclusion
*Not recorded*.
