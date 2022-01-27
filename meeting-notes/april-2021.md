---
title: April 2021 meeting notes
description: 
published: true
date: 2021-08-18T13:46:19.657Z
tags: 
editor: markdown
dateCreated: 2021-04-23T11:36:19.054Z
---

# 2021-04-26
## Welcome Pavish!
- Welcome!

## Last week retrospective
- Ghislaine: wireframes & roadmap update
    - Went well
    - Discovered a lot of things while making wireframes
    - Need to agree on what we'll cover in wireframes, and what we'll do in later steps
        - See questions in notes
- Brent:
    - Library splitting done
    - Code moving over from prototype - in progress
        - Crucial method in SQLAlchemy deprecated (meant to be internal method)
    - Doing a better job of testing the Mathesar db library (someday could be pip installable on its own)
    - Setup Mathesar to work with existing Postgres DB.
- Kriti:
    - Everything is now moved to the wiki
    - Collections -> tables, Applications -> schemas
    - Read-only APIs (APIs ongoing, CRUD and records API pending)
- Pavish:
    - Set up his CCI account
    - Started discussion re: front-end framework and repo structure
    - Finalized Svelte/Django templates + monorepo

## This week's plan
- Ghislaine:
    - Wireframes for data explorer
    - Move current work to wiki
- Brent:
    - Finish moving code over from the prototype
    - Types:
        - String
        - Email
        - Number types
        - Datetime types
- Kriti:
    - Update roadmap based on current work
    - Finish API work
    - Sync database tables and webapp tables
    - Import TSVs as well as CSVs
- Pavish:
    - Set up frontend repo
    - Set up workflows required for client
    - Set up Docker
    
## Community readiness check-in
- License
    - Hopefully finalized next week
- Ticket creation
    - Depends on wireframes/roadmap finalization, at least a couple of weeks away
- Other community building ideas?
    - Too early

## Internship update
- FYI, we have an intern from May 17 to Aug 20 (`@eito-fis`)

## Team event
- Galaxy Quest

## Discussion
- How to install Mathesar?
    - Use docker for now
    - Installation instructions for deployment, we'll figure this out as its own task:
        - see wiki.js as an example https://docs.requarks.io/install
- How to handle large amounts of data?
    - Two approaches: canvas vs. replace data in elements

# 2021-04-19
## Frontend hiring update
  - Pavish is onboard, pending logistics
  - 2 month notice, starts June 21st
  - Will join meetings and do some part-time work starting April 26th

## Wiki https://wiki.mathesar.org/
  - GitHub repo: https://github.com/centerofci/mathesar-wiki
  - Move mathesar-notes to it?
      - Affirmed by all
  - Set up private area for our competitor notes, strategy, meeting notes, etc.
  - Define rules for what is sensitive information in the wiki

## This week's plan
  - Ghislaine
      - Initial wireframes and roadmap update
  - Brent
      - Split up SQLAlchemy/psycopg2 into a library that the webservice imports
          - take engine as input
          - Django would store engines
      - Move code over from prototype and get rid of prototype repo
      - "Installation and configuration" from roadmap:
          - Access existing PostgreSQL databases via Mathesar using existing PostgreSQL user credentials.
              - Existing databases should reflect all columns and types correctly in the user interface.
          - Set up a PostgreSQL server automatically if none exists.
              - Create a new database from scratch.
              - Create an initial user if needed.
  - Kriti
      - Move stuff to the wiki and retire mathesar-notes repo
      - Rename collections and applications in codebase
      - Start work on API
          - CRUD for tables, schemas
          - CRUD for records

## Ticket creation
  - Everyone to create tickets for their work
  - Deferred to later discussion
      - Should we create an issue template for internal feature tickets? (existing templates only cover external feature requests)
      - When should we start creating tickets in advance for the next sprint or for contributors?

# 2021-04-13
## Team collaboration process
  - Standups
  - Weekly meeting
      - Agenda: planning for the next week (sprint)
  - Sprint cadence
      - Weekly
      - Tool: GitHub Project with Backlog column
  - Informal collaboration
      - Impromptu chat, video call encouraged
      - Chats are async, don't feel pressure to reply
  - Notes location
      - Public docs
      - Private notes (strategy, competitors, funding) etc. will live in mathesar-notes repo
      - Semi-public notes (e.g. user interview notes) - we'll figure out later
      - Technical discussions/decisions that we might want to go back to should go in GitHub Discussions
          - https://github.com/centerofci/mathesar/discussions
  - Todos
      - Kriti will invite Ghislaine and Brent to Miro
      - Kriti will set up a GitHub Project
      - Kriti to figure out first issue templates
      - In a couple of weeks, we'll talk about the process with collaborating with the community
          - Brent: think about "create a type" issue template

## Frontend hiring update
  - Two candidates in the pipeline
  - Perhaps Ghislaine would like to talk to the Frontend Engineer
      - TODO: Share interview notes with Ghislaine
      - TODO: Prepare Interview Questions

## Roadmap discussion
  - Goals
  - Timeline
      - Will be decided after we agree on MVP goals
  - Ghislaine's research/questions:
      - How people use Airtable
          - Sharing forms is a big use case, unlike SurveyMonkey etc., you don't need to connect to a Google sheet
              - from a table
              - This is opposed to bulk importing data
          - Automation
              - Zapier is a bit disconnected, Airtable pulls it all together
              - Improve the quality of data collection
      - Some industries need to automate processes for cost savings
          - for example, see librarians transitioning in the 70s
          - we could get some user journeys here
  - Process for further iteration
      - Ghislaine will do some research and write up user journey
      - Then we'll measure roadmap against it and refine roadmap

## Kriti's use cases for Mathesar
  - Book collection inventory
      - would be great to support barcode scanning that looks up books
  - DVD/Bluray collection inventory
  - Food inventory + grocery list creation
  - Health data tracking
      - would be great to be able to upload Apple Health exports, Migraine Buddy exports, MyFitnessPal exports etc. and find patterns in data, correlate different types of data
  - Track lectures/courses that I want to watch, have already watched, etc.

## Plan for this week
  - User journey and roadmap refinement
  - Continue code on essential things
  - Flag things that are potentially technically difficult
  - Set up for official sprints next week
