---
title: Getting Started with Frontend Codebase
description:
published: true
date: 2023-03-23T17:00:00.166Z
tags:
editor: markdown
dateCreated: 2023-03-23T17:00:00.166Z
---

## Introduction

This article aims to document the major patterns that are being used in the frontend codebase. Learning about these patterns will help speed up the process of onboarding on the codebase for a completely new person.

There are a lot of varying patterns that you will find in the codebase which we do not recommend anymore and hence are not even documented here.

## Rendering Architecture & Common Data

When you hit the base route in your browser's address bar, the initial request is served by the Django server. Depending on the authentication state of the user an appropriate HTML file is being served.

If the user is authenticated, the server embeds some data in the JSON format inside the HTML. The data is embedded inside an HTML tag with the id `common-data`. Internally we also refer to this data using the terminology `commonData`.

This JSON is used by the frontend code to render the UI on the first load without having to make additional round trips to the server.

Code related to this can be find inside: `src/utils/preload.ts`.

## State management

Our codebase uses two main svelte features in combination for managing the frontend state namely [stores](https://svelte.dev/tutorial/writable-stores) and the [context api](https://svelte.dev/tutorial/context-api)

> **Note:** Before moving on to the next part please make sure to familiarise yourself with svelte stores and the context API.

There are two main patterns used for creating stores

### The immutable class pattern - Coarse Reactivity

The whole instance of the class is being converted into a store. Whenever there is a change in any of the properties of the instance a new instance is created with the updated value and replaced in the store.

```typescript
immutableClassInstance.update((currentInstance) =>
  currentInstance.createAndReturnNewInstanceWithUpdatedProperties(
    propertiesToUpdate
  )
);
```

An example of this can be found here: `mathesar_ui/src/stores/table-data/filtering.ts`. Look for the `Filtering` class.

### The mutable class pattern - Granular Reactivity

Only the required instance properties of that class are writable stores. The only way to update those stores is by using an instance method.

The writable store variables are `readonly` so that they cannot be re-assigned from outside the class. We cannot make them `private` because we still want the caller to be able to subscribe to them. We also use the following typescript utility to make the `writable` stores `readable` before they are exported so that the caller cannot use the `.set/.update` methods directly. This helps us maintain encapsulation.

```typescript
type ChangeWritableToReadable<T> = T extends Writable<infer U>
  ? Readable<U>
  : T;

/**
 * This makes all Svelte store properties Readable instead of Writable. With
 * This utility type, we can write a class that has privately writable stores
 * which are read-only publicly, and then the safety check is enforced by TS at
 * compile time.
 */
export type MakeWritablePropertiesReadable<T> = {
  [P in keyof T]: ChangeWritableToReadable<T[P]>;
};
```

An example of this can be found here: `mathesar_ui/src/stores/users.ts`. Look for `WritableUserStore` class.

Other older patterns are being used for creating stores for example **Object stores** which you can read more about in `src/stores/database.ts` and `src/stores/schema.ts`.

### Context APIs

Stores once created are being passed around the components using the context API instead of prop drilling. This generally warrants creating two functions:

```typescript
function getStoreFromContext(): ReturnType | undefined {
  return getContext<ReturnType>(contextKey);
}

function setStoreInContext(): ReturnType {
  if (getStoreFromContext() !== undefined) {
    throw new Error("Context has already been set!");
  }

  // If the store is an immutable class
  const store = writable(new ImmutableClass());

  // If the store is a mutable class
  const store = new MutableClass();

  setContext(contextKey, store);
  return store;
}
```

### Store powering the table page

One of the most complex store built on the principles of mutable class pattern is: `TabularData`. It can found here: `mathesar_ui/src/stores/table-data/tabularData.ts`. This is the store that powers the whole table page.

## Navigating the directory structure

```
mathesar-ui
	src
	Entry point for all of the application frontend code

		api
		Contains all the api calls.

		component-library
		Custom component library for primitive reusable components. Can be later open-sourced to be used in other applications too.

		components
		Mathesar-specific reusable components. These components are being used inside multiple pages.

		icons
		All application-specific icons.

		layouts
		Contains layout components.

		pages
		Contains all the components for a particular page that are not being used anywhere else.

		routes
		Contains the root component for all of the routes.

		stores
		Contains all the stores.

		systems
		*??*

		utils
		Contains all of the utilities divided into different concerns.
```

## Dealing with APIs

In the majority of the codebase, the API calls are being tightly coupled with the stores. Look at the schemas store here: `mathesar_ui/src/stores/schemas.ts`.

But with the recent [proposal](https://github.com/centerofci/mathesar-wiki/blob/fe-rfc-users-permissions/engineering/specs/usersandpermissions.md#proposal) the API calls are being separate out in `src/api`.

1. There is a directory `src/api/` that contains `src/api/types` and `src/api/utils`. The new files will be placed within `src/api/`.
2. Each utility file will export its related types.
   A good example will be to look at: `src/api/users.ts`.

## Component library

Mathesar is built on top of its custom UI library. The library lives inside the `src/component-library`. The code inside the library has the following structure:

```
src
	component-library
		<component-name>
			__meta__
				This contains the storybook stories for this component

			ComponentName.svelte
			ComponentName.scss
```

1. Run the storybook: https://github.com/centerofci/mathesar/tree/develop/mathesar_ui#storybook
2. See the [Components README](https://github.com/centerofci/mathesar/blob/develop/mathesar_ui/src/component-library/README.md) for more details.

## Form library

Mathesar uses its own custom form creation and validation library. It lives in `src/components/form`.
You can read more about this library here: https://github.com/centerofci/mathesar/pull/1932 under the following headings in the PR description

1. An example form
2. How it works

## Icons

Mathesar uses svg icons throughout the application. There is an `Icon` (can be found here: `mathesar_ui/src/component-library/icon/Icon.svelte`) component inside the `component-library` that is responsible for rendering the correct icon given the svg data.

### Storage of icons from font-awesome

All icons are named after a concept that they denote instead of their appearance. These icons are also stored at two central locations:

1. Icons that belong to the component library - `src/component-library/common/icons.ts`
2. Icons that belong to the application codebase - `src/icons/index.ts`

More on icon naming here: https://github.com/centerofci/mathesar/issues/1187

### Custom Icons

There are a few cases where custom icons or non-font-awesome icons are being the user. The svg data of these icons are stored here: `src/icons/customIcons.ts`.
Custom icon data is stored so that it can again be rendered using the `Icons` component.
