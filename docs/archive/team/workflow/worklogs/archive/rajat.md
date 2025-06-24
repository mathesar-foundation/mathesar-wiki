# Rajat's work log

**TODO**

- Create an ESLint rule to catch all untranslated strings & fix all the current errors. [i18n](https://github.com/centerofci/mathesar/issues/2927)
- Review [add cell tab in table inspector for showing cell content](https://github.com/centerofci/mathesar/pull/2778)
- Wrapping raw strings with translation function in the whole codebase's PR update.
- Start an email thread on the dev mailing list for the i18n retrospective _(actively writing)_
- Pending i18n Documentations. [i18n](https://github.com/centerofci/mathesar/issues/2927)
- i18n testing

## 2023-10-23

- Repo-admin work
- Made some progress on: Create an ESLint rule to catch all untranslated strings & fix all the current errors. [i18n](https://github.com/centerofci/mathesar/issues/2927)
  - Rewriting rules from [no-literal-string](https://github.com/edvardchen/eslint-plugin-i18next/blob/main/lib/rules/no-literal-string.js) to be able to run on `svelte-eslint-parse`

## 2023-10-20

- Repo-admin work
- Made some progress on: Create an ESLint rule to catch all untranslated strings & fix all the current errors. [i18n](https://github.com/centerofci/mathesar/issues/2927)
  - Rewriting rules from [no-literal-string](https://github.com/edvardchen/eslint-plugin-i18next/blob/main/lib/rules/no-literal-string.js) to be able to run on `svelte-eslint-parse`

## 2023-10-19

- Repo-admin work
- Made some progress on: Create an ESLint rule to catch all untranslated strings & fix all the current errors. [i18n](https://github.com/centerofci/mathesar/issues/2927)
  - Finally able to run [no-raw-text](https://github.com/intlify/eslint-plugin-svelte/blob/main/lib/rules/no-raw-text.ts) rule from the local
  - Started reading about `svelte-eslint-parser` to understand how it works and how to make it work with new rules.

## 2023-10-18

- Repo-admin work
- Made some progress on: Create an ESLint rule to catch all untranslated strings & fix all the current errors. [i18n](https://github.com/centerofci/mathesar/issues/2927)
  - Struggling to run [no-raw-text](https://github.com/intlify/eslint-plugin-svelte/blob/main/lib/rules/no-raw-text.ts) rule from the local

## 2023-10-17

- Partially available
- Repo-admin work

## 2023-10-16

- Out sick

## 2023-10-13 (Running svelte plugin on the local)

- Repo-admin work
- Made some progress on: Create an ESLint rule to catch all untranslated strings & fix all the current errors. [i18n](https://github.com/centerofci/mathesar/issues/2927)
  - Trying to run [no-raw-text](https://github.com/intlify/eslint-plugin-svelte/blob/main/lib/rules/no-raw-text.ts) rule from the local so that its easier to make edits and test it.

## 2023-10-12

- Repo-admin work
- Made some progress on: Create an ESLint rule to catch all untranslated strings & fix all the current errors. [i18n](https://github.com/centerofci/mathesar/issues/2927)
  - Finding an existing plugin that does anything close to the requirement.
  - The closest one that I could find - [no-literal-string](https://github.com/edvardchen/eslint-plugin-i18next/blob/main/lib/rules/no-literal-string.js)
  - The plan is to extend the [existing svelte plugin](https://github.com/intlify/eslint-plugin-svelte/blob/main/lib/rules/no-raw-text.ts) to accommodate rules from [no-literal-string](https://github.com/edvardchen/eslint-plugin-i18next/blob/main/lib/rules/no-literal-string.js)

## 2023-10-11

- Repo-admin work
- Made some progress on: Create an ESLint rule to catch all untranslated strings & fix all the current errors. [i18n](https://github.com/centerofci/mathesar/issues/2927)
  - Started researching on how to write ESLint plugin

## 2023-10-10

- Repo-admin work
- Minor [fixes](https://github.com/centerofci/mathesar/pull/3223/commits/cb0857297a5189130a1ee7b0806bf17b76fe35a9) in [Db connection UI](https://github.com/centerofci/mathesar/pull/3223). The PR is approved but blocked on missing doc links.

## 2023-10-09

- Repo-admin work
- Synced with Mukesh regarding missing links in database ui PR.
- Replied to retro e-mail for the last cycle.
- Tackled review feedback & made ready for review - [[i18n] Load "en" translations parallely](https://github.com/mathesar-foundation/mathesar/pull/3102)

## 2023-10-06

- Worked on review feedback for - [[i18n] Load "en" translations parallely](https://github.com/mathesar-foundation/mathesar/pull/3102)

## 2023-10-05

- Tackle Review feedback for [Db connection UI](https://github.com/centerofci/mathesar/pull/3223) & made ready for review again

## 2023-10-04

- Made some progress on: Wrapping raw strings with translation function in the whole codebase's PR update. This needs some more work due to more development after last changes on this PR.

## 2023-10-03

- Made some progress on: Wrapping raw strings with translation function in the whole codebase's PR update. This needs some more work due to more development after last changes on this PR.

## 2023-10-02

- [Db connection UI](https://github.com/centerofci/mathesar/pull/3223) ready for review
- Repo-admin work

## Archive

- [September 2023 work logs](./2023-09/rajat.md)
- [August 2023 work logs](./2023-08/rajat.md)
- [July 2023 work logs](./2023-07/rajat.md)
