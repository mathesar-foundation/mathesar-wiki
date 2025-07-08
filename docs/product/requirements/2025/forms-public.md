# Forms (Public)

!!! danger "Old version"
	These requirements will be updated soon.

## Problem we're solving

Users need a way to collect structured data from people outside their organization, such as volunteers, customers, or survey respondents, without requiring those users to log in or provide any information beyond that needed by the form. 

Today, Mathesar only allows data entry through the logged-in spreadsheet interface, which:

* Limits collaboration to internal users  
* Makes it impossible to collect one-off or community-sourced submissions  
* Adds unnecessary friction for low-risk, high-volume data collection scenarios

Users have [explicitly requested](https://github.com/mathesar-foundation/mathesar/discussions/2264) this feature:

* *“If Mathesar had this, we would have selected it over NocoDB. We have a lot of plans for this, such as a contact us form on our website, customer satisfaction surveys, and data entry for our production systems.”*  
* *“If we could create and use different forms to fill the database that would be very interesting because it would avoid having to develop an entire database management interface.”*  
* *“This feature would enable diagnostics EUA submissions to the FDA where the FDA could spin up a table with an associated form for diagnostic manufacturers to populate.”*

## Features

* Allow data to be entered via public, sharable forms  
* Allow Mathesar users to create, configure, and publish forms

## Feasibility

This feature is a common one with lots of prior implementations to take inspiration from, and forms are a foundational part of frontend software engineering, so it’s unlikely our team would be unable to work on this. 

## User Stories

As the admin of a community movie database, I want to:

* Build a single form that allows community members to add new movies, generes, and the related crew in one place for ease and convenience.  
* Avoid users submitting invalid data so that our small team doesn't have to manage spam or invalid submissions.  
* Preview the form and test it before making it public, so that we don't provide a bad experience or collect data incorrectly in a way that messes up our dataset.  
* Make sure users know their submission was received correctly after they fill out the form, so that they aren't confused and don't contact us to verify.

## Ecosystem

Tools like Airtable and Google Forms support anonymous, public form submissions. Open-source alternatives like Baserow and NocoDB also support public forms with field-level validation. In fact, most products in Mathesar's ecosystem contain a “forms” feature, including but not limited to Airtable, Baserow, NocoDB, Teable, Grist, SeaTable, Tadabase, and Quickbase.

It’s arguable that this functionality is “industry standard” and is commonly-accepted as a key feature for any offering in this space.