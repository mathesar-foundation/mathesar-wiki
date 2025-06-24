# Databases

## About

A **database** is an organized collection of data, managed by software called a database management system. Please see ["What is a Database?" on Oracle's website](https://www.oracle.com/database/what-is-database/) if you'd like to know more about the general concept.

### Databases in Mathesar
Mathesar provides a friendly user interface for databases managed by the [PostgreSQL](https://www.postgresql.org/) database management software. This means that you can connect one or more PostgreSQL databases to Mathesar and use Mathesar to interact with your data.

Within a database, you can store different kinds of data in different [Schemas](/archive/product/concepts/schemas). Data is stored in [Tables](/archive/product/concepts/tables) and can also be manipulated through [Views](/archive/product/concepts/views).

## Usage
- Mathesar will create a new database for users unless one is already provided.
- We encourage users to use [Schemas](/archive/product/concepts/schemas) for storing different sets of unrelated data rather than creating multiple databases.