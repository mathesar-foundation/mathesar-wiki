# 2023-01-18 Frontend meeting on RFCs

Attendees: Core frontend team

## Problem
* Frontend currently has one person owning and working almost entirely by themselves on a feature.
  * This improves velocity, however it is troublesome for the long run.
  * When the person is not available, it becomes a bottleneck for the entire team.
* The current approach makes it harder for multiple people to collaborate when starting on a new feature.
  * When the feature is considerably large, the person cannot immediately get additional support during the implementation phase, since the rest of the team has little knowledge of the planned implementation details.

## Desired outcome
* An RFC like process to ensure the entire team has an overview of the implementation details for new features.
* We begin this process starting with the Users & Permissions feature.
* This process will only be applicable for new features and major refactoring.
  * When the feature is already implemented to a usable level, it's relatively easier for others to jump in and add enhancements, since they have access to working code. This is further enabled by descriptive GH issues. We're not changing this process.

## Decisions
* Before we start work on a feature, the feature owner will raise a PR on our wiki with a descriptive RFC document which explains 'what' needs to be done.
* The RFC will include sub-tasks. The feature will be split into medium-sized (relative to size of feature) chunks, not too small or big.
    >   - For eg., with Users and Permissions, the tasks will be split as:
    >     - Base work and stores needed for user profile
    >     - Utilites for user permissions
    >     - Account profile route & page
    >     - Users route & page
    >     - Login page rerouting & UI after password change
    >     - Work on each route & page in app to change view based on permission level
    >     - Modal for editing access level in DB page
    >     - Modal for editing access level in schema page  
* The RFC will not go into depth on the implementation details since it will hinder our speed at the current stage of our product.
* It'll target on high level details and on modules which affect the rest of the application.
* It'll target details that are common/used by more than one of the medium-sized chunks.
* It'll include TS interfaces, pseudo-code, and algorithms, wherever applicable.
* It will involve figuring out a high-level architecture, which is subject to changes.
* The RFC can be updated multiple times during the course of implementation, if need arises.
  > - For eg,. with Users and Permissions, the details would be like:
  >   - We'll need a store for user profile, containing username, id, email etc.,
  > 	- We'll have utility methods for current user's permissions which will part of the store.
  >   - This store will be in App context rather than being imported directly.
  >   - There will no stores for users listing. The users page and modals will always make API calls upon initialization.
  > - The RFC will contain TS interfaces for the user profile store and the permission utilities.
  > - The RFC will contain details on how the permission checks will be done on each page of the app.
* Once the RFC is reviewed and merged, we'll create a meta ticket on GH that contains the above medium-sized chunks as tasks.
* This ticket will order the tasks based on priority and mention which tasks block others.
* If the feature is to be worked on by multiple people, we'll assign a developer for the each of the sub tasks.
* The developer assigned to a task follows the RFC, but gets to decide on deeper implementation details without any need to update the RFC.
  - However, if they encounter a scenario which affects other tasks/has higher implications, they will update the RFC and let the rest of the people involved know.
* The developer can further split their tasks into multiple issues if they wish, and control the scope of their tasks.
  - They can decide to de-prioritize portions of their tasks (or in applicable cases, the entire task itself) and move them to later milestones.

