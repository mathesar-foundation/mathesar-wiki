# Engineering Decisions

!!! danger "Danger"
    This page is archived.


## June 2021
- We decided to use limit/offset pagination instead of cursor pagination.
	- **Discussion**: [Pagination options](https://github.com/mathesar-foundation/mathesar/discussions/177)
- We finalized on using TypeScript on the client.
	- **Discussion**: [Using Typescript on Client](https://github.com/mathesar-foundation/mathesar/discussions/145)

## May 2021
- We finalized what we expect the Mathesar "Money" type to look like.
	- **Discussion**: [Money type](https://github.com/mathesar-foundation/mathesar/discussions/118)
- We're going to store timezones with local timezone information, not as UTC.
  - **Discussion**: [Timezones](https://github.com/mathesar-foundation/mathesar/discussions/119)
- We're using `NUMERIC` Postgres types to power our general "Number" type on the roadmap.
	- **Discussion**: ["Number" types ](https://github.com/mathesar-foundation/mathesar/discussions/116)
- We finalized implementation details for table creation from file imports.
  - **Discussion**: [CSV importing / type inference](https://github.com/mathesar-foundation/mathesar/discussions/104)

## April 2021

- Mathesar _should_ function as a GUI to existing DBs, although it does a lot more. There should only be one source of truth for database-related data.
  - **Discussion:** [Mathesar: DB Client, or more integrated?](https://github.com/mathesar-foundation/mathesar/discussions/68)
- We're using Svelte for the frontend.
  - **Discussion:** ["Deciding the frontend framework" on GitHub Discussions](https://github.com/mathesar-foundation/mathesar/discussions/55)
- The frontend and backend code will live in the same repository.
  - **Discussion:** ["Repository structure to accommodate frontend code" on GitHub Discussions](https://github.com/mathesar-foundation/mathesar/discussions/53)
- We're storing web application related tables in a separate database.
  - **Discussion:** ["Separate DB for webapp tables and user tables" on GitHub Discussions](https://github.com/mathesar-foundation/mathesar/discussions/23)
  - **Additional Reasoning:** We want to be able to reflect an entire database in Mathesar without having to modify it.

## March 2021
- We're using SQLAlchemy to interact with user-defined database objects rather than Django models.
  - **Reasoning:** We don't want to define user-defined database objects in code, we want the database to be the single source of truth and reflect what's there.
- We're using Django and Django REST Framework for the web application backend.
  - **Reasoning:** We know it well and can build with it quickly.
- We're using Python for the backend.
  - **Reasoning:** We know it well and can build with it quickly.