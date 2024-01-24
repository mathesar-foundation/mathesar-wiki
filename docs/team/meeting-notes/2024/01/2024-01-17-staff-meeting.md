# 2024-01-17 staff meeting

## Release QA plan

Sean wants to brainstorm QA tasks to focus on during the QA phase for this release. So far, he has:

- Test clean installs with each of our installation methods. Follow docs pretending you're a new user.
- Test in demo mode. Pay particular attention to the changes in [Fix db list permissions in demo mode](https://github.com/mathesar-foundation/mathesar/pull/3129)
- Test upgrade from 0.1.3
- Test upgrade from 0.1.2
- Test connection to DB on remote pg server

### Discussion

- We don't expect to have any more code changes merged in
- We do have docs still waiting to be merge
- We should start with the tasks in the release process wiki page https://wiki.mathesar.org/engineering/release-process/
    - Cut release branch, etc.
- We need to have an image pushed to DockerHub to start QA
    - tagged 0.1.4
- Sean doesn't have much time left today
- Pavish can do all the logistics parts
- Brent will deploy to demo and internal servers
    - internal.mathesar.org will be temporarily on release branch
- Anish is out for the last week of January, FYI
- Brent will be traveling starting Feb 1
- Pavish needs to work on his pgconf talk - Feb 29 / Mar 1
    - 45 min
- compose.mathesar.org used for different installation method testing
    - same DB server, with different DBs for remote DBs
    - Anish will help test installation testing here
    - Also will assist anyone else doing installation with QA
        - Sean could help with QA
- 3 types of QA needed
    - Installation / Upgrade
        - Brent will work on a plan for QA on this
        - Pavish, Kriti and Sean will work on actual QA
    - Actually using the app (maybe on internal.mathesar.org)
        - Ghislaine and Adam could help with this
        - Everyone should look for regressions
        - Sean will work on QA plan next week.
- Anish is also making videos for installation
- Pavish: should we hire someone on Upwork to test the release?
    - We don't think this is worth it, given our short timeline
- Pavish will make basecamp tasks

## Release notes

Sean would like to show everyone the [release notes](https://hackmd.io/1_GFzwjCQ_-JbuORmir_9Q?edit) (private doc) that he's working on. He'd like high-level feedback, and he has a few questions. This agenda item is _not_ intended for detailed review of release notes content — it's more about process.

- Where should we put the release notes?
    - Thus far, we've been putting them in the GitHub release object. I'm inclined to put them somewhere slightly more discoverable like the wiki or maybe even in the main repo.
- What is our process for reviewing release notes?
- How should we deal with attribution within the release notes? Personally, I'd rather not deal with this.
- Should the release notes reference _issues_ as well as PRs?

### Discussion

- Everyone took a couple min to skim through Sean's release notes doc.
- Previous release notes: https://github.com/mathesar-foundation/mathesar/releases/tag/0.1.3
- Changes
    - More screenshots
    - Blog post type - complete sentences
- Why are "high effort" release notes important?
    - They are marketing
    - Motivate users to upgrade
        - We need to sell upgrade to them
    - Evaluating Mathesar vs. other products
        - Sign of life
        - Understand how well developers can communicate with users
        - Shows that we're using best practice (e.g. maintenance sections
- Release notes are shown within the Mathesar UI
    - Are they rendered within Mathesar or just linked to?
    - We should make sure it all works well
- We're agreed on the part that we need to create more "marketing" type release notes — somewhere.
- Who should review release notes?
    - Kriti, Brent, Ghislaine
- Can we skip attribution?
    - This is fine
    - Brent does like the "New Contributor" section — we can use GitHub to auto-generate this.
- Should we have the auto-generated section of PRs?
    - Yes, we'll have this at the bottom of the release notes. It will list all the PRs
- Should the release notes reference _issues_ as well as PRs?
    - We'll do whatever the GitHub automated feature does
- We'll have a CHANGELOG file committed at the root of our repo. It will list hyperlinks to PRs for each release and will be further categorized with the same sections as in the release notes.
- Some todos for Brent and Anish in the release notes
- HackMD draft is the place people should edit

## Upcoming funding announcement
Quick note by Kriti that we're working on announcing our recent funding. There is a [separate Basecamp project]( https://3.basecamp.com/5718119/buckets/35366254/todosets/6806782737) that tracks the work.

We're starting off with website changes and writing a blog post.
