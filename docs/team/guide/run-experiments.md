# Experiments

This quick guide outlines best practices for Mathesar staff when conducting "experimental" work. For example:

- Adding a feature to Mathesar without going through the product process.
- Promoting Mathesar in some previously-unknown venue.
- Adding an integration with a 3rd-party service to Mathesar or its repo, e.g., a 1-click deploy button.

We encourage experimenting with these sorts of things without the bureaucratic overhead of normal processes, but staff should make sure their experiment satisfies some basic guidelines.

## Guidelines for an acceptable experiment

These are ordered from most to least important.

### Easily reversible

An experiment should be easily reversible on a technical level. This means:

- Avoid distributing experimental code changes throughout the entire codebase. Contain them in a dedicated directory if possible.
- Make it obvious to other developers through comments or other means that they should not depend on the experimental code.
- Removing any code changes associated with the experiment should be a 5-minute project leading to an easily reviewable PR.
- Experimental GitHub workflows should be in their own file.

More importantly, an experiment must be _reversible w.r.t. our perceived obligations to the public._

- It should be obvious to a user that an experimental feature might disappear in the next release.
- Experimental wrappers or integrations must not set up a long-running dependency. For example, a 1-click deploy button is fine if it doesn't require any special Docker setup. In that case, a user could continue to upgrade and use Mathesar by following our Docker instructions, even if we stop supporting a given 1-click deployment method.
- Experimental promotions of Mathesar should not set up any obligations for the project (e.g., don't promote Mathesar at MySQL conferences by saying "we hope to support that someday").
- Experimental installation methods should not require changes to the main Mathesar codebase.

Finally, the experiment must be reversible _in your mind_. It's crucial to be honest with yourself and ask:

> - If this doesn't work, will I let it go without a second thought?
> - Am I going to be willing to admit when it isn't working?

If the answer to these questions are anything but a resounding "Yes and Yes!", staff are strongly encouraged to go through normal processes rather than just taking off on their own. This brings us to the next section.

### Doesn't break anything

- Obviously, added experimental functionality shouldn't break or obscure current functionality in the product.
- Experimental promotion of Mathesar in a new venue shouldn't contradict or dilute other marketing efforts.
- Changes to support an experimental 1-click deployment can't break any previous installation methods.

### Minimal time investment

This is obvious, but bears mentioning. Do not spend more than 8 hours working on something experimental without talking to anyone else about it. Even better, talk to someone else after 4 hours of time investment.

## Find an Accountabilibuddy

In the event that the 4 hour mark has been crossed in time investment in an experiment, staff are _strongly encouraged_ to find an accountabilibuddy. If time investment crosses 8 hours, this is required. 

- Choose any staff member (with sufficient context, and ideally a skeptical attitude) to be your accountabilibuddy for the experiment. 
- Their role is to listen to a short pitch, look at any examples or output of the experiment so far, and assess the experiment according to the guidelines above. 
- If it seems like the experiment is worth continuing, the staff member who originated the experiment and the accountabilibuddy should let the rest of the staff know what they're doing through typical channels (Matrix, email). 
- They should be prepared to be told to stop what they're doing, or go through the normal process if appropriate. In some cases, the consensus may be "just keep going".

## Responsibilities for PR reviewers

Pull requests adding functionality which hasn't gone through any typical process and which don't meet the above criteria to be easily reversible, or which aren't demonstrated to avoid breaking things should be closed with minimal discussion. Yes, this is a bit imprecise; staff should use their heads.

- A PR closing an issue which has been triaged by someone on the team (who didn't write it) counts as typical for now, subject to any product process imposed by Zack moving forward.
- A PR closing an issue written by the PR author with no discussion with anyone else is experimental. So, it must be easily reversible and effort should be spent making sure no current functionality should be broken by the proposed change. If that's the case, go ahead and merge.

On the other hand, if a PR

- meets the easily-reversible criteria above, and
- the reviewer is confident that the proposed change won't break anything, and 
- there's sufficient time before the next release to make sure the change doesn't really screw things up, then

it can (and in most cases should) be merged without much discussion about its value. However, it's crucial to think skeptically about the reversibility w.r.t. our perceived obligations in this analysis.

Importantly, we shouldn't discuss the _value_ of proposed changes in the PR reviews. That's way too late in the process, and the emotional investment of the PR author is probably too high at that point. Rather, PRs for experimental changes should instead be discussed w.r.t. safety and reversibility. They should be merged, rejected, or sent for a revision round based on _those_ considerations.

### What if proposed changes are actively _bad_?

There may be extreme exceptions, but I think it's generally okay to go ahead and merge, as long as current functionality isn't affected. Again, use your head. With this document, we want to encourage "moving fast and making mistakes". The point of harping on the reversibility aspect is that we can just merge it, see what (if any) feedback we get for a release (including from staff who notice the changes and love/hate them), and reverse the changes.
