# Guidelines for experiments and research

This quick guide outlines best practices for Mathesar staff when conducting "experimental" work. For example:

- Adding a feature to Mathesar without going through the product process.
- exploring a previously-unknown community where we may promote Mathesar.
- Adding an integration with a 3rd-party service to Mathesar or its repo, e.g., a 1-click deploy button.

We encourage experimenting with these sorts of things without the bureaucratic overhead of normal processes, but staff should make sure their experiment satisfies some basic guidelines.

## General concepts for experiments and research

These concepts will be expanded with examples in different contexts below.

- Make any changes reversible.
- Make sure experimental work doesn't interfere with your normal work.
- Don't obligate Mathesar Foundation to anything when experimenting.
- Timebox your experiment.
- Have a way to tell whether an experiment was successful.
- Talk to others on the team if you're unsure about any of the above.

## Experimental features

This section is concerned with experimental features in Mathesar, i.e., PRs that you want to raise in the repo without going through the normal product process. These guidelines are organized from most to least important.

#### Easily reversible

An experiment should be easily reversible on a technical level. This means:

- Avoid distributing experimental code changes throughout the entire codebase. Contain them in a dedicated directory if possible.
- Make it obvious to other developers through comments or other means that they should not depend on the experimental code.
- Removing any code changes associated with the experiment should be a 5-minute project leading to an easily reviewable PR.
- Experimental GitHub workflows should be in their own files.

More importantly, an experiment must be _reversible w.r.t. our perceived obligations to the public._

- It should be obvious to a user that an experimental feature might disappear in the next release.
- Experimental wrappers or integrations must not set up a long-running dependency. For example, a 1-click deploy button is fine if it doesn't require any special Docker setup. In that case, a user could continue to upgrade and use Mathesar by following our Docker instructions, even if we stop supporting a given 1-click deployment method.
- Experimental installation methods should not require changes to the main Mathesar codebase.

Finally, the experiment must be reversible _in your mind_. It's crucial to be honest with yourself and ask:

> - If this doesn't work, will I let it go without a second thought?
> - Am I going to be willing to admit when it isn't working?

If the answer to these questions are anything but a resounding "Yes and Yes!", staff are strongly encouraged to follow the standard product process instead of experimenting. This brings us to the next section.

#### Doesn't break anything

- Obviously, added experimental functionality shouldn't break or obscure current functionality in the product.
- Changes to support an experimental 1-click deployment can't break any previous installation methods.

#### Minimal time investment

This is obvious, but bears mentioning. Do not spend more than 8 hours working on something experimental without talking to anyone else about it. Even better, talk to someone else after 4 hours of time investment.

#### Clear success criteria

There should be some way to tell whether the experiment has succeeded or failed. The staff member conducting the experiment should think about any success criteria before proceeding, and (ideally) write them down. These success criteria should ideally involve user goals, or helping a user solve some problem when sensible.

### Find an "Accountabilibuddy"

In the event that the 4 hour mark has been crossed in time investment in an experiment, staff are _strongly encouraged_ to find an accountabilibuddy. If time investment crosses 8 hours, this is required. 

- Choose any staff member (with sufficient context, and ideally a skeptical attitude) to be your accountabilibuddy for the experiment. 
- Their role is to listen to a short pitch, look at any examples or output of the experiment so far, and assess the experiment according to the guidelines above. 
- If it seems like the experiment is worth continuing, the staff member who originated the experiment and the accountabilibuddy should let the rest of the staff know what they're doing through typical channels (Matrix, email). 
- They should be prepared to be told to stop what they're doing, or go through the normal process if appropriate. In some cases, the consensus may be "just keep going".

### Responsibilities for PR reviewers

Pull requests adding functionality that haven't followed standard procedures, aren't easily reversible, or lack demonstrations ensuring they don't break existing functionality should be closed with minimal discussion. Staff are expected to use their judgment in these situations.

- A PR closing an issue which has been triaged by someone on the team (who didn't write it) counts as typical for now, subject to any product process imposed by Zack moving forward.
- A PR closing an issue written by the PR author with no discussion with anyone else is experimental. So, it must be easily reversible and effort should be spent making sure no current functionality should be broken by the proposed change. If that's the case, go ahead and merge.

On the other hand, if a PR:

- meets the easily-reversible criteria above, and
- the reviewer is confident that the proposed change won't break anything, and 
- there's sufficient time before the next release to make sure the change doesn't really screw things up, then

it can (and in most cases should) be merged without much discussion about its value. However, it's crucial to think skeptically about the reversibility w.r.t. our perceived obligations in this analysis.

Importantly, we shouldn't discuss the _value_ of proposed changes in the PR reviews. That's way too late in the process, and the emotional investment of the PR author is probably too high at that point. Rather, PRs for experimental changes should instead be discussed w.r.t. safety and reversibility. They should be merged, rejected, or sent for a revision round based on _those_ considerations.

#### What if proposed changes are actively _bad_?

There may be extreme exceptions, but I think it's generally okay to go ahead and merge, as long as current functionality isn't affected. Again, use your head. With this document, we want to encourage "moving fast and making mistakes". The point of harping on the reversibility aspect is that we can just merge it, see what (if any) feedback we get for a release (including from staff who notice the changes and love/hate them), and reverse the changes.

## Community research and marketing

There are some special considerations when doing community research, outreach, or marketing without going through normal channels.

### No obligations

Avoid setting up obligations for the Mathesar Foundation.

- Do not, for example, set up a Mastodon server on Mathesar's behalf.
- Do not tell community members that we'll definitely implement this or that feature
- Don't promote Mathesar at MySQL conferences by saying "we hope to support that someday".

### Minimal time investment

It's fine and encouraged to participate in various communities to let people know about Mathesar, but try not to spend too much time on it.

- 4 hours is reasonable for a quick dive into some community or exploring a marketing opportunity
- 1 hour per week is the max for participating in a community without any process.

### Avoid ad-hoc marketing for Mathesar

Staff should avoid making representations on behalf of Mathesar without going through any process with Kriti or other team members.

### Bring your research results to the team

This concept is similar to the accountabilibuddy section, but the triggers that require staff to loop in other team members are different:

- More than 4 hours spent researching a community or other opportunity
- More than an hour a week spent engaging with some community

If some research or experimental community engagement reaches those metrics, then

- Pitch the idea to another staff member, and
- if they think it's worth pursuing, then
- bring the idea to the rest of the team.
