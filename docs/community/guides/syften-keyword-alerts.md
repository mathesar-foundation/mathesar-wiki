# Syften Keyword Alerts

!!! info "Tip"
    Have you been assigned a keyword alert task and are looking for what to do?
    See the [replying to users](#replying-to-users) or [documenting keyword alerts](#documenting-keyword-alerts) sections for next steps.


**Keyword alerts** refer to Mathesar-related keywords tracked across the web. We use a tool called [Syften](https://syften.com/) to monitor these keyword alerts, similar to Google Alerts, but more robust and tailored to technical products like Mathesar.

Keyword alerts need to be **triaged daily** to ensure timely engagement, community building, and brand reputation management.

## Understanding keyword alerts

We currently classify three types of keyword alerts. In order of their importance, they are:

1. **Mention**.
  Direct references to Mathesar. Actual discussions or mentions of our product in technical contexts (e.g., blogs, forums, social media). These are occasionally references to _Galaxy Quest's_ character of the same name. These mentions help us:
      - Collect user feedback.
      - Understand where users are coming from.
      - Find opportunities to respond to users directly.
1. **Recommendation**.
   Opportunities to recommend Mathesar to users of competitors, spreadsheets, or other products. these mentions help us:
      - Promote Mathesar to new users.
      - Identify user pain points.
2. **Competitor**.
   References to competing products. These mentions help us:
      - Identify user pain points.
      - Discover feature requests or gaps in competitors' products.
      - Gauge general sentiment and understand use cases within our space.

Keyword alerts are configured in [Syften](https://syften.com/setup).

## Daily keyword alert triage

!!! info "Tip"
    See the [daily checklist](#daily-tca-checklist) for a systemized "runbook" of the approach outlined here.


Keyword alerts are triaged daily by the Technical Community Advocate (TCA). A [script](https://github.com/mathesar-foundation/mathesar-infrastructure/actions/workflows/syften-to-asana.yml) runs every 30 minutes to convert the keyword alerts to asana tasks in the ["Community - Syften Keyword Alerts"](https://app.asana.com/0/1208897974386293/1208899405158619) Asana project.

The goals of the triage are to:

1. Close inactionable, irrelevant keyword alerts
1. Identify keyword alerts that need a response from the Mathesar team.
   - User support
   - User feedback
   - Opportunities to recommend Mathesar in a natural, relevant way.
1. Identify product feedback and user pain points to document, including from competitor and recommendation alerts.

### Assessing keyword alerts

Each keyword alert should be evaluated for any action items. If the keyword alert is actionable it should have it's "stage" field set as "Reply" or "Document" and assigned to a user. If neither of these sections seem appropriate for an alert, it likely isn't actionable! Keyword alerts moved to these categories are assigned to a Mathesar maintainer and given a due date by the TCA.

The TCA will leave on each task explaining its importance. For example:

- The keyword alert: "I am running nocodb and n8n currently. What are the benefits of using Postgres instead of sticking with what nocodb defaults with (i think it’s SQLite)?"
- The task comment: "This user wants to learn more about Postgres. We should provide general advice but disclose we work on a competing product called Mathesar {link to our homepage}"

Keyword alerts are **not actionable** when:

- The mention is not about Mathesar, a competing product, or the data needs of a potential user.
    - Examples:
        - "Mathesar was my favorite character in Galaxy Quest!"
        - Social media posts mentioning "Mathesar" in unrelated contexts like gaming or pop culture.
        - Repeated or low-value mentions like SEO-generated spam posts.
- The mention is a duplicate of an already reviewed entry.

#### Response schedule

Ideally users are responded to **as quickly as possible** by the assignee. Social media communications move quickly. Other products in this space also monitor their keyword alerts and perform similar outreach.

- Replies to users: **1 business day**
- Documentation: **2-3 business days**

It is important that we reply to users as quickly as possible and prioritize outreach over documentation.

### Assigning maintainers

Keyword alert tasks should be assigned to the most appropriate team member based on complexity and expertise, starting with @amandaj, then progressing to engineers or leads as needed.

Through this process we should develop and maintain a list of stock replies ([link here when created]()) to facilitate quick responses to common keyword alert types.

### Questions and feedback
If you have questions about this process of suggestions to improve it, feel free to reach out to community@mathesar.org with your ideas.

---


## Daily TCA checklist

This is the checklist for the daily triage of Keyword Alerts used by the Technical Community Advocate.

!!! info "Tip"
    If you do not see a particular category visible in Asana, it means there are currently no keyword alerts for that category.

In the [Syften Keywords Asana project](https://app.asana.com/0/1208897974386293/1208899405158619):

- [ ] 1. Check the ["past due" tab](https://app.asana.com/0/1208897974386293/1209010181792987) of the Asana project for any overdue replies or documentation. Ping the assignees of these tasks in the comments of the task. If tasks are repeatedly past due or require urgent atention, reach out to the assignee more directly using your preferred method (DM, email, etc.)
- [ ] 2. In the ["To Triage" tab](https://app.asana.com/0/1208897974386293/1208899405158619), Review the "Mention" category.
  - [ ] Set actionable tasks requiring a reply to the "Reply" stage, [assign a maintainer](#assigning-maintainers), and leave a comment with context. Set the due date to the end of the next business day.
  - [ ] Set actionable keyword alerts that do not require a response to the "Document" stage and assign a maintainer to respond within 2-3 business days. Be sure to leave a comment explaining what should be documented.
   - [ ] Mark all non-actionable tasks as completed and leave a comment explaining why they were not actionable.
- [ ] 3. In the [todo tab](https://app.asana.com/0/1208897974386293/1208899405158619), review the "Recommendation" category.
  - [ ] Set actionable tasks requiring a reply to the "Reply" stage, [assign a maintainer](#assigning-maintainers), and leave a comment with context. Set the due date to the end of the next business day.
  - [ ] Set actionable keyword alerts that do not require a response to the "Document" stage and assign a maintainer to respond within 2-3 business days. Be sure to leave a comment explaining what should be documented.
  - [ ] Mark all non-actionable tasks as completed and leave a comment explaining why they were not actionable.
- [ ] 4. In the [todo tab](https://app.asana.com/0/1208897974386293/1208899405158619), Check the "Competitor" category.
  - [ ] Set actionable tasks requiring a reply to the "Reply" stage, [assign a maintainer](#assigning-maintainers), and leave a comment with context. Set the due date to the end of the next business day.
  - [ ] Set actionable keyword alerts that do not require a response to the "Document" stage and assign a maintainer to respond within 2-3 business days. Be sure to leave a comment explaining what should be documented.
  - [ ] Mark all non-actionable tasks as completed and leave a comment explaining why they were not actionable.


## Replying to users

If you've been assigned a user reply, follow the below steps:

1. Read the original keyword alert and any comments left on the Asana task.
2. Draft your reply and leave it as an Asana comment.
3. Assign the Asana task back to the Technical Community Advocate (TCA) for review.
4. When your reply is approved, post it and leave a link on the Asana task.
5. Mark the task as completed.
6. Log the interaction in the [CRM](https://github.com/mathesar-foundation/mathesar-internal-crm).

## Documenting keyword alerts

There are two ways of documenting keyword alerts with slightly different processes.

## Replies

Any user outreach that resulted from a keyword alert should be documented in our [CRM](https://github.com/mathesar-foundation/mathesar-internal-crm). Typically the TCA will handle user outreach (or assign someone to do so), and after the interaction is done the task will be moved to the "Document" stage so a new assignee can document it in the CRM.

## Competitor information

Information about competitors, or feature requests should be documented in the Internal Mathesar instance. There is a table called "Product" in which any products related to Mathesar can be added. There is a table called "Product notes" where any notes about a product can be added. Typically, any Asana "Document" task will either be:

- A new competitor to add to "Competitors"
- A note about an existing competitor that should be added as a new "Product Note"

If there are any tasks to document that do not seem suitable for either category, please check in with the TCA.
