# User CRM and Interviews

* Sean and Pavish to identify subset of users from Github to start discussions
* Sean proposed plan:
    - Identify who we want to reach out to
    - Communication guidelines (email contents, questions)
    - How information is stored and documented

## 1. Finding people to contact

- We have a list of emails from mailing list
- Ghislaine: [Clearbit](https://clearbit.com/platform/enrichment) is an API for data enrichment, can be used to segment the list
    - This can give us more info about our subscribers
    - Pavish: seems more useful to send a mass email to everyone
- Ghislaine: what about putting a pop-up on the website that invites people to participate?
- Sean identified 27 users to target
    - We'll send targetted emails to all of them
- Mass email to our mailing list
    - We'll send one email to this list. It will include:
        - Funding announcement
        - Invitation to participate in user feedback process
    - It will not include:
        - Release announcement
    - We should send this email _after_ the 0.1.4 release

## 2. How to reach out to people

- How do we get their contact info?
    - Sean suggest cloning a git repo to which the user has committed. We can look at the email address and name in their commit.
- How do we contact them?
    - We'll email them. No Matrix
- What is the outcome of the email?
    - To engage them in a conversation. It will be open-ended with an invitation to participate in a call
- Should we use calendly?
    - We need to research the viability of calendly with multiple people
    - We could have a common account for all of Mathesar
    - Pavish will research and get Calendly set up
- How do we incentivize them to participate?
    - We'd like to offer gift cards
- What is the content of our communication?
    - We need a common template
    - Sean will write the first draft of the email template
        - Ghislaine/Pavish/Kriti will review it
- If we are able to get on a call:
    - what questions do we want to ask them?
    - Who should be on the call?
- How do we avoid spam traps?
    - Make sure to put this 
- Do we send a follow-up email if people don't respond?
    - Sean: I don't think I'd want to bug people more than once
    - We could discuss this later
- Are there any GDPR concerns here?
    - Pavish thinks no. We're getting their contact information from publicly available information.



## 3. CRM to store all the info

Options:

- Mathesar
    - Example of a contact record in Mathesar: 
        - https://internal.mathesar.org/db/mathesar_tables/522/tables/2194/9
        - Sean: This takes 15 seconds to load. I don't like it
- Google Sheets?
    - Hard to take notes
- Markdown files
    - One markdown file per contact
    - Where would it live? GitHub, HackMD?
    - Ghislaine prefers GitHub
    - Do we need a template? Probably not right away. We'll move forward without worrying about optimizing the process

Decision:

- We'll use markdown files in a GitHub repo


## Next steps

- Sean will write the first draft of the email message
- Ghislaine will begin the CRM and collect email addresses
- Pavish will figure out the Calendly setup

## To discuss in the future

- Details of sending the mass email to the mailing list

## Next Meeting

- We'll meet weekly. Meeting scheduled for next week.



