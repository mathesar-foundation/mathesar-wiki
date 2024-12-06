# 2024-01-22 QA testing meeting 

## General notes

- Infra: we'll set it up and tear it down soon afterwards
- Do we want separate database servers for everyone?
    - We'll use a single server for testing. We'll all prefix our database names with our own names, e.g. `sean_mathesar`
- Brent will set up a DB server separate from our internal server
- What pre-existing data should we have in place before upgrading?
    - lots of stuff going on in Django, e.g. Explorations
    - What can go wrong? Migrations, losing the connection between the service in its upgraded state and the correct user database — anything that would prevent the service layer from connecting to the internal DB.
- Kriti: Do we really need to test all these different combinations?
    - Brent: We need to encourage people to move to our own latest Docker compose setup. If they've rolled their own then that's fine, but if they're running an older docker-compose setup, then they need to change their setup.
- How aggressive do we want to be with changes for upgrades?
    - We'd like to suggest that users ask us for help if they run into trouble upgrading
    - It's okay if we cause users some pain right now
    - It's okay if users lose their explorations or other metadata. We can recommend that users contact us if they really need their explorations
- Who is going to write the upgrade instructions within the release notes?
    - Brent
- Where is the source of truth for release notes?
    - docs.mathesar.org, with each release as its own page
- Where is the source of truth for upgrade documentation?
    - in a section within the release notees page

## TODO

- We need to remove the upgrade system from the UI
    - This needs to become a "nag", with no button.
    - Should redirect to docs
    - **Sean** will do this
- Installation testing can happen now
    - Pavish, Sean, Kriti will work on this
- **Sean** will do some pairing with Adam on UI testing
- **Ghislaine** will go through library demo script
- **Ghislaine** will also test new testing steps for Explorations added by Pavish
- **Anish** will also work on testing
- **Brent** working on docs changes
- **Anish** will begin working on installation videos
- **Sean** will put release notes in docs

## For administrators

General tips for all 

- Follow docs as you perform steps. Report docs problems.

Specific steps

- [ ] Test all different installation methods
    - [ ] **Pavish** Docker compose
        - [ ] All defaults, local
        - [ ] Exposed on domain, DB server managed by Mathesar
        - [ ] Exposed on domain, DB server preexisting for users, managed DB for Django
        - [ ] Exposed on domain, DB server preexisting for all data
    - [ ] **Sean** Docker integrated image
        - [ ] Quick start from home page
        - [ ] All defaults, local
        - [ ] Exposed on domain, DB server managed by Mathesar
        - [ ] Exposed on domain, DB server preexisting for users, managed DB for Django
        - [ ] Exposed on domain, DB server preexisting for all data
    - [ ] **Kriti** Build from scratch
        - [ ] All defaults, local
        - [ ] Exposed on domain, DB preexisting for all data
- [ ] Test that previously installed versions of Mathesar can be upgraded to this release.
    - [ ] **Pavish** Docker compose -- All above variants for docker compose (this also applies to the guided script installation method)
        - [ ] Same docker compose file, same `.env`
        - [ ] New docker compose file, same `.env`
        - [ ] New docker compose file, bring `.env` into the new file
    - [ ] **Kriti** Build from scratch -- All above variants for build from scratch

## For users
*No specific notes*
