---
title: Responsibilities
description: 
published: true
date: 2023-03-16T12:06:27.167Z
tags: 
editor: markdown
dateCreated: 2023-03-15T20:53:04.526Z
---

## Assignments

|                           | Anish | Brent | Dom  | Ghislaine | Kriti | Mukesh | Pavish | Rajat | Sean |
| --                        | :--:  | :--:  | :--: | :--:      |  :--: | :--:   | :--:   | :--:  | :--: |
| ♻️ Team management        | ❕    | ❕    | ❕   | ❕        | ❕    | ❕    | ❕     | ❕    | ✅   |
| ♻️ Repo admin             | ❕    | ❕    | ❕   | ❕        | ❕    | ❕    | ✅     | ❕    | ❕   |
| ♻️ Release management     | ❕    | ❕    | ❕   | ❕        | ❕    | ❕    | ✅     | ❕    | ❕   |
| ♻️ User feedback          | ❕    | ♟️    | ❕   | ✅        | ❕    | ❕    | ❕     | ❕    | ❕   |
| ♻️ Marketing              | ❕    | ❕    | ❕   | ♟️        | ❕    | ❕    | ❕     | ✅    | ♟️   |
| ♻️ Assisting installs     | ❕    | ♟️    | ❕   | ❕        | ❕    | ✅    | ❕     | ❕    | ❕   |
| 🏆 [Funding][1]           | ❕    | ❕    | ❕   | ❕        | ✅    | ❕    | ❕     | ❕    | ♟️   |
| 🏆 [GSoC admin][2]        | ❕    | ❕    | ✅   | ❕        | ❕    | ❕    | ❕     | ❕    | ❕   |
| 🏆 [Improve install][3]   | ❕    | ❕    | ❕   | ❕        | ❕    | ✅    | ♟️     | ❕    | ❕   |
| 🏆 [Remove SQLAlchemy][4] | ❕    | ✅    | ❕   | ❕        | ❕    | ❕    | ❕     | ❕    | ❕   |
| 🏆 [Localization][5]      | ❕    | ❕    | ❕   | ♟️        | ❕    | ❕    | ❕     | ✅    | ❕   |
| 🏆 [Feedback kickoff][6]  | ❕    | ❕    | ❕   | ✅        | ❕    | ❕    | ❕     | ❕    | ❕   |
| 🏆 [Frontend perf][7]     | ❕    | ❕    | ❕   | ❕        | ❕    | ❕    | ✅     | ❕    | ♟️   |
| 🏆 [File data types][8]   | ❕    | ❕    | ❕   | ♟️        | ❕    | ❕    | ❕     | ❕    | ✅   |

[1]: ./projects/funding.md
[2]: ./projects/gsoc-2023-admin.md
[3]: ./projects/installation-improvements.md
[4]: ./projects/removing-sqlalchemy.md
[5]: ./projects/localization.md
[6]: ./projects/user-feedback-kickoff.md
[7]: ./projects/frontend-tables-performance.md
[8]: ./projects/file-data-types.md

Responsibility types
- ♻️ = Ongoing responsibility
- 🏆 = [Project](./projects.md) responsibility

Roles
- ✅ = Owner
- ♟️ = Helper 
- ❕ = Not involved *(having an emoji spacer helps the columns line up when editing)*


## Ongoing responsibilities

### Team management

- Schedule and facilitate team meetings
- Monitor people's standups and hold regular 1/1 meetings with all team members ensuring everyone is productive, happy, and accountable
- Schedule team/community events and make sure they have facilitators

### Repo admin

- Receive the firehose of GitHub notifications and take action on items as necessary.
- Triage new issues and PRs
- Actively shepherd PRs towards closing to help prevent them from going stale
- Troubleshoot GitHub actions and make improvements where necessary

### Release management

- Decide what goes in each release
- Decide when to release
- Publish each release, delegating tasks as needed
- Keep the team informed so that everyone knows the correct release to target with new tickets and new PRs
- Document our release process and support the team with questions about it
- Document our git branch strategy and support the team with questions about it
- Keep our broader goals and strategies in-mind, potentially planning multiple major/minor/point releases ahead.
- Decide when to update the staging and demo servers and delegate that work as needed

### User feedback

- Monitor “hello@mathesar.org” and “Request a free install” form and follow up with people as needed.
- TODO

### Marketing

- Be on the marketing@mathesar.org mailing list.
    - This list receives the “firehose” of Syften notifications, including all mentions of competitors and people looking for “spreadsheet-like” solutions.
- Handle Syften notifications
    - If Mathesar is mentioned, eagerly reply to to threads as needed, seeking to ameliorate people’s concerns and amplify people’s excitement.
    - If a problem that Mathesar could be used to solve is mentioned, then suggest using Mathesar in a tactful way.
        - Our goal here should not be to shoehorn Mathesar into all sorts of use cases. Instead, we should be on the lookout only for cases that Mathesar is a good solution for.
    - For the time being, Kriti should review any Reddit / Hacker News responses before they go out. This is not a long term solution, but there might be things that she knows that other people don’t know.
        - Eventually, we should create an “evangelism guide” ([example](https://about.gitlab.com/handbook/marketing/community-relations/developer-evangelism/social-media/))
    - If someone tweets about Mathesar, we should re-tweet it from our account and/or thank them for the shoutout.
- Forward noteworthy publicity to the rest of the team as needed (probably a post in the Matrix Marketing channel is enough)
- Track notable publicity for archival purposes on our [Marketing History](./marketing/history.md)
- Make progress on our [Mathesar launch publicity checklist](https://github.com/centerofci/mathesar-website/issues/78)
    - We’ll hold off on making new announcements until our installation process is improved
    - We should continue to add Mathesar to aggregators, though.
- Do research on more relevant aggregators that Mathesar could be added to and add them there.
- Keep track of where we’re getting traffic from (using GitHub Insights and our analytics), and track notable sources in the [Marketing History](./marketing/history.md) page
- If we need to improve messaging on Mathesar.org based on user feedback, make a proposal to Kriti outlining the problem and proposed changes.

### Assisting installs

- Help find notable use cases for Mathesar, and drive whatever needs to be built to make those use cases work.
    
    e.g. we talked about using Mathesar in the Chelsea Project to share wastewater data. someone needs to look at the data, get it into Mathesar, talk to Sam to get her requirements for what she wants sharing to look like, break it down into features for Mathesar, etc.

