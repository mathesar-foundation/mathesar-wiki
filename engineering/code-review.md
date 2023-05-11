---
title: Code Review Guidelines
description: 
published: true
date: 2023-05-11T14:29:23.172Z
tags: 
editor: markdown
dateCreated: 2021-04-29T17:28:01.167Z
---

Anyone is welcome to review pull requests!

If your review is requested, it means that you are responsible for reviewing the pull request. If the PR is large or you think someone who is familiar with a specific part of the code would be helpful, feel free to request additional reviewers through the GitHub interface.

## Process
- We should be aiming to turn around PR reviews within 1-2 working days. This means that there should be movement on the PR every 1-2 days, a new review, code review fixes, repeat if needed, and then merge.
- If you approve the PR, merge it unless someone else has requested changes.
  - If the person who has requested changes is unavailable, merge the PR anyway.
- Always merge using merge commits, never squash or rebase (the GitHub interface should disable squash and rebase, but check just in case).
- If the PR is from a community contributor and it only requires minor changes, feel free to make the changes yourself and merge them.

## Tips
- If the branch needs to be updated before merging (because it's out-of-date with the `master` branch), do so, as long as the merge can be performed automatically.  Otherwise, ask the Author to handle it.
- See [Backend Code Review](/engineering/code-review/backend) for guidelines specific to backend code.
- We should be aiming to merge PRs in and create new issues for improvements rather than keeping PRs in review until every possible issue is fixed.
- Code review should be a fairly quick process. Reviewers should be focused on asking the right questions, not on doing research into the answers and suggesting them. 
    - e.g. if you're wondering if the author considered a particular implication of a change they made, ask them that instead of doing research into all the implications yourself and informing the author of them.
- If you'd like to reconsider the architecture of a PR, create a draft issue for figuring that out rather than blocking the PR until you figure out the right architecture.
- When reviewing community contributed PRs, if it's easier to make the changes yourself rather than describe the changes needed as a code review, just make the changes and merge the PR. You can explain what you did and thank the contributor for their work.

## Modifying PRs before merging
You can modify an in progress PR before merging, if necessary.  If the PR is from a branch in the official Mathesar repository, just modify that branch.  If it's in a branch of a fork, it's a bit more complicated.  The smoothest way in that case is to
1. Add the fork repo as a remote, locked to the appropriate branch and fetch:
   ```shell
   git remote add -t $A_BRANCH_NAME -f $A_REMOTE_NAME $REPO_URL
   ```
   Here,
   - `$A_BRANCH_NAME` is the 3rd party branch name.
   - `$A_REMOTE_NAME` is chosen by the user; make it memorable.
   - `$REPO_URL` is set to the url of the 3rd party repo in question.
   - Note that the `-f` flag is *not* for 'force', but for 'fetch'.
2. Make changes in that branch.
3. Add, commit, and push your changes (the branch should already have the correct remote set).
4. Back in the official Mathesar repo, your changes should be shown.  Review and merge as appropriate.

If (3) fails, it may be a permissions issue.  In that case, you'll have to make a new branch in the official Mathesar repo based off of the PR.  To do that, follow the instructions [here](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/checking-out-pull-requests-locally).

## Reading
Some reading related to our process:

### Why not squash or rebase merges?
- [Why I’m against merging pull requests in squash mode or rebase mode?](https://myst729.github.io/posts/2019/on-merging-pull-requests/)
- [Squash merges are evil](https://medium.com/bananatag-engineering-blog/squash-merges-are-evil-171f55139c51)
- [Why git squash merges are bad](https://felixmoessbauer.com/blog-reader/why-git-squash-merges-are-bad.html)
- [Git merge - to squash or not to squash? - Stack Overflow](https://stackoverflow.com/questions/26999930/git-merge-to-squash-or-not-to-squash)

### Commits
- [Commit early, push often](https://www.worklytics.co/commit-early-push-often/)
- [Commit message guidelines](https://gist.github.com/robertpainsi/b632364184e70900af4ab688decf6f53)