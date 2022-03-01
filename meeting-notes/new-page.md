---
title: March 2022
description: 
published: true
date: 2022-03-01T15:22:47.085Z
tags: 
editor: markdown
dateCreated: 2022-03-01T15:12:30.780Z
---

# 2022-03-01

## Display options Discussion

Sync call to discuss about display options validation especially around `datetime`, based on [Matrix Discussion](https://matrix.to/#/!UZILDSNKobkelUYwBp:matrix.mathesar.org/$vY0BFdwHvKT-9NcKJ8-y7cZSmQ0QsOlJGg4piJN4fYA?via=matrix.mathesar.org)



- **Participants:** Kriti, Pavish, Mukesh, Dominykas, Sean

### Notes

- Validation
    - We do generally want display options to be validated by the backend.
    - For datetime types, it doesn't make sense to build in complete validation on the backend.
        - Formatting strings can contain arbitrary non-token information.
        - We need to make sure frontend and backend validation matches and that's a lot of work - probably unnecessary, will probably lead to inconsistencies in the implementation.
        - The backend will only validate length to make sure random data is not stored.
        - Frontend will enforce additional rules.
        - Frontend cannot strictly rely on data from the backen
        
- Format
    - Length = 255
    - Only one string for format