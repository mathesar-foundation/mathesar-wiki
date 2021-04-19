# Wander search

Related to [Innovate discovery](innovate-discovery.md)

## Problem

Standard search tools don't align with how I want to find media (music,
pictures).  Maybe I want a dark picture of a house, but not too dark, so that
it fits in with a webpage I'm designing.  I would have to look on a current
image search with the query "house", then try scrolling around till I find one
that suffices.

## Solution

Start with the flow above, then add the ability to search "around" the closest picture found in some space:
- "like this but a bit darker"
- "similar composition, but with a dog instead of cat"
- "similar to this picture, but with an open license"

And so on.  The idea is to let users "wander" in different directions through
the space of search results (or even the general space of a given type) in a
more natural way.

## Challenges

- How would we choose the right dimensions?
- The UX seems difficult.

## Thoughts

- Some of the dimensions can be automated (lighter<->darker, saturated<->gray,
  red<->green) for some types in obvious ways.  Others seem like they'd need
  more work.  For example, it might be possible to source inspirations for
  bands from somewhere, then let people discover music by following that graph
  around.  "Similar composition" can be detected, but requires (expensive)
  image processing at scale.
- The truly mind-blowing way would be to have a method of interpreting user
  input into directions in the space.  I.e., given a bunch of vectorized
  objects through which a user can wander, how can we translate "happy<->sad"
  as a query into a direction in that space?  (It would almost certainly just
  have to be more-less happy, since it's unlikely that happy and sad would be
  perfectly opposite).  If this was accomplished, the benefits would be huge.
  We'd be able to have a user start at a given image, then type a sequence of
  queries like:
  1. Like this, but a dog
  1. lighter
  1. with more trees
  1. with the dog further left in the shot
  1. etc.
  
  In betwen each query, they'd be presented with a list of search results,
  perhaps ranked by similarity to the image from which they're coming.  They'd
  pick a new image at that stage, and recurse.
- It might be difficult to help users understand "direction".  For example, if
  above the user input "with the dog facing left" as one of the steps, it would
  be fundamentally different than all the rest of the queries (kind of a
  discontinuous jump in the space).  We'd either need to include that
  functionality for some dimensions, or somehow discourage it through UX/UI
  magic.
- This seems somehow easiest to envision for images (thus the focus of most
  examples), but could certainly work for music.  For video, I can't envision
  the actual use case for this type of wandering.  (I want to see another video
  like this one, but shorter??)
- There may be some interesting machine learning innovations, for example with
  common sense AI or Probabilistic Computing that might help. Danny Hillis might
  have some good ideas too.
