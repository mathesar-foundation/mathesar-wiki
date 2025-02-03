# Worksheets Project

"Worksheets" is a _(still hypothetical)_ project to build a new user-facing abstraction that would combine the best of the table page and data explorer into a single, powerful tool.

This wiki page is the top-level place to organize information about the project.

## Specs

- (DRAFT) Product spec ([PR](https://github.com/mathesar-foundation/mathesar-wiki/pull/125))

## Meetings

### 2024-02-03 Sean/Brent

- [Recording](https://tldv.io/app/meetings/67a0d254ecf1250013570192) (1h 44m)
- We discussed some of Brent's concerns with the product spec proposal:
    - **Composition** Instead of the query _types_ being polymorphic, Brent wants query _transformations_ to be polymorphic. To enter raw SQL, you'd enter it into a transformation. This way transformations could be saved independently and composed without any display. Brent doesn't want _worksheet_ composition. He wants _transformation_ composition.
    - **DML** Brent would like to offer DML in worksheets, but with some additional guardrails put in place to help users avoid confusing situations. We looked at an example of editing an author name shown in a table of books. He also wants to allow DML that updates _more than one cell in PostgreSQL_. His vision for this is not entirely fleshed out yet. We need to spend more time exploring and discussing this.
    - **Row Grouping** Brent has some concerns about the proposed row grouping functionality. At one point he said it "reduces the utility of row grouping". We didn't fully chase this topic down though.

## Threads

- 2024-01-28 Email: [A "Worksheets for Everything" vision](https://groups.google.com/a/mathesar.org/g/mathesar-developers/c/CK7q1Wfg6D0/m/_5Tkdn-hAAAJ) - Sean introduces the concept of worksheets as a hypothetical future project

- 2024-01-31 Email: [Worksheets Product Spec](https://groups.google.com/a/mathesar.org/g/staff/c/XJH99KmBiAU) - Sean introduces a PR proposing a formal product spec. He invites people to read it but requests withholding detailed critique until the team has decided to pursue the project.

