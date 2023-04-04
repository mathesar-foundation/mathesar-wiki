---
title: Localization Project
description:
published: true
date: 2023-03-15T00:00:00.000Z
tags:
editor: markdown
dateCreated: 2023-03-15T00:00:00.000Z
---

- **Name**: Localization
- **Status**: In-Review

## Team

**Project Owner:** Rajat

|               | Workers | Reviewers |
| ------------- | ------- | --------- |
| **UX design** | Rajat   | Ghislaine |
| **Front end** | Rajat   | Sean      |
| **Back end**  | Mukesh  | _TODO_    |

## Problem

Currently, Mathesar has hardcoded English strings and only works for the English language. It should be enabled to support any language.

## Solution

### Language Detection

_TODO_

**Language Switcher**

### Translations

**Client-side rendered pages**

We will be using the [typesafe-i18n](https://github.com/ivanhofer/typesafe-i18n) library's [svelte adapter](https://github.com/ivanhofer/typesafe-i18n/tree/main/packages/adapter-svelte). This provides [type-aware](https://github.com/ivanhofer/typesafe-i18n#typesafety) translation usage across the codebase.

**Translation inside the components**

The [typesafe-i18n](https://github.com/ivanhofer/typesafe-i18n) library's [svelte adapter](https://github.com/ivanhofer/typesafe-i18n/tree/main/packages/adapter-svelte) setups stores to store translations strings, locale, etc. The two main stores are:

1. `LL` to translate strings inside a component. `{$LL.HELLO({ name: 'world' })}`.
2. `locale` to get the current locale. `$locale`

It also exports a function to update the locale in the store.
`setLocale` to update the current locale.

**Where will the translation file be stored?**

Translations files will be stored in the frontend repo. The structure will be:

```
i18n
  en
    index.ts
  fr
    index.ts
```

**If the message strings need to be sent to a translator**

The [typesafe-i18n](https://github.com/ivanhofer/typesafe-i18n) supports [exporting](https://github.com/ivanhofer/typesafe-i18n/tree/main/packages/exporter) whose output can either be sent to a third-party translations service, LSP, or downloaded as a csv/json file.

**Bundle size impact**

The bundle footprint of the suggested library is [low](https://github.com/ivanhofer/typesafe-i18n#sizes). ~2KB Gzipped.
The translation files will be [loaded asynchronously](https://github.com/ivanhofer/typesafe-i18n/tree/main/packages/generator#asynchronous-loading-of-locales) to avoid increasing the bundle size.

**Plurals/Formatting(date, time, currency, etc...)**

The [typesafe-i18n](https://github.com/ivanhofer/typesafe-i18n) library supports this on the client side using [formatters](https://github.com/ivanhofer/typesafe-i18n/tree/main/packages/formatters)

**Server-side rendered pages**

Our application has a few pages being rendered by the Django templating engine. To support localization in these templates there are two ways

1. Django already has good support for [translations](https://docs.djangoproject.com/en/4.1/topics/i18n/translation/#compiling-message-files). It also has the utilities for generating message files for new languages and compiling the translated message files back. In this method, we use the same message/compiled files to store the translations for both the server-side rendered pages as well as the client-side rendered pages. In this way, we lose the type-aware capabilities of the typesafe-i18n lib.
2. Another approach is to separate the translation files for the server and the client. The only reason why this approach could be feasible is that we have very minimal translatable strings on the server(only the non-auth pages). But this approach lets us leverage the type-aware capabilities of the typesafe-i18n lib. We can also have some Github checks using Github actions to warn if we somehow forgot to translate the server string and only translated the client strings.

I suggest the second approach. I can write it in more detail once we finalize the approach.

**Getting the translations**

There are multiple ways to do this:
| Property | Language Service Provider | Freelance Translators | Machine Translations |
| -------------- | -------------------------- | ------------------------- | ----------------------------------------------------------------------------- |
| Accuracy | Provides the most accuracy | Fairly accurate | Least accurate, especially for longer sentences. Majorly has grammatical errors |
| Ease of access | Takes time to find one | Relatively easier to find | Google translate. |
| Cost | Very costly relatively | Costly | Mostly free |

There is one more approach called the "Hybrid approach" where to avoid getting hit on the developer velocity, developers get the translations they need using the Machine translations strategy. The translation files are still sent to a translator but only according to a schedule(let's say once a month).

### Localized URLs

Generally seems very rare. There are problems like checking URLs for unsupported symbols, the complexity of the routes and code, broken links, and having the slugs for all supported locales at any particular point in time.
Hence, is out of the scope of this project.

### Other libraries considered & reasons for rejections

[svelte-i18n](https://github.com/kaisermann/svelte-i18n)

1. In-frequent updates
2. Inferior type awareness as compared to typesafe-i18n

[tolgee](https://tolgee.io/integrations/svelte)

1. Inferior type awareness as compared to typesafe-i18n
2. Their more interesting offering is the translations management platform, which is paid after a certain number of strings even for open source.

### Development Tooling

Plugin for VS code: https://github.com/lokalise/i18n-ally

## Timeline

This project should take 4 weeks.

## Risks

There are no language-specific risks since the goal of this project is not to provide support for some particular language but to enable Mathesar to support multiple languages.
