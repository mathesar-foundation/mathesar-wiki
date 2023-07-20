---
title: 2023-03-29 Team meeting
description: 
published: true
date: 2023-07-19T23:33:06.936Z
tags: 
editor: markdown
dateCreated: 2023-03-29T16:10:56.270Z
---

## Projects & responsibilities check-in
- **Summary**: I'd like to check in with everyone on the status of planned projects and ongoing responsibilities
- **Participants:** everyone

### Ghislaine
- Ghislaine: for user feedback, I was planning to check in every couple weeks to see what action items we have. Wondering how to turn user feedback into action items.
    - Kriti: Makes sense to do it ad-hoc for now but gradually move towards more of a process.
    - Ghislaine: It's more interesting once we can see patterns, so we'll keep collecting user feedback for now and look for action items once we can see patterns.
    - Kriti: It would be good to document your processes on the wiki page. Ghislaine.
- Ongoing responsiblitity and project pages are both very close to being completed and approved. Project page has some feedback to address. Will work on that today.
- Project is for establishing the "process". Ongoing responsibility is for _doing_ the process. Project should be done pretty soon.

### Kriti
- I have marketing. Wrote up notes on process. Didn't get any feedback, so assuming it's approved. Ties into user feeback.
    - Sean: I looked over it. Looked good.
- Funding: still working to document the funding project. Hoping to have that completed this week.
- Approved some projects and responsibilities. Waiting to hear back from other people.

### Dom
- GSoC is now an ongoing responsibility. This is taking up a lot of time/energy
- I have some items in backlog that are delayed due to GSoC. Ping me with questions/concerns
- GSoC ongoing responsibility documentation is done. More updates will be made as-needed
- Backup and restore project documentation has not begun yet. This is taking a back seat to GSoC at the moment.
- Kriti: if GSoc is still taking up lots ot time, check in with us later.

### Pavish
- Most of my time has been reviewing PRs
- release management
    - Scope of release management seems larger that what I expected
    - "Choosing the issues for the release" is still a "fuzzy" responsibility that I'm trying to figure out.
    - Would like to choose a theme for each release and build the tickets around that theme.
    - Still working to figure out the process
    - Once the process is more figured out, then I'll document it. Going to be a while before I'm fully set up with the process.
- Installation improvements:
    - More work on this will come after "Release Management" settles down
- Front end performance
    - This is on hold at the moment due to other things
- Comments
    - Kriti: might make sense to document what you already have while it's fresh in your mind. Fine to document what you already have.

### Rajat
- Repo admin
    - PR is open for responsibilities documentation. This is reviewed. Need to merge.
    - Work is going okay so far.
    - Sometimes contributors have specific questions and I'm not sure who to direct those questions to
        - Kriti: you can ask me if you need.
- Localization
    - started working on documentation. Will have draft to propose by the end of this week.

### Sean
- Usability improvements project
    - Documented and approved by Kriti
    - It's well specified and Sean's starting work on that
- Team management ongoing responsibility
    - Not put work into it yet, waiting till everyone settles down with the projects & responsibilities
    - There's no plan to document this
        - Kriti: It's fine not to document this

### Mukesh
- Installation assisting (ongoing)
    - This is Brent's responsibility, but Mukesh is helping while Brent is on leave
    - Had a call with Dan and Dan's friend. Planning to check in with them weekly. Tried out Mathesar locally.
    - Mukesh: I'll be documenting this after doing some more work on installation improvements
    - Kriti: I think Brent should document this once he's back -- Mukesh: ok
    - Kriti: We have three requests for installations
- Installation Improvements (project)
    - Would like to come up with proposals for what needs to be done
    - Kriti: This should be highest priority. We should try to split this into multiple projects
    - Mukesh: I'd like to split it up, but I'll need to figure out what needs do be done first
    - Would like to have some project documentation completed by the end of this week.
    - Pavish: I see a high priority for improving installation-related documentation. I suggest prioritizing this. Who is working on this?
        - Marius has done some work on this
        - Mukesh will be pulling in other people as needed
        - Pavish & Kriti: since users are actively requesting documentation improvements, we should be actively working on this in parallel with the broader planning-related tasks
- Remove SQLAlchemy
    - Working on researching a replacement query builder
    - Kriti: I would recommend deprioritizing this in favor of others
- The last week has mostly been GSoC and PR-review work


