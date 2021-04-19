# Automated Data Scraper / ETL (for the masses)

Related to:

- [Use Open Information / Science to Enhance Credibility](credibility.md)
- [Accelerate Knowledge, Creativity, and Innovation](accelerate-innovation.md)
- [Innovate Discovery](innovate-discovery.md)

Inspired by `needlebase`: https://www.youtube.com/watch?v=58Gzlq4zSDk

## Problem

Many applications exist for pulling large volumes of data from web pages (and
other sources), and transforming it into the desired data model. However,
writing web scraping scripts requires a specialized skill-set, and tends to be
somewhat boring / tedious work for those who _do_ have the skill-set.

## Solution

Automate it. The fact that writing such scripts is often boring / tedious
indicates that it should be possible to automate it. The ideal user flow would
involve some GUI that lets them
1. create a data model, 
1. select parts of a data source to map to different elements
1. export a script implementing the mapping in some language (e.g., python)
1. just do the scraping via GUI if they prefer and export the resulting data.
1. Add more data sources as desired to the data through the same model.

Probably should integrate with AWS (or other cloud services) to store large
volumes of data.

## User flow for product
  
## Technical feasibility

- There are a number of proprietary solutions that do similar things to what
  we're thinking. Therefore, it should be possible.
- We'd want to handle each of:
  - APIs (JSON only, or also XML?)
  - JSON, line separated JSONs
  - XML
  - Parquet
  - TSVs / CSVs
  - Excel spreadsheets
  - WARC (e.g., Common Crawl)
  - Scraping web pages
  - etc.
  
  as input formats at some point.
- It should be possible to start with our favorite input format (as long as
  it's generic enough, e.g., JSON or XML), then map all other formats to that
  one for further extensions
- There are some parts that could help with the web scraping goal, but we don't
  think we should start at that level yet.
- However,  there are some browser
  automation frameworks (e.g., Selenium) that could be used to record user
  navigation and clicks. This could provide a way to do the crawling part of
  web scraping by emulating and generalizing a user's path through the site.
- Also interesting is the open source tools apify


## Real world use cases

## Competition

- [Octoparse](https://www.octoparse.com/)
  - Closed source, but seems like a pretty good product.
- [Web Scraper](https://webscraper.io/)
  - This is a fantastic product, and has a free Chrome browser extension. It's
    unfortunately proprietary. It's so good that I suspect we'll not have much
    success drawing users away without other integrated components.
- [AWS Glue](https://aws.amazon.com/glue/)
  - This is another product with a subset of the intended eventual
    functionality. It can take a number of filetypes and databases and convert
    between them (i.e., set up a map and actually shunt the data about).  It
    does not, however, include any web scraping functionality, and the
    filetypes are restricted. Also, it only exists on AWS (obviously).
- [Talend](https://www.talend.com/products/talend-open-studio/)
  - This is a really high-quality open source project.  The downsides are that
    it has kind of an old school enterprise software vibe. **More investigation
    of this product is definitely needed**
- [Airbyte](https://airbyte.io/)
  - They seem to be aimed at solving many (maybe all) of the problems we are
    looking at with this idea.
- [DBT](https://www.getdbt.com/)
  - Lower-level than Airbyte.
  - Open source
  - Really cool ideas and UI around determining and verifying data provenance
    and transformations.

## Challenges

- This idea is susceptible to getting Mongoed (i.e., AWS could create a
  managed, proprietary version). Perhaps it's niche enough to avoid the
  problem, but then is it something we really need to work on?
- For cleaning and checking the data, it may be that specialized skills would
  still come into play.

## Thoughts

- Developing a community around this would be extremely beneficial, and
 probably relatively easy.
 - Some more tech-savvy users would probably be able / willing to contribute
  some cleaning scripts for models associated with popular websites. These
  should be shareable and it should be possible to collaborate on them.
- This _may_ be a solved problem: See
 - https://apify.com/
 - https://en.wikipedia.org/wiki/Data-driven_journalism#Finding_data (see the
  other scrapers listed)
- Brent is becoming more and more convinced that this is a solved problem (or
  at least that the effort-reward ratio isn't great for us in this space)
