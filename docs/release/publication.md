# Publishing a release

!!! warning "Warning"
    These steps are currently structured in a manner that is convenient for Mathesar developer but leaves a window open during which the documentation will be out of sync with other assets required for installation and upgrades.

    For example: the docs get published as soon as the release PR is merged into master. At that point the tag won't yet exist in GitHub (meaning readers won't be able to download the referenced docker-compose file) and the image won't yet exist on DockerHub.
    
    We would like to improve this process. But in the mean time, be sure to follow these steps quickly so as to reduce the duration of this "out of sync" window.

<!--
  NOTE TO DOCS EDITORS:

  This page has a substantial amount of content duplicated with cutting.md.
  Be sure to propagate changes there as necessary.
-->

1. **Set a VERSION variable in your shell**

    Run this command to set a local variable within your shell to the version number of the release you're making.

    ```sh
    VERSION=1.2.3 # ⚠️ CUSTOMIZE THIS
    ```

    !!! note
        Do _not_ prefix the version with `v`.

1. **Merge the release notes PR** (if not yet done)

    This should merge the release notes file into the release branch.

1. **Merge the release PR**

    This should merge the release branch into `master`.
    
    Before moving on, ensure the release branch is deleted within GitHub after merge. This should happen automatically after merging. The PR should show an entry in the activity timeline like:

    > seancolsen deleted the `0.1.5` branch 1 minute ago

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

    1. Log in to DockerHub

        ```sh
        docker login
        ```

        (Use your personal Docker credentials. Your personal Docker account will need to be a member of our [mathesar Docker org](https://hub.docker.com/orgs/mathesar/members).)

    1. Locally clone the repo into a clean directory and go there.

        ```sh
        REPO_DIR=$(pwd)
        CLEAN_REPO_DIR=$(mktemp -d)
        cd $CLEAN_REPO_DIR
        git clone -b master --single-branch --no-tags "$REPO_DIR" .
        ```

        (This ensures that files which are ignored by git don't end up in the Docker image.)

    1. Run the following commands:

        ```sh
        docker buildx build \
          -t mathesar/mathesar-caddy:$VERSION \
          -t mathesar/mathesar-caddy:latest \
          --builder=cloud-mathesar-release-builder \
          --platform=linux/amd64,linux/arm64 \
          --push \
          -f Dockerfile.caddy .

        docker buildx build \
          -t mathesar/mathesar-prod:$VERSION \
          -t mathesar/mathesar-prod:latest \
          --builder=cloud-mathesar-release-builder \
          --platform=linux/amd64,linux/arm64 \
          --push \
          --build-arg PYTHON_REQUIREMENTS=requirements-prod.txt .
        ```

        These commands build, push, and tag the images as `latest`.

1. Clean up

    ```sh
    cd "$REPO_DIR"
    rm -rf $CLEAN_REPO_DIR
    docker logout
    ```

1. **Create GitHub release**

    ```
    gh release create \
      --latest \
      --title "Version $VERSION (alpha release)" \
      --notes "__[Release notes](https://docs.mathesar.org/releases/$VERSION/)__" \
      $VERSION
    ```

1. **Merge master into develop**

    GitHub will automatically create a PR for this. Find it and merge it.

1. **Close the release milestone**

    Move any outstanding issues to the next milestone.

