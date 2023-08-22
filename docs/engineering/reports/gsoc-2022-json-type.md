# GSoC 2022: JSON data type

# GSoC 2022: JSON data type

**Author**: [Jinxiao Li](https://github.com/Jinxiao0302)

> Jinxiao originally sent this project report to the developer mailing list, [see here](https://groups.google.com/a/mathesar.org/g/mathesar-developers/c/7iHlVobzW08)
{.is-info}


---

Hey all, 

I am Jinxiao Li, a lucky Mathesar contributor at Google Summer of Code 2022. During this three-month coding period, I am delighted to work with [@Brent Moran](mailto:brent@centerofci.org) and [@Pavish Kumar Ramani Gopal](mailto:pavish@centerofci.org) to implement Mathesar database functions for JSON data types. I am very grateful for the support of every team member and the enjoyable time I spent on this project.

The works are listed below at the Github links and you can also have a look at the project description [here](https://summerofcode.withgoogle.com/programs/2022/projects/ggLRaaH3). We implemented two main custom types for this goal: Mathesar JSON array and Mathesar JSON object. Most of the functions are settled down while a few are in progress but can be completed very soon. Feel free to leave comments and suggestions.

**JSON type reading and casting implementation**

- Main implementation: [https://github.com/centerofci/mathesar/pull/1443](https://github.com/centerofci/mathesar/pull/1443)  
- Minor issue fixes: [https://github.com/centerofci/mathesar/pull/1474](https://github.com/centerofci/mathesar/pull/1474)

**JSON type sorting implementation**

- Sorting for JSON array type: [https://github.com/centerofci/mathesar/pull/1482](https://github.com/centerofci/mathesar/pull/1482)
- Sorting for JSON object type: [https://github.com/centerofci/mathesar/pull/1565](https://github.com/centerofci/mathesar/pull/1565)

**JSON type filtering implementation**

- JSON array length equals function as well as tests: [https://github.com/centerofci/mathesar/pull/1493](https://github.com/centerofci/mathesar/pull/1493)
- JSON array length <, <=, >, >= functions as well as tests: [https://github.com/centerofci/mathesar/pull/1528](https://github.com/centerofci/mathesar/pull/1528)
- JSON object filtering functions (in progress): [https://github.com/centerofci/mathesar/pull/1606](https://github.com/centerofci/mathesar/pull/1606)

**Other issue fixes**

- Fix reference column bug when deleted: [https://github.com/centerofci/mathesar/pull/1275](https://github.com/centerofci/mathesar/pull/1275)
- Fix loading skeleton issue when rows are deleted: [https://github.com/centerofci/mathesar/pull/1351](https://github.com/centerofci/mathesar/pull/1351)

Jinxiao Li