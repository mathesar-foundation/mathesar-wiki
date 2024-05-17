# 2024-04-03 staff meeting notes

## 0.1.6 release retrospective

### What went well?
- Kriti:
    - Release out on time!
    - People seemed less stressed.
- Pavish:
	- Release went smoothly and it didn't feel like an event we all were involved deeply in (this is good!).
- Ghislaine: 
    - Planning seems to be working. We are making iterative improvements after each release.
- Brent
    - Seemed to take less mindshare than normal

### What could've gone better?
- Kriti:
    - Release took until the end of the month, not much time to do more work until we cut the April release.
- Pavish:
	- QA tasks could have been planned and assigned ahead of time.
- Ghislaine:
    - I was confused by the initial QA assignments. I also don't have much experience triaging new bugs, not clear how to assign milestones / decide if they should be prioritized etc.
- Anish:
    - Release could’ve gone smoother if I clearly knew what should go in the QA plan and release notes. Which has now been documented by Sean for upcoming releases.  

### Shout outs
- Kriti:
    - Anish for owning the release, communicating progress, and ensuring it got out.
    - Pavish for helping Anish.
    - Pavish for Japanese UI translations - long time in the making.
    - Brent for taking the initiative on Python/Postgres version support and Anish for doing the work.
    - Sean & Ghislaine for usability analysis and long text field work.
- Pavish:
	- Anish for doing a splendid job as the release owner.
- Ghislaine:
    - Anish did a great job as first-time release owner.
    - Sean for thorough QA and testing the Japanese translation.
- Anish:
    - Pavish & Kriti for guiding me through the release process.
    - Sean for smoothing out our release processes.
    - Everyone for cooperating with me.

### Ideas
- Kriti:
    - Aim to ship release quickly after it's cut, hopefully that week.
- Brent: Don't use internal for QA, deployments get inconsistent
- Pavish: QA should be handled by only 2 people per release (for minor releases). One of them should be the release owner.


### Action items
- Plan a focused meeting around QA (assigned to Ghislaine)
    - Figure out how installation and upgrade testing should work 
        - Minimal fuss, easy cloud deployments, plan for testing should balance thorough testing from user standpoint with minimal work on our end
    - Figure out who's doing the prescriptive / tailored user QA
        - We need a previous release deployed to check for regressions
    - Who's doing the infra work
    - Aim to reduce number of people in QA process
    - Document QA process better
    - Should we do tailored QA mid-cycle before the release is cut?
    - Check QA plan basecamp task after the meeting
- Get Demo working reliably before the ChennaiFOSS conference

## 0.1.7 planning

### Pre-meeting notes
- Pavish:
	- I don't think we should release when a month has no PRs merged. We should also determine if merged PRs are worth making a release for.

### Notes
- Release owner: Ghislaine
- Release cut date: Apr 15
- Closing out 0.1.6
    - Debug images for 0.1.6?
        - Brent will do this today
    - Documentation task is moved to 0.1.7
- General question: are we okay with a month that has zero PRs merged?
    - Are we okay skipping months?
    - Yes, if there's no work, there's no use making a release.
    - But make sure to have a retro every month to evaluate why we didn't have PRs.
- Should we do monthly releases given that beta is top priority?
    - Yes, help us establish release cadence
        - Builds trust for users to know changes come frequently
        - Release best practices figured out before beta, we'll need to release quickly in response to user feedback
    - Lowers QA effort per-release
    - Help us process-ize release
    - Better CI setup and regular / mid-cycle QA will also help
- What should go in this release?
    - What's blocking beta work on backend refactor and permissions?
    - 0.1.7 work to consider
        - Backend refactor
        - Basecamp project tasks: https://3.basecamp.com/5718119/buckets/36802215/todosets/7206519344
        - GitHub milestone: https://github.com/mathesar-foundation/mathesar/milestone/75
        - Record page changes: https://hackmd.io/@mathesar/BJmQzqWyC
        - Markdown editor: https://hackmd.io/1o57ZQYTSZiqRJA3CqoeBw
        - Cell selection
        - Get Demo working properly
        - Try to get installation / upgrade outsourced
- Figure out how to unify tracking "current priorities" vs. "definitely in this release" 

### Final list for release
- Cell selection - touches a lot of frontend code, lets get this merged
- Backend refactor
    - Get initial RPC endpoint + frontend work merged
