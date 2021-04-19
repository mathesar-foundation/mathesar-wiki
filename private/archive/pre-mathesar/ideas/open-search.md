# Open Search

## Vision
The long term vision for “Open Search” is to
[accelerate knowledge, creativity, and innovation in the world](accelerate-innovation.md)
through: 
* making freely reusable IP discoverable through community driven search and
  curation tools.
* providing robust collaboration and community tools around open IP

## Option:  Focus on scholarly work, e.g., academic journal articles

### Goals

* Enable easy access to and citation of scholarly works
* Emphasize and promote scholarly works which are freely available
* Increase the production of new freely available and reusable scholarly works
* Strengthen the network of open scholarly works by providing rich contextual
  (meta)data
  
### Questions * Is lack of access to freely available scholarly resources _actually_ a
  barrier to creating more scientific work?
* Is the lack of collaboration tools _actually_ a barrier to creating more
  scientific work?
* Can a small team tackle the lack of collaboration tools in a way that will
  scale to different uses and domains?
* Is open science a good place to start or should we target another user group
  first?

### Competition
* Google Scholar:  Basically just google search but indexing Journal articles.
  Does not differentiate between freely available and non-freely-available in a
  meaningful way.  It does, however provide a download link when a
  freely-available version is found.  Shows all known versions of the article.
  Provides a citation helper widget that is quite nice.  For signed in users,
  it's possible to save results in a library for later perusal.  This is
  definitely the thing to beat (for basic search, anyway).  They seem to have
  full-text search working for most PDFs.
* Internet Archive Scholar:  Pretty great.  Version-aware, but not perfectly
  so.  Doesn't seem to be able to detect the "real" journal versions of
  pre-prints.  (See "Polynomial Bounds for the Grid-Minor Theorem" as a search
  query for an example)
* Sci-Hub:  Unbeatable user flow (to me) when it comes to finding a free
  download for a journal article.
* Unpaywall:  browser extension that detects when you're on a journal article
  site with a paywall, and then offers a 1-click button to download a legally
  available free version if possible.
* Open Access Button:  Offers similar functionality to Unpaywall, plus a
  similar search option to Sci-Hub.
* Academia.edu:  Kind of a social network for academics, but not very
  featureful.  There is a premium (pay) version with more features, but I'm not
  convinced it's worth it.  Even so, they claim to have ~ 145 million users.
  Depends on authors being members, and uploading copies of their papers.  Not
  possible to search without joining.
* Researchgate:  Fairly popular academic social network.  _Very_ closed to
  non-academic outsiders; joining is a massive pain, but it's possible to
  search without joining.  Somewhat known for copyright problems (not judging,
  but it might indicate a market opportunity)
* ORCID - Open Researcher and Contributor ID. More focused on allowing researchers
  to create profiles and ID, but tracks their publications and allows you to search.
  Similar to Researchgate and Academia.edu, in that it provides incentives for
  researchers to add their works and connect things together.
* Crossref - not really search, but a tool for generating DOIs and supporting
  tools such as ORCID. "Crossref makes research outputs easy to find, cite, link,
  assess, and reuse. We’re a not-for-profit membership organization that exists to
  make scholarly communications better."
* [Microsoft Academic](https://academic.microsoft.com/home) Similar tool for researchers to set up profiles and link their
  publications. Similar to Google Scholar, Reseachgate and Academia.edu.
  
### Integrations with other ideas 
* Source Commentary Ecosystem
  - This is fairly obvious, but if the search becomes popular enough, it could
    be a reasonable place for folks to discuss.
* Article Checker
  - This would be a natural search type:  You paste the link to some journal
    article, and retrieve PDFs of any referenced academic journal articles, for
    example
* Wander Search
  - I think this concept could work pretty well, with a couple of initial edge
    definitions being authors and citations.  That is, in academic research,
    it's common to want to follow citations of or by a paper (I.e., look up and
    downstream), as well as to find other papers by the same authors, or some
    subset of the set of authors.  I couldn't find any journal search that made
    these easy or natural.
