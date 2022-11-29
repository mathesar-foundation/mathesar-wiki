---
title: Users & Permissions
description: 
published: true
date: 2022-11-29T23:37:17.842Z
tags: 
editor: markdown
dateCreated: 2022-09-09T13:25:30.516Z
---

This spec describes how the initial version of users & permissions will work in Mathesar.

## Feature Goals
- Facilitate user collaboration by giving multiple users access to the data in Mathesar
- Allow Mathesar administrators to follow the security best practice of the principle of least privilege 
- Allow Mathesar administrators to set up user accounts, view or change current users and their privileges, and delete users.
- Allow users to customize their Mathesar experience, including:
	- Display settings such as table inspector show/hide, etc.
	- Private Explorations.

### Bonus Goals
*We may not get to implementing these in 2022.*
- Allow users to be represented in Mathesar data and workflows through a User data type
- Allow restricting access to subsets of tables, schemas, or explorations based on user attributes

### Library Use Case
To make these goals more concrete, here's how these features could be used in [the library use case](https://www.figma.com/file/F0FmNaNz8hvrgxPax3Bix1/Cycle-3-reference?node-id=0%3A1) we've been working on for Cycles 2 and 3.

- Enable the **IT administrator** to set up Mathesar, invite new users, set up new schemas, etc.
- Enable the **library manager** to administer the Library management schema, including changing the structure of tables.
- Enable the **library staff** to input data and add/remove/modify explorations, but not change the underlying structure of data.
- **If our bonus goals are met:**
	- Enable the **library patrons** to view select explorations (e.g. books available for checkout)
	- Allow **library staff** to associate **library patrons** with their Mathesar accounts in the Patrons table
	- Allow **library patrons** to log in and see only their own checkouts with the associated due dates.

## Scope & Assumptions
This is meant to be a very basic framework for users & permissions that we can implement in 2022 in Cycles 4 and 5. 

We're making the following assumptions for this spec to reduce implementation complexity. These should ***not*** be treated as permanent assumptions for the product.

### Users will be Mathesar-specific.
This means:
- Users created using the Mathesar UI will not be able to log in to the PostgreSQL DB using the same credentials. 
- Existing Postgres DB users will not be able to log in to Mathesar using their credentials.

Although it would be ideal to reflect Postgres users in Mathesar and vice-versa, this involves either figuring out how to store people's DB credentials securely or have them log in every time they open the application. Neither seems ideal.

### User passwords cannot be reset via email
To do this, we'll need to implement email infrastructure into Mathesar.  While we need to figure this out at some point, I don't think it's worth doing it now just so that users can reset passwords.

Users should be able to reset their passwords from the UI. Administrators can reset anyone's password. We should follow security best practices so that the admin does not ever see the user's permanent password.

