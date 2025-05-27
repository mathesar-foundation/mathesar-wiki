# Release QA testing

This page describes manual QA testing routines that we perform before a release.

## Administrator-facing QA {:#admin}

### Pre-requisites for testing Installation & Upgrades

#### For direct install on Linux, macOS, and WSL

- Ensure that there is a release on GitHub and the release assets can be downloaded via public url.
- This should have been done when cutting the release branch.

For upgrades:

- Run the new install script pointing to the same directory as the previous installation.

#### For docker related setups

For installations:

- Clear out remains of any previous installations.

For upgrades:

- Clear out remains of any previous installations.
- Install the current published version of Mathesar.

For both:

- Locally download and tag the new version images as `latest`:

    ```sh
    docker image pull mathesar/mathesar-caddy:<version_number>
    docker image tag mathesar/mathesar-caddy:<version_number> mathesar/mathesar-caddy:latest

    docker image pull mathesar/mathesar:<version_number>
    docker image tag mathesar/mathesar:<version_number> mathesar/mathesar:latest
    ```

### Understanding Database connections

#### Database types

- **Mathesar Database** - The Django database used by Mathesar
- **Data database** - The user database(s) being explored in Mathesar's UI

#### Connection types

- **Local** - On the host machine
- **External** - Outside of the host machine
- **Integrated** - Inside of Mathesar's docker image
- **Docker Postgres service** - Postgres service running in a docker compose network

### Tasks

- [ ] Test direct install on Linux and macOS by following our documentation
- [ ] Test all different installation methods
    - [ ] [Docker compose](https://docs.mathesar.org/latest/administration/install-via-docker-compose/)
        - [ ] Local using all default settings
        - [ ] Exposed on domain with different database configurations:
          - [ ] Docker Postgres service Mathesar, Docker Postgres service Data
          - [ ] Docker Postgres service Mathesar, External Data
          - [ ] External Mathesar, External Data
    - [ ] [Docker "Try Mathesar" command](https://docs.mathesar.org/latest/#try-mathesar) with different database configurations:
          - [ ] Integrated Mathesar, Integrated Data
          - [ ] Integrated Mathesar, External Data
    - [ ] Direct install on Linux
        - [ ] Exposed on domain, DB preexisting for all data
        - [ ] Local using all default settings
        - [ ] Exposed on domain with Local Mathesar, Local Data
- [ ] Test that previously installed versions of Mathesar can be upgraded to this release.
    - [ ] Docker compose -- All above variants for docker compose
        - [ ] Same docker compose file, same `.env`
        - [ ] New docker compose file, same `.env`
        - [ ] New docker compose file, bring `.env` into the new file
    - [ ] Direct install on linux (Previously known as Install from scratch) -- All above variants


## User-facing QA {:#users}

!!! tip "Tips:"
    - Don't just aim to complete the tests with the minimum possible steps — try to test the edges around each of the features, seeing if you can hammer at Mathesar to break something or uncover bugs.
    - If you find a bug, try to reproduce it against the latest release (e.g. on the demo site). If you _can_ reproduce it on the latest release, then it's not a regression. It's still worth reporting, but it won't be as high of a priority. If you _can't_ reproduce it on the latest release, then it _is_ a regression. It's important to specify this.
    - The PRs for issues should be based off of the release branch, and merged into the release branch.

Tasks:

- Test create/update/delete for:
    - [ ] Mathesar users
    - [ ] Connection
    - [ ] Schema
    - [ ] Table
    - [ ] Column
    - [ ] Constraint
- Import
    - [ ] Test basic import.
    - [ ] Try different options for "Data Source"
    - [ ] Try different options for "Column Data Types"
- Table Page
    - [ ] Test filtering, sorting, grouping
    - [ ] Test pagination
    - [ ] Test updating cell values for all data types
    - [ ] Test showing/hiding/resizing table inspector and collapsing/expanding sections
    - [ ] Test keyboard shortcuts to move active cell, enter edit mode, save value
    - [ ] Ensure the context menu looks correct for data cells, column header cells, and row header cells
    - [ ] Test table sharing
    - [ ] Test cell selection via: dragging from data cell to data cell, dragging from column header cell to column header cell, dragging from row header cell to row header cell
    - [ ] Test custom record summary template
    - [ ] Test updating column data type
    - [ ] Test updating column display settings
    - [ ] Test setting column default value
    - [ ] Test column re-ordering via drag & drop
    - [ ] Test "Create Link" dialog
    - [ ] Test "Extract Column Into a New Table"
    - [ ] Test "Move Column To Linked Table"
    - [ ] Test "Share" functionality — and test that the share page works
- Record Selector
    - [ ] Test filtering on multiple columns
    - [ ] Test picking an existing record
    - [ ] Test creating a new record from within the record selector
    - [ ] Test selecting a record from within a nested record selector
    - [ ] Test horizontal and vertical scrolling for narrow and short viewports
- Record Page
    - [ ] Test updating direct fields
    - [ ] Test setting field values to null
    - [ ] Test navigating to linked records through linked record input
    - [ ] Test loading a record page with linked records
- Data Explorer
    - [ ] Test creating and saving an exploration from Data Explorer view
    - [ ] Try joining columns from multiple tables without summarization
    - [ ] Try joining columns from multiple tables with summarization
    - [ ] Try renaming column in column properties
    - [ ] Test pagination
    - [ ] Test 'Filter' transformation
    - [ ] Test 'Sort' transformation
    - [ ] Test 'Hide Columns' transformation
    - [ ] Test 'Summarization' transformation
    - [ ] Try summarizing with different aggregations
    - [ ] Test opening an existing exploration
    - [ ] Test editing and saving an existing exploration
    - [ ] Create an exploration from Table page -> Inspector -> Actions -> Explore Data
    - [ ] Test "Share" functionality — and test that the share page works

## Cleanup

!!! info "After QA"
    Cleanup before another round of QA and before publishing the release

- Destroy any infra setup on GCP that was created for QA purposes.
- Delete the pre-release and tag that were created when testing "Direct installation on Linux, macOS, and WSL".
    - Recommended: Do this via the GitHub UI to avoid any potential mistakes.
    - Delete the pre-release.
    - Delete the tag associated with it.
    - Commands, if you're confident:
        ```sh
        VERSION=1.2.3 # ⚠️ CUSTOMIZE THIS

        gh release delete "$VERSION" -y
        git tag -d "$VERSION"
        git push -d origin "$VERSION"
        ```
