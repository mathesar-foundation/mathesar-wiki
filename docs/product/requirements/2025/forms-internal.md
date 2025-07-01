# Internal Forms

| **Role**     | **Person**  | **Status**     |
| ------------ | ----------- | -------------- |
| **Author**   | Zack Krida  | 🟢 Done        |
| **Reviewer** | Kriti Godey | 🔵 In review   |
| **Reviewer** | Brent Moran | 🔵 In review   |

## The Problem

In environments where structured data must be collected—such as libraries, schools, or office systems—users often need to submit information without having full visibility into the underlying dataset. There is a need for a secure and structured method of data entry that ensures cleanliness, consistency, and control.

Internal forms address this by allowing **authenticated users** to submit data within a shared system context. Unlike public forms, internal forms link submissions to user accounts and system metadata such as timestamps, providing an auditable and secure workflow. These forms are also integrated into the Mathesar UI for logged-in users, rather than exposed via public "share" links.

### Is it feasible?

This feature builds on _existing_ work on anonymous forms and leverages Mathesar's current UI elements and RPC methods. The primary new work involves:

- Enhancing the form interface to be more accessible throughout the app.
- Introducing support for dynamic defaults and new data types like timestamps and "user".
- Ensuring a clear separation between data entry and table visibility.

Overall, implementation is technically straightforward and aligns well with Mathesar's architectural foundations.

## Use Cases

As a staff member managing a **library makerspace** with 3D printers, I want to:

- Allow patrons to log in at a self-service station using their library credentials and submit their own print jobs through a simple form, so staff don't need to manually input submissions.
- Restrict form access to authenticated library members only.
- Automatically associate each submission with the patron's identity and a timestamp, so we can track who submitted each job and when without asking for that information explicitly.
- Present only the relevant fields required for a submission (e.g., file upload, filament color, printer selection), and hide other sensitive data such as the full print queue or other patrons' submissions.
- Ensure that it's easy for patrons to access the forms after logging in, without navigating through many UI pages and the entire "Database => Schema => Table" stack to access their form.

## Success Criteria

How we'll know this feature is successful:

- We identify active users with new use cases that depend on this functionality.
- Feedback from early users (e.g., via GitHub issues, community channels) indicates ease of use and appropriateness of the functionality.

## Requirements

- Add default values that are dynamically set (e.g., current timestamp, current user) without being displayed to the form submitter.
- Ensure forms are easily-accessed within Mathesar. Examples:
  - There could be a "default view" for users of a certain role which displays a form.
  - Forms could be accessible from the Mathesar "home" page.
  - If a user _only_ has access to a form or forms but no or limited table permissions, we can present things in the UI differently.

## Ecosystem Analysis

**Airtable** and its open-source alternatives (e.g., Baserow, NocoDB) support form creation and submission but treat in-app forms largely as public interfaces or external collection tools. By contrast, enterprise systems such as **Salesforce**, **WordPress admin panels**, and **Django Admin** emphasize controlled, authenticated, structured input in operational workflows.

This proposal aligns more closely with these latter examples, enabling Mathesar to serve as a secure data-entry layer in structured environments without exposing the underlying data models to all users.

More research should be done on some of these platforms and how they use forms internally.
