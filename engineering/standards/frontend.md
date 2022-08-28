---
title: Front end code standards
description: 
published: true
date: 2022-03-18T22:22:43.557Z
tags: 
editor: markdown
dateCreated: 2022-03-18T22:22:43.557Z
---

## General

### Naming conventions

* File names for Components, Classes and Stylesheets should be in PascalCase. Examples:
    
    ```txt
    App.svelte
    CancellablePromise.ts
    App.scss
    ```

* Typescript file names should be in lowerCamelCase. Examples:
    
    ```txt
    index.ts
    utilityFunctions.ts
    ```

* All variables and constants should be in lowerCamelCase. Examples:
    
    ```javascript
    export let randomVariable;
    let aNewVariable = 'new variable';
    const someValue = 'constant value';
    ```

* All function names should be in lowerCamelCase. Examples:
    
    ```javascript
    function someFunction() { /* ... */ }
    let someOtherFn = () => { /* ... */ };
    const someConstFn = () => { /* ... */ };
    ```

* All directory names should be in kebab-case (hyphen-delimited). Examples:
    
    ```txt
    /components/text-input/
    /components/combo-boxes/multi-select/
    ```

* Acronyms within PascalCase and camelCase should be treated as words. Examples:

    ```txt
    UrlInput.svelte
    ```

    ```ts
    function getApiUrl() { /* ... */ }
    let currentDbName;
    ```

    - [discussion](https://github.com/centerofci/mathesar/discussions/908)
    - Not all code conforms to this standard yet, and bringing existing code into conformance is a low priority.

* Use American English spelling instead of British English spelling. Examples:

    ```txt
    LabeledInput.svelte
    ColorSelector.svelte
    ```

    - [discussion](https://github.com/centerofci/mathesar/discussions/891)

* If a TypeScript file contains _only_ type definitions (without any values or implementation), then use the file extension `.d.ts` instead of `.ts`. If you use `enum` or `const` you'll need make the file a `.ts` file. If you only use `type` and `interface`, then make the file a `.d.ts` file.

* Prefer the term "delete" in code and UI over similar terms like "remove" and "drop".

    - [discussion](https://github.com/centerofci/mathesar/discussions/872)

## HTML

### Build components for valid DOM nesting

When working inside a component that _might_ be placed where [phrasing content](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Content_categories#phrasing_content) is required, be sure to only use phrasing content elements (like `span`) instead of _not_-phrasing content elements (like `div`).

-  ✅ Good

    `FancyCheckbox.svelte`

    ```ts
    <span class="make-it-fancy">
      <input type="checkbox" />
    </span>
    ```

- ❌ Bad because it uses `div` instead of `span`

    `FancyCheckbox.svelte`

    ```ts
    <div class="make-it-fancy">
      <input type="checkbox" />
    </div>
    ```

Rationale:

- For example, let's build on the "Bad" example above and write the following Svelte code:

    ```svelte
    <label>
      <FancyCheckbox />
      Foo
    </label>
    ```

    That Svelte code will render:

    ```html
    <label>
      <div class="make-it-fancy">
        <input type="checkbox" />
      </div>
      Foo
    </label>
    ```

    That markup has invalid DOM nesting because a `label` element can only contain phrasing content -- but a `div` is _not_ phrasing content.

Tips:

- You can make a `span` _act_ like a `div` by setting `display: block` if needed.

Notes:

- Not all of our components adhere to this guideline yet.

## CSS

### CSS units

- Don't use `px` — use `rem` or `em` instead.

    Exceptional cases where `px` is okay:

    - when setting the root `font-size`

Note: some of our older code still does not conform to this standard.

### Component spacing and layout

Components should not set any space around their outer-most visual edges — instead the consuming component should be responsible for layout and spacing.

- **margin**: The component's root element should not set any margin.

- **padding**: If the component's root element has border, it's fine to set padding because the border will serve as the outer-most visual edge. But if there's no border, then there should be no padding.

## JavaScript

### `function` vs `const`

Prefer `function` over `const`

-  ✅ Good

    ```ts
    function withFoo(s: string) {
      return `${s} foo`;
    }
    ```

- ❌ Bad

    ```ts
    const withFoo = (s: string) => {
      return `${s} foo`;
    }
    ```

Rationale: 

- The `function` syntax is more concise, with less likelihood of line wrapping.

- With TypeScript, adding explicit return type annotations becomes significantly more verbose when using the `const` approach. For example,

    ```ts
    export const withFoo: (s: string) => string = (s: string) => {
      return `${s} foo`;
    }
    ```

    We don't require explicit return types everywhere, but we do use the [explicit-module-boundary-types](https://github.com/typescript-eslint/typescript-eslint/blob/v4.33.0/packages/eslint-plugin/docs/rules/explicit-module-boundary-types.md) linting rule to require them for _exported_ functions. This makes TS errors appear closer to the code that should be fixed and also provides some small performance gains with `tsc`.


## TypeScript

### `type` vs `interface`

- Prefer `interface` when possible.
- Use `type` when necessary.

### `null` vs `undefined`

Prefer using `undefined` over `null` where possible.

-  ✅ Good

    ```ts
    const name = writable<string | undefined>(undefined);
    ```

- ❌ Bad because it uses `null` when it could use `undefined`

    ```ts
    const name = writable<string | null>(null);
    ```

- ❌ Bad because it uses an empty string to represent an empty value when it probably should be using `undefined` for greater code clarity.

    ```ts
    const name = writable<string>('');
    ```

- ❌ Bad because it mixes `null` and `undefined` into the same type.

    ```ts
    const name = writable<string | undefined | null>(null);
    ```

-  ✅ Acceptable use of `null` because it's necessary for data that will be serialized to JSON. (Using `undefined` here would result in that key/value pair being removed from the JSON string).

    ```ts
    await patchApi(url, { name: null });
    ```

-  ✅ Acceptable use of `null` because the `Checkbox` component is designed to accept a `null` value to place the checkbox into an indeterminate state.

    ```svelte
    <Checkbox value={null} />
    ```

Considerations:

- In some cases you may need to coalesce a `null` value to `undefined`. For example:

    ```ts
    function firstCapitalLetter(s: string): string | undefined {
    return s.match(/[A-Z]/)?.[0] ?? undefined
    }
    ```

Additional context:

- [discussion](https://github.com/centerofci/mathesar/discussions/825)

### API type definitions

TypeScript types (including interfaces) which describe API requests and responses (and properties therein) should be separated from other front end code and placed in the `mathesar_ui/src/api` directory. This structure serves to communicate that, unlike other TypeScript types, the front end does not have control over the API types.

[Discussion](https://github.com/centerofci/mathesar/discussions/875)

## Svelte

### Minimize Svelte store instances

- ✅ Good because only one `cost` store is created.

    ```ts
    function getCost(toppings: Readable<string[]>) {
      return derived(this.toppings, t => 10 + t.length * 2);
    }

    class PizzaOrder {
      toppings: string[];
      cost: Readable<number>;

      constructor() {
        this.toppings = [];
        this.cost = getCost(this.toppings);
      }
    }
    ```

- ❌ Bad because separate calls to `cost` will create separate stores which may lead to more subscribe and unsubscribe events in some cases, risking performance problems.

    ```ts
    class PizzaOrder {
      toppings: string[];

      constructor() {
        this.toppings = [];
      }

      get cost(): Readable<boolean> {
        return derived(this.toppings, t => 10 + t.length * 2);
      }
    }
    ```

Additional context:

- [Discussion](https://github.com/centerofci/mathesar/pull/776#issuecomment-963831424)



### Usage of `{...$$restProps}`

We use `{...$$restProps}` occasionally in our code despite some drawbacks.

Example:

- `Child.svelte`

    ```svelte
    <script>
      export let word;
    </script>

    <span class="child">{word}</span>
    ```

    `Child` explicitly accepts a `word` prop.

- `Parent.svelte`

    ```svelte
    <script>
      import Child from './Child.svelte`;
    </script>

    <Child {...$$restProps} />
    ```

    `Parent` _implicitly_ accepts a `word` prop.

- `Grandparent.svelte`

    ```svelte
    <script>
      import Parent from './Parent.svelte`;
    </script>

    <Parent word="foo" />
    ```

    This renders `<span class="child">foo</span>`


Benefits of using `{...$$restProps}`:

- It reduces code duplication when composing components.

Drawbacks (with commentary added):

- In the example above, `Parent.svelte` gives little indication that it accepts a `word` prop, making its behavior somewhat opaque. Further, the `Parent` component lacks type safety on the `word` prop.

    However, we expect Svelte to eventually address these shortcomings by allowing us to provide more [explicit typing](https://github.com/sveltejs/rfcs/pull/38) for component props in these cases.

- On using `{...$$props}` and `{...$$restProps}`, the [Svelte docs](https://svelte.dev/docs#template-syntax-attributes-and-props) say

    > It is not generally recommended, as it is difficult for Svelte to optimise

    However, thus far we have not identified any performance issues here.
