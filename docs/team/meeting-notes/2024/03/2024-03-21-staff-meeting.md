# 2024-03-21 staff meeting

## Quick release check in

- What's left to do?
    - Write + review release notes (Anish)
    - Test build from source Mac (Anish)
    - Docs changes (debug images, 3.12) (Brent)
    - Test upgrades (Pavish)
    - Review docs (Sean)
    - Scanning PR for red flags (Sean, Brent)
- Who's doing what?

### Discussion

#### Moved to next release

- Bump release publication atomic task to next release
- Create requirements for better error logging

#### Left to do

- QA is still in progress
    - Update docs to take out 3.12
    - Pavish testing upgrades
- Sean reviewing docs

### Action Items

Ghislaine is 0.1.7 release owner
- update QA plan (also in template)
- Sean will assist

## Beta planning

- Current status and next steps for:
    - Backend performance
        - Status:
            - Notes are drafted
            - Once we have buy-in, start building
                - GitHub issues for first step, replacing tables and columns endpoint with RPC endpoints
                - Sean will do frontend changes
                    - We need to completely switch from REST to RPC in a single release for consistency
                - Then we'll delete old code
            - Do we need to preserve old endpoints?
                - Not too much extra work
            - Frontend and backend needs to discuss how we're going to make this change across multiple releases
                - We need to be on the same page about what we're doing for each release 
                - Also try to minimize work
            - We need to be able to track progress on this
                - Brent will create meta issue with bullet points (not all filled out), can change over time
        - Todos:
            - Kriti, Sean to review architectures notes
    - Usability improvements
        - Sean, Ghislaine, and Kriti did independent evaluations of moving CRM to Mathesar
        - We have a list of recommendations for improvements
        - [Sean's list](https://hackmd.io/pfh-XVLlRjiWg8lvZtU8WA)
        - [Ghislaine's list](https://hackmd.io/8aKlQZy3SFqRtRGsPPAHRA)
        - [Conclusions](https://hackmd.io/ei6Im5IwRci3l4YmeK6ANg)
        - Want to improve navigation and space usage in record page; Ghislaine is working on wireframes.
            - Not blocking beta, but nice to have. Depends on capacity.
        - Blocking improvements are already done (Great!)
        - Found 2 more high-priority improvements that would be nice. Ghislaine is working on those.
        - We'll continue to prioritize improvements from the original list as appropriate.
        - May find more things once we actually move the CRM over to Mathesar.
    - Release optimization
        - We should try to get the requirements for hiring someone to help with this done by mid-April if we can
        - Added task for Ansible script
        - Added task for manual QA plan
    - Permissions refactor
        - Done so far:
            - Architecture mostly solidified
                - Still have some things to go - how to derive permissions for Mathesar objects 
                - Backend can go any which way
                - We're all agreed that exploration permissions will be managed in the service layer
                - Ghislaine: Is this related to Mathesar table metadata?
                    - Pavish would like to derive those from postgres permissions
                    - Sean would like to derive from exploration permissions
                        - Simpler to implement
            - Backend can do a few weeks worth of work without solidifying remaining issues
                - No schema level permissions yet other than through DB roles, we can add pieces once this UX is solidified 
                - We will need to add pieces, but we don't need to undo anything
            - Next step: UX exploration to finalize frontend implementation (and remaining backend architecture)
                - Pavish and Ghislaine had an initial call
                - Call to plan work / set expectations, put work in Basecamp
                - Kriti, Pavish, Ghislaine, Sean
        - Discussions:
            - Schema level permissions vs. not
            - UX requirements for permissions and how to present Mathesar metadata permissions
    	        - Considerations: https://hackmd.io/@mathesar/S1RjAC8pT
        - Backend work will be tracked in the same meta issue as backend performance ("backend refactor")
    - Installation improvements
        - Not looking at these until backend refactor
        - Then we'll look at this again
    - Beta "go to market"
        - Demo tasks
            - Try to do a bit every release
            - Should be part of demo planning
        - Metrics for beta
        - Marketing for beta
    - Planning and organization
        - Kriti: set up a call for the "go to market" of the beta
        - Kriti: check in on beta progress in weekly meetings as needed
- Are we missing anything else?
    - Added to "other features to consider"
        - Security audit
            - Wait until backend refactor is closer to done
            - Should be outside audit
            - Sean was on CiviCRM security team
            - Table renaming bug could be related to security
                - We do sanitize on the backend
            - Security vulnerabilities should be tracked privately
            - We need a flow for people to report security issues with us
                - SECURITY.md file, etc.
- Check in on everyone's current work, ensure it's aligned with beta
    - No time for full check in
    - If anyone is working on something that they don't know if it's a priority, please talk to Kriti
- Timeline for beta
    - We should have a release that we're aiming for being the beta
    - We'll discuss this next week
    - Kriti will start an email thread to get people's opinions on this
    - NOT April release
- Plan for 0.1.7
    - Releases can be similar to cycles, all work should be tracked there
    - Talk about this next week
- We've made a lot of progress since the last beta check-in, nice work everyone.

### Action Items

- Ghislaine to update QA plan for 0.1.7 release and release template in Basecamp
- Sean and Brent will sync on the process plan for the architectural change.
    - Communicate plan to team afterwards.
- Brent will create a metaissue to track overall plan for architectural changes.
- Brent should double-check that backend performance plan makes sense.
- Sean, Ghislaine, and Kriti should look through the Considerations doc, plan a call with Pavish.
- Everyone: let Kriti know if you are working on something not prioritized for the beta
- Kriti:
    - schedule "business goals for beta" meeting
    - start email thread about beta timeline
    - add beta timeline & 0.1.7 plan to next week's meeting
