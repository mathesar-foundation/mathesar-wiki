# 2024-03-06 Staff Meeting

## 0.1.5 release retrospective

### What went well

- Kriti:
    - Release went out on time
    - We made our build process faster, next time release will be smoother
    - Documentation improvements for release process 
    - Demo deployment changes
- Ghislaine:
    - Even though I had low participation, it felt like the process was smoother. I felt more informed of what needed to be done.
    - Communication with team was good.

### What could've gone better

- Sean:
    - The amount of organizational overhead we have for each release still feels significantly larger than I would like to see for a task we're performing every month. I'd like to continuing finding ways to streamline it.
    - During the previous two releases, we've made the release very near the end of the month, having almost no time to spare. For me personally this time crunch adds significantly more stress to my overall experience as a Mathesar dev. In general I do not like missing deadlines or failing to meet goals. The idea of consistently having a "near miss" every month is uncomfortable for me.
- Kriti:
    - Docker build issues took a while
- Ghislaine:
    - Nothing specific to the release. QA will be more organized once I finish the QA scripts I'm working on. I don't have enough experience to compare with previous releases.

### Shout outs

- Sean:
    - Brent and Pavish for resolving the buildx issue
- Kriti:
    - Sean for documentation improvements
    - Sean for helping with release management
    - Brent and Pavish for build issue resolution
    - Ghislaine for QA
    - Anish and Brent for demo deployment

### Ideas

- Sean:
    - Simplify Basecamp project
    
        I'd like to condense the [Basecamp project template](https://3.basecamp.com/5718119/buckets/36260906/todosets/7069685162) by shifting some of that complexity into documentation that lives in wiki pages.

        I wrote an [email](https://groups.google.com/a/mathesar.org/g/staff/c/VyyS7Vboao8) about this which [proposes a new template](https://gist.github.com/seancolsen/1127514bd71deb9333650a32db3f3899), but I'm not attached to that template specifically.
        
        I've been steadily improving our [Release docs](https://wiki.mathesar.org/release/). Now, [cutting a release](https://wiki.mathesar.org/release/notes/), [writing the release notes](https://wiki.mathesar.org/release/notes/), and [publishing a release](https://wiki.mathesar.org/release/publication/) are all clear, self-contained processes that can be completed in under 30 minutes. For processes such as these, I think a single task within Basecamp is sufficient. I would expect that, if someone hits a snag during one of these processes and is unable to complete it, they can add new tasks to Basecamp at that point to track the work necessary to resolve the snag.

    - Can we set up some sort of continuous deployment from the master branch?

    - Assign the same people to perform the tasks every month.

    - Decide on a consistent point within the month when we will cut the release. Thus far, we have been making this decision on a ad hoc basis. I think we would benefit from greater consistency.

    - I'd like to cut the release earlier in the month. For example, let's say we cut the release every month on the 15th. This gives us a longer grace period for publishing the release before the end of the month. For me, a change like this would serve to reduce stress. Note that cutting on the 15th would _not_ mean that we only have 2 weeks to get stuff into the release. We'd still have a whole month. This change I'm suggesting is a matter of shifting the phase (in the mathematical sense) of our release workflow relative to the phase of the calendar months. I see it as potentially increasing the _latency_ of releases in some cases. But I don't see it as reducing our overall _throughput_ of delivering meaningful changes in our releases.

- Pavish:
    - GH workflow for building and publishing Docker images, whenever a tag is created.
        - I'd like to do this in 0.1.6
- Anish:
    - We should look into better error logging for helping users with installation/upgrade issues

### Meeting notes

- "What went well" comments
    - We reviewed people's comments
    - Nothing new added
- "What could've gone better"
    - Brent: We were in "release mode" for about a week. We need to improve this if we're doing this every month.

#### Ideas

- Basecamp project template
    - We all reviewed the project template together and made some changes

- Continuous deployment
    - We can't do this until we have more automated testing between releases
    - Easier to do for the demo, but still not priority for this release

- Assign the same people to perform the tasks every month
    - Pavish: useful to rotate roles to make sure that the workflow works for everyone
    - Sean: it would be useful to have a "release owner" that automatically gets assigned to many of the tasks, then we only have to make one choice
    - We'll rotate release owners
    - Who should be in the rotation?
        - Brent, Pavish, Ghislaine, Sean, Anish
        - Kriti will not be in the rotation. This will give her time to focus on other tasks

- consistent point within the month when we will cut the release
    - Kriti: fine with doing it earlier in the month
    - Pattern: **We'll cut the release on the third Monday of the month.**

- Increasing automation
    - Pavish: would like to automate
    - Kriti: make sense to do this for 0.1.6
    - Sean: Want to defer increase in automation until after some of the other kinks are sorted out
    - Pavish: I don't want anyone to manually build frontend files — I want that to be an automated step

- better error logging
    - Anish wants to be able to look at a text file and figure out what has gone wrong with a user's installation/upgrade process
    - Sean: users have asked for this too. Would be good to work on.
    - Kriti: need to figure out requirements

## 0.1.6 plan

- What should be in it?
- Who's managing it?
- Deadlines

What to work on

- Automate cutting release process
- Error logging
    - Brent: it would be good to figure out what we _want_ to do, even if we don't end up doing it for this release. We'll work on figuring out the requirements.
- Brent would like to improve support for Python versions. Added.
- i18n
    - Maybe we could have this is if we're able to receive the translations in time
    - Yes, we'll try to get this in.

Logistics:

- Cutting on 18th March
- Release owner: **Anish**
- We reviewed the 0.1.6 milestone

NodeJS dependency

- Pavish raised a PR for removing NodeJS from our Docker Image
- For install from scratch, we'll have a separate meeting with Pavish, Sean, Brent

Work not related to 0.1.6

- Sean is working on a frontend refactor, will unblock other stuff
    - Will prioritize more important stuff if it comes up

