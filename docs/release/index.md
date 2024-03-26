# Release process

## Steps

1. Plan the release — this is done in Basecamp and GitHub milestones
1. [Cut the release](./cutting.md)
1. [QA the release](./qa.md) and [write the release notes](./notes.md)
1. [Publish the release](./publication.md)
1. [Update our servers](../engineering/server-update-process.md)
1. Announce the release

## Prerequisites

Some of the commands within our release process require you to have the following utilities installed.

- **[buildx](http://github.com/docker/buildx)**

    Depending on how you installed Docker, you may already have this. Verify with:

    ```
    docker buildx version
    ```

    Your version of buildx needs to contain the "cloud driver". We think buildx `0.12.1` or newer should suffice. You may need to install Docker 25.0.3 or newer to get this version of buildx.

- Create a local instance of our cloud driver:

    ```
    docker buildx create --driver cloud mathesar/release-builder
    ```

    This will create a Docker container on your system. You'll need to do this step again if you delete that container at some point.

- **gh** (aka the [GitHub CLI](https://cli.github.com/))

    Verify with:

    ```
    gh --version
    ```

