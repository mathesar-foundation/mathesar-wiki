# 2024-03-27 staff meeting notes

## Welcome Mishelle

- Mishelle is our new EA, via Magic
- We did introductions

## 0.1.6 release check-in
- What's left to do?
- Timing and responsibilities

### Discussion
- Pending item: Update Release notes, review, and merge
	- Anish is prioritizing that
	- Sean might be available to review, if not, Kriti will review and merge
- ETA of release
    - Anish is working on release notes changes
    - Tomorrow

## Increasing development velocity 

- What's slowing us down?
    - User calls 
    - Research for user help
    - Admin work
        - Notes, CRM updates
        - Marketing monitoring
    - Context switching
    - Troubleshooting user reported issues
    - Marketing tasks
    - Discussions
    - Planning / specs
- How can we speed things up?
- Designated "put fires out" person every release?
- Are we having too many discussions?
- Any other ideas?

### Discussion

#### What's slowing us down?

Pavish's response from email:
> I'd like to not talk to users, not work on marketing tasks, reduce discussions, and focus entirely on coding until we get the Beta out. I'm also going to hit a pause on conferences/talks after the one I have on April 6.
- Brent:
	- We're discussing and planning too much and coding too little.
	- Pessimistic on the timing (June)
		- Backend work is currently blocked because we're still planning stuff
	- We discuss, plan, and get into this cycle, and code little. We should be bold and go forward instead of spending a lot of time on discussions.
	- Should be willing to be wrong, and fix it later.
    - Much bigger priority than user calls
- Pavish:
	- Not a lot of value in installation calls at this point, Mathesar doesn't seem like it will help people just yet
	    - Maybe try to get information async
	    - Not worth engineering time before stable version / beta
    - Marketing
        - Conferences + talks
    - Need to focus on coding
- Ghislaine:
	- Over documenting stuff and not getting started with designing sooner
		- We could reduce the documentations to conversations
- Anish:
	- Installation requests take time, mostly identifying what went wrong because user doesn't provide enough information
	    - GitHub issue without much info: [Impossible to install mathesar](https://github.com/mathesar-foundation/mathesar/issues/3444)
	- There's a lot of back and forth with the user
    - Brent adds: this is a matter of professional / personal curiosity, but it's very time consuming to debug
		- Some users like Alasdiar have issues mostly to do with k8s and not Mathesar. Figuring out what's wrong with their installation is very time consuming.
		- Not worth it at this juncture.
- Sean:
    - Hardly spent time coding recently
    	- A symptom of the low-velocity problem
	- Reduce marketing efforts like reducing user calls
	- Suggests that we change our approach to product design to design more modular features that users can compose in more powerful ways. E.g. our custom types functionality, the data explorer
	- Performance problems are blocking us from endorsing Mathesar, so in a way, we haven't genuinely launched Mathesar
		- After Beta, we could spent a lot of time marketing
		- Kriti:
			- Our objective was to see what people think of Mathesar when we launched.
			- Now we have a clear idea of what's preventing users getting started with Mathesar. We had no external feedback before launch.
	- Different process for planning
		- Very important to make sure everyone's on the same page
		- We need more planning but the right kind of planning
		- A top down approach might be better than everyone pitching in and figuring things out together
		    - Could be either Kriti for everything, or one "owner" who is empowered to make decisions
		        - Like Brent: architecture and Pavish: permissions
		        - Specs could be very useful, opinion diverges from Brent
                - 1:1 conversations to get it to completion
                - Spec is source of truth, interface that glues other conversations together
        - Brent's "rebuttal":
            - Agrees it makes sense for architecture notes
            - There's no source of truth for permissions, it's nice to have a spec
                - HackMD, Figma
            - Brent doesn't want to have specs for too far into the future, just this month
        - Pavish:
            - Permissions had 1:1 conversations, but UX/DB concerns are different, the documents were meant to discussions

#### What do we do about it?
- Come back to how to build new features discussions (specs, planning, higher-level product design) after beta
- This call, focus on beta action items
- Permissions - sort out metadata permissions
- Talking to users is not worth engineering time, not high value
    - Definitely not worth two engineers
    - Sean can join without much prep
- Disable request installation help on the site
- No more conferences until we have Beta, other than the ones we've already planned
- Reducing context switching:
	- Eg., Logging things in CRM can be taken over by Mishelle
	- Brent: User requests, handling bugs
		- Would have to recreate a setup to get into these and it's affecting current work.
		- It might be better for us if users reported bugs on GH than sending an installation help email
- How much work do we put into troubleshooting?
    - Kriti: Having a person every release to put fires out i.e. identifying severity of issues in each release
    	- Sean: This is something I consider part of the repo admin work to identify the severity of issues and loop people in as necessary
    	- Sean's just going to do this, no rotation for efficiency
- Planning:
    - Don't add things, focus on beta stuff
    - Plan multiple releases out?
        - No
- Discussions:
    - Time spent is fine, blockages are bad
    - Moratorium on ticket planning meeting until after beta
    - team events stay as-is
    - weekly meetings stay as-is
    - people consider 1:1s on their own, reduce if needed
	- Mishelle is going to take care of incoming communications like syften
		- Sean responds to Syften notification like discussions that come up on Reddit
			- Sean will continue doing that

## Beta timeline
Which release should we aim to be the beta?

### Discussion
- Pavish proposed June
	- Brent:
		- We can do enough on the new architecture by June
		- Blocked by outside influence so not sure about committing to the timeline
			- Metadata permissions
		- Once we have plan for the first few steps, we can get started on code
		- There will be frontend work for it and there'll be back and forth. We will not be implementing this for a month.
		- It might take July (Pretty aggressive deadline).
			- We'll have to cut scope in May based on this deadline.
- What's blocking permissions backend work?
    - Mainly namespaces for metadata permissions
- Deadline: July
    - Including backend, frontend, testing
    - Backend will do tables and columns, then frontend can work on that while backend moves on to other things
- Sean:
	- Unknowns:
		- Metadata: Doesn't change time whatever approach we go with
		- Schema level permissions

## Permissions discussions
*This was a short meeting after the staff meeting, attended by Kriti, Brent, Pavish, and Sean*

- Metadata permissions - decision made
	- Users will be tied to the exploration permissions directly instead of the role.
	- We'll have to tie roles and exploration permissions to the Mathesar user
	- Having a single option to read/read-write Mathesar metadata (includes Explorations & all metadata namespaced on the database)
- What is a base in Mathesar - Schemas vs Databases? - decision made
	- Users will create a role with access to just a particular schema, and the permission will depend on that role. There will be a user database entry where the permissions for metadata will also be setup.
 - 