### Anish
- Working on [Make Deployment Type 2 work with DBs on localhost](https://github.com/centerofci/mathesar/issues/2571) (connecting Mathesar to local database)


### High level questions
- Ghislaine: If I want to create a new project, how do I do that?
    - Kriti: We don't have a process yet for how to do this. Until we do, talk to me.
- Pavish: When people work on the same issue, I still don't know how we should handle this.
   - Tabled for async discussion

## Where to put what kind of docs
- **Participants:** Sean, Kriti
- **Summary**: 

    Since we are working on cleaning up and fleshing out our documentation, I want to seek some clarity on the scope of our different docs sources, attempting to eliminate ambiguity and disagreement.

    Currently we put documentation in the following places

    |                    | docs site | markdown near code | wiki | HackMD |
    | --                 | --        | --                 | --   | --     |
    | Administrator docs | X         |                    |      |        |
    | Developer docs     | X         | X                  | X    |        |
    | Code docs          |           | X                  |      |        |
    | Team docs          |           |                    | X    | X      |

    Kriti [said](https://github.com/centerofci/mathesar-wiki/pull/86#issuecomment-1476955157)

    > Rather than spreading documentation across the wiki / docs / repo READMEs, I think we should standardize on the docs site.

    I'd prefer to use the docs site only for administrator docs (e.g. install/upgrade) and user docs (which we don't have yet). I'd prefer to put developer docs in markdown near code. Why?

    - Sometimes we have highly specific markdown files like [this one](https://github.com/centerofci/mathesar/blob/a813767c196dbe3127d8f7e10d30c02d44147121/mathesar_ui/src/systems/table-view/link-table/diagram/README.md) that would feel awkward in the docs site. Putting this documentation content as close as possible to the code that it documents is a great way to keep it up-to-date and discoverable. If we keep that file in its place and also choose to move some of the README content into the docs site then it seems a little hard to draw a clear/consistent line between the two. What about [this README](https://github.com/centerofci/mathesar/blob/a813767c196dbe3127d8f7e10d30c02d44147121/mathesar_ui/src/component-library/README.md), for example? It's much higher-level, but still not _top_-level.

    - The docs site is published from the `master` branch, and that's important because we want to ensure that it reflects the latest _released_ version of Mathesar so that docs readers who are installing or using Mathesar don't see content before it's actually applicable. But what's "applicable" to _developers_ is not the latest released version -- it's the development version. Here's a [PR](https://github.com/centerofci/mathesar/pull/2683) that made a some docs improvement for developers. We merged it last week but it's still not published because the author targetted `develop` (by default) and I failed to notice/think that perhaps it should have targetted `master` instead. EDIT: I just found [another such PR](https://github.com/centerofci/mathesar/pull/2696) after investigating a [complaint](https://matrix.to/#/!vXLxAqmrJWsDMWPSpo:matrix.mathesar.org/$0SAiuvZwAlvOC9FL93jNslyuH3HivBACFgK1K1D4Pyc?via=matrix.mathesar.org&via=matrix.org&via=t2bot.io) about incorrect documentation.
    
    To be clear: I very much support the initiative to move dev docs out of the wiki. I would just rather put them in plain markdown files within the codebase instead of putting them into the docs site.

    Putting content into the docs site certainly has its benefits. I have more thoughts about some of the nuance and gray area, and I think it might be best to chat about it so that we can agree on some guidelines as we flesh out our docs.

### Notes

- Sean and Kriti discussed this
- Kriti's points:
    - Discoverability is very important. We need to make sure that if docs content is outside of mkdocs that readers can still discover it somehow.
    - [Django docs](https://docs.djangoproject.com/en/4.1/) is a good example of versioned docs that has a `dev` version too
    - [NocoDB](https://docs.nocodb.com/engineering/architecture) has docs with dev docs published. They don't appear to have them versioned
    - Our main readme shouldn't be too bloated. It should link to other things
    - Material foor MkDocs appears to have a way to set up [versioning](https://squidfunk.github.io/mkdocs-material/setup/setting-up-versioning/)

- Sean's points
    - I'd rather not set up versioned docs right now. I'll do some research into that versioning system to see how easy it might be to implement

- OUTCOME
    - Kriti is open to Sean's proposal to put docs content in unpublished markdown files, but would like to see a more detailed plan that specifies where content would go and how it would be discoverable
    - Sean will open a PR to the wiki documenting/proposing more specific guidelines for where we would put stuff

