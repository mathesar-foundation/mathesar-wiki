# Release Process

These are the steps that we follow for creating a new Mathesar release.

## Pre-release

The owner of the release project will be responsible for publishing a new Mathesar release.

For details on the Release management process, refer the [Release management ongoing responsibility document](/team/responsibilities/release-management.md).

### 1. Track the process in a GH issue {:#tracking-issue}

Create a meta issue to track progress of the release process with the label `work: release`. Follow the template of [Release 0.1.1](https://github.com/centerofci/mathesar/issues/2705).

### 2. Create the release branch and update version number {:#create-branch}

1. Create a new git branch for the release based on `develop`.

    Use a name like `0.1.2`. (Don't prefix with `v`.)

1. On the release branch, push a commit which updates the version number in the following places:

    - In  `mathesar/__init__.py`
    - In `install.sh`

        This should be the default value for the `github_tag` variable. For example, for version `0.1.3`, you'd put ;

        ```
        github_tag=${1-"0.1.3"}
        ```

    - In the documentation for the Installation instructions

### 3. Push images to Dockerhub {:#images}

!!! caution
    Do **not** tag as `latest`. Customized these commands with the specific release version number.

1. Clone the branch locally.
1. Ensure you're logged into Dockerhub. (Credentials are in 1Password.)
1. Run the following commands to build images from the branch and push the images to Dockerhub with the specified version number.

    ```sh
    docker buildx create --name container --driver=docker-container
    docker buildx build -t mathesar/mathesar-caddy:<version_number> --builder=container --platform=linux/amd64,linux/arm64 --push -f Dockerfile.caddy .
    docker buildx build -t mathesar/mathesar-prod:<version_number> --builder=container --platform=linux/amd64,linux/arm64 --push --build-arg PYTHON_REQUIREMENTS=requirements-prod.txt .
    ```

    These images are not tagged as latest will not affect installation flow for users.

- Log out of Dockerhub to avoid accidental pushes during testing.

### 4. Test the installation process for the new version

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
    bash <(curl -sL https://raw.githubusercontent.com/centerofci/mathesar/<version_number>/install.sh)
    ```

    - Note that the installation command will vary based on the installation method you use. The above command used the interactive installer.
    - Ensure that the installation process does not throw any errors.

#### (Optional) For releases which have changes to installation/upgrade setup:

- In case if the release contains changes to installation/upgrade setup, we need to attempt all installation methods and upgrade processes additionally.
- Ideally, this testing would already be taken care of during the course of the release projects.
- To test upgrades for the docker-compose setup, follow the below steps:
    - Clean up local docker images and containers.
    - Install the current published version of Mathesar.
   		- Eg., Assuming the current version is `0.1.0`, and the new version we need to release is `0.1.1`:

            ```sh
            bash <(curl -sL https://raw.githubusercontent.com/centerofci/mathesar/0.1.0/install.sh)
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

### 5. QA testing

#### For Administrators

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
          
        
#### For users

Tips:

- Don't just aim to complete the tests with the minimum possible steps — try to test the edges around each of the features, seeing if you can hammer at Mathesar to break something or uncover bugs.
- If you find a bug, try to reproduce it against the latest release (e.g. on the demo site). If you _can_ reproduce it on the latest release, then it's not a regression. It's still worth reporting, but it won't be as high of a priority. If you _can't_ reproduce it on the latest release, then it _is_ a regression. It's important to specify this.
- The PRs for issues should be based off of the release branch, and merged into the release branch.
- Once all issues are fixed, restart the process from the step where you [pushed images to Dockerhub](#images).

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

### 6. Write up Release notes

- Write the release notes and get approval from Kriti.
- These should be written in Markdown outside of GitHub.
- These should not list the issues closed; GitHub will automatically generate that.

## Publishing the release

!!! warning "Warning"
    These steps are currently structured in a manner that is convenient for Mathesar developer but leaves a window open during which the documentation will be out of sync with other assets required for installation and upgrades.

    For example: the docs get published as soon as the release PR is merged into master. At that point the tag won't yet exist in GitHub (meaning readers won't be able to download the referenced docker-compose file) and the image won't yet exist on DockerHub.
    
    We would like to improve this process. But in the mean time, be sure to follow these steps quickly so as to reduce the duration of this "out of sync" window.

1. **Merge the release PR**

    This should merge the release branch into `master`. Before moving on, ensure the release branch is deleted within GitHub after merge. This should happen automatically after merging.

1. **Create the tag**

    Locally tag the commit you've just merged with the version number of the release. Then push to GitHub.

    ```sh
    VERSION=0.1.4 # ⚠️ CUSTOMIZE THIS
    git checkout master
    git pull
    git branch -d $VERSION
    git tag $VERSION
    git push origin $VERSION
    ```

1. **Publish Docker images**

    1. Clone a fresh version of the repo from `master`.

        A fresh clone is necessary because all files in the directory will be present within the built Docker image. You don't want to have any ignored files like `.env` in there.

    1. `cd` to repository, check out the commit that you've tagged.
    1. Make sure you're logged into DockerHub (credentials are in 1Password)
    1. Run the following commands:

        ```sh
        VERSION=0.1.4 # ⚠️ CUSTOMIZE THIS

        docker buildx create --name container --driver=docker-container

        docker buildx build \
          -t mathesar/mathesar-caddy:$VERSION \
          -t mathesar/mathesar-caddy:latest \
          --builder=container \
          --platform=linux/amd64,linux/arm64 \
          --push \
          -f Dockerfile.caddy .

        docker buildx build \
          -t mathesar/mathesar-prod:$VERSION \
          -t mathesar/mathesar-prod:latest \
          --builder=container \
          --platform=linux/amd64,linux/arm64 \
          --push \
          --build-arg PYTHON_REQUIREMENTS=requirements-prod.txt .
        ```

        Note that the release needs to be tagged as `latest`.

1. **Create GitHub release**

    From the [Releases page](https://github.com/centerofci/mathesar/releases), click "Draft a new release".

    - Choose the tag you just created.
    - The title should be formatted like `Version 0.1.3 (alpha release)`
    - Click "Generate release notes"
    - Edit the release body markdown to hyperlink to the release notes as published on docs.mathesar.org.
    - "Set as a pre-release" should be false
    - "Set as the latest release" should be true
    - "Create a discussion for this release" should be false

1. **Merge master into develop**

    After the release is made successfully, merge the `master` branch into `develop`. Open a new PR for this and queue it to merge when the workflows finish.

## Post release

1. Update the servers once the release is complete

    The process to update the server is [noted here](server-update-process.md)

