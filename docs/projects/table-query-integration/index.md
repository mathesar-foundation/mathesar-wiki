# Table Query Integration

"Table Query Integration" is project to build a new user-facing abstraction that would combine the best of the table page and data explorer into a single, powerful tool.

This wiki page is the top-level place to organize information about the project.

## High-level product specs

### Adopted

_(none yet)_

### Proposed

- Product spec
    - Sean's "Worksheets" proposal: [PR](https://github.com/mathesar-foundation/mathesar-wiki/pull/125) / [rendered](https://github.com/mathesar-foundation/mathesar-wiki/blob/worksheets_product_spec/docs/projects/worksheets/worksheets-product-spec.md)
    - Brent's "Data Palettes" proposal: [rendered](https://github.com/mathesar-foundation/mathesar-wiki/blob/data_palettes/docs/projects/data-palettes.md)

## Specific implementation specs

These specs are listed in the order in which we plan to implement them.

1. [Exploration Display Improvements](./specs/exploration-display-improvements.md)
1. [Exploration DML](./specs/data-explorer-dml/index.md)

## Meetings and video presentations

### 2025-02-03 Sean/Brent

- [Recording](https://tldv.io/app/meetings/67a0d254ecf1250013570192) (1h 44m)
- We discussed some of Brent's concerns with Sean's Worksheets product spec proposal:
    - **Composition** Instead of the query _types_ being polymorphic, Brent wants query _transformations_ to be polymorphic. To enter raw SQL, you'd enter it into a transformation. This way transformations could be saved independently and composed without any display. Brent doesn't want _worksheet_ composition. He wants _transformation_ composition.
    - **DML** Brent would like to offer DML in worksheets, but with some additional guardrails put in place to help users avoid confusing situations. We looked at an example of editing an author name shown in a table of books. He also wants to allow DML that updates _more than one cell in PostgreSQL_. His vision for this is not entirely fleshed out yet. We need to spend more time exploring and discussing this.
    - **Row Grouping** Brent has some concerns about the proposed row grouping functionality. At one point he said it "reduces the utility of row grouping". We didn't fully chase this topic down though.

### 2025-02-05 Sean/Pavish

- [Recording](https://tldv.io/app/meetings/67a38afeb4d4720013ed8288) (1h 14m)
- We mostly discussed questions that Pavish had about Sean's proposed Worksheets product spec in order to clarify Pavish's understanding of how Worksheets would work.
- Clarification seemed to resolve many of Pavish's concerns.
- **Where to worksheets get "saved"** was a question we spent some time on, with Sean being open to different approaches. Pavish didn't seem 100% convinced that saving a worksheet within a schema would be the best approach because (for example), the worksheet could reference DB objects outside the schema which could be confusing for the user. Perhaps some or all worksheets could or should be stored at the database level? We didn't fully chase down this thread to reach a point of clarity and agreement.
- **DML**: Sean gave Pavish a review of some of the user-facing problems that Brent had previously pointed out. We also discussed implementation details for DML. Pavish didn't raise any significant concerns or strong opinions here.
- **"Nested" data** (for lack of a better term) we discussed a new UI idea from Pavish to place aggregated data inside or underneath certain cells. Pavish's vision for this feature is still not 100% clear to Sean, but Sean expressed interest an enthusiasm for it. It's not something in the current draft of the spec, and Pavish seemed okay with that for the time being.

### 2025-02-06 Sean/Brent

- [Recording](https://tldv.io/app/meetings/67a4c0183608ca001388c5bd) (1h 30m)
- We discussed the differences between composition, and query-building in Sean's Worksheets vision and Brent's Data Palettes vision, with an emphasis on clarifying Brent's vision for Sean.

### 2025-03-07 Sean/Brent

- [recording](https://tldv.io/app/meetings/67cb10ef85a7070013ce452d) (1h 36m)
- **Short term vs long term goals**:
    - Brent expressed concerns that Sean has been focusing too much on long term goals at the expense of short term goals.
    - Sean expressed a strong intent to prioritize short term goals too. He conceded that his proposed Worksheets product spec did not articulate his desire to build incrementally. Sean wants the whole team to be aligned on the long term goals before building.
    - Brent wanted to know exactly _how much clarity_ do we need on the long term goals before we can start building.
        - Sean didn't have a simple answer.
        - But in talking it through, Brent and Sean seemed reasonably well aligned on this topic of "how much clarity do we need". We should figure out _roughly_ where we're going, and then identify strategies for building incrementally as soon as possible.

- **Long term — Worksheets vs Data Palettes**:
    - At the start of the call, Sean and Brent did not feel aligned on a long-term product vision for the user to define queries.
    - **Joins**:
        - Interestingly, Sean and Brent were able to identify (and hone in on) the concept of _joins_ as a sticking point, mutually, in their concerns with one another's designs.

        - Sean expressed concern that joins in Data Palettes would be too hard to use.

            Specifically he worried that they would require a conceptual understanding of joins which business users would be unlikely to have. He briefly mentioned difficulties that he had when learning joins, and said he's seen others struggle with these concepts too. Brent found this interesting and suggested circling back to it in another call. But Brent and Sean didn't explore any means to solve this problem within Data Palettes.

        - Brent expressed concern that joins in Worksheets would not offer enough power.
        
            Specifically he worried that the Basic Query would be incapable of joining a worksheet with a table or other worksheet. This join-related concern seemed to be the crux of his larger concern about worksheets being ill-suited for composition. Sean found Brent's join-related concern thrilling since he had also been pondering it, and he readily offered two potential solutions:

            1. The most elegant (but hardest) approach would be to use static analysis of SQL queries to identify join paths along existing foreign keys. He offered an example. This made sense to Brent.
            1. As a quicker solution, we could allow users to manually codify join paths between worksheets and tables, persisting those join paths in Mathesar metadata. It would be the responsibility of more technical users to specify the join paths. Then less-technical users would automatically gain access to them. This also made sense to Brent.
            
            Brent seemed rather appeased by Sean's potential solutions.

    - Brent expressed a desire to focus on Worksheets moving forward.
    
        His attempts at polishing out the problems with Data Palettes has required a lot of UI/UX thought, and he would like to think less about user interfaces moving forward.
    
        Instead, he would like to focus on identifying specific problems with Worksheets and working with Sean to find solutions to those problems.

    - Overall, this conversation brought Sean and Brent significantly closer to alignment on the long term goals!

- **Short term goals — editing exploration cells**:
    - Conveniently, Sean and Brent agreed that the nearest-term goal should be: allowing users to edit cells within explorations.
    - How to trace data provenance
        - Sean suggested building a SQL static analysis tool into which we could feed the SQL generated by the data explorer.
            - Brent didn't want to spend time on static analysis, at least not yet. He worried this would introduce too much delay in our deliverables. Sean understood this concern.
        - Brent suggested that we instead rely on the query structure within the data explorer.
            - Sean expressed concern that we'd be throwing away that work later.
            - Brent agreed we'd throw it away, but said it would only constitute about a week's worth of work.
            - Sean was satisfied with the throw-away work being small enough.
            - Both agreed.
    - How to hand off the right info to the front end
        - Sean suggested the following:
            - The `exploration.run` API would return some "analysis" data along with the result set.
            - For every column in the result set, the analysis would specify its origin table/column as well as which _other_ column in the result set would provide the row-reference values. Sean walked through some examples.
        - Brent liked Sean's approach
    - Both agreed we should aim to complete this editing flow for the 0.2.3 release.

### 2025-03-17 Sean/Brent

- [Recording](https://tldv.io/app/meetings/67d82b048f1e7a001325ba58) (56m) (Worksheets talk begins at ≈12:50)
- Sean and Brent have different opinions on how best to implement the "transport structure" for Worksheets.
- They have scheduled a follow-up meeting for next week where Brent will present specific problems to Sean.

### 2025-03-24 Sean/Brent

- [recording](https://tldv.io/app/meetings/67d855218f1e7a001325d83e) (1h 59m)
- This call focused on Brent's critique of Sean's Worksheets vision, with an emphasis on Sean's previously-state opinions of relying on SQL as the "transport structure" (terminology still in flux).

### 2025-03-27 Sean/Brent/Zack

- [recording](https://tldv.io/app/meetings/67e5610b32abaa0013ae274d)
- Sean presented a detailed critique of Data Pallettes. His _pre_-call notes are available [here](https://gist.github.com/seancolsen/182c8f682d46af865dce0283d3bc533e).

### 2025-04-02 Sean/Zack

- [Recording](https://tldv.io/app/meetings/67ed7b0edbc58600137debfc) 1h 9m
- Sync up on latest state of the plans
- Discuss how to reconcile disagreements between Sean/Brent

### 2025-04-03 Sean/Zack

- [Recording](https://tldv.io/app/meetings/67eecd6a1c3ba100136fdee9) 1h 18m
- Deep dive into Sean's vision for Basic Query
- Also talked about DML in explorations

### 2025-04-04 Sean video presentation

Sean presents a high-level vision for DML in explorations

57m

https://drive.google.com/file/d/1_iegEHHQaXiavVe_APng1y3W-h_iFm1h/view?usp=drive_link

### 2025-04-07 Sean/Pavish

- [Recording](https://tldv.io/app/meetings/67f3d3955cf32a0013fe65ed)
- Focused on plans for DML in explorations
- Also got Pavish up to speed on the disagreements that Sean and Brent have been having over the longer-term visions for query-building.

### 2025-04-10 Sean video presentation

Sean presents a vision for a "Pipeline Query" that could bridge the gap between "Worksheets" and "Data Palettes".

34m

https://drive.google.com/file/d/1hkL_WB3mHNYiLSVI3aqwplOUqRKbe7Cs/view?usp=drive_link

### 2025-04-10 Sean/Ghislaine

- [Recording](https://tldv.io/app/meetings/67f7c50e0ca096001444e7d4)
- Discussed plans for DML in explorations
- Ghislaine almost entirely on board with Sean's plans for UX
    - She wants to explore one potential change: using a split screen to multi-record cell contents in a panel below the table instead of inside a dropdown 

### 2025-04-14 Sean/Brent

- [Recording](https://tldv.io/app/meetings/67fd14ae0a16540013ef3f57)
- Reached several point of agreement on implementation of DML in explorations
- Brent seems more on board with Sean's longer-term vision for query-building

## Threads

- 2024-01-28 Email: [A "Worksheets for Everything" vision](https://groups.google.com/a/mathesar.org/g/mathesar-developers/c/CK7q1Wfg6D0/m/_5Tkdn-hAAAJ) - Sean introduces the concept of worksheets as a hypothetical future project

- 2024-01-31 Email: [Worksheets Product Spec](https://groups.google.com/a/mathesar.org/g/staff/c/XJH99KmBiAU) - Sean introduces a PR proposing a formal product spec. He invites people to read it but requests withholding detailed critique until the team has decided to pursue the project.

