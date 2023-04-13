---
title: Installation Documentation Improvements
description: 
published: true
date: 2023-04-13T06:24:48.302Z
tags: 
editor: markdown
dateCreated: 2023-04-06T19:15:47.704Z
---

**Name**: Improve Mathesar Installation documentation
**Status**: In review

## Team

| Role                                   | Assignee                                          | Notes                                                                      |
|----------------------------------------|---------------------------------------------------|----------------------------------------------------------------------------|
| **Owner**                              | Mukesh                                            |                                                                            |
| **Approver (project plan)**            | Kriti                                             | *Needs to approve project plan*                                            |
| **Approver (project plan)**            | Brent                                             | *Needs to approve project plan*                                            |
| **Contributor (requirements)**         | Mukesh                                            | *Creates GitHub issues*                                                    |
| **Contributor (documentation)**        | Mukesh                                            | *Creates Documentation*                                                    |
| **Contributor (documentation review first pass)** | Pavish, Marius (contractor)            | *Reviews documentation and the docker-compose code changes*                |
| **Contributor (documentation review second pass)** | Kriti                                 | *Reviews documentation after Pavish and Marius have reviewed it*           |  
| **Contributor (Testing)**              | Pavish, Contributors from Upwork(yet to be hired) | *Test out the instructions from the documentation and make sure they work* |
| **Contributor (Hiring)**               | Kriti                                             | *Hire contributors from Upwork to help with testing*                       |

## Problem
* Users are trying to use Mathesar with various setups and our installation documentation is lacking information to help them with it
  1. Users want to use Mathesar with Kubernetes, Nomad etc. Our docker-compose script won't be helpful in such cases
	2. The installation script asks for `sudo` access, [so some users are not comfortable with it](https://github.com/centerofci/mathesar/issues/2761)
  3. The installation script is tightly coupled, [preventing them from using it with their own setup](https://hackmd.io/wUpuiOwLRhGDy2y7H-ccHw). The user cannot use the script to do only certain tasks, for example, they cannot use the script to only create a configuration file and skip other steps. 
 	4. Configuration files don't have enough comments, [leading to confusion](https://github.com/centerofci/mathesar/issues/2655#issuecomment-1465731661) when users try to change it manually.
  5. Only Docker-based installation is listed in our docs. But [Users want to install Mathesar without using Docker](https://news.ycombinator.com/item?id=35007769)
  6. The docker-compose file is [complex](https://www.reddit.com/r/selfhosted/comments/11n2fxx/comment/jbnmdvi/?utm_source=share&utm_medium=web2x&context=3)



## Solution
- [Add Documentation for setting up Mathesar with the Mathesar Service Docker Image](https://github.com/centerofci/mathesar/issues/2783). Fixes Problem[a]
- [Add Documentation for installing Mathesar without using install.sh](https://github.com/centerofci/mathesar/issues/2761). Fixes Problem[b] and [c]
- [Documenting our config files so user can manually edit them](/en/projects/installation-documentation-improvements)https://github.com/centerofci/mathesar/issues/2784). Fixes Problem[d]
- [Documenting setting up Mathesar without Docker](https://github.com/centerofci/mathesar/issues/2427). Fixes Problem[e]
- [Document upgrade instructions for non-docker-compose environments](https://github.com/centerofci/mathesar/issues/2785)
- [Document limitations involved with the installation script](https://github.com/centerofci/mathesar/issues/2787). Auxiallary fix for Problem[b] and [c]
- [Separate docker-compose file for production](https://github.com/centerofci/mathesar/issues/2788). Fixes Problem[f]

## Risks
- There are unknowns with testing since we’re hiring external people, which might affect the timeline.
- Issues uncovered during testing might affect the timeline.

## Resources
- **Issues**: [GitHub meta issue](https://github.com/centerofci/mathesar/issues/2789)

## Timeline
This project should take **3 weeks** for the features to be implemented, tested, reviewed and additionally **1 week** for final testing, so **4 weeks** in total. Testing will start happening in  parallel as soon as a documentation gets completed.


| Date       | Outcome                                                                                                                                                                                                                                                          |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 2023-04-11 | Work starts, we start PRs which make changes to the code and then move to documentation.                                                                                                                                                                                      | 
| 2023-04-13 | Review of the PRs starts in parallel                                                                                                                                                                                                                             |
| 2023-04-16 | Instructions(scenarios to test on like Non-root user, OS etc) for the Testing team will be created                                                                                      |
| 2023-04-17 | PR ready for all the issues in the meta issue #2789 except [Allow users to install Mathesar without Docker (on Debian)](https://github.com/centerofci/mathesar/issues/2427)                                                                                      |
| 2023-04-17 | Feedback + Testing(both done by the testing team) for **documentation** PRs starts in parallel. This ensures the documentation can be understood by different user segments(technical users, less technical users) and works with various scenarios |
| 2023-04-21 | PR for all issues in the meta issue #2789 should be in review state.                                                                                                                                                                                             |
| 2023-04-28 | All the PRs in #2789 are merged. #2789 will still be open in order to address any issues found during the Final testing done in the next step.                                                                                                                   |
| 2023-04-28 | Final Testing starts. The documentation would already been tested to a good extent at this point. The final testing ensures there is no change is needed(very minimal if any)                                                                                    |
| 2023-05-05 | Final Testing, review, addressing review complete                                                                                                                                                                                                                |