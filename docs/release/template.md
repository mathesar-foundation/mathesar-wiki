This is our release notes template. The template part follows the horizontal rule.

---


# Mathesar [VERSION]

???+ note "Optional CTA for user research, sponsorship, etc."
	Make the CTA specific, it's often better to aim for a smaller niche than go too general.
	For instance, we might mention wanting to talk to users who would like a specific feature.

## Summary

> **The summary should be 2-4 sentences.**
>
> **First sentence:** Summarize the type of release this is / what the release focuses on.
>
> Examples:
>
> - Mathesar 0.3.0 focuses on improvements to Mathesar’s installation experience, look-and-feel, usability, and stability. 
> - This release contains targeted fixes for bugs within Mathesar’s new UNIX socket connection feature, as released in version 0.2.3.
> - Mathesar 0.2.1 addresses a number of bug fixes identified by members of our community during our beta release. 
>
> **Second and third sentence:** Mention highlights of the release from the point of view of what's changed for the user (which may not always be how we think about things internally e.g. 'record selector improvements' gets translated to 'improvements in locating records').
>
> Examples:
>
> - Highlights include a new dark mode theme, a UI refresh in light mode and a new install method using a one-line script. We've also improved usability of the Data Explorer, finding table records, and creating records. 
> - This release includes some quality-of-life improvements to Mathesar like nicknames for databases, persisted column widths, and the ability to connect databases without a password.
> - This release introduces a UUID data type, enhanced primary key handling including support for UUIDs as primary keys, more flexible primary key handlind during data import, and more.
>
> **Last sentence:** Just an indicator that there's more in the release, not just the mentioned highlights. Only include if applicable.
>
> Example:
>
> The release includes several other smaller fixes and improvements.

> We include this info box to flag that this is the canonical / comprehensive list of all changes to the release.

!!! info "This page provides a comprehensive list of all changes in the release."

## Improvements

> The improvements section can be skipped if there are none. Improvements are basically user-facing or admin-facing features or enhancements.

### A specific improvement

> The improvement title should be a brief description of the improvement that focuses on what changed, from the user PoV. Examples:
>
> - A new look for Mathesar
> - Updated “from scratch” installation workflow
> - New access control system based on PostgreSQL roles and privileges
> 
> The text should describe:
>
> - What we did in terms of changes e.g. "we streamlined Mathesar's from scratch install workflow", "we completely redesigned Mathesar's access control system" etc.
> - What that does, in neutral, externally observable terms e.g. 
> 	- "eliminates several steps from the process"
>	- "allows users to use UNIX sockets to connect their Postgres instance to Mathesar"
>	- "You can now use Mathesar to configure roles and privileges in PostgreSQL and to set granular access control at the individual schema and table level."
> - Links to any relevant documentation that's new.
> 
> If this improvement involves a UI change, or there is some other visual representation possible (docs screenshot, SQL command, etc.), please include one.
>
> Other notes:
>
> - Describe everything from the external change point of view, from the user's perspective. For example, when we set up `uv` as an installation method, we described as the "from scratch" installation method changing because from the user's PoV, the docs page with that heading now has new instructions. Even though behind-the-scenes it was a whole new technology.
> - Anything user or adminstrator facing counts as an improvement - new security policy for the project, minor usability changes, etc.
> - Each change should get its own section. Do not combine multiple changes into a single section. It's fine for the description to only involve one sentence.
> - Generally make sure each sentence has a purpose. It's better to say less than more.
> - Avoid "selling" the feature i.e. don't describe how it will benefit the user or use notably positive or emotionally loaded terms. Aim for accurate but neutral-ish language.
> 	- "Simplifies" is fine if there are fewer steps in something.
> 	- "Improves" is fine if there's a visible change in affordances.
> - Avoid explaining to the user why the feature is useful. For example, if we introduce public forms, avoid saying things like "forms can be used for surveys, etc."

*Related work:*

> List of PRs, only with numbers.


## Bug Fixes

> The bug fixes section can be skipped if there are none. 
>
> This is just a list of bug fixes that link to the relevant PR. No need for subsections.
>
> Notes:
>
> - Always describe the bug fix from the user PoV of what changed.
> 	- e.g. a PR titled "Fix not null SQL" becomes "Fix issue where `NOT NULL` constraints could only be set in the `public` schema" in this section.
> - Always look at the base issue, not just the PR title. Sometimes PR titles are very different from the issue being fixed.
>	- e.g. a PR titled "Always display external links icon in the DocsLink component" becomes "Fix issue with some external links not showing the external link icon"
> - Some items may not be framed as bugs in GitHub, but count as bugs.
> 	- e.g. "Add language selector to complete installation template" seems like a feature, but it's actually fixing an issue where localization wasn't available during installation.

## Documentation

> The documentation section can be skipped if there are no user-facing or admin-facing docs changes.
>
> Documentation changes should be represented similarly to Improvements – subsection for each change, screenshots, etc.

## Maintenance

> The maintenance section can be skipped if there are none. Maintenance should only be for things that truly do not result in user-facing or admin-facing changes e.g. refactors, housekeeping.
>
> This is just a list of changes that link to the relevant PR. No need for subsections.
>
> The last item on the list can be "Work related to our internal workflows" and just link to a list of PRs (this is reserved for housekeeping / repo maintenance tasks that are _not_ product changes, e.g. tests, GitHub workflows, etc.)

## Features removed

> The features removed section can be skipped if there are no features removed.
>
> There should be one subsection per feature removed. Screenshots are not needed.

## Upgrading to [VERSION]  {:#upgrading}

> Include a subsection for each installation type.
