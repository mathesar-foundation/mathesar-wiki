# Dom's work log
## Active

- Create and prioritize issue for writing tests for db creation/update/removal via API
  - Discovered that there are no tests for this when trying to reproduce [#3230](https://github.com/centerofci/mathesar/issues/3230)
  - Associated code is messy, fix it up as well
- Make sure [#3230](https://github.com/centerofci/mathesar/issues/3230) (db reflection bug) is not reproducible anymore
- See [#3245](https://github.com/centerofci/mathesar/issues/3245) (db bug fixes) reviewed and merged
- Open some good first issues
  - Got a few ideas
- Do [#2844](https://github.com/centerofci/mathesar/issues/2844) (api for bulk upserting of records)
  - on pause; >75% done, but seems low priority
    - frontend aspect can't fit into 0.1.4

## Backlog

- Consider automating finding 404 in our wiki
- Do [#3076](https://github.com/centerofci/mathesar/issues/3076) (automate deploying internal mathesar)
- Process selected TODO comments into issues [#2181](https://github.com/centerofci/mathesar/issues/2181)
- Consider adding a make-like tool to main repo for common tasks

### 2023-10-23

- Sync with Brent
- Troubleshoot CI failing for [#3245](https://github.com/centerofci/mathesar/issues/3245)
  - Found the (seemingly) last bug that kept tests from passing in CI
- Attempt to reproduce [#3230](https://github.com/centerofci/mathesar/issues/3230) (db reflection bug) with [#3245](https://github.com/centerofci/mathesar/issues/3245) merged
  - Can't, but I found the bug elusive to reproduce before
  - Asked Rajat to try as well

### 2023-10-20

- Troubleshoot CI failing for [#3245](https://github.com/centerofci/mathesar/issues/3245)
  - Found one of the problems, but ran into another

### 2023-10-19

- Troubleshoot CI failing for [#3245](https://github.com/centerofci/mathesar/issues/3245)
- Discuss using Zulip

### 2023-10-18

- Present GSoC proposal phase notes to team
- Finish preparing GSoC proposal phase note page in wiki
- Respond in Sean's product vision follow-up email thread

### 2023-10-17

- Troubleshoot CI failing for [#3245](https://github.com/centerofci/mathesar/issues/3245)
- Respond in UX question about DB connections email thread
- Process notes from GSoC summit on proposal phase into a document
  - https://github.com/centerofci/mathesar-wiki/pull/106

### 2023-10-16

- Traveling from Sunnyvale to Dominican Republic

### 2023-10-13

- Submit PR related to [#3230](https://github.com/centerofci/mathesar/issues/3230) (db reflection bug)

### 2023-10-12

- Traveling to Sunnyvale for GSoC summit

### 2023-10-11

- Traveling to Sunnyvale for GSoC summit

### 2023-10-10

- Traveling to Sunnyvale for GSoC summit

### 2023-10-09

- Read GSoC summit updates
- Respond in CRM intro email thread

### 2023-10-06

- Respond in cycle 0.1.4 retrospective email thread
- Worked on [#3230](https://github.com/centerofci/mathesar/issues/3230)
  - Continued working through the connection leak
    - Significant progress, but there's still a major leak somewhere
      - Can't yet merge

### 2023-10-05

- Worked on [#3230](https://github.com/centerofci/mathesar/issues/3230)
  - Changes to reflection caused the connection leak bug to creep up again
    - Have to fix that in order to merge

### 2023-10-05

- Conversation in frontend channel
- Team sync

### 2023-10-04

Had a very hard time being productive, effectively took most of day off.

- Sync with Sean

### 2023-10-03

- Started working on [#3230](https://github.com/centerofci/mathesar/issues/3230) (db reflection bug)
- Respond in [#3223](https://github.com/centerofci/mathesar/issues/3223) (Rajat's db connection pr)
- Review [#3201](https://github.com/centerofci/mathesar/issues/3201) and merge
- Review [#3200](https://github.com/centerofci/mathesar/issues/3200)

### 2023-10-02

- Respond in rsqla1 retrospective
- Sync with Brent
- Respond in ux design process for importing excel/json email thread
- See Anshumna's final evaluation performed

### 2023-09-29

Away on sick leave.

### 2023-09-28

Away on sick leave.

### 2023-09-27

Away on sick leave.

### 2023-09-26

- Last sync with Anshuman

### 2023-09-25

- Do Supabase integration tests [#3141](https://github.com/centerofci/mathesar/issues/3141)

### 2023-09-22

- Submitted draft PR for Paste API
- Fix GSoC summit travel arrangements, broken due to a cancellation

### 2023-09-21

Feeling burnt out, trying to get work in, but starting late and energy levels
are low.

- Respond to Anshuman in group chat

Ended up working mostly on my dev setup and other minimally-productive things
that were easy to focus on.

### 2023-09-20

- Respond to Anish in Matrix
- Respond in GSoC group chat

### 2023-09-19

- Sync with Anshuman
- Sync with Anish

### 2023-09-18

- See [#3186](https://github.com/centerofci/mathesar/issues/3186) reviewed and merged
- Sync with Brent
- Sync with Sean

## Complete

### 2023-09-16 (Saturday)

Resumed work.

### 2023-09-15

Spent the day getting a VPS and setting it up for work; ended up being more
work than I expected; important part of my configs didn't survive the death of
my previous dev box; but, by the end of the day I have a working development
environment.

Decided that I'll make this Saturday (09-16) a workday to make up for some of
the lost time.

### 2023-09-14

Had technical difficulties with my development machine today: I bricked my
motherboard during a component upgrade; was not able to work; spent the day
troubleshooting my hardware and concluded that I cannot repair it within a
practical timeframe: will look for alternatives;

### 2023-09-13

- Make requested changes in [#3186](https://github.com/centerofci/mathesar/issues/3186) (support for column comments in backend)

### 2023-09-12

Had technical difficulties with the internet today, cut workday short.

- Respond in rsqla1 retrospective email thread
  - hard deadline is Sept 15th
  - but I said I'll do it Sept 12th (Tuesday)
    - so we can do more rounds of conversation
- Sync with Anshuman
- Did final RSVP for GSoC summit

### 2023-09-11

- Sync with Brent
- Post Monday's weekly project update
- Review [#3200](https://github.com/centerofci/mathesar/issues/3200) (contributor's pr)

### 2023-09-08

I've been taking a long time to get into our SQL code; the learning curve is
somewhat steep, I find. I do feel like I'm making good progress though.

- Review and merge [#3195](https://github.com/centerofci/mathesar/issues/3195) (anshuman's pr)
- Finish making requested changes to [#3186](https://github.com/centerofci/mathesar/issues/3186) (support for column comments in backend)
- Sync with Brent

### 2023-09-07

- Make most of requested changes to [#3186](https://github.com/centerofci/mathesar/issues/3186) (support for column comments in backend)
- Respond in [#3195](https://github.com/centerofci/mathesar/issues/3195) (anshuman's pr)

### 2023-09-06

- Start [#2844](https://github.com/centerofci/mathesar/issues/2844) (api for bulk upserting of records)
- Team sync
- Catch up on emails
- Sync with Anshuman
- Review [#3195](https://github.com/centerofci/mathesar/issues/3195) (anshuman's pr)

### 2023-??-??

Unavailable due to family reasons

### 2023-08-29

Largely unavailable due to family trouble

- Setup a bi-weekly sync with Sean until the end of cycle
- Cancelled sync with Anshuman
- Started drafting a developer guide for working with our Postgres library

### 2023-08-28

- Sync with Brent
- Review and merge [#3155](https://github.com/centerofci/mathesar/issues/3155) (anshuman's pr)
- Add support for column comments in backend in [#3186](https://github.com/centerofci/mathesar/issues/3186)

### 2023-08-24

- Spent all day debugging support for column comments

### 2023-08-24

- See [#3140](https://github.com/centerofci/mathesar/issues/3140) (test third party table with long identifiers) reviewed and merged
- See [#3129](https://github.com/centerofci/mathesar/issues/3129) (fix db list in demo) reviewed and merged
- Respond in release email thread

### 2023-08-23

- Review and merge [#3156](https://github.com/centerofci/mathesar/issues/3156) (brent's test bug workaround pr)
- Respond in installation email thread
- Respond in appetite email thread

### 2023-08-22

- Sync with Anshuman
- Respond in stale bot issue thread
- Respond in niche research thread
- Respond in should we install on user db email thread

### 2023-08-21

- Start work on backend fixes
- Respond in installation email thread
- Respond in xy problem email thread

### 2023-08-18

- Published worklog
- Prepare for team meeting
- Respond in criteria for closing user issues email thread
- Update backend fixes project with outcome
- Read the newly posted and newly updated project documents
- Respond in investigate interop with preexisting dbs email thread
- Respond in appetite email thread
- Respond in release email thread

### 2023-08-17

- Make reservations for the GSoC mentor summit
- Catch up on email
- Respond in release email thread
- Respond in xy problem email thread
- Respond in package version management email thread
- Respond in should we install on user db email thread
- Respond in summarizations for json email thread

### 2023-08-16

- Make progress in cleaning up a backend issues created during last few months
- Prioritize tasks for backend fixes of next cycle [#3144](https://github.com/centerofci/mathesar/issues/3144)
- Figure out when and who will do Supabase research [#3144](https://github.com/centerofci/mathesar/issues/3144)
- Sync with Sean on prioritization of issues

### 2023-08-14

- Respond in should we install on user db email thread
- Respond in todo list for cooldown email thread

### 2023-08-11

Home life interfered, had to push most of today's work to Monday.

- Create issue [#3141](https://github.com/centerofci/mathesar/issues/3141) (investigate supabase integration)

### 2023-08-10

- Sync with Sean and Kriti over backlog prioritization
- Respond in Criteria for closing user-reported tickets email thread
- Team sync
- Submit PR with test case for long identifiers in preexisting database [#3140](https://github.com/centerofci/mathesar/issues/3140)

### 2023-08-09

- Review [#3133](https://github.com/centerofci/mathesar/issues/3133) (pavish's pr)
- Review [#3127](https://github.com/centerofci/mathesar/issues/3127) (pavish's pr)
- Attend weekly meeting
- Prepare for weekly meeting
- Reread last Wednesday's weekly meeting notes
- Sync with Brent

### 2023-08-08

- Report [#3135](https://github.com/centerofci/mathesar/issues/3135) (column endpoint is slow when columns are many)
- Review [#3050](https://github.com/centerofci/mathesar/issues/3050) (sean's column inference pr)
- Sync with Anshuman
- See [#3083](https://github.com/centerofci/mathesar/issues/3083) (anshuman's excel tests pr) reviewed
- Respond in backend fixes weekly update email thread

### 2023-08-07

- Post weekly project update
- Got a database dump from Sean to see if I can reproduce
- Sync with Sean about imports and weird HTTP/reflection problems he's facing
- Push changes to [#3113](https://github.com/centerofci/mathesar/issues/3113) to fix connection leak
- Organize keeping more detailed meeting notes for Anshuman's project
- Push changes to [#3113](https://github.com/centerofci/mathesar/issues/3113) to make it clearer
- Sync with Pavish over [#3113](https://github.com/centerofci/mathesar/issues/3113)

### 2023-08-04

- Prepare/organize Friday's core team event
- Finish [#3129](https://github.com/centerofci/mathesar/issues/3129) (fix db list in demo mode)
- Fix demo README.md instructions to include `python manage.py setup_demo_template_db`
- Update [#3128](https://github.com/centerofci/mathesar/issues/3128) with meeting notes
- Review [#3113](https://github.com/centerofci/mathesar/issues/3113) (pavish's pr)
- Sync with Brent over [#3128](https://github.com/centerofci/mathesar/issues/3128) (allow whitelisted dynamic defaults)
- Notify developer email list of breaking changes in dev db container

### 2023-08-03

- Review [#3113](https://github.com/centerofci/mathesar/issues/3113) (pavish's pr)
- Pushed draft pr [#3129](https://github.com/centerofci/mathesar/issues/3129) (fix db list in demo mode)
- Review and merge [#3059](https://github.com/centerofci/mathesar/issues/3059) (anshuman's pr)
- Create and update [#3128](https://github.com/centerofci/mathesar/issues/3128) (allow whitelisted dynamic defaults)
- Respond in the release email thread
- Respond in Varsha's API endpoint email thread

### 2023-08-02

- Sync with Anshuman
- Review [#3059](https://github.com/centerofci/mathesar/issues/3059) (anshuman's pr)
- Read conversation about fdws in backend channel
- Read conversation with plan2 in general channel

### 2023-07-27

- Review [#3107](https://github.com/centerofci/mathesar/issues/3107) (brent's PR)
- Made part of reservations for the GSoC summit

### 2023-07-27

- Sync with Mukesh
- Notify of my break this week starting one day later than planned (and ending as planned)

### 2023-07-26

- Sync with Brent over [#3097](https://github.com/centerofci/mathesar/issues/3097) (brent's pr)
- Respond in [#3078](https://github.com/centerofci/mathesar/issues/3078) (dynamic defaults via function lists)
- Update [#3095](https://github.com/centerofci/mathesar/issues/3095) (improve support for unknown types) based on Brent's comment
- Prepare for team meeting
- Do Anshuman's midterm evaluation
- Finish reviewing [#3097](https://github.com/centerofci/mathesar/issues/3097) (brent's pr)

### 2023-07-25

- Review around half of [#3097](https://github.com/centerofci/mathesar/issues/3097) (brent's pr)
- Review [#3092](https://github.com/centerofci/mathesar/issues/3092) (pavish's backend pr)
- Created [#3095](https://github.com/centerofci/mathesar/issues/3095) (improve support for unknown types)
- Update [#3007](https://github.com/centerofci/mathesar/issues/3007) (support for point type)
- Update [#2959](https://github.com/centerofci/mathesar/issues/2959) (support for citext type)
- Close as fixed [#2709](https://github.com/centerofci/mathesar/issues/2709) (unknown types breaking Mathesar bug report)
- See [#3040](https://github.com/centerofci/mathesar/issues/3040) (rudimentary support for unknown types) reviewed and merged
- Respond in [#3040](https://github.com/centerofci/mathesar/issues/3040)
- See [#3025](https://github.com/centerofci/mathesar/issues/3025) reviewed and merged
- Respond in Varsha's API endpoint uid email thread

### 2023-07-24

- Do Friday's project update
- Respond in [#3083](https://github.com/centerofci/mathesar/issues/3083) (anshuman's excel tests pr)
- Review [#3059](https://github.com/centerofci/mathesar/issues/3059) (anshuman's excel import pr)
- Respond in [#2751](https://github.com/centerofci/mathesar/issues/2751) (update readme with troubleshooting instructions)
- See [#3029](https://github.com/centerofci/mathesar/issues/3029) merged
- Read projects' friday updates
- Respond in Varsha's API endpoint uid email thread

### 2023-07-21

- On sick leave

### 2023-07-20

Feeling under the weather, having trouble focusing

- Create [#3078](https://github.com/centerofci/mathesar/issues/3078) (dynamic defaults via function lists)

### 2023-07-19

- Read weekly meeting agenda
- Review [#3029](https://github.com/centerofci/mathesar/issues/3029) (gunicorn user instructions PR)
- Report adding unique constraint failing on point types [#3067](https://github.com/centerofci/mathesar/issues/3067)
- Report being able to sort by unsortable types [#3066](https://github.com/centerofci/mathesar/issues/3066)
- Respond in [#3040](https://github.com/centerofci/mathesar/issues/3040)

### 2023-07-18

- Do [#3024](https://github.com/centerofci/mathesar/issues/3024) (support for unknown types) in [#3040](https://github.com/centerofci/mathesar/issues/3040)
- Add email thread links to backend fixes project wiki page
- Respond in [#3050](https://github.com/centerofci/mathesar/issues/3050) (make column type inference optional)

### 2023-07-17

- Worked on [#3024](https://github.com/centerofci/mathesar/issues/3024) all day
- Review [#3042](https://github.com/centerofci/mathesar/issues/3042)
- Make sure GSoC's tax form is filled out

### 2023-07-14

- Offload [#3039](https://github.com/centerofci/mathesar/issues/3039) (Anshuman's max_level PR) to Anish
- Post friday's backend fixes project update
- Handover a frontend bandaid-workaround for [#2995](https://github.com/centerofci/mathesar/issues/2995) (fix big csv imports timing out) to Sean
  - He said he'll create an issue for it
  - He also said he'll start a conversation about UX work for a more wholesome solution to [#2995](https://github.com/centerofci/mathesar/issues/2995)
- Sync with Sean about [#2995](https://github.com/centerofci/mathesar/issues/2995) (fix big csv imports timing out)
- Start conversation with Sam and Kriti about the GSoC tax form whose deadline is tomorrow
- Put all backend fixes project tickets in 0.1.3 milestone
- Respond in 2023-07 installation improvements project email thread
- Review projects

### 2023-07-13

- Seek advice on matrix backend channel about [#3024](https://github.com/centerofci/mathesar/issues/3024) (support for unknown types)
  - [Message link](https://matrix.to/#/!UZILDSNKobkelUYwBp:matrix.mathesar.org/$kklKnZZ3_pnpul-xH5lDqGNogKfjZp25ymOhsGm2OVk?via=matrix.mathesar.org&via=matrix.org)
- Ask Sean to take up [#2346](https://github.com/centerofci/mathesar/issues/2346), which is a mostly-frontend fix for [#2995](https://github.com/centerofci/mathesar/issues/2995) (fix big csv imports timing out)
- Review and merge [#3008](https://github.com/centerofci/mathesar/issues/3008)
- Tidied up comments in [#2346](https://github.com/centerofci/mathesar/issues/2346)

### 2023-07-12

- Update backend fixes project
- Update backend fixes project to say that [#3024](https://github.com/centerofci/mathesar/issues/3024) is an alternative approach to [#2959](https://github.com/centerofci/mathesar/issues/2959) and [#3007](https://github.com/centerofci/mathesar/issues/3007)
- Investigate [#3024](https://github.com/centerofci/mathesar/issues/3024) (graceful handling of unsupported types)
- Reproduce [#2709](https://github.com/centerofci/mathesar/issues/2709) (unknown types breaking Mathesar bug report)
- Respond in querydown email thread
- Respond in [#3024](https://github.com/centerofci/mathesar/issues/3024) (graceful handling of unsupported types)
- Respond in [#2161](https://github.com/centerofci/mathesar/issues/2161)
- Update backend fixes project
- Respond in backend fixes email thread
- Respond in [#2995](https://github.com/centerofci/mathesar/issues/2995) (type inference timeout bug report)
- Make sure Aritra's midterm evaluation is submitted in time

### 2023-07-11

- Sync with Anshuman
- Do [#2245](https://github.com/centerofci/mathesar/issues/2245) (multi-column unique and pk constraints) in [#3025](https://github.com/centerofci/mathesar/issues/3025)
- Make metaticket for backend fixes project [#3022](https://github.com/centerofci/mathesar/issues/3022)
- Start work on backend fixes
- Review and merge [#3016](https://github.com/centerofci/mathesar/issues/3016)

### 2023-07-10

- Triage [#3009](https://github.com/centerofci/mathesar/issues/3009)
- Review [#3008](https://github.com/centerofci/mathesar/issues/3008)
- Respond to Anshuman's DM
- Finish backend fixes project's timeline
- Review [#3016](https://github.com/centerofci/mathesar/issues/3016)
- Try doing querydown in lispy syntax for discussion with Sean

### 2023-07-07

- Write up backend fixes project
- Review and merge [#2993](https://github.com/centerofci/mathesar/issues/2993) (remove lazydict)
- Split reviewing Anshuman's PRs with Anish
- Open [#3007](https://github.com/centerofci/mathesar/issues/3007)
- Respond in backend+frontend fixes email thread

### 2023-07-06

- Filter unassigned+backend+frontend issues to what we might do
- Review and merge [#2968](https://github.com/centerofci/mathesar/issues/2968)
- Troubleshoot a bug with Anshuman
- Review and merge [#2977](https://github.com/centerofci/mathesar/issues/2977)
- Review, make changes and merge [#2992](https://github.com/centerofci/mathesar/issues/2992)
