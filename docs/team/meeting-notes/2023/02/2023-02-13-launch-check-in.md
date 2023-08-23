# 2023-02-13 launch check-in

## General check-in

### Users & Permissions

- Pavish: looking pretty good, PRs are awaiting review
- Rajat: Working on Table Inspector permissions – hasn't started, has been reviewing designs
- Access control waiting for PR 2443 to be merged (blocking other work)
    - Other permissions issues shouldn't be started until 2443 is merged
- Rajat should prioritize PR review

### Deployment and Installation
- Brent: Working through `install.sh`, reviewing PR #2444, relevant to documentation
- Moved some tickets from 'blockers' to 'nice to have'
- There's a PR for compressing static assets

### Load testing live demo
- Dom's getting started with that.

### Upgrade
- Sean's getting started
- Final say on user flow will live in #277

### Product Usability testing
- Done for now
- People were having real trouble renaming a table, wanted to put a table name in when creating from scratch.
    - Had trouble changing the table name later.
- Ghislaine will create an issue for setting table name when creating a table
- Will be launch nice to have

### Website
- Waiting on docs and demo video to be done for integrating
- Some issues with OpenGraph tags
- Some issues reported by Google search console
    - Just for mathesar.org, not for demo (or staging)
- Got great feedback on current version of website
- We should probably update website copy to mention SaaS version coming soon + 
- Add social proof section of website
    - Testimonials
    - Feedback quotes
    - Try to do this in a tasteful way
    - Suggested by multiple people
- Usability note:
    - How to get back to the site from the demo?
    - Maybe even for general installations of the app.
    
### Analytics
- Nice to put some on live demo website
- Mukesh will work on this after Kriti creates an issue

### Error logging and reporting
- Might be useful for tracking down bugs, etc.
- Only useful for demo at the moment, need to think about self-hosted

### Users & Permissions QA
- Anish will document what needs to be tested 
- Kriti will provide feedback

### Launch milestone updates
- Kriti will make some issues for new things mentioned above
- We'll kick out extra users & permissions and deployment types from launch nice-to-haves

## Schema Sharing Modal Design
**Attendees**: Pavish, Kriti, Rajat

- The schema sharing modal design doesn't show people with DB access, should we show it?
- Yes, it should be similar to how "Admin" is shown, but it should be "DB Manager", "DB Editor", "DB Viewer"
- Users cannot edit DB roles.
- Users can add schema roles for people who already have DB roles. This will just show as "Editor", "Manager", "Viewer".
- Pavish may improvise some help text.
- In general it's fine to improvise design work on this feature.
