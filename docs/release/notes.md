# Writing release notes

## Workflow

You can begin this process before the release is [cut](./cutting.md).

1. Generate a release notes document. Follow steps [here](https://github.com/mathesar-foundation/mathesar/blob/develop/docs/docs/releases/README.md).

1. Create a PR for the release notes.

1. Push a commit to the PR adding the PR itself within the release notes (under "Documentation").

1. As the release nears, keep the PR up-to-date periodically by re-running the release notes helper script.

1. Have other team members review the release notes as necessary.

The release notes PR will be merged at the start of the [publication](./publication.md) process.

## Guidelines

- Write for an audience of Mathesar users and administrators. Keep in mind that these readers may not be technical and almost certainly won't understand acronyms internal to our team (e.g. RSQLA1) that occasionally appear in PR titles.

- Within each section, order the items with the most compelling ones first. Begin with the things that you think readers are most likely to care about.

- For each item within the "Improvements" section:

    - In addition to the title, write a short blurb to describe the improvement.
    - Add a screenshot if possible.
    
    (See [0.1.4](https://docs.mathesar.org/releases/0.1.4/) as an example of these "improvements" guidelines in practice.)

- PRs which fix mid-cycle regressions should be lumped into their originating items. For example, if we implement a feature that in turn breaks some functionality elsewhere, that's a regression. If the regression never gets released, then from the user's perspective it's not actually a bug. Rather, the regression is just part of our internal process of building the feature.

- Keep it concise.


