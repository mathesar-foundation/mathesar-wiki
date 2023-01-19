---
title: Users and Permissions frontend RFC
description:
published: true
date: 2023-01-19
tags: 
editor: markdown
dateCreated: 2023-01-19
---

**Feature**: Users & Permissions frontend
**Meta ticket**: [Users & Permissions Frontend - Meta ticket](https://github.com/centerofci/mathesar/issues/2205)
**Design**: [Figma design link](https://www.figma.com/file/xHb5oIqye3fnXtb2heRH34/Styling?node-id=3666%3A25085&t=b2Pw2pUJh42nRKQ3-1)
**Related**: N/A

This document is a RFC for high level technical specification and a task list for the initial version of the Users & Permissions feature. Note that this only focuses only on the frontend.

# Task list
* API utility for users
* API utility for permissions
* Stores needed for user profile
* Utilities for user permissions
* Account profile route & page
* Users route & page
* Password reset page UI & rerouting logic
* Permission based restriction in DB route
* Permission based restriction in Schema route
* Permission based restriction in Table route
* Permission based restriction in Exploration routes
* Permission based restriction in Record route
* Modal for editing access level in DB page
* Modal for editing access level in schema page

# High level implementation details
## Dedicated API utils
### Issue
* We have been utilizing stores directly and encapsulated all API calls within them.
* This is problematic for a number of reasons including:
  - Not being able to make API calls that do not affect the store.
  - Certain objects do not require a store (in this case - Users).
* We have been side-stepping these issues by:
  - Having utility functions within store files to make API calls & not update the store.
  - Making API calls directly within components

### Proposal
* A long-term solution is to separate out API calls from the stores, and have dedicated API utils for each of our endpoints.
* We have a directory `/api/` that contains `/api/types` and `/api/utils`. The new files will be placed within `/api/`.
* We will no longer place types within `/api/types`. Each utility file will export it's own related types.
* We'll start this approach with Users & Permissions.
* Existing stores stay as they are, until we are ready for a refactor.
* We will have a utility file that is placed here:
  * `/api/users.ts`
* This file will export the necessary types and contain a default export of an object or class that an interface like:
  ```ts
  export interface User { ... }
  export interface UnsavedUser extends Omit<User, 'id'> {
    password: string;
  }

  interface UsersApi {
    // endpoint: GET: /users/
    list: () => PaginatedResponse<User>;
  
    // endpoint: GET: /users/<user_id>/
    get: (userId: User['id']) => User;
  
    // endpoint: POST: /users/
    add: (user: UnsavedUser) => User;
  
    // endpoint: DELETE: /users/
    delete: (userId: User['id']) => void;
  
    // endpoint: PATCH: /users/<user_id>/
    update: (userId: User['id'], properties: Partial<Omit<User, 'id'>) => User;
  
    // endpoint: POST: /users/<user_id>/password_change/
    changePassword: (userId: User['id'], password: string) => void;

    // endpoint: POST: /users/<user_id>/password_reset/
    resetPassword: (userId: User['id'], password: string) => void;

    ... // endpoints for adding/removing roles
  }

  const usersApiUtility: UsersApi = { ... };
  export default const usersApiUtility;
  ```
* The above interface and propety naming are tentative and can change during implementation.

## Routes
Below are the new routes that'll be added:
  - `/admin/`
    - `/admin/general/`
      - Default sub route.
      - Will be used by upgrade & installation info. Unrelated to Users & permissions.
    - `/admin/users/`
      - List users.
      - `/admin/users/new/`
        - Add new user.
        - Upon saving redirects to `/userId`, without re-rendering page.
      - `/admin/users/<userId>/`
        - Edit user.
  - `/profile/`
    - User profile page
    - In the future, this will contain customization options like themes, language etc.,

## Stores & data fetch logic for User profile
* Current user's information will be loaded along with `common_data`.
* This will be a top level store, exported from `/stores/userProfile.ts`
* The store will make use of the Users Api utility and will not directly make any API calls.
* It will be loaded as a context variable at the `App` level.
* We'll have utility functions to set & get the context and use it wherever required. These functions will be part of the store file.
* The User profile will contain a `hasPermission` function which accept any of the permission utility objects. (More on permissions below).
* The profile class would be something like:
  ```ts
  class UserProfile implements User {
    ...
    hasPermission(calculateAccess: Permission): boolean {
      return calculateAccess(this.roles);
    }
  }
  ```

## Utilites for Permissions
* We'll have utility classes for all objects that require access control.
* These utilities will be stored within `/utils/permissions/`.
* The utility classes currently will include:
  - database
  - schema
  - table
  - exploration
* Each of them will accept constructor parameters as required.
  - database:
    - None
  - schema:
    - `{ databaseId: Database['id'] }`
  - table:
    - `{ databaseId: Database['id'], schemaId: Schema['id'] }`
  - exploration:
    - `{ databaseId: Database['id'], schemaId: Schema['id'] }`
* Each of these classes/objects will export:
  - `view: (roles: UserRoles) => boolean`
  - `edit: (roles: UserRoles) => boolean`
  - `manage: (roles: UserRoles) => boolean`
* In the future, we'll extend this to contain more granular operations based on each item.
  - For eg., `table.ddl, table.share` etc.,
* The interface would be like:
  ```ts
  type Permission = (roles: UserRoles) => boolean;

  interface AccessController {
    [permissionName: string]: Permission
  }

  class AccessControlledObject implements AccessController {
    constructor(args) {
      ...
      this.db = args.db;
    }
    edit: Permission = (roles) => { ..., return false; }
    view: Permission = (roles) => { ..., return true; }
  }
  ```
* `UserRoles` would contain all roles & permissions of the user i.e `is_superuser, database_roles, schema_roles`. 

## Permission access level checks in App routes
* Checks across the app would function like this:
  ```ts
  const currentUser = getUserProfileContextStore();

  $: schemaAC = getSchemaAccessController({ databaseId });
  $: hasManagerAccess = currentUser.hasPermission(schemaAC.manage);

  $: tableAC = getTableAccessController({ databaseId, schemaId });
  $: hasTableEditAccess = currentUser.hasPermission(tableAC.edit);
  ```
* The access controller objects will be set in context as required.

## Data fetch logic for users
* `/admin/users/` route & sub-routes will not use a top level store. If required, we'll have route specific stores.
* It will make API calls using the API utilities.
* If the user being updated is the current user, it will update the top level profile store.
