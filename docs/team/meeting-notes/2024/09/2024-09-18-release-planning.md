# 2024-09-18 release planning meeting

**Attendees**: Adam (partial), Anish, Ghislaine, Kailash, Kriti, Pavish, Sean

## Current status of work

### Sean's high-level status report

- **Database Page**: ✅

    - RPC changes done
    - Ready for QA _except_:
        - Permissions features (which I can't comment on)

- **Schema Page**: ✅

    - RPC changes done
    - Ready for QA _except_:
        - Explorations features
        - Permissions features (which I can't comment on)

- **Import page**: ✅

    - RPC changes done
    - Ready for QA (I think we should perform extensive QA here)

- **Explorations**: ❌

    - **RPC needs extensive front end work still, and likely some minor backend work too**
    - It's difficult to accurately estimate the remaining time. Best case: ready for QA Sept 25. Worst case: ready for QA Oct 8.

- **Record selector**: ✅

    - RPC changes done
    - Ready for QA 

- **Table page**: 🟡

    - Most front end work done.
    - Tiny bit of front end work blocked:
        - "split table" & "move columns" features in [draft PR](https://github.com/mathesar-foundation/mathesar/pull/3849) with further front end progress blocked by backend issue [Return value needed from data\_modeling.split\_table](https://github.com/mathesar-foundation/mathesar/issues/3848)
    - Some QA could potentially begin, with knowledge of above limitations

- **Record page**: 🟡

    - Front end work likely done.
    - QA blocked by backend issue: [Make records.get work with stringified PK values](https://github.com/mathesar-foundation/mathesar/issues/3844)

### Pavish's status report - permissions
- **Database page**
	- Settings tab - Complete, ready for QA
	- Permissions modal
		- 'Share' tab - Complete, ready for QA
		- 'Transfer Ownership' - pending
- **Schema page**
	- Permissions modal
		- 'Share' tab - Complete, ready for QA
		- 'Transfer Ownership' - pending
		- Disable actions based on user's privileges - pending
- **Table page**
	- Permissions modal
		- 'Share' tab - Complete, PR open
		- 'Transfer Ownership' - pending
		- Disable actions based on user's privileges - pending

ETA for getting PRs open for the above pending functionality.

- 20th EOD.
- My current buffer is exhausted, so I might end up using the weekend as a buffer period if something comes up.

### Anish's update
- All issues blocking Sean are resolved.
- Only 4-5 backend endpoints left for permissions, ETA Friday unless there's more blocking work from Sean.

### Ghislaine's update
- QA script for permission is in review.
- Visual consistency / improvements work PRs are in progress or review, should be done by early next week.
- Hasn't started on visual improvements for permissions, planned for next week.

### Adam's availability
- Adam is available to help with QA next week.
- Either in a session, or independently with instructions.

## Release work plan and timeline

Here's the rough work plan and check-in points for the release.

We won't have a specific date we're aiming for, since the work is pretty well defined but has some unknowns.
- Instead, we'll set up several checkpoints, completing each checkpoint will also trigger beginning other work.
- We'll also check in at the daily progress meetings and evaluate if we can cut scope.

### Individual tasks we're working on, other than below checkpoints
- QA script
- Visual improvements work
- Other small issues that may come up
    - Kriti will continue to look through the notes and flag anything we missed.
    - No need to track record summary UI changes or hiding public shares, they are alrwady done.

### 1. All RPC frontend work merged except explorations.
All balls for this currently in Sean's court. Once this is done:

- Ghislaine will start (unstructured) QA on the `develop` branch locally.
    - Mathesar should be set up in production mode for QA
    - Pavish will help Ghislaine set it up. 

### 2. All planned work on permissions is merged.
Pavish and Anish are working on this. This triggers:

- Kriti & Ghislaine will do a visual review of permissions.
- Anish will deploy a QA server.
- Kailash will run through the QA script (except explorations).
- Adam will help with QA.
- Ghislaine will work on updating user documentation.

### 3. Explorations RPC work is done.
- QA on explorations begins,
- Everyone participates in QA.

### 4. Installation documentation work is done.
- Administrator-focused QA begins.
- Triage of QA issues to figure out what to fix / what to defer.
- We fix critical QA issues.
- Review and fix issues with user documentation

### 5. QA + critical fixes complete
- Release process begins

## Priorities for each person

### Adam
- Perform QA when ready.

### Anish
- Backend endpoints for permissions
- Unblock Sean with backend fixes as needed
- Installation testing & docs
    - Talk to Kriti to break down task before getting started.
- Perform QA when ready.

### Ghislaine
- Wrap up visual improvements PRs ASAP to make room for other work.
- Finish QA script work so QA is unblocked.
- Review and visual improvements for permissions.
- User docs for permissions.
    - Talk to Kriti to break down task before getting started.
- Perform QA when ready.

### Kailash
- Review QA script from PoV of someone who will be using it.
- Perform QA when ready.

### Kriti
- Continue release planning and organization
- Perform QA when ready.

### Pavish
- Get permissions done.
- Perform QA when ready.

### Sean
- Merge non-explorations RPC work
- Explorations RPC frontend work
- Perform QA when ready,

## Release logistics

### Name
What do we call the release?

- "release candidate" is probably not good, implies too much polish.
- Language like "testing build" probably makes more sense.
- "Pre-beta testing build 1" works for people.

### Version
- Do we even need a version?
    - We're not supporting upgrades or tagging as `latest`
- Where do we use the version?
    - Someone should chase this down by looking at the code.
    - Off the top of our heads:
        - GitHub release "object"
        - Docker build
        - Docs, marketing updates, blog post, social media, etc.
        - GitHub tag
- We need something to name the GitHub tag, etc.
    - Shouldn't be `0.1.7` since this is a very different Mathesar from last release, same version number doesn't indicate that.
    - Should not be `0.1.8`, this is not an upgrade (yet)
    - Should not follow `number.number.number` pattern to make it clear it's not a usual version.
- Beta will probably be `0.2.0`
    - Not `1.0-beta` because we don't have a fixed plan for 1.0.
- We could do something like `0.2@next.1` if we went with how Svelte does things. They have a `4.2.19` version but also a `5.0.0@next.X` for next version testing builds.
    - The `@` is weird. Other options
        - 0.2.0-testing-1
        - 0.2.0-testing.1
        - 0.2.0.testing-1
- DECISION: **`0.2.0-testing.1` wins!**

### Communication
- Do we need to make a GitHub release?
    - No, but GitHub does support marking releases as "pre-releases" and not showing as latest.
        - Should work for us without any code changes.
    - Having a GitHub release will make the build more visible.
    - Let's do it.
    - Sean to do some investigation to ensure that this doesn't screw up anything for `0.1.7` BEFORE we make the actual GitHub release changes.
- We should do:
    - Matrix post
    - Blog post
    - Dev mailing list post
    - Twitter post
- We need to specify "DO NOT UPGRADE" prominently in all comms
- Communication ideas
    - We can use the concept of a "calf" release (riffing off our elephant logo) to convey that the release is still a bit unsteady on its feet and needs to grow up. :)
    - Good motif to use in comms
    - Can also use "mammoth" motif for indicating final / stable version.

### Publication
- Where do we host testing instructions?
    - Blog post seems more appropriate than docs.
    - But we need a place to host docs for the testing build.
        - New URL?
        - mkdocs version switcher? (we've been kicking that can down the road)
            - Django has development docs hosted this way.
    - Let's do mkdocs version switcher unless it proves untenable.
        - Sean to try setting it up.
    - Instructions can live on the docs like the other releases, but the docs site will default to `0.1.7`.
    - We can link to appropriate versioned docs for testing build when we make our comms about the release.
- Docker repo
    - Can we use Mathesar debug, to indicate it's a testing build?
        - Yes, everyone's in agreement.
    - We should investigate turning on the debug logging like we have for other debug images
        - Only if it doesn't affect performance.
        - We will investigate.
    - Aside: for final beta version, we should consider setting up `mathesar/mathesar` repo instead of `mathesar-prod`

### Community engagement
- What to ask community for feedback on?
    - Performance improvements
    - Permissions, how does this work for your use case, etc.
    - Usability feedback?
        - Give them some hints / specific questions to guide feedback.
        - Need to work on what those are.
    - That's enough, don't want to overwhelm.
- How to collect feedback?
    - Multiple channels to make it easier for different kinds of users.
    - Consider issue template on GitHub
        - plus issue form
        - for people who prefer structured feedback (like Kriti)
    - Also encourage email or Matrix feedback that's unstructured for people who prefer that (like Sean)
    - Can also open a single GitHub discussion thread for reactions on comments about the release.
- We should reach out to specific users that we've corresponded with and we think would be good fits to test.
    - Can look through our internal CRM.
    - Kriti has some idea who to start with, should reduce work needed to look through CRM

## Task management
We did not have time to look through GitHub & Basecamp in the meeting, Kriti will follow up via email.

### Kriti's notes on this topic
- Ensure 22 open items on [Pre-beta test build #1](https://github.com/mathesar-foundation/mathesar/milestone/77) milestone belong there.
- Should we split items we're not doing for this release into new issues?
    - [Architectural overhaul for beta](https://github.com/mathesar-foundation/mathesar/issues/3516)
    - [Implement permissions revamp frontend](https://github.com/mathesar-foundation/mathesar/issues/3686)
    - [Implement RPC API functions needed for Permissions revamp](https://github.com/mathesar-foundation/mathesar/issues/3639)
    - [RPC front end implementation](https://github.com/mathesar-foundation/mathesar/issues/3621)
- Walk through work tracked in Basecamp, see if we need to put anything in GitHub
- Need to create issues for:
    - table / schema `PUBLIC` issue, needed for permissions to work
- Could be more smaller issues, still going through all the meeting notes.
