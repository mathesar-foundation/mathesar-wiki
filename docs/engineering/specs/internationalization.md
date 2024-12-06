# Internationalization of Mathesar Codebase

## Language Detection & Language Switcher

The `selected_language` will be stored inside the DB and sent to the front end inside the `common_data`. For a particular user when there is no `selected_language` stored, the backend will detect the language from the `Accept-Language` HTTP header with a fallback to `en`.

The logged-in user will have a language switcher with a list of all of the currently supported languages by Mathesar. This option will be provided on the user profile page available at `/profile` path. Selecting a new language from here will make an API call to the backend to update the `selected_language` in the DB.

## Enabling codebase to be translated

### Translating client-side rendered pages

We will be using the [typesafe-i18n](https://github.com/ivanhofer/typesafe-i18n) library's [svelte adapter](https://github.com/ivanhofer/typesafe-i18n/tree/main/packages/adapter-svelte). This provides [type-aware](https://github.com/ivanhofer/typesafe-i18n#typesafety) translation usage across the codebase.

**Reasons for choosing typesafe-i18n**

1. First-class type safety
2. Official Svelte adapter
3. Built-in Async loading
4. Built-in Export functionality

**Other libraries considered & reasons for rejections**

[svelte-i18n](https://github.com/kaisermann/svelte-i18n)

1. In-frequent updates
2. Inferior type awareness as compared to typesafe-i18n

[tolgee](https://tolgee.io/integrations/svelte)

1. Inferior type awareness as compared to typesafe-i18n
2. Their more interesting offering is the translations management platform, which is paid after a certain number of strings even for open source.

**Bundle size impact & loading the translations files**

The bundle footprint of the suggested library is [low](https://github.com/ivanhofer/typesafe-i18n#sizes). ~2KB Gzipped.

Translations files will be loaded in parallel with the FE code. There are two approaches to it:

1. Detecting the language and adding the translations for that language in the common_data. But this will lead increase in the size of the common_data since the translations will grow with time.
2. Loading the translations via a script tag. This will require having a global loader in the index.html which gets hidden once the translations are loaded.

The final approach will be decided during the implementation and the tech spec will be updated accordingly.

**Translation inside the components**

The [typesafe-i18n](https://github.com/ivanhofer/typesafe-i18n) library's [svelte adapter](https://github.com/ivanhofer/typesafe-i18n/tree/main/packages/adapter-svelte) sets up svelte stores to store the translations strings, locale, etc. The two main stores are:

1. `LL` to translate strings inside a component. `{$LL.HELLO({ name: 'world' })}`.
2. `locale` to get the current locale. `$locale`

It also exports a function to update the locale in the store.
`setLocale` to update the current locale.

**Where will the translation file be stored?**

Translations files will be stored inside `mathesar_ui`. The structure will be:

```
i18n
  en
    index.ts
  fr
    index.ts
```

**Translating RichText and strings with embedded components**

Throughout the codebase, there are a lot of strings that contain components embedded inside them. Translating them becomes tricky, here is how we'll do it:

Consider,

```json
"welcomeMessage": "Welcome, {name}! Click {on-this-component} or {on-this-span} to continue!"
```

the usage could be simplified to:

```svelte
<RichText text={t('welcomeMessage', {name})} let:activeSlot>
  {#if activeSlot === 'on-this-component'}
    <Component/>
  {:else if activeSlot === 'on-this-span'}
    <span>some content</span>
  {/if}
</RichText>
```

`RichText` would only parse the result of the translated string, i.e. it will not perform any translation within it. It would be a general-purpose component that gets a string and replaces placeholders with its slot content.

The RichText component would parse the string, identify placeholders, split it, and render it as an array or arrays, rendering them with slots passing down the `activeSlot` property. This allows us to use both Components or DOM elements as we see fit.

The `RichText` component would look something like this.

```svelte
<script>
  export let text: string;
  // text would contain `Welcome, DemonLord! Click {on-this-component} or {on-this-span} to continue!`

  ...

  $: splitText = parse(text);
  /** The text would be parsed, and split to return something like:
    * [
    *   ["Welcome, DemonLord! Click ", "on-this-component", " or "],
    *   ["", "on-this-span", " to continue!"]
    * ]
    */
</script>

{#each splitText as [prefix, slotname, postfix]}
  {prefix}<slot activeSlot={slotname}/>{postfix}
{/each}
```

**Standards for creating keys**

1. Immutable strings will be used as keys for translations.
2. All such keys will be in `camelCase`.

**Translations inside the components library**

Some components inside the component library that has some strings hard-coded inside them. E.g. `FileUpload.svelte`. We will refactor such components to accept those strings as props or slots (with English strings hard-coded in the component as defaults)

**Plurals/Formatting(date, time, currency, etc...)**

The [typesafe-i18n](https://github.com/ivanhofer/typesafe-i18n) library supports this on the client side using [formatters](https://github.com/ivanhofer/typesafe-i18n/tree/main/packages/formatters)

Ex:

```typescript
Delete {labeledCount(selectedRowIndices, 'records', {
  casing: 'title',
  countWhenSingular: 'hidden',
})}
```

Using the message format from the typesafe-i18n lib

```svelte
<script>
const translations = {
  //                                        singular | plural
  deleteRecords: "Delete {{1 record | ?? record}}"

  // There are other formats possible: {{zero|one|two|few|many|other}}
  // See the full list here: https://github.com/ivanhofer/typesafe-i18n/tree/main/packages/runtime#plural
}

console.log(LL.deleteRecords(1)) // Delete record
console.log(LL.deleteRecords(2)) // Delete 2 records
</script>
```

Translations services like Transifex have a very user-friendly UI to show this to the translators: https://help.transifex.com/en/articles/6231958-working-with-plurals-and-genders#h_51e09ec18a

### Translating server-side rendered pages & API error messages

Our application has a few pages being rendered by the Django templating engine. To support localization in those templates:

Use the Django translations mechanism for templates and other backend-related translations including but not limited to API error messages that are shown on the UI as it is. This will lead to two separate translations file which should be fine. Both of the files(server-generated and client generated) can be uploaded to the translations service. This will be somewhat similar to i18next's namespaces approach. The benefits that we get here are two folds:

1. Using the Django translations with Django templates is very straightforward and we do not need to do any JS trickery to use the npm installed typesafe-i18n version inside the templates.
2. We also get translations for the API error messages. Also, note that most of the framework-generated error messages are already translated by the respective package. For ex: https://www.django-rest-framework.org/topics/internationalization/.

**Error messages generated by the Postgres**

Some of the error messages are being generated by Postgres directly. Translating them will not be part of this project due to the high effort and complexity.

### Working with translations

**Getting the translations**

There are multiple ways to do this:
| Property | Language Service Provider | Freelance Translators | Machine Translations |
| -------------- | -------------------------- | ------------------------- | ----------------------------------------------------------------------------- |
| Accuracy | Provides the most accuracy | Fairly accurate | Least accurate, especially for longer sentences. Majorly has grammatical errors |
| Ease of access | Takes time to find one | Relatively easier to find | Google translate. |
| Cost | Very costly relatively | Costly | Mostly free |

There is one more approach called the "Hybrid approach" where to avoid getting hit on the developer velocity, developers get the translations they need using the Machine translations strategy. The translation files are still sent to a translator but only according to a schedule(let's say once a month).

**Automated workflow for integrating new translations**

This section describes the approach to automating the process of sending the strings to be translated to the translator and integrating the response back into the codebase.

We can use [Transifex](https://www.transifex.com/open-source/) for this automation:

1. The file [exported](https://github.com/ivanhofer/typesafe-i18n/tree/main/packages/exporter) with all the strings can be uploaded to Transifex using its GitHub sync feature.
2. Add the languages that need we need the translations in and invite translators.
3. Submitted translations can be reviewed and finally integrated back into the codebase automatically using [Transifex's GitHub integration](https://help.transifex.com/en/articles/6265125-github-via-transifex-ui).

Other options:

1. [Lokalise](https://lokalise.com/) has a free plan for open-source projects.
2. [Inlang] also has a free tier for open-source projects.

**Translations update workflow**

Any change in the base language(English) text will require the developer to notify the translator via the translation service([Transifex](https://transifex.com/)). This will be part of the developer docs as well as the guidelines for translators mentioned in the project [proposal](/projects/internationalization).

### Development Tooling

**Linting**
A new eslint rule will be written as part of this project to help identify untranslated strings.

The rule would work like this:

1. Any raw text longer than 2 characters occurring directly in the Svelte template is an error.
2. Also, any string in JS that looks like UI text is an error.

**Plugin for VS code to work with translations**
https://github.com/lokalise/i18n-ally

## Localized URLs

Generally seems to be used very rarely. There are problems like checking URLs for unsupported symbols, the complexity of the routes and code, broken links, and having the slugs for all supported locales at all times in the codebase.
Hence, is out of the scope of this project.
