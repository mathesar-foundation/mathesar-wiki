# Publishing a release

!!! warning "Warning"
    These steps are currently structured in a manner that is convenient for Mathesar developer but leaves a window open during which the documentation will be out of sync with other assets required for installation and upgrades.

    For example: the docs get published as soon as the release PR is merged into master. At that point the tag won't yet exist in GitHub (meaning readers won't be able to download the referenced docker-compose file) and the image won't yet exist on DockerHub.
    
    We would like to improve this process. But in the mean time, be sure to follow these steps quickly so as to reduce the duration of this "out of sync" window.

1. **Set a VERSION variable in your shell**

    Run this command to set a local variable within your shell to the version number of the release you're making.

    ```sh
    VERSION=1.2.3 # ⚠️ CUSTOMIZE THIS
    ```

1. **Merge the release PR**

    This should merge the release branch into `master`. Before moving on, ensure the release branch is deleted within GitHub after merge. This should happen automatically after merging.

1. **Create the tag**

    Locally tag the commit you've just merged with the version number of the release. Then push to GitHub.

    ```sh
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

    From the [Releases page](https://github.com/mathesar-foundation/mathesar/releases), click "Draft a new release".

    - Choose the tag you just created.
    - The title should be formatted like `Version 0.1.3 (alpha release)`
    - Click "Generate release notes"
    - Edit the release body markdown to hyperlink to the release notes as published on docs.mathesar.org.
    - "Set as a pre-release" should be false
    - "Set as the latest release" should be true
    - "Create a discussion for this release" should be false

1. **Merge master into develop**

    After the release is made successfully, merge the `master` branch into `develop`. Open a new PR for this and queue it to merge when the workflows finish.