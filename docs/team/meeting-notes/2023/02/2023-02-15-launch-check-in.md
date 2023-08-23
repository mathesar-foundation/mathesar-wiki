# 2023-02-15 launch check in

## General check in

### Users and permissions
- Pavish is out sick. From matrix:  
 *There’s a bit of a delay. I’m working on a PR containing the items assigned to me, I’m not confident that they’ll be merged by end of this week. I should have the PR open by this weekend.*

- Sean's work went swimmingly. So well, he's out of work and plans to take on tasks from Pavish/Rajat as needed
- Rajat has a PR in for documentation of access control, other PR for Table pages' access control(s) coming tomorrow
- Anish: Users and permissions PR is ready for review by Pavish
    - Pavish is out; someone else should probably jump onto reviewing this.
    
### Live Demo
- Dom: Did some load testing
- Initial load testing uncovered a few issues
- There are a few open items there
    - Dom is debugging issues found
- Since Dom is out Thu/Fri, Mukesh or Brent should take over if needed
    - Issue status will be documented
- Some frontend improvements are also available to take on.

### Upgrades

- Sean has been working on front end implementation, ahead of a fully functional API.
- To discuss the process for testing upgrades Sean, Brent, and Dom met after the meeting separately, with Kriti attending for some of the discussion. Outcomes were as follows...
- Release data
    - The front end will fetch release info directly from GitHub. No need to proxy through our backend anymore. Dom will remove existing proxy code and forward instructions to Sean for fetching release info from the GitHub API. Dom will also make changes so that the tag name of the current release is included in the common-data blob.
- Testing on upgrades on live releases
    - Before doing any Mathesar publicity, we will publish two releases to GitHub and DockerHub so that we can fully test the in-app upgrade process, ensuring it works smoothly from start to finish.
    - Before tagging any releases, we will reset migrations.
- Executing an upgrade
    - Currently, we have an API endpoint at /api/ui/v0/upgrade/ which accepts GET requests.
    - We need to change this to POST instead
    - Testing this endpoint needs to be done in prod mode, not dev. Setting up Mathesar in prod mode is now a bit tricky, especially if you want to keep any data you have in your docker volume.
    - When hitting this endpoint, the response status is 200 and the response body is empty. We're fairly certain that the endpoint gives this same response regardless of success or failure scenarios, and it seems like we probably won't have any control to easily modify that behavior. This setup is a temporary solution anyway, so we don't want to put much work into polishing it.
    - The lack of response info means that the UX will be devoid of any error information if something goes wrong during an upgrade. After a failed upgrade, the user will see the page refresh. If Mathesar is still running, then they'll see the upgrade screen again, showing that an upgrade is available. We're planning to cross our fingers and hope the upgrade works for people, because we likely don't have the time to handle failure scenarios more gracefully.

### Deployment and installation
- `install.sh` v1 is ready
    - Please test, command in Mathesar - Code channel on Matrix
    - Took a lot longer than anticipated
    - There are a lot of different ways that people run Docker, turns out
- Documentation is in a branch
    - Sean volunteered to review
- Kriti will look for someone on Upwork to test installation in various environements

### Usability improvements
- Ghislaine made an issue for specifying table name when creating a table
    - She's working on design for it
- There are some open usability improvements issues for the frontend team, please take them on if there are no pending issues for users/permissions

### Demo video
- Demo video V2 is open for review
- Lacks polish, rethinking the plan of integrating it into our website.
    - re-recorded audio but not video

### Website
- Making some updates to the website to mention a hosted version coming up.
- Ghislaine and Kriti will work on this.

### Analytics for live demo server
- Mukesh has been reading docs and writing up an email for what's needed.
- If we want more detailed events, we may need more than Simple Analytics
- Kriti suggests a call instead of email
- Mukesh prefers email
- Decision: start with email, take it from there

## Is GitHub prioritization working?
- Yes, people can find what they need on GitHub
