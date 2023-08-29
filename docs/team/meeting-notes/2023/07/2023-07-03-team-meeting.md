# 2023-07-03 team meeting

## Brent's update about Mathesar users
Brent did an update on what he's learned from the Mathesar users he's been talking to.

Brent's notes (private): https://hackmd.io/4DId5uYKR1icDXZs8Bq9oQ

### Notes
- Brent has been responsible for responding to installation requests through the website (~15 so far)
- This means he's met some potential users
- There are some things we can learn
- Notes are here: https://hackmd.io/4DId5uYKR1icDXZs8Bq9oQ, Brent won't go through all the notes in the call, please read if interested.
- Users are referred to in general terms (since notes are public)
    - Business in Italy, wants to use Mathesar for ERP/CRM
        - Loves data modeling capabilities, he is already familiar with entities relevant to his business
        - Wanted to do it locally
        - Trying it out before committing to it
        - Stuff he wants:
            - Basic UI stuff like color coding cells, etc.
            - Calculations / formulas
        - Tried and didn't like NocoDB
        - Understands portability and having a standard format for the data set
        - Didn't need installation help – needed help with some UI confusion
    - Real estate office under large conglomerate
        - Use case: more like CRM than ERP
        - Currently using Airtable
        - Wants to integrate with mapping
        - Wants to access DB directly, knows SQL
            - Was frustrated with Airtable's inability to do this
        - Stuck at installation on existing hosting provider
            - Shared hosting
            - Couldn't figure out SSH access
            - Wants to use cPanel to install software
    - User at large French company
        - SaaS provider
        - Wants to use Mathesar to enable customer support using Postgres
            - Can't modify schemas
            - Since Mathesar's install adds schemas, it's a no-go from the tech team
    - User want to use it for project management
        - Was confused about installing it on a web server
        - Seemed to want a SaaS solution, but didn't express it in so many words
        - Currently using NocoDB
        - Using Windows
    - A couple of different users want to use Mathesar instead of a Postgres client or code
        - Currently using: pgweb, pgadmin, command line / Python
- Summary:
    - We're attracting interest from business users, not tech users
    - We're not best equipped to help these types of users because of our installation
    - These users are not using Mathesar for critical operations, and we wouldn't suggest they do, because they're not technical enough to manage it.
        - We can improve Mathesar for these use cases (e.g. offering hosted Mathesar, or hosted DB)
- Discussion:
    - It's interesting that some people want us for our capabilities, not just because we're a "free Airtable", it proves some of our hypotheses 
    - It's good to know there are business users interested in data tools
    - Seems like some users are coming from a PoV where running their business on spreadsheets is no longer sustainable
        - Don't think about things like backups
        - We may need to educate them or make things easier for them
    - People who use shared hosting might be satisfied with a SaaS offering (rather than integrate with things like cPanel)
    - We might need to have an opinionated flow on how to set up Mathesar for specific use cases (have a hosted database, cost $X per month)
    - Ideal customer seems to be customers who need non-technical users to have existing databases (like the SaaS provider)
        - Will pay a bunch of money for Mathesar
    - We should keep track of installation requests and users in a database
        - We don't really have standardized data for this

## What should we be working on in the next two weeks?
- Wrapping up current work.
- Cleaning up open PRs.
- Organizing our GitHub issues and prioritizing ones for the next release.
- Planning out projects for the next cycle.
- Discussing goals, priorities, and vision for Mathesar – we should all be on the same page by the time the next cycle ends.

## What should our next projects be?
- Getting user feedback from existing users
- Should be focused on increasing user adoption
- At least:
	- Getting a better picture of Mathesar's users (maybe personas)
	- Having a clear idea what getting to beta and v1.0 looks like
	- Simplifying installation
	- Making data in Mathesar sharable
	- Addressing bugs and features requested by users
	- Designing the first experiments towards sustainability
- After this cycle, we should aim to have enough information to select the next round of projects.

Projects

- Kriti & Ghislaine: Strategy / user research
- Rajat: Localization
- Brent and Anish: RSQLA1
- Mukesh: Simplifying installs
- Pavish: Shareable links
- Sean & Dom: Improvements for 0.1.3