---
title: Social network centered on source material
description: 
published: true
date: 2021-04-19T21:17:09.151Z
tags: 
editor: markdown
dateCreated: 2021-04-19T20:19:20.433Z
---

Related to both [credibility](../goals/credibility), and [accelerate innovation](../goals/accelerate-innovation).

## Problem

Modern social networks and discussion sites are constantly linking out to the
actual material folks are discussing:  A huge number of reddit posts, for
example, are about a news article or some other material that's hosted
somewhere else.  This makes it difficult to track the context around the
discussion, since only snippets of the article are available inline with the
commentary.  This makes claims in discussion difficult to verify.

## Solution

For openly licensed material, this is unnecessary.  Imagine being able to
discuss, e.g., a scientific publication inline (think M$ Word or Google Docs
comments).  Even better would be if there was a way to smoothly follow a
conversational thread through multiple sources (since a good discussion might
reference different things).  This is sort of the "inverse" of the way most
discussion of articles happens at the moment (yes, there are comments available
on many articles, but the experience is not uniform and the UX is often not
great).

## Potential Users
- General public
- Researchers (this would be fantastic for understanding new research in
  collaboration with others in the field, for example)
- Students (similar to researchers, but to work with others struggling on a
  topic)
- Journalists (this could be a great place for them to transparently discuss
  some source that's being reported upon.)

## Challenges
- The UX/UI challenges would be significant (how would you organize the user's
  flow between sources while following the same conversation?).
- This would take clicks away from source material.  For some (e.g., scientific
  articles) that's probably not a problem, but for others (e.g., blog posts)
  that could be a big issue.
  - This could be solved by making it a browser extension.  For privacy
    reasons, we'd need to be quite judicious about when or how to "phone home"
    to see if there's a discussion about a relevant article (and retrieve the
    discussion if desired).
    
## Thoughts
- As we see from Personal Knowledge Management (PKM) everyone has different
  learning styles, reading styles, annotation styles, sharing styles and
  it might end up looking more like a system of tools and UX/UI hacks rather
  than a single one. This is harder to scale, but maybe more acceptable. This
  idea of a "single user interface" for all knowledge and "literature notes"
  has been explored and is very interesting in the PKM community.
- It would be cool / interesting if one could "subscribe" to different meta-net
  feeds to discuss pages/articles, links between pages, and maybe even
  groupings of different pages that are user-generated in real-time while
  reading them.  This could happen in an extension-provided sidebar, for
  example.  I think that could help with the "social" aspect, and allow one to
  be more judicious about how and with whom they discuss or annotate.  It
  should be possible to keep your own personal annotations as well.  Imagine
  something like youtube stream chats, but for the broader internet (and
  require subscribing to different groups of people).  What if you could "pull"
  people to where you are in a page or article to say "look at this" in real
  time?
- The model could be something like:
  - each URI on the internet can be referenced in an arbitrary number of
    discussions.
  - Discussions themselves have URIs.
  - Also, each discussion can reference an arbitrary number of URIs (including
    itself, or other discussions on some subset of the URIs involved).

  The user could start in discussion-land by just checking their feeds, or
  enter discussion land from an interesting webpage by checking their extension
  to see if anyone is talking about it.
- Kind of a meta-net over the normal net that enables discussion.
  
## Integration

This could integrate with both [Open Search](./open-search) and
[Article Checker](./article-checker) as entry points.