### Privileges will be Mathesar-specific
Although it would be ideal to support the full range of [Postgres privileges](https://www.postgresql.org/docs/14/sql-grant.html) (e.g. users can give `TRUNCATE` privileges on a table to someone else), this will involve a lot of implementation and design work to get right. It's probably not useful for the vast majority of use cases.

Instead, we will have more "user friendly" privileges that combine permissions for both Postgres and Mathesar-specific objects.

### Only local username and passwords are supported
We won't support social log in or SSO protocols at this time. As with the rest of this list, we may want to do so in the future.

## Sub-Features Needed
This is a list of features needed for the product in order to complete the "Users & Permissions" feature.

### Mathesar installation
When Mathesar is first installed, we'll create a default "Administrator" user. This user cannot be deleted, although the username and password can be changed if needed.

### User management page
Mathesar administrators should be able to navigate to a user management page and take the following actions:
- Add a user
- Delete a user
- Edit user details
- Reset the user's password
- See the user's permissions
- Add / remove user permissions

*Wireframes are for illlustrative purposes, they are not meant to reflect final design.*
![users.png](/assets/product/specs/users-permissions/users.png)
![user-page.png](/assets/product/specs/users-permissions/user-page.png)![user-page-custom.png](/assets/product/specs/users-permissions/user-page-custom.png)

### Log in and Log out
Users should be able to log in and log out of Mathesar using their username and password.
![sign-in.png](/assets/product/specs/users-permissions/sign-in.png)

### User Profile Page
Individual users should be able to edit their own information. This is also going to be where they edit their settings for using Mathesar, once we have some.

### Schema sharing
There should be a way for users to share individual schemas with others.

#### Table Page changes
We need different UI for tables based on whether the user is a Viewer, Editor, or Manager.

#### Schema Page changes
We need different UI for this page based on whether the user is a Viewer, Editor, or Manager.

#### Database Page changes
We need different UI for this page based on whether the user is a Viewer, Editor, or Manager.

#### Exploration Page changes
We need different UI for this page based on whether the user is a Viewer, Editor, or Manager.

#### Navigation changes
We need different navigation options based on the objects the user has permissions for.

### User data to save
We should have a place to save the following kinds of data per user:
- Table inspector show/hide settings
- Last access time per-table
- Last access time per-exploration
- Last access time per-schema
- Favorite tables
- Favorite schemas
- Favorite explorations

The frontend should save this stuff and respect table inspector show/hide settings. This will not be exposed to the user via any UI, it's just saved automatically.

Last access / favorite will be used on the schema and database homepages, but those designs are out of scope for this spec.

### API permissions
We also need to implement permissions on the API that match user permissions. 

### Bonus Goals: Table & Exploration sharing
There should be a way for users to share individual tables and explorations with others.
![sharing.png](/assets/product/specs/users-permissions/sharing.png)


### Bonus goals: User data type & row level permissions
Here's some ideation on this feature. Further details will be specified if we have time to implement them.
![rls.png](/assets/product/specs/users-permissions/rls.png)

## Implementation Details
High-level notes on how we should implement these features.

### Users in the service layer
Users should be Django `User` objects with the following attributes:
- Username (required)
- Password (required)
- Full name (required)
- Short name (optional)
- Email (optional)

### Users in the database layer
From a security PoV, it would be ideal if we could create a Postgres role for every user and use that role to access the DB when the user is logged in. That way, we can't even see or use objects the user doesn't have access to.

We will not do this for the initial version of this feature, but this remains our long term plan.

### Permissions: Basic
We will have the following layers of permissions. The implementer needs to figure out how to map these to Postgres privileges.

#### User
All users can:
- Edit their own user's attributes, including reset their own password
- Create private explorations based on data they have access to.

#### Administrator
A superuser. They have every permission related to the Mathesar installation listed below.

For now, only the default admin user can have this permission. New users cannot be created with this permission. 

#### Database permissions
These permissions apply to a single database.
| Permission | Database Manager | Database Editor | Database Viewer |
|---|---|---|---|
| Add new Mathesar users | x | - | - |
| Add and remove schemas | x | - | - |
| Permissions on all contained schemas | Manager, Editor, Viewer | Editor, Viewer | Viewer |

#### Schema permissions
These permissions apply to a single schema.
| Permission | Schema Manager | Schema Editor | Schema Viewer |
|---|---|---|---|
| Share schema with other users | x | - | - |
| Add and remove tables | x | - | - |
| Add and remove shared explorations | x | x | - |
| Permissions on all contained tables and explorations  | Manager, Editor, Viewer  | Editor, Viewer | Viewer |

### Public schema
All users should have Manager access to the `public` schema by default (to align with Postgres conventions). We should make that clear in the design when we implement these features.

### Permissions: Bonus
These permissions are planned to be implemented at some point, but are not required for the initial version of this feature.

#### Table permissions
These permissions apply to a single table.
| Permission | Table Manager | Table Editor | Table Viewer |
|---|---|---|---|
| Share table with other users | x | - | - |
| Modify structure of table (DDL operations) | x | - | - |
| Modify widgets on record page | x | - | - |
| Edit data within table | x | x | - |
| Edit data within record page | x | x | - |
| View table | x | x | x |
| View record page | x | x | x |
| Apply filter/sort/group to tables (not saved) | x | x | x |
| Apply filter/sort/group to record page widgets (not saved) | x | x | x |

#### Exploration permissions
| Permission | Exploration Manager | Exploration Editor | Exploration Viewer |
|---|---|---|---|
| Share exploration with other users | x | - | - |
| Edit the exploration | x | x | - |
| View exploration | x | x | x |
| Apply filter/sort/group to explorations (not saved) | x | x | x |

- To have `Editor` or `Manager` permission on an Exploration, a user needs to at least have `Viewer` permissions on all dependent tables.

---

**Note**: If we implement additional bonus features, we will also have additional permissions for subsets of tables and explorations here (only certain rows/records and columns). Those are not specced out here.
