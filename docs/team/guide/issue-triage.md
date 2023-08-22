# Issue Triage

Triaging an issue means setting all the appropriate fields on it.

## Responsibility

- Everyone creating issues should do their best to triage them at creation time.
- Team members who work on the [repo admin](/en/team/responsibilities/repo-admin) responsibility should catch issues opened by non-team members or were not properly triaged during creation.

## How to triage one issue

1. **Set required labels**

    | Prefix | Required count | Notes |
    | - | - | - |
    | `work:` | 1+ | All `work: design` issues should also be marked `restricted: design team` because only the design team can currently work on those. |
    | `type:` | 1 | |
    | `status:` | 1 | _Should not be `status: triage`_ |

1. **Set optional labels**
  
    Scan through the full labels list and apply other labels as necessary. Learn more about the [meaning of all our labels](https://github.com/centerofci/mathesar/labels).


1. **Verify Project and fields**

    Set the Project to "Mathesar".

    Within the project, ensure that the `status`, `priority`, and `work` fields are set. Set the `feature` field to the appropriate feature.

    If you don't know what feature to put something in, talk to Kriti.

1. **Set milestone**

    If an issue is directly associated with a milestone, put it in the milestone. Otherwise, put it in the "Backlog" milestone.

    If you don't know what milestone to put something in, talk to Kriti.

    Do not create any new milestones.  

## Notes on Labels and Milestones

The list of available labels and milestones should only be changed in the `mathesar` repo. They are synced every day to the other repos related to the project using [this GitHub action](https://github.com/centerofci/mathesar/blob/master/.github/workflows/sync-github-labels-milestones.yml).