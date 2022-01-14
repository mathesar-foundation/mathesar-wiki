---
title: Front end standards
description: 
published: true
date: 2022-01-14T19:02:19.924Z
tags: 
editor: markdown
dateCreated: 2022-01-14T19:02:19.924Z
---

# Front end code standards

## Naming conventions

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