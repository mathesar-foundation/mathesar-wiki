# Sean's work log

## TODO

### Review

- Review [Pavish: Upgrade node](https://github.com/centerofci/mathesar/pull/3214)
- Review [Rajat: Export & import translations](https://github.com/centerofci/mathesar/pull/3123)
- Review [Anshuman: Excel import docs](https://github.com/centerofci/mathesar/pull/3204)
- Review [Fidal: Close record selector on overlay](https://github.com/centerofci/mathesar/pull/3220)

### Soon

- Set up 1/1 with Anshuman and figure out who is going to help with with design and UI
- Help find work for Anish
- Start email thread about internal CRM
- [Refactor CellSelection data structure and store](https://github.com/centerofci/mathesar/pull/3037)
- [2023-08 Front end work](https://github.com/centerofci/mathesar/issues/3150)

### Backlog

- Figure out what to do with [wiki sync PR](https://github.com/centerofci/mathesar-wiki/pull/103)
- Research [i18n Ally](https://marketplace.visualstudio.com/items?itemName=Lokalise.i18n-ally) to see if we can use it to navigate to base translation source
- [Investigate Supabase integration](https://github.com/centerofci/mathesar/issues/3141)
- Begin "User Communication Guide", as a wiki page
- Comment on or about [Cannot import large csv tables](https://github.com/centerofci/mathesar/issues/2995)
- Resolve [front end code standard prohibiting usage of events on components](https://github.com/centerofci/mathesar/pull/3191)
- PR to add docs on running front end in prod mode
- PR to add docs on loading sample data

--------------------------------------------------------------------------------

## 2023-09-25 Monday

- 1/1 with Pavish
- Some thinking on product direction
- Review [Mukesh: install docs](https://github.com/centerofci/mathesar/pull/3212)
- Review [Pavish: column descriptions](https://github.com/centerofci/mathesar/pull/3219)
- 1/1 with Kriti

## 2023-09-22 Friday

*(Out due to two sick kids)*

## 2023-09-21 Thursday

*(Partial day due to one sick kid)*

- 1/1 with Brent
- Sync with Ghislaine and Pavish re: niche
- Review [Mukesh: installation docs](https://github.com/centerofci/mathesar/pull/3212)

## 2023-09-20 Wednesday

*(Out due to two sick kids)*

## 2023-09-19 Tuesday

*(Partial day due to two sick kids)*

- 1/1 with Mukesh
- Try removing all event listeners from cell-related components to see if it improves performance.
- Troubleshooting running the front end in prod mode
- Some smaller discussions

## 2023-09-18 Monday

*(Partial day due to two sick kids)*

- 1/1 with Rajat
- Sync with Brent and Dom about API for pasting data into cells
- 1/1 with Dom
- Several smaller discussions on Matrix
- Review [docs: Add troubleshooting guide link](https://github.com/centerofci/mathesar/pull/3210#pullrequestreview-1631836244)

## 2023-09-15 Friday

- Attend community event
- Some chat with community members in Matrix General
- Some tinkering with baby steps towards building an internal Mathesar [CRM instance](https://internal.mathesar.org/db/mathesar_tables/522/tables/2194/)
- Briefly look into [Handle API errors on schema page](https://github.com/centerofci/mathesar/pull/2829) to help answer [question](https://matrix.to/#/!UnujZDUxGuMrYdvgTU:matrix.mathesar.org/$p6PuoNBhBjZHicNXnVgP9A-4YXLNYlW6ISnOKWo50gY?via=matrix.mathesar.org&via=matrix.org) from Rajat
- Some continued work on JS table rendering performance research
- Some continued work on CellSelection
- Some smaller discussions

## 2023-09-14 Thursday

*(Shorter due to headache)*

- Review Ghislaine's niche research report
- 1/1 with Ghislaine re: niche research project
- Some continued work on JS table rendering performance research
- Cleanup of some tickets

## 2023-09-13 Wednesday

*(Out due to sick kid)*

## 2023-09-12 Tuesday

*(Half day due to sick kid)*

- Spend a little time profiling JS perf with table page rendering to get a rough sense of where our bottle necks are.
- 1/1 with Mukesh
- Survey work meeting
- Wordsmith [options](https://hackmd.io/MCqmgnH9TymhKfj3L0fYJg?both) for survey

## 2023-09-11 Monday

- Push some more commits to my [CellSelection PR](https://github.com/centerofci/mathesar/pull/3037)
- Open ticket [Reactivity problem with cell value in Data Explorer table inspector](https://github.com/centerofci/mathesar/issues/3205)
- 1/1 with Rajat
- Some time exploring MotherDuck product

## 2023-09-08 Friday

- Some smaller team management check-ins and follow-ups
- Several small discussions
- Partial 1/1 with Rajat
- Re-review [[i18n] Save preferred\_language for auth user in db](https://github.com/centerofci/mathesar/pull/3103)
- Re-review [[i18n] Language switcher for anon users](https://github.com/centerofci/mathesar/pull/3104)
- Review community PR [fix: cell loses focus when clicking on its outline](https://github.com/centerofci/mathesar/pull/3185)
- 1/1 with Ghislaine
- Review [Dont show "Go to Record Page" for error rows](https://github.com/centerofci/mathesar/pull/3114)

## 2023-09-07 Thursday

- A number of smaller team management tasks
- 1/1 with Anish
- 1/1 with Mukesh
- Review copy in [DB config UI](https://www.figma.com/file/xHb5oIqye3fnXtb2heRH34/Styling?type=design&node-id=6075-18452&mode=design&t=kz3pGsUL09ZqMmdS-0#549330977), commenting in Figma, and starting a [discussion](https://matrix.to/#/!UZILDSNKobkelUYwBp:matrix.mathesar.org/$jEGirwFlqkfARDdA1GvJ3eQTwqa38fSKWuonv31_JFA?via=matrix.mathesar.org&via=matrix.org) on Matrix.
- Finish and send critique of user survey
- Some minor clean up in some tickets and PRs
- Review docs changes in [Remove db superuser requirement](https://github.com/centerofci/mathesar/pull/3117)

## 2023-09-06 Wednesday

- Catch up on emails
- Some prep work for team meeting
- Team meeting
- 1/1 with Pavish
- Re-review user survey and begin drafting response

## 2023-09-05 Tuesday

*(Vacation day)*

## 2023-09-04 Monday

*(Out for US holiday)*

## 2023-09-01 Friday

- Team event
- Discuss scheduling of niche research meeting with Pavish and Ghislaine
- Push more commits to my Cell Selection refactor PR

## 2023-08-31 Thursday

- Brief team-management-related check-ins with Brent, Pavish, Ghislaine, Anish, Rajat
- Open ticket [Configure code formatting for Markdown within docs and wiki sites](https://github.com/centerofci/mathesar/issues/3194)
- Raise [mdformat bug](https://github.com/executablebooks/mdformat/issues/413) preventing us from using it
- Publish [Markdown Style Guide](https://wiki.mathesar.org/engineering/markdown/)
- Send [Markdown syntax](https://groups.google.com/a/mathesar.org/g/mathesar-developers/c/7hAgMsWgMZw/m/xayJFNtvAgAJ) email
- Some continued work on Cell Selection refactor

## 2023-08-30 Wednesday

- Respond to "Avoiding regressions" email thread
- Respond to "Product level permissions to account for related entities" thread
- 1/1 with Brent
- Write [script to identify stale work logs](https://github.com/centerofci/mathesar-wiki/commit/74a5d48f7e27d6ad2e1d3188742c999dc1465675)
- Review "Quick User Check-in" survey, emailing critique
- Clean up [FE code standard PR](https://github.com/centerofci/mathesar-wiki/pull/93), moving it to a [draft PR](https://github.com/centerofci/mathesar/pull/3191) on the main repo.

## 2023-08-29 Tuesday

*(Shorter day due to some intermittent family demands throughout the day)*

- 1/1 with Mukesh
- Work on Sheet selection refactor
- 1/1 with Ghislaine
- Some smaller conversations
- Begin drafting response to "Avoiding regressions" thread

## 2023-08-28 Monday

- Chat with Rajat about upcoming tasks
- Review QA tickets opened by Brent, adding some comments
- Work on Markdown style guide
- Work on Sheet selection refactor

## 2023-08-25 Friday

- Review [Move UserProfile to the App level context from Route level context](https://github.com/centerofci/mathesar/pull/3175)
- Some prep work for team management while Kriti is away
- Push more commits to my draft [CellSelection PR](https://github.com/centerofci/mathesar/pull/3037)

## 2023-08-24 Thursday

- Address Review feedback in [Migrate wiki to MkDocs](https://github.com/centerofci/mathesar-wiki/pull/102)
- Handle deployment of new mkdocs wiki site
- Troubleshoot changes with CNAME file on wiki deployment
- 1/1 with Kriti
- Create ticket [Decommission Wiki.js server](https://github.com/centerofci/mathesar/issues/3173)
- Resume work on [Refactor CellSelection data structure and store](https://github.com/centerofci/mathesar/pull/3037)

## 2023-08-23 Wednesday

- Team meeting
- Bring PR to [Migrate wiki to MkDocs](https://github.com/centerofci/mathesar-wiki/pull/102) out of draft state

## 2023-08-22 Tuesday

- Resolve conflicts in [Refactor CellSelection data structure and store](https://github.com/centerofci/mathesar/pull/3037)
- Resolve conflicts in [Make column type inference optional](https://github.com/centerofci/mathesar/pull/3050)
- Address Kriti's feedback in [Make column type inference optional](https://github.com/centerofci/mathesar/pull/3050)
- Begin work to [Migrate wiki to MkDocs](https://github.com/centerofci/mathesar/issues/3079)

## 2023-08-21 Monday

- Troubleshoot some computer issues
- Discussions

## 2023-08-18 Friday

*(shorter day due to some kid stuff)*

- Update project page from previous cycle
- Team meeting
- Team event
- Some smaller discussions

## 2023-08-17 Thursday

- Catch up on several email and Matrix discussions
- Some cleanup of GitHub tickets

## 2023-08-16 Wednesday

- Call with Dom regarding priorities for cycle
- Organize front-end cycle work into [2023-08 Front end work](https://github.com/centerofci/mathesar/issues/3150) ticket
- Respond to "Package version management" email thread
- Respond to Brent's "installing stuff" email thread

## 2023-08-15 Tuesday

*(out sick)*

## 2023-08-14 Monday

*(out sick)*

## 2023-08-11 Friday

- Review [[i18n] Language switcher for anon users](https://github.com/centerofci/mathesar/pull/3104#pullrequestreview-1573587295)
- Continue [Discussion about active cell height design and regression](https://github.com/centerofci/mathesar/issues/3091)
- Read and mull over Brent's "install things" email. I have a lot to say about this, and I've already written a lot, but I'm not really sure how to respond in the thread, given how entrenched in our current approach the backend team already seems to be.
- Open ticket [Turn off the Stale Issues Bot](https://github.com/centerofci/mathesar/issues/3142)
- Identify high-priority issues for the cycle

## 2023-08-10 Thursday

- Team meeting
- Review [[i18n] Save preferred_language for auth user in db](https://github.com/centerofci/mathesar/pull/3103#pullrequestreview-1571895592)
- Write a response to Brent's "Should we install things on the DB" notes (not sent yet, since Brent hasn't begun the email thread).
- Poke my head into some of the SQL work going on the backend to take a look at it, as it relates to Brent's "Should we install things on the DB" thoughts


## 2023-08-09 Wednesday

- Team meeting
- Review [[i18n] RichText component](https://github.com/centerofci/mathesar/pull/3100#pullrequestreview-1570307778), adding some commits
- Open ticket [Flatten BaseTranslation object](https://github.com/centerofci/mathesar/issues/3137)
- Partially review [[i18n] Export & import translations](https://github.com/centerofci/mathesar/pull/3123)
- Review [[i18n] Load "en" translations parallely](https://github.com/centerofci/mathesar/pull/3102)

## 2023-08-08 Tuesday

*(Partial day due to sick kid)*

- Continue troubleshooting Docker issue
- Review [Shared queries - Auth handling for query requests, frontend consumer view, API tests](https://github.com/centerofci/mathesar/pull/3113)

## 2023-08-07 Monday

- Call with Dom re troubleshooting API weirdness
- Continue troubleshooting issues with weird errors. Try unsuccessfully to wipe out all my Docker state
- 1/1 with Kriti
- Bring optional [inference PR](https://github.com/centerofci/mathesar/pull/3050) out of draft state

## 2023-08-04 Friday

- Team event
- Some work on optional inference
- Some smaller discussions

## 2023-08-03 Thursday

- Some thinking about "niche" conversations and email thread
- Call with Ghislaine about use cases
- Some [discussion](https://matrix.to/#/!UnujZDUxGuMrYdvgTU:matrix.mathesar.org/$ZBG79ELY4prXkTqki5zKqZ68NQAXk_GscW0fG-V8Snc?via=matrix.mathesar.org&via=matrix.org) about how to prioritize front end work this cycle
- [Resolve](https://github.com/centerofci/mathesar/pull/3050/commits/b9177583a9699c2cf439ec8e47bb9e594df31075) tricky git conflicts in my optional inference PR due to i18n work
- Some work on optional inference

## 2023-08-02 Wednesday

*(Another short day)*

- Some work on optional inference
- Team meeting

## 2023-08-01 Tuesday

*(Only able to work a couple hr due to failed kid nap)*

- Some work on optional inference

## 2023-07-31 Monday

*(Half day)*

- [Discuss](https://matrix.to/#/!UnujZDUxGuMrYdvgTU:matrix.mathesar.org/$ElSJKdD-NZu-FTThS51fThj5eSYsGYq5gypqp_ilbLU?via=matrix.mathesar.org&via=matrix.org) front end issue with installing packages
- Review [[i18n] Install typesafe-i18n & translates one component](https://github.com/centerofci/mathesar/pull/3099) and email dev list about package issue
- Some work on optional inference
- Some smaller discussions

## 2023-07-30 Sunday

*(Some work during kids nap)*

- Matrix [discussion](https://matrix.to/#/!vXLxAqmrJWsDMWPSpo:matrix.mathesar.org/$9aqrfj-lyZJ_2LAV7csmqRLTWsmn-kqZR8W0dLI94XY?via=matrix.mathesar.org&via=matrix.org&via=t2bot.io) with user about feature requests

## 2023-07-28 Friday

*(half day)*

- Continue email discussion about user-reported tickets
- Help troubleshoot [Type suggestions broken](https://github.com/centerofci/mathesar/issues/3105)
- Send frontend fixes weekly project update email
- Continue troubleshooting [docker/npm problem](https://github.com/centerofci/mathesar/pull/3099#issuecomment-1655756340)
- Some progress continuing to review [[i18n] Install typesafe-i18n & translates one component](https://github.com/centerofci/mathesar/pull/3099)


## 2023-07-27 Thursday

- Open ticket [Type suggestions broken](https://github.com/centerofci/mathesar/issues/3105)
- Spend some time partially reviewing [[i18n] Install typesafe-i18n & translates one component](https://github.com/centerofci/mathesar/pull/3099#pullrequestreview-1550390792)
- Open email discussion about [Criteria for closing use-reported tickets](https://groups.google.com/a/mathesar.org/g/mathesar-developers/c/w9CskyV9r3s)
- Resolve merge conflicts in [Refactor CellSelection data structure and store](https://github.com/centerofci/mathesar/pull/3037)
- Push some more commits to my [optional inference PR](https://github.com/centerofci/mathesar/pull/3050)

## 2023-07-26 Wednesday

- Continue work on optional inference
- Team meeting
- Some smaller discussions

## 2023-07-25 Tuesday

- [Chat](https://matrix.to/#/!UnujZDUxGuMrYdvgTU:matrix.mathesar.org/$f5v5Bd_KRNHHVUN4HF-MK9AeV-qDo4uEeXcyYvHabr4?via=matrix.mathesar.org&via=matrix.org) about next steps for Rajat's [i18n PR](https://github.com/centerofci/mathesar/pull/3087).
- Review Pavish's [Shareable links frontend PR](https://github.com/centerofci/mathesar/pull/3093#pullrequestreview-1546069582)
- Push some more commits to my [optional inference PR](https://github.com/centerofci/mathesar/pull/3050)
- Read and respond to product strategy documents in preparation for Wednesday's meeting

## 2023-07-24 Monday

- Open ticket: [Discussion about active cell height design and regression](https://github.com/centerofci/mathesar/issues/3091)
- Review [Use Truncate component in Record Selector table cells](https://github.com/centerofci/mathesar/pull/3077/), pushing some additional commits and merging
- Begin [discussion](https://groups.google.com/a/mathesar.org/g/mathesar-developers/c/45M2ZxoN-Qg) about i18n project workflow
- Open PR to [Copy formatted cell values to clipboard instead of raw values](https://github.com/centerofci/mathesar/pull/3094)
- A small amount of work on optional inference

## 2023-07-21 Friday

- Respond to Ghislaine's ticket [Change in Behaviour of Sorting, Filtering, Grouping and Copy-Paste for Linked Records](https://github.com/centerofci/mathesar/issues/3080)
    - Create ticket: [Copying FK cells should copy the record summary instead of the PK value](https://github.com/centerofci/mathesar/issues/3085)
    - Create ticket: [Behavior when sorting FK columns may be confusing to users](https://github.com/centerofci/mathesar/issues/3084)
- Send weekly project update emails for frontend fixes project and my work within the backend fixes project
- Team meeting
- Continued work on optional inference, pushing some more commits to my [draft PR](https://github.com/centerofci/mathesar/pull/3050)

## 2023-07-20 Thursday

- Meet with Brent and Aritra about summarization functions
- Chat about wiki sync problems
- Create PR with [1 hour quick stab at migration to mkdocs](https://github.com/centerofci/mathesar-wiki/pull/99)
- Create issue [Migrate wiki to MkDocs](https://github.com/centerofci/mathesar/issues/3079)
- Continue working on [Make column type inference optional](https://github.com/centerofci/mathesar/issues/2358)

## 2023-07-19 Wednesday

- Team meeting
- Matrix chat with Kriti about some product design process stuff
- Help triage [Support for column descriptions/comments](https://github.com/centerofci/mathesar/issues/3069)
- Create ticket [Help users understand the connection between descriptions and PostgreSQL comments](https://github.com/centerofci/mathesar/issues/3071)
- Several other smaller discussions
- Push more commits to my draft [CellSelection PR](https://github.com/centerofci/mathesar/pull/3037), beginning to integrate new CellSelection code into TabularData class

## 2023-07-18 Tuesday

- Chat with Rajat about cell selection PR
- Help answer questions for community contributor working on [Use Truncate component in Record Selector table cells](https://github.com/centerofci/mathesar/issues/2345)
- Push more commits to my draft [CellSelection PR](https://github.com/centerofci/mathesar/pull/3037), filling in logic within the scaffolding

## 2023-07-17 Monday

- Open draft PR to [Make column type inference optional](https://github.com/centerofci/mathesar/pull/3050) and begin a discussion soliciting feedback from others
- Open ticket [Gracefully recover from failed type inference during import](https://github.com/centerofci/mathesar/issues/3051)
- Discuss [Refactor CellSelection data structure and store](https://github.com/centerofci/mathesar/pull/3037) with Pavish
- Address review feedback in [Clean up import docs](https://github.com/centerofci/mathesar/pull/3042) and merge
- Review [Scroll sheet all the way down when clicking the New Record button](https://github.com/centerofci/mathesar/pull/3045), adding another commit and merging

## 2023-07-14 Friday

- Send [project update email](https://groups.google.com/a/mathesar.org/g/mathesar-developers/c/GJIzUwk3Zs8)
- Review [Date Input closes now on tab](https://github.com/centerofci/mathesar/pull/3038)
- Call with Dom to discuss type inference issues and brainstorm solutions
- Open PR with [Small clean up to import help text code](https://github.com/centerofci/mathesar/pull/3041)
- Open PR to [Clean up import docs](https://github.com/centerofci/mathesar/pull/3042)
- Some progress to [Make column type inference optional](https://github.com/centerofci/mathesar/issues/2358)

## 2023-07-13 Thursday

- GSoC project meeting with Aritra
- Continued work on cell selection refactor
- Add some more content to my "Querydown for Mathesar devs" Gist, explaining [why I think "mandatory aggregation" is important](https://gist.github.com/seancolsen/42d5f3873e644e3905eaac0b69f876ac#why-i-think-mandatory-aggregation-is-important), with an example using the Data Explorer
- Minor [updates](https://github.com/centerofci/mathesar-wiki/commit/11b9cb8266b72d86718953eceb3ce44843e6c1ca) to [frontend fixes](/projects/2023/07/2023-07-frontend-fixes.md) project description

## 2023-07-12 Wednesday

- Open draft PR with scaffolding to [Refactor CellSelection data structure and store](https://github.com/centerofci/mathesar/pull/3037), and write a summary requesting Pavish and Rajat review the approach.

## 2023-07-11 Tuesday

- Re-review [Updated frontend to send a single bulk delete request instead of one request for each record](https://github.com/centerofci/mathesar/pull/2985)
- Re-review [Added margin between breadcrumb selector and bottom of the veiwport](https://github.com/centerofci/mathesar/pull/3014)
- Start discussion about [graceful fallback behavior for all unsupported Postgres data types](https://github.com/centerofci/mathesar/issues/3024)
- Review Varsha's [Sample schema file for API Documentation](https://groups.google.com/a/mathesar.org/g/mathesar-developers/c/invt1JTg7hk)
- Installation planning meeting
- Some progress writing code for [SheetSelection refactor](https://github.com/centerofci/mathesar/issues/1732)

## 2023-07-10 Monday

- Mark Usability Improvements project as "cut short" so that it can be closed
- Add [2023-07 frontend fixes](https://github.com/centerofci/mathesar-wiki/blob/master/projects/2023-07-frontend-fixes.md) project page
- Respond to comment on [Date input should close date picker when losing focus via Tab or Shift+Tab](https://github.com/centerofci/mathesar/issues/1769), posting clearer steps to reproduce.
- Review [Added margin between breadcrumb selector and bottom of the veiwport](https://github.com/centerofci/mathesar/pull/3014)
- Open ticket [Time cell not saved after pressing Tab key](https://github.com/centerofci/mathesar/issues/3018)
- Open ticket [Confusing timezone issue when editing Time cells](https://github.com/centerofci/mathesar/issues/3019)
- Review [Add Peak Time aggregation function](https://github.com/centerofci/mathesar/pull/2981)
- Review [Add Peak Day of Week aggregation function](https://github.com/centerofci/mathesar/pull/3004)
- Review [Add Peak Month aggregation function](https://github.com/centerofci/mathesar/pull/3006)
- Review [Updated frontend to send a single bulk delete request instead of one request for each record](https://github.com/centerofci/mathesar/pull/2985)

## 2023-07-07 Friday

- Team event
- Catch up with some email discussions from the past week
- Re-review [Publicly Sharable Links spec](https://wiki.mathesar.org/en/product/specs/publicly-shareable-links)
- Begin mapping out some thoughts for the SheetSelection refactor RFC

## 2023-07-06 Thursday

- Many meetings:
    - Front end team meeting
    - Core team meeting
    - List data types meeting
    - Installation planning meeting
    - 1/1 with Kriti
- Some work organizing info for upcoming project
- Some work planning Friday's team event
- Review/merge small community dev docs pr [Fix typo error in DEVELOPER_GUIDE.md](https://github.com/centerofci/mathesar/pull/2999)

