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

### 5. Testing

- Perform a smoke test on the product – Install the library management dataset, [follow the library management demo video](https://www.youtube.com/watch?v=Edbba-h4L-M&t=17s) and ensure everything works as expected.
- Certain releases might require extensive testing. This will be mentioned in the release project spec.

#### If problems are encountered:

- If problems are encountered during testing, make issues in the same release milestone.
- The PRs for issues should be based off of the release branch, and merged into the release branch.
- Once all issues are fixed, restart the process from the step where you [pushed images to Dockerhub](#images).

### 6. Write up Release notes

- Write the release notes and get approval from Kriti.
- These should be written in Markdown outside of GitHub.
- These should not list the issues closed; GitHub will automatically generate that.

## Publishing the release

### 1. Merge into master

1. Merge the release branch into `master`.
1. Ensure the release branch is deleted after merge. This should happen automatically after merging.

!!! warning "Warning"
    Note that after merging the documentation change, if someone is using the docs off of the `master` branch, they'll get a 404 until the tag actually exists. Therefore, avoid going to lunch while things are in this state.

### 2. Create a tag

- Tag the commit you've just merged with the version number of the release.
- Tags are created at https://github.com/centerofci/mathesar/tags. You can also tag locally and push the tag to GitHub.

### 3. Build, tag, and push release Docker images

1. Clone a fresh version of the repo from `master`.
1. `cd` to repository, check out the commit that you've tagged.
1. Make sure you're logged into DockerHub (credentials are in 1Password)
1. Run the following commands, replacing `<version_number>` with the actual version:

    ```sh
    docker buildx create --name container --driver=docker-container
    docker buildx build -t mathesar/mathesar-caddy:<version_number> -t mathesar/mathesar-caddy:latest --builder=container --platform=linux/amd64,linux/arm64 --push -f Dockerfile.caddy .
    docker buildx build -t mathesar/mathesar-prod:<version_number> -t mathesar/mathesar-prod:latest --builder=container --platform=linux/amd64,linux/arm64 --push --build-arg PYTHON_REQUIREMENTS=requirements-prod.txt .
    ```

    Note that the release needs to be tagged as `latest`.

### 4. Create release in GitHub

- Releases are made here: https://github.com/centerofci/mathesar/releases
- The release should be associated with the tag you made in the previous step and use the release notes.
- Auto generate the list of closed issues using GitHub's UI and add them to the release notes. 

### 5. Merge master into develop

- After the release is made successfully, merge the `master` branch into `develop`.


### 6. Update the servers once the release is complete

- The process to update the server is [noted here](server-update-process.md)