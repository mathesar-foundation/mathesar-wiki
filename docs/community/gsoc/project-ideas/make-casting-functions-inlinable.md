# Make casting functions inlinable

## Classification
- **Difficulty**: Medium
- **Skills needed**: Python, PostgreSQL, SQLAlchemy
- **Length**: Long (~350 hours)

## The Problem

When importing a table from a CSV file, we attempt to give reasonable types to the columns of the resulting column, and we do that by repeatedly attempting to cast its columns to various types and seeing which of those attempts succeed. We call this type-inference. We would like to improve the performance of our type inference. This project is about doing that by making our casting SQL functions [0] inlinable [1] so that they can be exposed to Postgres' query planner, which can apply various optimizations. We expect the most significant result to be an increase in how row-parallel casting is.

## Tasks

- Find a way to tell when a casting SQL function is inlinable;
- Design a testing suite for whether or not our casting SQL functions are inlinable;
- Outline a strategy to make our casting SQL functions inlinable;
- Implement that strategy, making all of our type casting SQL functions inlinable.

## Expected Outcome

- All our type casting SQL functions are inlinable;
- We are able to test that that doesn't change.

## Application Tips

- Demonstrate proficiency with the required skills;
- Demonstrate interest in learning new and esotheric things; Postgres inlining is poorly documented and will require the willigness to dig for information and to experiment;
- Present some preliminary research into how our SQL type casting functions are defined and how they could be made inlinable;
- Describe your plan or preliminary research for each of the Tasks with clarity.

## Resources
- [0] [https://github.com/centerofci/mathesar/blob/master/db/types/operations/cast.py](https://github.com/centerofci/mathesar/blob/master/db/types/operations/cast.py) 
- [1] [https://wiki.postgresql.org/wiki/Inlining_of_SQL_functions](https://wiki.postgresql.org/wiki/Inlining_of_SQL_functions)

## Mentors
**Primary Mentor**: Dominykas
**Secondary Mentor(s)**: Brent
