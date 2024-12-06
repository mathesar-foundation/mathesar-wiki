# 2024-01-29 Staff Meeting

## Release check in

- Pavish: we do have one critical issue: [Met with empty schemas page after docker-compose upgrade](https://github.com/mathesar-foundation/mathesar/issues/3426) 
- Pavish and Brent chatted a bit to troubleshoot this
- Pavish was able to upgrade. All the users were there. All the connections were there. He just couldn't connect and see schemas.

QA testing notes

- [Pavish's notes](https://hackmd.io/@mathesar/BJv77x-9T)
- [Kriti's notes](https://hackmd.io/9MZdwS6VQEGXvEA3caQZcw)
- [milestone](https://github.com/mathesar-foundation/mathesar/milestone/72)

Work remaining

- Merge docs PR
- Upgrade bug that Pavish found: [Met with empty schemas page after docker-compose upgrade](https://github.com/mathesar-foundation/mathesar/issues/3426)
- Other two bugs that Pavish found:
    - [Attempting to add connection with both Library Management and Movie Collection schema results in a 502](https://github.com/mathesar-foundation/mathesar/issues/3423)
    - [New connection creation flow does not handle schema creation failure scenarios](https://github.com/mathesar-foundation/mathesar/issues/3420)
- Decide what to do with build from scatch stuff + any work from that
- Re-test installation / upgrade
- Plan out post-release docs updates

Build from scratch

- Brent has modified some docs to address some of the problems that Kriti ran into.
- Brent ran through the steps on Debian 12 and got it running.
- Kriti proposes that we skip the upgrade testing for "build from scratch"
- Audience:
    - Kriti: it would be nice to have a guide for people setting up a cloud server, e.g. GCP
    - We'll hone this better for the next release

TODO items **blocking** release:

- **Sean**: Modify "build from scratch" docs to bump the Node and npm versions up to newer versions
	- Node: At least v18
    - npm: At least v9
- **Sean**: docs changes blocking release:
    - Add general disclaimer for upgrade instructions
    - Add special disclaimer for "build from scratch" upgrade instructions
    - Invite reader to contribute docs improvements within build from scratch install and upgrade docs
- **Brent**: Address [Met with empty schemas page after docker-compose upgrade](https://github.com/mathesar-foundation/mathesar/issues/3426) 
- **Sean**: Merge docs PR 
- **Pavish**: If #3426 has code changes, re-test after changes. (If it's docs-only changes, then no re-testing necessary)
- **Pavish** will re-build images after testing
- **Sean and Pavish**: work together to do all release steps

TODO after release:

- [New connection creation flow does not handle schema creation failure scenarios](https://github.com/mathesar-foundation/mathesar/issues/3420)
- [Attempting to add connection with both Library Management and Movie Collection schema results in a 502](https://github.com/mathesar-foundation/mathesar/issues/3423)
- Docs
    - Sean: Polish on upgradees
    - Kriti, Sean: Holistic docs review
        - Look at [Pavish's notes](https://hackmd.io/@mathesar/BJv77x-9T)
    - Ghislaine: installation review
- **Sean**: clean up CHANGELOG content, including discussion with team
- **Brent & Pavish**: (Wednesday) update servers to latest release
