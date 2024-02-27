# Release QA testing

This page describes manual QA testing routines that we perform before a release.

## Administrator-facing QA {:#admin}

- [ ] Test installing the release from scratch by following our documentation
- [ ] Test all different installation methods
    - [ ] Docker compose
        - [ ] All defaults, local
        - [ ] Exposed on domain, DB managed by Mathesar
        - [ ] Exposed on domain, DB preexisting for users, managed DB for Django
        - [ ] Exposed on domain, DB preexisting for all data
    - [ ] Docker integrated image
        - [ ] All defaults, local
        - [ ] Exposed on domain, DB managed by Mathesar
        - [ ] Exposed on domain, DB preexisting for users, managed DB for Django
        - [ ] Exposed on domain, DB preexisting for all data
    - [ ] Build from scratch
        - [ ] All defaults, local
        - [ ] Exposed on domain, DB preexisting for all data
- [ ] Test that previously installed versions of Mathesar can be upgraded to this release.
    - [ ] Docker compose -- All above variants for docker compose
        - [ ] Same docker compose file, same `.env`
        - [ ] New docker compose file, same `.env`
        - [ ] New docker compose file, bring `.env` into the new file
    - [ ] Build from scratch -- All above variants for build from scratch

### Test the installation process for the new version

1. Clear out your docker containers, images, and volumes:

    ```sh
    docker rm -f $(docker ps -a | awk '{print $1}')
    docker rmi $(docker image ls | awk '{print $3}')
    docker volume rm $(docker volume ls | awk '{print $2}')
    ```
    This is just to ensure that the below validation starts from a known state.

1. Clear out remains of any previous installations.

	- Delete `.env` file and `docker-compose.yml` file within `/etc/mathesar`.

1. Locally tag the new version as `latest`:

    ```sh
    docker image pull mathesar/mathesar-caddy:<version_number>
    docker image tag mathesar/mathesar-caddy:<version_number> mathesar/mathesar-caddy:latest
    
    docker image pull mathesar/mathesar-prod:<version_number>
    docker image tag mathesar/mathesar-prod:<version_number> mathesar/mathesar-prod:latest
    ```

1. Install the new version:

    ```sh
    bash <(curl -sL https://raw.githubusercontent.com/mathesar-foundation/mathesar/<version_number>/install.sh)
    ```

    - Note that the installation command will vary based on the installation method you use. The above command used the interactive installer.
    - Ensure that the installation process does not throw any errors.

### Test upgrades

!!! tip "Optional"
    This only needs to be performed for releases which have changes to installation/upgrade setup.

- In case if the release contains changes to installation/upgrade setup, we need to attempt all installation methods and upgrade processes additionally.
- Ideally, this testing would already be taken care of during the course of the release projects.
- To test upgrades for the docker-compose setup, follow the below steps:
    - Clean up local docker images and containers.
    - Install the current published version of Mathesar.
        - Eg., Assuming the current version is `0.1.0`, and the new version we need to release is `0.1.1`:

            ```sh
            bash <(curl -sL https://raw.githubusercontent.com/mathesar-foundation/mathesar/0.1.0/install.sh)
            ```

    - Open Mathesar on browser, create a few tables. Ensure the version shown in the product is the old one. i.e `0.1.0`.
    - Run the following commands while Mathesar is running:

        ```sh
        docker image pull mathesar/mathesar-caddy:0.1.1
        docker image tag mathesar/mathesar-caddy:0.1.1 mathesar/mathesar-caddy:latest

        docker image pull mathesar/mathesar-prod:0.1.1
        docker image tag mathesar/mathesar-prod:0.1.1 mathesar/mathesar-prod:latest
        ```

        - Replace `0.1.1` with the new version number.
    - Open browser, make the following request manually. The request cannot be made via UI since there isn't a GH release at this point:

        ```js
        fetch('http://localhost/api/ui/v0/upgrade/', { method: 'POST', headers: { 'X-CSRFToken': '<replace_with_csrf_token>', 'Content-Type': 'application/json' }, body: JSON.stringify({}) });
        ```
    - The CSRF token can be found by looking at your cookies. It is named csrftoken.
    - Reload the page after request ends. Mathesar should now be upgraded.
    - Ensure the version in the Software update page shows the new version. Eg., `0.1.1`.
        - It will show an error saying release notes aren't present. This is expected.
    - Ensure that the upgrade process does not throw any errors.

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
