# DDL Operations

Data Definition Language (DDL) operations are those involving creating, altering, or dropping (deleting) database objects like:
- Tables
- Views

The main interest we'll have in these operations in this context is to allow the user to refine or modify their data model, and have that model reflected in the underlying DB model. We'll mostly focus on table creation and manipulation, since that's the main expected operation of this type.

## Goals
- User should be able to create tables
- User should be able to define tables in terms of already existing tables (e.g., joins, or by splitting columns out of a table)
- User should be able to recover previous models. 
	- For DDL ops, it's not clear this should be an "undo" flow. The user might start with one big table, normalize their DB schema to reduce repetition for some manual input, then want to see everything back on one big table again. It's more of having different models with the same underlying data.

## DDL function signatures
- Since DDL operations do not consistently support transactions, we should prioritize safety and correctness for these functions.
- In Python, these functions should take non-immutable types (e.g., strings) as input, and return non-immutable types as outputs.
- Ideally, these immutable types should be strings.
  - This will enhance safety of these functions, and guarantee that they check the DB themselves for its state before commencing any changes.
  - This will also enable better composability of these functions (it's easy to chain functions together that have the same output type (or tuples of it) as input type)