* Automated Credibility Metrics
  - This could be incorporated into ranking of results, or just part of the
    information shown about an article.  Also possible would be PageRank (or
    some other eigenvector centrality metric)
### Apparent Market gaps in freely available journal article discovery

The only decent search-focused product I found is Google Scholar.  It's quite
good, and seems to be the project to beat.  The main weakness is that
navigating the citation graph is clunky and one-way.  That is, you can easily
find articles that cite a given article, but not articles that are cited _by_ a
given article.  This seems like an opportunity, since chasing references is a
normal thing to do in academic research.

When citations are given inline, it should be possible to track a given section
of a paper back to an upstream source.

For a more social, interactive product the things to beat are Researchgate and
academia.edu.  These are weaker products (IMO) than google scholar.  They are
closed from the outside (except for search on Researchgate), and require
membership to be very useful.  Neither provides a real useful means to comment
on or discuss a paper.

### Suggested MVP to distinguish in the market

A search product that makes it easy and intuitive to visually navigate the
citation graph around a given article.  Even cooler would be if it was possible
to navigate the inline citations in a similar way.  The initial search bar
should accept:
- A search query
- A URL
- A DOI

The second and third options above would enable navigating the citation graph
if you already have the article you want.

A super-cool feature would be to "reverse PDF search" an article by uploading a
PDF.  When I was doing research, I'd sometimes (often) end up with a PDF where
I didn't recall the origin, and would have to do the entire search process to
find wherever I'd found it.  It would have been pretty cool to upload it
somewhere, and be handed the location online of the paper, as well as be placed
in the citation graph.

### UI/UX ideas

#### Initial search page
![Initial search page](https://share.balsamiq.com/c/jYVE4jpBvyXgRH3KceDWcR.png)

#### The results page
![Results Page](https://share.balsamiq.com/c/nreLYp6H9yMgT7Y1ij2cyo.png)
The abstract and other details are hidden until the user clicks on a result.
The "Choose Version" drop-down allows switching between different locations
where the article appears online.  It should have info about whether the
version is a pre-print, and how much a pdf costs at that location.

#### Citation graph navigation
![Citation Graph View](https://share.balsamiq.com/c/oo5msy9DEkdP92rqbuxzwH.png)
This shows a UI for navigating the citation graph. "Upstream Articles" are
articles that the central article cites. "Downstream Articles" are articles
that cite the central article.  Clicking on the expanded up/down-stream article
should put it in the center; recurse.
  

## Option: More general focus on freely available content 

### Goals

* Enable communities using open content to curate their own data
* Enable the creation of community-led search engines for open content 
* Increase the production of new freely reusable IP
* Strengthen the network of open content by providing rich contextual data

### Questions
* Is the discoverability of open resources _actually_ a barrier to creating
  more open art and science?
* Is the lack of collaboration tools _actually_ a barrier to creating more open
  art and science?
* Can a small team tackle the lack of collaboration tools in a way that will
  scale to different uses and domains?
* Is open science a good place to start or should we target another user group
  first?

### One Potential Roadmap

Use the CC Search backend infrastructure to build a new product focused on
making open access publications and patents accessible to researchers and
innovators.

Once the product for researchers and innovators has found its footing, we will
then target more communities and turn the product into integrated platforms
that allow communities to curate data and build their own search engines.

#### Stage 1: Data ingestion, user research & discovery
* Identify current frictions, concerns, needs of researchers and innovators.
* Create MVP idea and product roadmap.
* Ingest open access research publications into the database
* Merge Prior Art Archive and Open Search infrastructure

#### Stage 2: Create new UI for researchers and innovators
* Create API
* Create UI for patents and open access publications
* Create collaboration tools
* Create curation tools

#### Stage 3: Expand into additional content types and communities
This could include:
* Textbooks
* Datasets
* 3D models
* Audio
* Video
* Journalism
* General text (e.g., Wikipedia articles)
* Code?
* Documentation?
* Sheet music?
