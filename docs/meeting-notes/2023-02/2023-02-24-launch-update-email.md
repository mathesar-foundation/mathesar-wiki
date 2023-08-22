# 2023-02-24 launch update email

*We discussed launch in an internal email instead of having a meeting. Highlights:*

The only remaining launch blockers are:
1. Getting installation working smoothly.
2. Figuring out our release process and publishing our release.
3. Completing QA for users & permissions + fixing any issues.
4. Completing QA for upgrades + fixing any issues.
5. Writing up our launch related posts.

However, we're going to need an extra day or two to get the installation working smoothly before we cut the release. Installation isn't something we can quickly fix on-the-fly after we launch. So [Kriti is] going to move our target launch date to **Wednesday or Thursday next week**.

Here is the plan for next week:
- Monday's launch check in cancelled because I don't think there's much for the entire team to discuss.
- Brent, Mukesh, and Kriti will work on installation and release. I don't think these tasks can be parallelized further.
- Dom will continue work on increasing live demo throughput and support testing upgrades.
- Pavish will continue work on testing upgrades and any users/permissions issues.
- Anish will complete users and permissions QA.
- Kriti will also work on writing up launch related posts.

Team members who are free should work on (in priority order):
1. Supporting team members working on launch blockers, if requested
2. Any available tasks in Launch Nice to Haves: https://github.com/orgs/centerofci/projects/1/views/45
3. Reviewing community PRs and generally engaging with the community.
4. Reviewing GSoC project ideas and making sure the implementation details look good
5. Reviewing our documentation and making improvements.
    (i) some ideas here are moving documentation from various READMEs in the repo to docs.mathesar.org. We've already done this with local setup documentation.
    (ii) another idea is adding documentation about our codebase. This will be helpful for community contributors.
6. Creating well-specced out issues for community members to work on (or looking at older issues and speccing them out well enough).
7. Working on high-priority Backlog items.
    (i) Pavish & Ghislaine – you may want to work on a solution to this https://github.com/centerofci/mathesar/issues/2537 so we don't have to have a note in the docs about it.

We also decided to have a `develop` branch as our default branch for merging PRs. `master` will be dedicated to release-blocking issues. This is a temporary workflow, we'll decide on a permanent Git workflow after launch.