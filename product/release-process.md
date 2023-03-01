---
title: Release Process
description: Steps we follow when creating a release of Mathesar
published: true
date: 2023-03-01T08:55:45.534Z
tags: 
editor: markdown
dateCreated: 2023-02-24T12:48:27.636Z
---

These are the steps that we follow for creating a new Mathesar release.

# Pre-release
## 1. Designate a release owner
The release owner is in charge of carrying out the steps to create a release and coordinating with the rest of the team as needed.

## 2. Ensure product is release-ready
- In a branch off `master`, update the version number in the repo in  `mathesar/__init__.py`
  - We use semantic versioning. The alpha release of Mathesar will be `0.1.0` and upcoming releases should be `0.1.x` where `x` is incremented.
- Also update the version number in `install.sh` if needed.
	- This should be the default value for the `github_tag` variable. For example, for version `0.0.3`, you'd put 
    ```sh
    github_tag=${1-"0.0.3"}
    ```
- Clear out your docker containers, images, and volumes:
  ```sh
  docker rm -f $(docker ps -a | awk '{print $1}')
  docker rmi $(docker image ls | awk '{print $3}')
  docker volume rm $(docker volume ls | awk '{print $2}')
  ```
  This is just to ensure that the below validation starts from a known state.
- Create local builds of the prod and caddy Docker images (no need for multiplatform at this stage):
  ```sh
  docker build --build-arg PYTHON_REQUIREMENTS=requirements-prod.txt -t mathesar/mathesar-prod:latest .
  docker build -t mathesar/mathesar-caddy:latest -f Dockerfile.caddy .
  ```
- Push your branch to github, and run `install.sh` on the commit you've made and make sure everything works.
  ```sh
  ./install.sh <your_branch_name>
  ```
- Do a quick smoke test on the product – ensure you can
  - log in
  - create a schema
  - edit records
- Modify the docs to use the correct install script for this tag. For example, if the version is 0.0.3 (and so the tag is 0.0.3), use:
  ```sh
  bash <(curl -sL https://raw.githubusercontent.com/centerofci/mathesar/0.0.3/install.sh)
  ```
  Note that at this point, if someone is using the docs off of the `master` branch, they'll get a 404 until the tag actually exists. Therefore, avoid going to lunch while things are in this state.
- Merge the branch to `master`

## 3. Create a tag
- Tag the commit you've just merged with the version number of the release.
- Tags are created at https://github.com/centerofci/mathesar/tags. You can also tag locally and push the tag to GitHub.

## 4. Write release notes
- Coordinate with Kriti to write the release notes
- These should be written in Markdown outside of GitHub

# Release process
## 1. Create, tag, and push release Docker images
- Clone a fresh version of the repo.
- `cd` to repository, check out the commit that you've tagged.
- Make sure you're logged into DockerHub (credentials are in 1Password)
- Run the following commands, replacing `<version_number>` with the actual version:
  ```sh
  docker buildx create --name container --driver=docker-container
  docker buildx build -t mathesar/mathesar-caddy:<version_number> -t mathesar/mathesar-caddy:latest --builder=container --platform=linux/amd64,linux/arm64 --push -f Dockerfile.caddy .
  docker buildx build -t mathesar/mathesar-prod:<version_number> -t mathesar/mathesar-prod:latest --builder=container --platform=linux/amd64,linux/arm64 --push --build-arg PYTHON_REQUIREMENTS=requirements-prod.txt .
  ```

## 2. Create release in GitHub
1. Releases are made here: https://github.com/centerofci/mathesar/releases
2. The release should be associated with the tag you made in the previous step and use the release notes.

