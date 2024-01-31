# How to set up a new GitHub repo

Setting up a new GitHub repo involves a bunch of different steps to tie into our GitHub workflows.

## Setup tasks

If you're creating a GitHub repo, please make sure you do all of these things. 

- [ ] Repo name should use hyphens, not underscores
- [ ] Default branch name should be `master`, not `main`
- [ ] Repo collaborators should ONLY use Teams, not individual accounts.
    - [ ] Private repos only the "Mathesar Maintainers" should have access, and the access level should be "Maintain". 
    - [ ] Public repos should also have the "Mathesar Community Team" added with "Write" permissions.
- [ ] Set up our default GitHub workflows
    - This plugs the repo into the main Mathesar project and sets up some QoL automations
    - See update of `sync.yml` in this [example PR](https://github.com/mathesar-foundation/mathesar/pull/3234)
- [ ] Merge the new PR this generates ([example](https://github.com/mathesar-foundation/mathesar-internal-crm/pull/3))
- [ ] Set up comprehensive `.gitignore` file
    - You can copy this from `mathesar-private-notes` repo since it's fairly basic and doesn't involve code-specific things.
- [ ] Set up label & milestone sync
    - This syncs labels and milestones between repos
    - See update of `sync-github-labels-milestones.yml` in [this example](https://github.com/mathesar-foundation/mathesar/pull/3234)
- [ ] Run the workflow above manually in the `mathesar` repo (so you don't have to wait a day for labels and milestones to sync)
    - Click "run workflow" [here](https://github.com/mathesar-foundation/mathesar/actions/workflows/sync-github-labels-milestones.yml)
- [ ] Verify that the new milestones and labels are now available on the new repo
- [ ] Delete default labels created by GitHub that we don't use (i.e. `bug`, `documentation`, `enhancement`, `question` etc.)
- [ ] Ensure that repo has access to correct GitHub token for actions
    - This involves going to the org settings > Secrets & variables > Actions and granting the new repo permissions to the `MATHESAR_ORG_GITHUB_TOKEN` secret
- [ ] Set up repo settings 
    - [ ] Ensure Issues is on 
    - [ ] Turn off Wikis
    - [ ] Turn off Projects (we use org-level projects, not repo-level projects)
    - [ ] Turn off Discussions
    - [ ] Pull requests
        - [ ] Turn off squash merging
        - [ ] Turn off rebase merging
        - [ ] Turn on auto-merge
        - [ ] Turn on automatically deletion of head branches 

## Teardown tasks

If you're removing a GitHub repo, please make sure you do all of these things.

- [ ] Remove all references to the repo from within the `.github` directory of the main `mathesar` repo.

