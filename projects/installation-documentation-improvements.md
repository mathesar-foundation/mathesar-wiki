---
title: Installation Documentation Improvements
description: 
published: true
date: 2023-04-06T23:01:23.177Z
tags: 
editor: markdown
dateCreated: 2023-04-06T19:15:47.704Z
---

**Name**: Improve Mathesar Installation documentation
**Status**: In review

## Team

| Role                                   | Assignee                                         | Notes                                                                      |
|----------------------------------------|--------------------------------------------------|----------------------------------------------------------------------------|
| **Owner**                              | Kriti                                            |                                                                            |
| **Approver (project plan)**            | Kriti                                            | *Needs to approve project plan*                                            |
| **Contributor (requirements)**         | Mukesh                                           | *Creates GitHub issues*                                                    |
| **Contributor (documentation)**        | Mukesh                                           | *Creates Documentation*                                                    |
| **Contributor (documentation review)** | Pavish, Marius (contractor)                      | *Reviews documentation*                                                    |
| **Contributor (Testing)**              | Pavish, Contractors from Upwork(yet to be hired) | *Test out the instructions from the documentation and make sure they work* |
| **Contributor (Hiring)**               | Kriti                                            | *Hire contributors from Upwork to help with testing*                       |

## Problem
* Users are trying to use Mathesar with various setups and our installation documentation is lacking information to help them with it
  - Only Docker-based installation is listed in our docs. But [Users want to install Mathesar without using Docker](https://news.ycombinator.com/item?id=35007769)
  - Configuration files don't have enough comments, [preventing users from tinkering.](https://github.com/centerofci/mathesar/issues/2655#issuecomment-1465731661)
  - The installation script is tightly coupled, [preventing them from using it with their own setup](https://hackmd.io/wUpuiOwLRhGDy2y7H-ccHw). The user cannot use the script to do only certain tasks, for example, they cannot use the script to only create a configuration file and skip other steps. 
  - The installation script asks for `sudo` access, [so some users are not comfortable with it](https://github.com/centerofci/mathesar/issues/2761)
  - Users want to use Mathesar with Kubernetes, Nomad etc. Our docker-compose script won't be helpful in such cases

## Solution
- Add Documentation for setting up Mathesar with the Mathesar Service Docker Image
- Add Documentation for installing Mathesar without using install.sh
- Documenting our config files so user can manually edit them
- Documenting setting up Mathesar without Docker
- Documenting upgrades and changes in UI to add instructions for non-docker-compose environments
- Document limitations involved with the installation script.
- Separate docker-compose file for production

## Risks
- There are unknowns with testing since we’re hiring external people, which might affect the timeline.
- Issues uncovered during testing might affect the timeline.

## Resources
- **Issues**: [GitHub meta issue](https://github.com/centerofci/mathesar/issues/2789)

## Timeline
This project should take **2 weeks** and additionally **2 weeks** for testing, so **4 weeks** in total. Testing will start happening in  parallel as soon as a documentation gets completed.


| Date       | Outcome                                                                                                                                                                     |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 2023-04-10 | Work starts                                                                                                                                                                 | 
| 2023-04-12 | Testing + Review of the PRs starts in parallel                                                                                                                              |
| 2023-04-14 | PR ready for all the issues in the meta issue #2789 except [Allow users to install Mathesar without Docker (on Debian)](https://github.com/centerofci/mathesar/issues/2427) |
| 2023-04-20 | PR for all issues in the meta issue #2789 should be in review state                                                                                                         |
| 2023-05-5  | Testing, review, addressing review complete                                                                                                                                 |