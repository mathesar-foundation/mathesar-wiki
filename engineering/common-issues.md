---
title: Common Issues
description: How to fix common issues with the code
published: true
date: 2021-10-12T10:41:11.354Z
tags: 
editor: markdown
dateCreated: 2021-08-31T11:34:49.699Z
---

# Hot module replacement doesn't work on windows
Hot module replacement, currently does not work when the project is present on a windows filesystem and WSL is used to run docker. This is a known limitation of WSL.

Moving the project to a linux filesystem should resolve this.

This issue https://github.com/centerofci/mathesar/issues/570 keeps track of workarounds and detailed discussions on common problems encountered while working on windows.

# npm audit Failures

> Fixing this issue is restricted only to [maintainers](/team). If you are facing this, please notify the maintainers on our [Matrix channels](/community), or raise an issue on GitHub.
{.is-warning}

If the `audit` check on your pull request fails, here are the steps to fix it:

* If the audit failure indicates that the issues are auto-fixable, the following commands need to be run to fix them:
	```
	npm audit fix
	npm install
	```
  
  Please make sure to run these within the container only. If you are running Mathesar locally, without Docker, make sure you use the same node and npm versions.
* If the issues are non auto-fixable, identify the packages that are vulnerable.
	- If they are directly used packages, update their versions.
  - If they are dependencies of packages used by us (most common), update the parent packages.
  - Most often, newer parent packages may not have been released yet. In which case, we can use the 'resolutions' field in package.json to force the version of packages. Make sure to only update it to the closest non-vulnerable minor release, in this case.
  - Force resolving dependencies to a particular version should only be done when the vulnerabilities are not false positives. [This article](https://overreacted.io/npm-audit-broken-by-design/) by Dan Abramov from the React team, gives a good explanation on why most reported vulnerabilities are false positives.

# Error while running docker-compose up

* On running `docker-compose up` command, gets an Error like:
> ERROR: for db Cannot start server db: driver failed programming external connectivity on endpoint mathesar_db (70c521f468cf2bd54014f089f0051ba28e2514667): Error starting userland proxy: listen tcp4 0.0.0.0:5432: bind: address already in use.

* The above Error indicates that port usually used by Postgres is already in use.
 
* Here are some steps to solve this Error.
 - The Docker container won't start if a Postgres server is already running on your host machine. To stop that run:
  `sudo service postgresql stop`.
 - Then run `docker-compose up` again.

* This will solve the above Error, If still getting some Error then feel free to ask in IRC channel.

> Note that you'll need to manually start your Postgres server on your host machine again if you want to continue working on other projects which rely on that. And the next time you restart your machine, you'll probably need to stop Postgres again before you can begin working on Mathesar.
{.is-warning}


