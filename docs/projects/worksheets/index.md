# Worksheets Project

"Worksheets" is a _(still hypothetical)_ project to build a new user-facing abstraction that would combine the best of the table page and data explorer into a single, powerful tool.

This wiki page is the top-level place to organize information about the project.

## Specs

### Adopted

_(none yet)_

### Proposed

- Product spec
    - Sean's initial: [PR](https://github.com/mathesar-foundation/mathesar-wiki/pull/125) / [rendered](https://github.com/mathesar-foundation/mathesar-wiki/blob/worksheets_product_spec/docs/projects/worksheets/worksheets-product-spec.md)
    - Brent's "Data Palettes" proposal: [rendered](https://github.com/mathesar-foundation/mathesar-wiki/blob/data_palettes/docs/projects/data-palettes.md)

## Meetings

### 2024-02-03 Sean/Brent

- [Recording](https://tldv.io/app/meetings/67a0d254ecf1250013570192) (1h 44m)
- We discussed some of Brent's concerns with the product spec proposal:
    - **Composition** Instead of the query _types_ being polymorphic, Brent wants query _transformations_ to be polymorphic. To enter raw SQL, you'd enter it into a transformation. This way transformations could be saved independently and composed without any display. Brent doesn't want _worksheet_ composition. He wants _transformation_ composition.
    - **DML** Brent would like to offer DML in worksheets, but with some additional guardrails put in place to help users avoid confusing situations. We looked at an example of editing an author name shown in a table of books. He also wants to allow DML that updates _more than one cell in PostgreSQL_. His vision for this is not entirely fleshed out yet. We need to spend more time exploring and discussing this.
    - **Row Grouping** Brent has some concerns about the proposed row grouping functionality. At one point he said it "reduces the utility of row grouping". We didn't fully chase this topic down though.

### 2024-02-05 Sean/Pavish

- [Recording](https://tldv.io/app/meetings/67a38afeb4d4720013ed8288) (1h 14m)
- We mostly discussed questions that Pavish had about Sean's proposed product spec in order to clarify Pavish's understanding of how Worksheets would work.
- Clarification seemed to resolve many of Pavish's concerns.
- **Where to worksheets get "saved"** was a question we spent some time on, with Sean being open to different approaches. Pavish didn't seem 100% convinced that saving a worksheet within a schema would be the best approach because (for example), the worksheet could reference DB objects outside the schema which could be confusing for the user. Perhaps some or all worksheets could or should be stored at the database level? We didn't fully chase down this thread to reach a point of clarity and agreement.
- **DML**: Sean gave Pavish a review of some of the user-facing problems that Brent had previously pointed out. We also discussed implementation details for DML. Pavish didn't raise any significant concerns or strong opinions here.
- **"Nested" data** (for lack of a better term) we discussed a new UI idea from Pavish to place aggregated data inside or underneath certain cells. Pavish's vision for this feature is still not 100% clear to Sean, but Sean expressed interest an enthusiasm for it. It's not something in the current draft of the spec, and Pavish seemed okay with that for the time being.


## Threads

- 2024-01-28 Email: [A "Worksheets for Everything" vision](https://groups.google.com/a/mathesar.org/g/mathesar-developers/c/CK7q1Wfg6D0/m/_5Tkdn-hAAAJ) - Sean introduces the concept of worksheets as a hypothetical future project

- 2024-01-31 Email: [Worksheets Product Spec](https://groups.google.com/a/mathesar.org/g/staff/c/XJH99KmBiAU) - Sean introduces a PR proposing a formal product spec. He invites people to read it but requests withholding detailed critique until the team has decided to pursue the project.

