# Forms (Public)

## The Problem

Users need a way to collect structured data from people outside their organization, such as volunteers, customers, or survey respondents, without requiring those users to log in or provide any information beyond that needed by the form.

Today, Mathesar only allows data entry through the logged-in spreadsheet interface, which:

- Limits collaboration to internal users
- Makes it impossible to collect one-off or community-sourced submissions
- Adds unnecessary friction for low-risk, high-volume data collection scenarios

Users have [explicitly requested](https://github.com/mathesar-foundation/mathesar/discussions/2264) this feature:

- *"If Mathesar had this, we would have selected it over NocoDB. We have a lot of plans for this, such as a contact us form on our website, customer satisfaction surveys, and data entry for our production systems."*
- *"If we could create and use different forms to fill the database that would be very interesting because it would avoid having to develop an entire database management interface."*
- *"This feature would enable diagnostics EUA submissions to the FDA where the FDA could spin up a table with an associated form for diagnostic manufacturers to populate."*

### Is it feasible?

This feature is a common one with lots of prior implementations to take inspiration from, and forms are a foundational part of frontend software engineering, so it’s unlikely our team would be unable to work on this.

We can look to examples like Airtable, NocoDB, Baserow, and even Google Forms to design and implement an ideal flow.

## Use Cases

As the admin of a community movie database, I want to:

- Build a single form that allows community members to add new movies, generes, and the related crew in one place for ease and convenience.
- Avoid users submitting invalid data so that our small team doesn't have to manage spam or invalid submissions.
- Preview the form and test it before making it public, so that we don't provide a bad experience or collect data incorrectly in a way that messes up our dataset.
- Make sure users know their submission was received correctly after they fill out the form, so that they aren't confused and don't contact us to verify.

## Success Criteria

This problem is worth spending a substantial, "large" amount of time on. We'll know it's successful when:

- Analytics data indicates that users are creating forms.
- Surveyed users are creating forms or identifying forms as a "key feature" that led to their Mathesar adoption.

## Requirements

These requirements are from the point of view of the user and aim to represent all of the interaction surfaces that they have with this feature in Mathesar. They are not meant to map to implementation details. Some requirements may not need any implementation work done to fulfil them.

### Form Creation & Management

- Users can create a form for any table they have access to.
- Users can choose which fields to include, reorder them, and configure field-level settings (e.g., required, help text, placeholder).
- Users can preview a form before publishing.
- Users can customize the title, description, and confirmation message shown after submission.
- Users can delete forms.

### Form Sharing

- Form access does not provide acces to tables, the Mathesar UI, or any underlying data.
- Users can generate a public URL to share the form.

### Submission Experience

- Form submitters do not need to log in.
- Users receive a confirmation message or page redirect after submitting.
- Submissions are validated against field types and constraints (e.g., required fields, enum values).
