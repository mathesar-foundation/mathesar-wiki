# 2024-02-28 release check-in

- Build issues fixed, QA build is done
- What's left blocking the release process?
    - Brent to review release notes and docs changes
        - Release notes will then be final
        - Docs can be merged after review
    - gh cli task (from Basecamp)
        - Sean will do this as part of publishing release, mainly release process docs updates
    - QA
        - Library demo testing pending
        - Ghislaine had a question on Matrix on how to QA the demo. 
            - Ghislaine doesn't need to worry about QA for demo for this release, deploying the demo can serve as QA
            - Also, Brent has done QA already.
            - Brent suggested a new DockerHub repo for demo images, but we decided we don't need it since the long term plan is to change the demo setup and remove demo mode.
        - Feature / bugfix tests are done
            - Ghislaine tested bugfixes
            - Brent tested feature (loading data speedup)
- Bumped to next release
    - Make release process atomic (Basecamp task)
        - Sean needs to talk this through with someone with context of installation steps
        - May have installation implications
    - Consider separate DockerHub repo for demo
        - We don't need it for this release, but we may want to consider it for the next one based on the state of the new demo infrastructure.
    - Debug Ghislaine's installation issue (Basecamp task)
        - Check this off for now in Basecamp
        - Ghislaine - try installation blocker locally again after 0.1.5 is out, might be fixed with Anish's issue
        - If there's still an issue, we'll uncheck later

## Next steps
- Brent reviews docs + release notes
- Ghislaine completes QA
- Sean makes the release
