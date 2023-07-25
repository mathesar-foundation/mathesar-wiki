---
title: Number display and entry
description: Goals and strategies for the display and entry of numerical data
published: true
date: 2023-07-19T23:28:08.005Z
tags: 
editor: markdown
dateCreated: 2022-03-17T17:35:25.376Z
---

## Product goals

- **(Goal A)** Mathesar is capable of displaying and accepting entry for all [numbers which Postgres is capable of storing](https://www.postgresql.org/docs/current/datatype-numeric.html).

- **(Goal B)** Aside from the numbers, `NaN`, `-Infinity`, and `Infinity`, users are able to type all numbers into Mathesar exactly as Mathesar displays those numbers to them.

- **(Goal C)** When a user enters data which cannot be accurately stored in the column exactly as-entered, then Mathesar stores the nearest acceptable value and clearly communicates to stored value to the user.

    For example, a `float8` column cannot accurately store the value `9999999999999999` (because it will instead be stored as `1e+16`). In this example, Mathesar will store `1e+16`, displaying that value back to the user after entry.

- **(Goal D)** Mathesar displays numbers and accepts entry of numbers in the user's desired locale, including the correct decimal separator and grouping separators.

- **(Goal E)** Mathesar auto-formats numbers as the user types.

- **(Goal F)** Mathesar accepts entry of numbers in scientific notation and displays numbers in scientific notation when the user is likely to prefer it. For example `1E100` instead of 1 followed by 100 zeros.

## Implementation strategies

### API

- The API transmits numbers as strings because most JSON parsers are not capable of accurately parsing high precision numbers or special Postgres numbers stored plainly in JSON. The format for such strings is described below.

### Canonical stringified number format

Throughout our stack, we may want to represent numbers as strings. When doing so, we follow a format very similar to numbers in JSON.

- The decimal separator is an ASCII dot.
- The minus sign is an ASCII hyphen.
- The exponent separator is an uppercase "E".
- Grouping separators are disallowed.
- The strings `"NaN"`, `"-Infinity"`, and `"Infinity"` are used to represent special Postgres numbers. Note that this is one way in which our stringified number format differs from JSON -- raw values like `NaN` are _not_ valid inside JSON.
- The string `"NULL"` should _not_ be used. In JSON, the _value_ `null` should be used instead.
- Examples:

    - `"NaN"`
    - `"-Infinity"`
    - `"Infinity"`
    - `"0"`
    - `"1234.5"`
    - `"99999999999999999999999999999999"`
    - `"-1.2E-15"`


### Locale

- To satisfy Goal D, Number columns have an optional `locale` display option which is set by the front end and read by the front end. If a column's `display_options` does not have a `locale` value, then the front end infers the locale from the user's browser. The back-end remains locale-agnostic and never uses the `locale` display option for any back-end logic.

- Mathesar is limited to only displaying and accepting entry for numbers using the latin numbering system. This means sacrificing Goal A for the locales  "bn", "fa", and "mr" (Bengali, Persian, Marathi) which use non-latin numbering systems by default.

- The minus sign is always displayed using an ASCII hyphen, regardless of locale (even though some locales like 'li' use the Unicode minus sign). The Unicode minus sign (and similar characters) will be accepted in all locales while _entering_ numbers though.

- For display of scientific notation, the exponent separator is always displayed using the ASCII "E" regardless of locale even though some locales use other exponent separators. For input, other strings are accepted too, such as "e" (lowercase) and "Е" (U+0415) and variations of "x10^".

### Parsing

- The front end parses **user input**, by performing string transformations to normalize the input into canonical stringified form. For example, all characters matching the current locale's decimal separator are converted to ASCII dots.

- The front end parses **canonical stringified numbers** (as produced above, or received from the API) by attempting to produce a `number` or `BigInt` which can be re-formatted exactly to match the input (without loss of precision).

- The front end will **fail** to parse canonical stringified numbers like `"99999999999999.99"` (which cannot be accurately represented by any of JavaScript's built-in data types) because they will fail to be reformatted without loss of precision.

- The front end actually _almost_ doesn't need to parse numbers at all. But it does so for the following reasons.

    1. Because we want to format a cell's numerical value for display. There are a variety of smaller goals here.

        - Likely the most important goal is to format the decimal separator in accordance with the user's locale (dot or comma). That's easy to do with strings, so if that's all we care about, then we can actually stick with strings.
        - Adding grouping separators is _nice_, but not crucial. Even if the separators are applied after the user finishes typing, I think they offer a significant UX improvement in some situations. If we stick exclusively to strings, it's actually quite hard to add the grouping separators in a locale-aware way. The `Intl` API takes care of it for us, but only if we have a `number` or `BigInt` -- so that requires parsing.
        - Similar to above, `Intl` offers a bunch of other [formatting options](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/NumberFormat) that we'll likely want to utilize at some point in the future, like `style: 'percent'`, `style: 'currency'`, `minimumFractionDigits`, and `maximumFractionDigits`. That stuff is trivial to implement when using `Intl`, but harder to do with raw strings.

    1. Because we also want to accept user-entered number in other contexts, besides the cell values

        For editing a cell, we'll likely never need access to the _numerical value_ of the cell on the front end (beyond the need to format the number for display). But we will need access to numerical values of user input on the front end in the future. For example, when/if we allow the user to configure the minimum number of fraction digits, I'd want to take that user input and feed it back into `Intl.NumberFormat` to display a formatted preview of a sample number. I think we'd also want client-side validation to ensure that `minimumFractionDigits` is within `0` and `20`, as required by `Intl.NumberFormat`.

### Formatting

- The front-end formats numbers for display in the browser's locale.

- Values from the API are formatted (to satisfy Goal D), and values from the user are formatted as the user types (to satisfy Goal E). In both of these cases we begin with a string.

- When the front end can parse the input into a `number` or `BigInt`, it uses `Intl.NumberFormat` for formatting, which allows robust handling of grouping separators across various locales.

- When the front end cannot parse the canonical stringified number, it falls back to a simplistic formatter which only performs string transformation to ensure only that the decimal separator matches the user's locale. This produces a formatted result which lacks grouping separators, partially sacrificing Goal D.

### UX

- The front-end allows users to enter the Postgres numbers `NaN`, `-Infinity`, and `Infinity` using a context menu -- and it displays those numbers stylized (similar to `NULL`).

- While the user is entering a number, Mathesar _partially_ reformats the user's entry in order to match the final display of the number as closely as possible (to satisfy Goal E). For example, with a "en-US" locale, the entry `1234` is reformatted to `1,234` as the user types. However, some entries cannot be _fully_ reformatted as the user types. For example, an entry of `1.` would be fully formatted to `1` but must preserve the trailing decimal so that the user may type additional characters.

    After the user shifts focus away from the number input, Mathesar _fully_ reformats their entry. For example, `1.` will be reformatted to `1` (removing the trailing zero).

### Scientific notation

- To satisfy Goal F, Mathesar delegates to the front-end the responsibility to decide between displaying a number in standard notation or scientific notation.

    The algorithm for making this decision is as follows.
    
    - If the front-end cannot parse the number, then it retains the notation used in the stringified number.
    - If the front-end can only produce a `BigInt`, then it will use standard notation because: (a) `Intl.NumberFormat` is not capable of accurately formatting very large `BigInt` values due to its upper limit on `maximumFractionDigits` of `20`, and (b) standard notation makes it clearer to the user that the value is an integer.
    - If the front-end can produce a `number`, then it will use some yet-to-be-determined heuristics to make a best guess as to whether the user would prefer to see the number in standard notation or scientific notation.

### Loss of precision

- To satisfy Goal C, Mathesar delegates responsibility to the back-end for transforming precise values entered by the user into less-precise values stored by Postgres. The front-end does not attempt any rounding or truncation. The back-end responds with the value saved in Postgres and the front-end displays this value. At this point, it is the responsibility of the user to notice that their value has been rounded or truncated. (This behavior is consistent with `psql`, spreadsheets, and AirTable.)

## Future consideration

- At some point we may add display options for numbers, which allow users to customize things like: percentages, minimum fraction digits, maximum fraction digits, parentheses for negative numbers, forcing scientific notation on/off, forcing grouping separators on/off.
