# Schemas

## About

A **schema** is a workspace within a [Database](/product/concepts/databases) that contains [Tables](/product/concepts/tables), [Views](/product/concepts/views), and other database objects. 

### Schemas in Mathesar
You can organize your data into schemas in Mathesar and switch between schemas. In the Mathesar UI, you can only open one schema at a time.

Every database starts off with a schema called `public`.

## Usage
- If you have different sets of unrelated data, we recommend using one schema for each set of data. For example, you can use separate schemas for (a) tracking your movie collection, and (b) budgeting.
- If you're familiar with [Airtable](https://airtable.com/), think of schemas as a "Base". 

## Resources
- To learn more about how schemas work at the database level, visit the [PostgreSQL documentation](https://www.postgresql.org/docs/current/ddl-schemas.html).