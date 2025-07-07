# MCP Server

| **Role**     | **Person**  | **Status**     |
| ------------ | ----------- | -------------- |
| **Author**   | Zack Krida  | 🟢 Done        |
| **Reviewer** | Kriti Godey | 🔵 In review   |
| **Reviewer** | Brent Moran | 🔵 In review   |

## The Problem

["Vibe coding"](https://en.wikipedia.org/wiki/Vibe_coding) has become a popular paradigm for software development, empowering users with varied expertise to create their own software. Databases are an inherently complex, but often necessary, part of software development. Interacting with them typically requires significant technical knowledge. This is often a pain point for users ([example](https://www.reddit.com/r/vibecoding/comments/1kx72kj/how_do_you_keep_your_ai_agents_vibing_with_your/), [example 2](https://www.reddit.com/r/vibecoding/comments/1k5su89/vibe_coding_got_me_far_but_backend_almost_broke/)) that Mathesar can help solve.

Mathesar can serve as a development companion and admin back-end for vibe-coded applications. When integrated with a [Model Context Protocol (MCP) server](https://modelcontextprotocol.io/introduction) server, Mathesar transforms into a natural-language-powered bridge between the complexity of databases and the ease of vibe-coding.

Although users haven’t explicitly asked for this functionality, there are strong indicators—drawn from competitors, the tech media, and internal stakeholders—that a simple, beta-level MCP server integration would be highly valuable. This is an opportunity to be at the forefront of AI integrations in data platforms.

### Is it feasible to solve?

We’ve already conducted a time-boxed 2-hour experiment that yielded a working prototype. Some refinement is needed, especially for type safety and authentication, but technical feasibility is confirmed.

## Use Cases

As a non-technical t-shirt business owner "vibe coding" my shop's application using an LLM, I want to:

- Model my app's database schema using natural language, where prompts like "I need a way to store users and their passwords in my application" result in the creation of database tables.
- Have an easy-to-use user interface for making quick edits to my app without having to code an entire backend.
- Ask an LLM to show me my app's top-selling products without configuring a complex data exploration interface.
- Generate product descriptions via AI and populate them in the product table using a single natural language prompt.

## Success Criteria

We'll know we've succeeded if users are using the MCP server, as indicated by the following signals:

- Users give feedback on the MCP server, via GitHub issue. Bug reports, feature requests, or outright complaints are all positive signals here.
- GitHub stars on the MCP server repository increase.
- Content (blog and social posts primarily) about Mathesar's MCP server sees notable traffic.

## Requirements

- Create an MCP server which users can run locally to connect to a Mathesar instance.
- Give access to the same DML and DDL tools available in Mathesar's user interface to the LLMs integrated with the MCP server.
- Ship quickly to catch the current "MCP wave" and to start getting feedback as quickly as possible.

## Ecosystem Analysis

**Supabase**: Has a built-in MCP server with broad exposure (100k+ views on demos). Allows full SQL execution without restrictions: powerful, but riskier.

**Baserow**: Provides a controlled MCP experience with CRUD functionality:

- Create: e.g., "Add a new task called ‘Review Documentation’."
- Read: e.g., "Find all projects due this week."
- Update: e.g., "Change the status to ‘In Progress’."
- Delete: e.g., "Delete completed tasks older than 30 days."

**Others**:

- NocoDB, Teable, and other platforms have experimental or unofficial MCP servers with limited capabilities.

This landscape validates the opportunity for Mathesar to offer a differentiated, natural-language-driven data platform experience.
