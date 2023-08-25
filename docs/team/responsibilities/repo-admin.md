# Repo administration

**Owner**: Rajat  
**Helper**: Sean

## Responsibilities at a Glance

- Receive the firehose of GitHub notifications and take action on items as necessary.
- Triage new issues and PRs
- Actively shepherd PRs toward closing to help prevent them from going stale
- Troubleshoot GitHub actions and make improvements where necessary

### Owner's Tasks

#### Acting on GitHub notifications for issues and PRs

Make sure your notifications setting for all of the Mathesar repositories is set to **All Activity**.

Go through each of your notifications for the Mathesar repositories and follow the approach documented below:

- If the notification is about the following, ignore it
  - Closing an issue
  - Merging/Closing a PR
  - Any activity on a draft PR, apart from making it ready for review.
- For the rest of the notifications, **if it's about a PR**
  - Assignee - Make sure it's assigned to someone. You might want to check the recent conversation to validate the assignee.
  - Label - Make sure it has the correct `status:` label.
  - Milestone - Make sure it's in the same milestone as the issue it fixes.
  - Description: Make sure it follows our [PR template](https://github.com/centerofci/mathesar/blob/develop/.github/PULL_REQUEST_TEMPLATE).
  - Personally follow up with the assignees if there hasn't been any activity on it from the last 3-4 working days.
    - If it's a core team member, you can reach out via Matrix.
    - If it's a non-core team member, you can tag and ask for an update using the PR comments.
  - When a non-core team member does not reply for more than a week, check with the core team reviewer. If she is comfortable with moving the PR forward and merging it then assign the corresponding issue to her otherwise close the PR.
- For the rest of the notifications, **if it's about an issue**
  - Make sure to read the issue description and the recent conversation on it before moving to the next steps.
  - Make sure the issue is triaged properly as per our guide [here](/team/guide/issue-triage)
    - A mental model for labels:
      - "difficulty: easy" => "help wanted" & "good first issues"
      - "difficulty: medium" => "help wanted"
      - "difficulty: hard" => _no extra labels_
      - "difficulty: extra hard" => "restricted: maintainers"
    - Pay extra attention before marking an issue as ready. Do not mark issues as `status: ready` until they have enough details for someone to work on them.
  - Assignee:
    - Make sure to assign the issue if someone wants to claim it and the issue is not restricted to maintainers.
    - Make sure to un-assign the issue if there has been no activity from a community contributor from the last 1 week, as per our [contributing guidelines](https://github.com/centerofci/mathesar/blob/develop/CONTRIBUTING.md)
  - Notifications about the GitHub bot marking an issue `stale`: If the issue already exists, remove the stale label otherwise add a comment and close it as done.

- If a comment or issue can be considered user feedback or helpful for marketing materials, please flag it to the owners of these responsibilities ([user feedback](/team/responsibilities/user-feedback), [marketing](/team/responsibilities/marketing.md)) respectively.

#### Acting on notifications from GitHub Discussions

Flag discussion-related notifications to the marketing and user feedback teams for a response. This can be done by sending a notification to the [Marketing](https://matrix.to/#/#marketing:matrix.mathesar.org) channel and tagging the owner of [user feedback](/team/responsibilities/user-feedback) and [marketing](/team/responsibilities/marketing.md) responsibilities.

#### Assigning reviewers fairly

Depending if the PR is related to the backend or frontend, assign it to a core team member who has the least no of reviews already assigned.

#### Triage

Use the following script to list issues/PR that need triage.

You need to install [github-cli](https://github.com/cli/cli#installation) to use the below script.

```
export GH_PAGER=cat
gh -R centerofci/mathesar issue list --search "is:open no:milestone"
gh -R centerofci/mathesar issue list --search 'is:open label:"status: triage"'
gh -R centerofci/mathesar pr list --search "is:open no:assignee -is:draft"
gh -R centerofci/mathesar pr list --search "is:open no:milestone -is:draft"

gh -R centerofci/mathesar-wiki issue list --search "is:open no:milestone"
gh -R centerofci/mathesar-wiki issue list --search 'is:open label:"status: triage"'
gh -R centerofci/mathesar-wiki pr list --search "is:open no:assignee -is:draft"
```

### Helper's Tasks
- Take action on GitHub notifications every Monday since that's when we have one of the largest influx.
- Fill in for the owner by doing the tasks mentioned above when he is out of the office.
