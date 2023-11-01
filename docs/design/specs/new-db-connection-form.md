# "New Database Connection" Form Design Specs

## Overview

Mathesar stores two kinds of "database connections"

- One and only one **"_internal_ database connection string"**

    This is stored in the `.env` file and allows Mathesar to connect to its internal database, either PostgreSQL or SQLite. Mathesar does not allow users to edit these connection details through the UI.

- Zero or more **"_user_ database connection objects"**

    These are metadata objects which each allow Mathesar connect to a user database. They are stored in Mathesar's internal database and each contain:

    - an unique auto-incremented id
    - host name, e.g. `localhost` or `example.com`
    - port, e.g. `5432`
    - user name
    - password (AES encrypted via Mathesar's Django secret key)
    - database name
    - a unique connection "nickname" (used for abbreviated display in the UI)

The "New Database Connection" form allows the user to

- Create a new user database connection object
- Optionally, create a new _database_ (within Postgres) for the connection
- Optionally, create a new postgres user for the connection

This form is especially relevant during installation because the person installing Mathesar must complete this form in order to create and connect to the first user database.

## Scope of these specs

This spec only concerns itself with the UI _within_ the "New Database Connection" form. It does not concern itself with the manner in which the user arrives at that form or where they go next. The form might open in a modal, or in a new page, or inline within a page listing connections &mdash; we're not sure yet.

The form to _edit_ existing DB connections is much more straightforward and thus is not covered here.

## Terminology

With this spec...

- **"Credentials"** (or one "set of credentials") refers to a tuple containing the *host*, *port*, *user*, and *password*.

    I call attention to this term because it's important in these specs, but not necessarily widely considered to mean _exactly_ those four things together. (I'm open to suggestions for better terms!)

## The form at its simplest

This is the simplest (and hopefully most common) incarnation of this form. As an example, the user should (somehow) arrive at this form after installing Mathesar using the Docker installation method.

<img src="/assets/design/specs/new-db-connection-form/a.png" width="550px">

Notes:

- The "Credentials to use" input contains options for all user database connections, plus the one internal database connection (if using Postgres for the internal database). The list of options should contain distinct host/port/user tuples so as to avoid presenting visually indistinguishable options to the user.

    **Implementation notes:**

    Mathesar's metadata currently stores connections flatly, such that, if two connections use the same host/port/user/password to connect to two different databases, those connection credentials are duplicated across the connection records. Likewise, credentials may occur in duplicate across the `.env` file and the internal database. This data model complicates the process of generating a form which contains distinct options for "Credentials to use". This process is to be improvised during implementation, either by improving the data model or by employing de-duplication logic somewhere in the stack. Such de-duplication logic would present some strange edge cases. For example, consider two connections to the with the same host/port/user but with different stored passwords. One connection succeeds, while the other fails. For the sake of this form, we need to present only _one_ of these options to the user, but we don't know which one. If we stick with the data model we have, then we should de-duplicate by preferring the `.env` connection over any user db connections and by preferring user db connections with higher `id` values. 

- The credentials info is pre-filled according to the following logic:

    - If Postgres is used for the internal DB, then:

        - "Credentials source" = "Reuse credentials..."
        - "Credentials to use" = the credentials for the internal DB, from `.env` 

    - Else, (SQLite is used for the internal DB) then:
    
        - If at least one connection exists to a user database, then:

            - "Credentials source" = "Reuse credentials..."
            - "Credentials to use" = the credentials from the user database with the highest `id`

        - Else, (no user database connections exist), then:

            The "Credentials source" question will be omitted from the form, and the remaining questions will generated as if the user had selected "Enter new connection credentials" (as shown below).
        
- `db` is pre-filled as a suggested database name only if no user database connections exist. If at least one connection exists to a user database, then the input is empty.

- Under the "Create this database..." checkbox field, the help text includes a postgres user name in quotes. That user name is dynamic so as to match the user name of the chosen connection.

- The "Connection nickname" field auto-updates as the user enters the database name, but the user can modify the "Connection nickname" value independently of "Database name". (This behavior of auto-generating a nickname is the reason for putting the field last.) 


## Manually entering new connection credentials

If, on the form depicted above, you change "Credentials source" to "Enter new...", then the "Credentials to use" field will be replaced by the fields shown below:

<img src="/assets/design/specs/new-db-connection-form/b.png" width="550px">

Notes:

- `localhost` is pre-filled as a default Host name value
- `5432` is pre-filled as a default Port value

## Creating a new Postgres user

If, on the form depicted above, you change "User type" to "Create a new...", then the "User name" and Password fields will be replaced by the fields shown below:

<img src="/assets/design/specs/new-db-connection-form/c.png" width="550px">

Notes:

- As the form above demonstrates, we need an existing set of credentials in order to connect to the PostgreSQL server and "bootstrap" the new user. If no such credentials exist for the host and port as the user entered it above, then the "User type" field will be omitted from the form and the form will be rendered with the "Use an existing PostgreSQL user" logic.

- The "Create user via" input uses sorting and pre-filling logic similar to the "Credentials to use" field as described above. Additionally, its options are filtered to only show credentials matching the host name and port that the user entered above.

