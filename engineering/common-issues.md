---
title: Common Issues
description: How to fix common issues with the code
published: true
date: 2021-08-31T11:34:49.699Z
tags: 
editor: markdown
dateCreated: 2021-08-31T11:34:49.699Z
---

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
  
Issue https://github.com/centerofci/mathesar/issues/124 should ensure that audit failures do not fail the workflows, but instead raise a GH issue automatically.
