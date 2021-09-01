---
title: September 2021 meeting notes
description: 
published: true
date: 2021-09-01T12:10:46.346Z
tags: 
editor: markdown
dateCreated: 2021-09-01T12:10:46.346Z
---

# 2021-09-03

**Meeting topic**: "State of Mathesar", part 2 - progress so far and next steps.  
**Attendees**: Brent, Ghislaine, Kriti, Pavish

Please see the previous meeting's notes below to get full context for this meeting.

## Process Retrospective

### Product process
*Notes will be added after the meeting.*

### Design process
*Notes will be added after the meeting.*

Topics brought up at the previous meeting:

- We're focusing on designing features, not about how to guide non-technical users through the designs.
    - Do we need to complete the features first before guiding the users first?
        - We can't guide users until the product is fully finished.
        - Some decisions need to be made with that in mind.
    - Two stage process:
        - Test with users and make improvements before release
        - Continue to make imporvements after release.

### Frontend
*Notes will be added after the meeting.*

### Backend 
*Notes will be added after the meeting.*

Topics brought up at the previous meeting:

- How to take a better approach to iteration?

### Frontend & backend collaboration
*Notes will be added after the meeting.*

### Weekly planning
*Notes will be added after the meeting.*

## Deadline Review
*Notes will be added after the meeting.*

# 2021-09-01

**Meeting topic**: "State of Mathesar", part 1 - progress so far and next steps.  
**Attendees**: Brent, Ghislaine, Kriti, Pavish

## Introduction
- We've been focusing mainly on day-to-day work for a while now.
- This meeting's goal is to take some time to look at the bigger picture.

## State of Mathesar
### Where we are
- The entire team has been working together for about 2.5 months
- 6 milestones (4 feature milestones) and 200+ issues closed
- Until Monday, we had 20 more feature milestones to go.
  - It would be untenable to complete those in 3 months, even with more team members.
  - This was anticipated, our roadmap was fairly ambitious.
- Now we have 13 more to go, with the timeline extended to December. 

### Our goals
- Our timeline has not changed, ship an alpha version of Mathesar in 2021.
  - Timeline can be extended from November to December, but we can't go longer than that.
  - We only have funding (currently) through the end of 2022, it's essential that we have as much time as possible to find Mathesar some users.
- Our product goal is to show the value proposition of Mathesar in our alpha release.

### Getting to our goals
Steps for getting to our goal (and agenda for this meeting):

- Make sure we're on the same page about the vision for Mathesar
- Organize our planned features into:
  - Essential for alpha (alpha: release to a few specific users)
  - Essential for the beta, but not alpha (beta: release to the public)
  - Nice to have for the alpha or beta
- Talk through our process and come up with potential improvements to increase speed (without sacrificing quality).
  - A secondary goal is to increase community-friendliness.
- Ensure our milestones and associated deadlines make sense.

## Vision for Mathesar

Also doubles as the value proposition for Mathesar.

- Self-hosted
- Works with existing DBs
- Modular (`db` vs. API vs. client)
- Encourages exploration
- Works for non-technical users
- Works for technical users

See also: [Product Principles](https://wiki.mathesar.org/product/principles)

- Are we sticking to these well? Any feedback?
    - We're all in agreement about the vision and product principles

## Planned Features
- Should we have features between alpha and beta or should beta just be focused on stabilizing the features in the alpha release.
    - Alpha doesn't include viz yet, but having those for beta might be valuable enough
        - maybe also plugins
    - When do we want to do beta release
        - March 2021
        - Will that be enough time to build in features?
            - Maybe plugins and viz aren't too intensive?
            - We'll also have a bigger team
        - We need time for public launch related tasks, e.g. branding, documentation
- Kriti will make updates to milestones based on categorization below

### Alpha
* Editable Tables
* Working with Tables
* Initial Data Types
* Working with Views
* Data Modeling
* Multiple Database Support
* User Management
* Computed Data
* Summarized Data
* Undo and Redo (DML)
* Bulk Operations on Records
* Better Editing Experience
    * (new milestone)
    * Form based editing for records
* Sharing
    * (new milestone)
    * Sharing forms for people to enter data
    * Sharing views publicly
* Deployment
* Improvements for Non-Technical Users
  * (new milestone) 
  * Will need usability testing with real users
  * Will benefit from co-design from users
* Alpha Release
  * Documentation
  * Dedicated website
  * Branding 
  * Target users currently using spreadsheets, Airtable, database GUI
      * Try to find problems users solve using those tools and explain how Mathesar can solve them.
      * Our user experience is not as simple as Airtable in some ways, might be jarring.
      * Focus on benefits from data integrity improvements (e.g. in COVID data)

### Beta
* API v1
* Undo and Redo (DDL)
    * (new milestone)
* Plugin Architecture
* Graph Visualizations
* Beta Release
    * (new milestone)

### Post-Beta
* Calendar Visualization
* Kanban Visualization
* Data Export
    * We'll need an asynchronous layer to make this work well 
* Search (product-wide)
    * We have filters
    * We need to start adding indices etc., will be complicated
* Real-time Collaboration
* Spreadsheet-like Editing

