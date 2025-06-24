# Pavish's work log

# Working on:
* I18n project - translating the app

# Soon
* Set up calls for Product "big picture" meetings
* Clean up django migration scripts

# Later
* Figure out E2E testing strategy and user flows
  - Test Cypress as a possible tool to use (Playwright is still my choice at the moment)
  - Come up with a docker setup for E2E tests
  - Come up with user flows

# Daily logs
## 2023-12-06 Wednesday
* Raised [PR translating '/src/components/'](https://github.com/mathesar-foundation/mathesar/pull/3337)
* Quick call with Sean to resolve review comments
* Started work on translating 'src/systems'
* Responded to [Add loading and error indications in the database page](https://github.com/mathesar-foundation/mathesar/issues/3330)

## 2023-12-05 Tuesday
* i18n work
  * Continued translating app
* Ticket approval meeting

## 2023-12-04 Monday
* i18n work
  * Raised [PR for replacing old eslint svelte plugin with new official one](https://github.com/mathesar-foundation/mathesar/pull/3334)
  * Continued translating app
* Re-reviewed and merged [Handle failed API requests on schema page](https://github.com/mathesar-foundation/mathesar/pull/3323)
* Recorded video to clarify issue [#2123](https://github.com/mathesar-foundation/mathesar/issues/2123)

## 2023-12-01 Friday
* Continued i18n work
* Design session call

## 2023-11-30 Thursday
* Raised [PR for DB connections UI](https://github.com/mathesar-foundation/mathesar/pull/3326)
* Sent mail on design issues to address in DB connections UI
* Created issues:
  - [Frontend followup work on Database connections UI](https://github.com/mathesar-foundation/mathesar/issues/3328)
  - [Internal server error when database connection fails](https://github.com/mathesar-foundation/mathesar/issues/3329)
  - [Add loading and error indications in the database page](https://github.com/mathesar-foundation/mathesar/issues/3330)
* Repo admin work

## 2023-11-29 Wednesday
* Continued work on DB connections UI
* Call with Brent
* Call with Kriti
* Repo admin work

## 2023-11-28 Tuesday
* Re-reviewed and requested changes in [Handle failed API requests on schema page](https://github.com/mathesar-foundation/mathesar/pull/3323)
* Continued work on DB connections UI
* Repo admin work

## 2023-11-27 Monday
* Reviewed and requested changes in [Added Focus styles to Schema Row, Table Row and Buttons](https://github.com/mathesar-foundation/mathesar/pull/3313)
* Reviewed and merged [Fixed formatting strings for timestampsWithTZ](https://github.com/mathesar-foundation/mathesar/pull/3325)
* Reviewed and requested changes in [Handle failed API requests on schema page](https://github.com/mathesar-foundation/mathesar/pull/3323)
* Repo admin work
* Team meeting

## 2023-11-24 Friday
* Started working on DB connections UI
* Repo admin work

## 2023-11-23 Thursday
* Went through [Connections PR](https://github.com/mathesar-foundation/mathesar/pull/3309), and fixed breaking frontend changes
* Call with Ghislaine
* Added Transifex integration config and more notes in the [Django i18n PR](https://github.com/mathesar-foundation/mathesar/pull/3321)

## 2023-11-22 Wednesday
* Caught up on emails and chats, updated email address to mathesar.org domain
* Raised [PR for django translations and instructions for maintainers](https://github.com/mathesar-foundation/mathesar/pull/3321)
* Weekly team meeting
* Took a look at [Connections API PR](https://github.com/mathesar-foundation/mathesar/pull/3309)

## 2023-11-20 Monday & 2023-11-21 Tuesday
* I was out sick

## 2023-11-17 Friday
* Responded to [orderable field issue](https://github.com/centerofci/mathesar/issues/3066)
* Responded to [Add focus indications issue](https://github.com/centerofci/mathesar/issues/2837)
* Renewed certificate for staging.mathesar.org
* Added commits to update roles in [website update PR](https://github.com/mathesar-foundation/mathesar-website/pull/97)
* Responded to mail for visiting researchers from Henkaku center
* Chat & call with Sean on me picking up some of the DB Connections work
* 1:1 with Kriti

## 2023-11-16 Thursday
* Pondered a bit more on permissions and workspaces
* Design sessions call

## 2023-11-15 Wednesday
* Call with Brent
* Responded to work check-in email
* Got [Replace typesafe-i18n with svelte-i18n PR](https://github.com/centerofci/mathesar/pull/3302) ready for review

## 2023-11-14 Tuesday
* Prepared proposal for PGConf India 2024
  - Got it reviewed from Kriti
  - Submitted proposal
* Spent some time thinking about permissions and workspaces

## 2023-11-13 Monday
* Call with Kriti on end-to-end workflow for translations
* Continued work on cleaning up [Replace typesafe-i18n with svelte-i18n PR](https://github.com/centerofci/mathesar/pull/3302)
* Did some searches for conferences we could attend

## 2023-11-10 Friday
* Thought more about processes around translation
* Researched other open-source products using transifex
* Community team event

## 2023-11-09 Thursday
* Cleaned up en & jp svelte translation files, added some more translations
* Linked GH repo in Transifex and point to the en & jp json files to test it out
* Responded to review email for 'Bidirectional Navigation Between Table and Explorations'
* Call with Ghislaine

## 2023-11-08 Wednesday
* Responded to Brent's email on installations
* Core team meeting
* Call with Adam
* Continued i18n work

## 2023-11-07 Tuesday
* Continued i18n work
  - Decided to replace typesafe-i18n with a library that supports the [ICU format](https://unicode-org.github.io/icu/userguide/icu/i18n.html)
    - Raised [a draft PR with svelte-i18n](https://github.com/centerofci/mathesar/pull/3123) and added utilities to handle our existing customizations
    - Long call with Sean to see if he had any objections as he involved in the i18n project spec

## 2023-11-06 Monday
* Raised [PR to simply Dockerfile and dev compose file](https://github.com/centerofci/mathesar/pull/3295)
* Continued i18n work
  - Continued figuring out automation workflow 
  - Chat with Kriti on ordering translations
* Created an issue to track [cleaning up migration scripts](https://github.com/centerofci/mathesar/issues/3296)

## 2023-11-03 Friday
* I18n work
  - Continued figuring out approach to integrate with GH actions
  - Chat with Brent on separate dev Dockerfile
  - Chat on cleaning up backend migrations
* 1-1 with Kriti

## 2023-11-02 Thursday
* Reviewed UX for DB connections page, responded to Ghislaine's email
* Continued looking through pending i18n work
  - Started figuring out ways to make existing approach cleaner

## 2023-11-01 Wednesday
* Core team meeting
* User call retrospective meeting
* Started looking at i18n work to assess what's pending

# Archive
 - [October 2023 work logs](/archive/team/workflow/worklogs/archive/2023-10/pavish)
 - [September 2023 work logs](/archive/team/workflow/worklogs/archive/2023-09/pavish)
 - [August 2023 work logs](/archive/team/workflow/worklogs/archive/2023-08/pavish)
 - [July 2023 work logs](/archive/team/workflow/worklogs/archive/2023-07/pavish)
