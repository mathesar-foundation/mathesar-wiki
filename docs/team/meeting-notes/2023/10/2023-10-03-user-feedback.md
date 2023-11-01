# 2023-10-03 User Feedback meeting

## Details

- Attending: Sean, Ghislaine, Pavish
- Note-taker: Sean

## Review CRM together

- We reviewed the [Internal CRM](https://github.com/centerofci/mathesar_internal_crm) together
- We need to eliminate some duplication of data
- We discussed keeping the CSV vs putting data in markdown
    - **Decision**: put data in markdown, delete CSV
- TODO (Ghislaine):
    - Move "Source" data from CSV file to markdown files
    - Delete CSV file
    - Delete index file
    - Migrate remaining markdown files to frontmatter structure to follow "Adam Jones"
- More thoughts:
    - Sean: We could have a script that reads the markdown frontmatter and generates a CSV or SQLite database from it so that we can look at data alongside each other.
        - Not sure this is worth it right now, but something we could do when we need
    - Pavish: I'd like us to not spend a lot of effort on maintaining this before we move it into Mathesar


## Email message

- How do we avoid spam?
    - Sean: I think we have a low risk of hitting spam boxes
    - Pavish: but how do we make sure we reach their _priority inbox_?
- Should we contact them again if they don't reply
    - Pavish: not sure
    - Pavish: maybe we _should_ reach out to them again, just in case our message didn't reach their priority inbox
    - **Decision**: we'll leave this open-ended, but we'll remove content from the message that promises we won't reach out again.
- Content
    - Sean has a [PR](https://github.com/centerofci/mathesar_internal_crm/pull/1/files) for this
    - Pavish thinks it's mostly good.
    - Pavish: proposal: take out "(If you don't reply, we won't bug you again.)" because we don't want to necessarily commit to that.
        - Sean: agree
- Email subject:
    - Pavish: not sure "How are you using Mathesar?" is best
        - What if they are not actually using Mathesar yet. The subject might not fit well.
    - Brainstorm:
        - Help make Mathesar better
        - How are you using Mathesar?
        - Does Mathesar solve your problems?
            - Sean likes this
    - Pavish will think on it outside the meeting
    - We should mention the time limit as 30 minutes
- Who is the email "from"?
    - Ghislaine: thinks it would be better if it's from a specific person.
        - Pavish: agree
    - Pavish: we'd like the email to be visible to others. We could CC a separate group at https://groups.google.com/ for this. Maybe we could use an existing group or create a new one.
        - Ghislaine will work this out with Kriti
    - The FROM field
        - Ghislaine: it would help if the sender is someone whose name the user will recognize from GH interactions
        - Sean: I'd be happy to the be the FROM person
    - **Decision** the email will be from Sean, with a google group CC'ed for visibility
- Timing
    - When do we want to begin sending these messages?
        - Sean: I'd like to start sending them this week
    - Pavish: what time of week is best to send them?
        - Sean: suggests weekdays
    - Decision: The goal for this week is to have everything ready so that we can begin sending them next week

## Calendar system

- Pavish is making some progress on this. Still working

## Incentives for joining a call

- Ideas
    - Amazon gift card
        - **Decision**: We all agree this should work well
    - Amount?
        - Ask Kriti

## The call

- How long do we anticipate the call taking?
    - 30 minutes
- Questions
    - Max 3 or 4
    - shouldn't be too specific
    - could be similar to the survey question
    - we could improvise follow-up questions as needed
    - mostly: we need to understand their problems
    - why they were exploring Mathesar
- Overall thoughts
    - the call should feel informal and friendly
    - We need to "drill down" into the problem, in order to avoid the XY problem
    - The "set of questions" are not actually mandatory. They're just there to help in case conversation stagnates. We should try to keep the call organic and conversational instead of interview-like
    - We need to identify the "jobs to be done" instead of the "tools" used to accomplish those jobs
- **Decision**: We will keep the call open-ended without mandating a specific set of questions. We'll formulate a set of "possible questions" for inspiration on the call.
- Possible questions
    - What drove you to explore Mathesar?
    - How do you use data?
    - What data-related problems are you trying to solve?
    - Where are you in your journey with Mathesar?
    - What other products have you researched or used?
    - What was your workflow _before_ Mathesar?
    - Is Mathesar actually solving your problems?
    - What kind of features would you like to see in Mathesar?
- What is the video platform we plan to use for the call?
- Can we record the call???
    - We could have another core team member there to take notes
- Who should be on the calls?
    - Sean: I like the idea of one core team member leading the call and another there to take notes
        - Yes, we decided to do this
    - Pavish is worried about timezone conflicts and having a hard time getting two core team members
        - Sean: not so worried
        - Sean: can we have SavvyCal sort out some of these logistics
            - Pavish: we can use it to find the "primary" person, but we'll need to handle the note-taker on an ad-hoc basis
- How do we handle people who schedule calls on very short notice?
    - Pavish will look into the logistics of setting a "buffer" with SavvyCal
- System for assigning the calls
    - Ghislaine will receive all call scheduling info and assign specific team members to each calls. She will make sure that each call has a "primary" core team member assigned to lead the call as well as a "secondary" person to take notes.


## TODO:

- Sean:
    - Remove "(If you don't reply, we won't bug you again.)" from email message content.
    - Add 30 minute call time limit to email content
- Ghislaine: TODO items within the CRM topic above
- Pavish: finish calendar setup
- Ghislaine: chat with Kriti about
    - Get email message content approved
    - Figure out the google group which we will CC from the email. Create new one if necessary.
    - Make sure Kriti is okay with Sean being the "FROM" for the email
    - Decide on the amount for the Amazon gift card


## TO discuss later

- Content of email to newsletter list
- Expanding to additional sources of users
