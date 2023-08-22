# Release Management

# Team
| Role | Assignees |
|-|-|
| **Overall process owner** | Kriti |
| **Current release owner** | Rajat |


**Note**: Each release will have different owners. No specific person has been assigned as a helper, but the release will be a top priority for everyone during cooldown.

# Guide
This guide is common for the owner and the helpers of the Release management responsibility. The owner is responsible for ensuring the work gets complete, and the helpers assist the process and cover for the owner when they are not available.

**Examples used in the guide**
This guide explains the release management process citing the versions 0.1.2 and 0.1.3 as examples.
   > v0.1.1 is the latest version which is released.
   > v0.1.2 is the current ongoing project which hasn't been released yet.
   > v0.1.3 is the next release project.

## Planning a release
1. Create necessary milestones
    - Create 1 milestone ahead of the next release. When planning for v0.1.3, we'll have the milestone created for v0.1.4.
    - Note that the milestone for v0.1.3 will already exist when v0.1.2 is in progress.
    -  We use semantic versioning for releases.
1. Come up with a list of ideas to consider as the main focus of the upcoming release.
    - Each release will be focused around a project or a theme.
    - For eg.,
      - Installation improvements is a project which is the main focus of v0.1.2.
      - Fixing user raised bugs is a theme which can be the focus of a release. v0.1.1 fixed all issues raised by users during a specific interval from the release of v0.1.0.
    - The Release management team will choose the items from the [list of Current projects](https://wiki.mathesar.org/en/projects#current-projects) and issues the team is working on [from the "Next release" milestone](https://github.com/centerofci/mathesar/milestone/71).
1. Start an email thread with the subject: `Release plan v{release_version}`.
    - For eg., `Release plan v0.1.3`.
    - This thread will be public and all mails will be addressed to `mathesar-developers` mail group.
    - Send the list of ideas to the team and ask for suggestions.
1. Based on the discussions in the mail thread, finalize the items to focus for the release, and **get approval from Kriti**.
1. Create a project for the release and spec it out.
    - Discuss with people needed for the release, decide on the work plan and the timeline.
    - Eg., [Spec for Release v0.1.2](https://wiki.mathesar.org/en/projects/release-0-1-2)
1. Send the project spec for review, **get approval from Kriti and people involved with the release**.
1. Clean up the release milestone, update milestone due date.
    - Ensure issues needed for the release are created and placed in the release milestone.
      - The release will be blocked until all these issues are resolved.
    - Move issues not planned for the release out of the milestone.
    - All other issues people are working on, which may end up with the release, should go in the ["Next release" milestone](https://github.com/centerofci/mathesar/milestone/71). The release will not be blocked by items present in this milestone.

### Timeline for the plan
1. When to start planning for the next release?
    - The release plan needs to begin when the current release is still underway, preferably during the last week.
    - The process for v0.1.3 should begin during the last week of the deadline for the release of v0.1.2.
1. What is the deadline for the release project spec getting approved?
    - The plan for the upcoming release should be finalized and release spec should get approved before 4 working days from the date of the current release.
    - If v0.1.2 is released on `2023-05-08`, the release project spec for v0.1.3 needs to be approved by EOD `2023-05-12`.

## Making a release
1. Once all the items needed for the release is merged into `develop`, follow the [Release process document](https://wiki.mathesar.org/en/engineering/release-process) to publish the release.
1. Ensure that all private servers running Mathesar maintained by the core team are upgraded.
1. Coordinate with Marketing team to [make release announcements](https://wiki.mathesar.org/en/team/responsibilities/marketing#make-release-announcements).

## After a release
1. Keep an eye out for user reported issues with the new version for the next week.
1. Pay extra attention towards:
	 - Installation and upgrade related issues
   - Regressions

## Handling hotfix releases
1. In case we encounter critical issues in a published release, we'll make emergency hotfix releases.
    - This will depend on the severity of the issues and the user impact.
1. Hotfix releases should be the next minor version. The ongoing release version will become the next release after that.
    - A hotfix release over `v0.1.2` will be `v0.1.3`.
    - All items planned for `v0.1.3` will be moved to `v0.1.4`.
1. Hotfix release branches should be based off on `master`.
    - The fixes will go direclty into the release branch.
    - `develop` will not be involved for hotfix releases.
1. All other processes from the [Release process document](https://wiki.mathesar.org/en/engineering/release-process) will remain the same as a regular release.

## Incorporating user feedback into release plan
Yet to be planned

## Deciding on major/minor releases
Yet to be planned