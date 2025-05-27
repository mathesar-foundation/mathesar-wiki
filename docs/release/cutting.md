# Cutting a release

When we "cut" a release, we _begin_ the process of making a release. (This is not to be confused with [_publishing_](./publication.md) a release, which is the last step.) After a release is cut, we can perform manual QA testing and polish any remaining small changes.

<!--
  NOTE TO DOCS EDITORS:

  This page has a substantial amount of content duplicated with publication.md.
  Be sure to propagate changes there as necessary.
-->

1. **Set a VERSION variable in your shell**

    Run this command to set a local variable within your shell to the version number of the release you're making.

    ```sh
    VERSION=1.2.3 # ⚠️ CUSTOMIZE THIS
    ```

    !!! note
        Do _not_ prefix the version with `v`.

1. **Cut the release branch**

    Run these commands from within the repo, locally.

    ```sh
    git checkout develop
    git pull origin develop
    git checkout -b release-$VERSION
    ```

1. **Notify team that release branch is cut**

    This is important because engineers will need to know to target the release branch with any subsequent PRs intended for the release.

1. **Update version numbers**

    ```sh
    sed -i "s/^__version__ =.*\$/__version__ = \"$VERSION\"/" mathesar/__init__.py
    sed -i "s/^  mathesar_version:.*\$/  mathesar_version: $VERSION/" docs/mkdocs.yml
    git commit -a -m "Update version numbers to $VERSION"
    ```

1. **Create the release PR**

    ```sh
    git push -u origin release-$VERSION
    gh pr create -d -B master -m "v$VERSION" -t "Release $VERSION" -b ""
    ```

1. **Publish Docker images for QA**

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
        git clone -b release-$VERSION --single-branch --no-tags "$REPO_DIR" .
        ```

        (This ensures that files which are ignored by git don't end up in the Docker image.)

    1. Build and push images to DockerHub

        ```sh
        docker buildx build \
          -t mathesar/mathesar-caddy:$VERSION \
          --builder=cloud-mathesar-release-builder \
          --platform=linux/amd64,linux/arm64 \
          --push \
          -f Dockerfile.caddy .

        docker buildx build \
          -t mathesar/mathesar:$VERSION \
          --builder=cloud-mathesar-release-builder \
          --platform=linux/amd64,linux/arm64 \
          --push .
        ```

        (These images are intentionally not tagged as latest — that will happen during [publication](./publication.md).)

        If you have trouble running these commands, make sure you've run the [prerequisite setup steps](./index.md#prerequisites).

    1. Clean up

        ```sh
        cd "$REPO_DIR"
        rm -rf $CLEAN_REPO_DIR
        docker logout
        ```


1. **Create a pre-release for QA**

    1. Create and push a tag on GitHub with the release version.

        ```sh
        git checkout "release-$VERSION"
        git pull
        git tag "$VERSION"
        git push origin "$VERSION"
        ```

    1. GH will automatically create a draft release containing the installation assets for this tag. This will take a few minutes.

    1. Update the release name & description to make it clear that it's a testing release.

    1. Publish this draft release as a `Pre-release` via the GitHub UI.

        !!! warning "Do not set the release as `latest`"
            - Ensure that the checkbox mentioning `latest` is **not checked**.
            - Only set the release as a `Pre-release`.
            - Double check this before publishing.
