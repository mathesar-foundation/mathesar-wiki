# 2023-10-05 team meeting

**Attendees**: Anish, Brent, Dom (partial), Ghislaine, Kriti, Mukesh, Pavish, Rajat, Sean

## 0.1.4 release check in

### Pre-meeting prep
- **Discussion goal**: Check in on release, identify what's remaining, make sure we're all thinking of release as top priority

### Discussion
- https://github.com/centerofci/mathesar/issues?q=is%3Aopen+is%3Aissue+milestone%3Av0.1.4
- Mukesh summary: There are PRs for all the issues that are in 0.1.4
- issue 3053 - package repository has been figured out via email, needs to be closed
- Sean and Mukesh will pair on the documentation for #3167 and related issues
- Rajat - all work will have PRs by tomorrow morning
- Pavish brought up UX issues, should they be resolved before release?
    - Yes!
    - After all the issues are done, there will be a significant amount of work going through and making sure the installation flows well and any UX or other issues are resolved
    - Sean will start coordinating this process once more release issues are closed
- issue 3230: Dom is working on it, Anish has offered suggestions on how to fix
    - Dom is not at the meeting, so we don't know the status
        - Please let Dom know that we should retain the database models, even if it's marked delete:true (Perhaps change the name of the flag). The user will manually disconnect them from the UI.

## Internal CRM

### Pre-meeting prep

- **Discussion goals**:
    - Promote awareness of the CRM so that people think to incorporate it into their workflows
    - Address any questions/concerns people have about our CRM

### Discussion
- Please see Sean's email to core team for more details: https://groups.google.com/a/mathesar.org/g/core-team/c/miMgz6-PJD4/m/kT4kXtN-HwAJ
- CRM is ready to use now, but very rough around the edges
- CRM is very important for many reasons - systematizing user interactions, product direction, etc. - please prioritize familiarizing yourself with it and using it
- If anyone has issues, please come to Sean. Don't assume it's your fault if you can't use the CRM as intended.

## Product vision brainstorming

### Pre-meeting prep
- **Discussion goal**: What outcome should we be aiming for at the end of our product vision / direction conversations? 

By "outcome", I mean "the final output" of the process.
- e.g. if it's a document describing our product vision, what questions should it answer / what topics does it need to cover? What timeline do we set the product direction for? How would we use the document?
- if it's not a document, what does the tangible output look like?
- are there any intermediate ouputs we need along the way?

### Discussion
- Ghislaine:
    - We can look at our roadmap and see that all the items in it are grounded in reality or things that are currently happening
    - Market, etc.
    - We can check where we are and know how far we are from a destination
    - We need to have some goals and metrics
        - e.g. more installation requests from X type of users
        - e.g. in X months, we have Y small business users doing stuff with Mathesar
    - If we're only getting hobby users and not small businesses, maybe we're on the wrong track – could be marketing or features
- Pavish:
    - What does Mathesar look like in 6 months or a year
    - Clarity (similar to how we had our storyboard for librarian for launch)
    - Help with communicating to users
    - What direction is Mathesar going?
    - What features?
    - What users are targeted?
    - What is our position in our market compared to other tools?
    - What's our emphasis level on a SaaS version?    
- Sean:
    - "What is the outcome?" is a good framing
    - SaaS version may be a different question
    - What are the problems we want Mathesar to help people solve?
    - Library demo is an example of solving a problem with Mathesar
        - Mathesar owns the data in this scenario
    - Options
        - Mathesar connects to data
        - Mathesar owns data
        - Mathesar augments data
    - Recently, emphasis has been on connecting to data
        - What advantages can be gained from this perspective?
    - Identify our advantages over competitors
    - Outcome could be informal understanding among the team, doesn't necessarily need to be a document
- Pavish
    - Agrees with Sean, but SaaS should be a consideration sooner because it affects architecture
- Brent
    - A SaaS product is essentially a different product that uses Mathesar as a tool
    - The product level decisions are totally different from self-hosted - e.g. multi-tenancy 
        - It's not "how do we implement multi-tenancy", it's "what do we want the UX for hosted users to be?"
    - We do need product vision for SaaS, but I'm not sure it's the same thing as the vision for Mathesar the product
    - Outcome:
        - It would be good to re-emphasize and hone in on why people would want to connect a GUI like Mathesar to a pre-existing Postgres DB
            - What are they trying to do?
            - We should try to potentially concentrate
        - Product vision should be general, high-level
            - Common understanding written down
            - e.g. advantage over competitors is something we all agree on
        - Would be phenomenal to lock in whether we're focused on transactional or analytical data.
            - Different advantages to each approach
            - Different UI emphasis
            - Commit to it for some time, not forever
        - Would be nice to know what scale we're emphasizing
            - Postgres can do Airtable scale to big data pipeline scale
            - We're not probably looking at inputting billions of rows scale
- Pavish:
    - Would like something more specific than high-level product vision
        - i.e. library demo type thing
        - maybe multiple storyboards similar
        - at 6 month level, doesn't have to be called "product vision"
- Ghislaine:
    - All these questions seem to tied down to: are we doing BI, are we doing internal tools, etc.
    - There are concepts in those direction that tie to specific products, e.g. "data mart"
    - If it's evidence based, then we tend towards more saturated markets (e.g. there's a lot of evidence for small businesses wanting BI)
    - We need more clarity from our users, not from generic research (because the data that is abundant is for saturated)
- Sean:
    - Outcome idea: document with 5-10 use cases - 1 paragraph each - describing a specific problem the user is solving, where Mathesar is the _best_ tool they can use to solve that problem
    - We need to figure out how similar the use cases are – if they are very diferent, then we can't go after them all in a reasonable basis. If they are very similar, then our market will be too narrow
- Rajat:
    - Kind of users to target
    - Problems they want to solve
    - Solutions offered by Mathesar
    - SAAS could become a path towards those solutions. 
- Pavish:
    - Having use cases
    - Try to gather more info before focusing too much on use cases
    - Wait until we have the feedback before forming the vision
- Mukesh:
    - Same; make some use cases
    - What kind of data is coming in
    - Where Mathesar fits into a data flow
    - For users who manage data
    - SWOT Analysis of our strengths
    - Product vision should include our ideologies
    - Having evidence of the feedback helps derive more information
- Brent:
    - Sean suggested we needed to choose between a wide set of use cases and a narrow set of use cases. I don't know if I agree. We could focus on one operation that applies to a bunch of different use cases, then that could be stategic. E.g. if we make Mathesar capable of accessing the same data for different types of users, then we can serve a bunch of use cases. Look at Unix -- small tools that serve many different use cases.
    - Important to be "exciting and dynamic" with a new product. We don't necessarily need to wait for user feedback before we develop the product vision. We might not get enough data any time soon. Being exciting is more important than being right.
- Rajat:
    - If we had 5 very different use cases, then we could choose to focus on only one or two in the short term, with the intent of doing the others in the longer term.
    - We can use market cap, competitor analysis, our strengths, etc to decide between these use cases. 
- Dom:
    - Agrees that the product vision should be exciting
    - How do we feel about the trade off between a product vision that we _personally_ find exciting vs a product vision that we deem to be practical?
    - Is the vision "use cases" or "features"? It might be more helpful to frame the vision in terms of features because it would be easier for people on our team to understand.
    - As a starting point, I would prefer a vision that's exciting over a vision that's practical.
- Kriti:
    - Helpful for me to think of the produt vision as a "go to market strategy".
    - I'd like a more integrated plan, including sustainability, e.g. SaaS vs donations.
    - There are many different forms that output could take. Want to make sure that the output works for everybody and has buy-in.
