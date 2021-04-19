# Local document full text search

## Problem

A journalist might want to digest a large volume of pages in various electronic
formats, potentially organized over a number of files. For example, when going
through FOIA-released documents. Further, the documents should not leave the
journalist's computer or physical possession. Also, when working on a story,
time is often short. This means any analysis must be done quite quickly and
efficiently.

Current solutions to this problem seem to fall into a number of categories:
- Cloud based: This is unacceptable for security reasons
- Server-client on local machine: Setting these up is too technical for most
  journalists
- Incomplete: There are some document management systems that handle only
  `.pdf` files, but not, e.g., `.docx` files.
  
All current solutions that do something similar seem to be focused on helping a
user organize their own scans of their own documents. This means the current
solutions generally can't handle the potential scale of a document dump that a
journalist might explore, and also lack the type of organization tools they
might want/need.  They're also organized around directories representing
document type, rather than projects representing documents that are connected
somehow.

## Solution
A local app that can index and search documents of various types at large scale,
as well as make connections between different documents, or different sections
of the same document.  A client-server interface (i.e., opening a browser
window at localhost:XXXX) might work initially, but the installation would have
to be completely non-technical.

## Feasability

There are a number of tools that could be patched together to build this
quickly and easily.  There already exist tools to do the separate steps of the
following process:
1. Extract text from various file formats (images, pdfs, docx, etc.).
2. Index the text for fast fuzzy searching.
3. Display the relevant file formats

Missing pieces are:
- A viewer that handles arbitrary document formats for viewing and annotating
- A UI for organizing different documents or pieces of documents into a
  "project"
- A way to link search results from plain-text versions of arbitrary files to
  locations in the original
- An easy-to-use installation process for non-techie users.
  
## Potential Users
- journalists (see the motivating problem)
- scientists and other academics (a number of papers are based on analyses of
  large volumes of previous work)
- archivists (making collections of digitized works searchable)

## Challenges

- User base is specialized, and may have specific needs that are difficult to
  predict.
- Keeping up with changing file formats will be a drag over time (perhaps we
  could lean on parts of libreoffice to help)

## Questions

- What scale is necessary for this to be useful?
- How common is the envisioned task (searching through a large volume of
  documents) for the intended users?

## Competitors

There are a number of open source "Document Management Systems".  See the list
from [Awesome Self
Hosted](https://github.com/awesome-selfhosted/awesome-selfhosted#document-management).
These have some of the desired functionality, but generally fail to handle the
necessary scale, and also have user flows focused on managing one's _own_
documents (e.g., mail) rather than looking through large volumes of unfamiliar
documents.  Also, since they're not generally aimed at research, they generally
lack the annotation and connection functionality desired.

The best competitor (we're aware of) _would_ have been
[CaseBox](https://www.casebox.org/), but it's been discontinued.  We should
_absolutely_ talk with them to see why they discontinued the product, and what
their understanding of the landscape is.
