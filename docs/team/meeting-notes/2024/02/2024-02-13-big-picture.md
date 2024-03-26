# 2024-02-13 Product big-picture meeting

## External anonymous sharing

* When sharing a table externally to anonymous users, should I be able to choose a DB role for the share?
	* Scenario:
		* **Tech company 'Stack Underflow'** has a table with the results of their survey of popular programming languages, called **Survey results**.
		* Employees of the tech company should be able to perform DDL and DML operations on the Survey results table.
		* They want to share this Survey results table to the public. The share should be restricted to only allow "read-only" view of the table.
		* For safety reasons, they create a new role on the DB called 'readonly_role' and grant it access to only view the table.
		* They generate a URL to share the table.**They choose the 'readonly_role' and associate it with the share.**
		* Anonymous users viewing the URL should be presented with a read-only view of the Survey results table. The underlying DB request should utilize the 'readonly_role'.
		* Tech company employees should also be able to view the url to get a sense of how it will look before sending the url to others. They should be able to do this *while they're still logged into Mathesar*.
	* Are we all agreed that we need to support this?
	* How would this work on the backend?
	* Similar scearnio applies for Mathesar objects like explorations. How would the solution work for them?

* Can the same table be publicly shared multiple times by multiple users, generating multiple urls? If so, who all should be able to view the shared url list?
	* Scenario:
		* **Event management company** has multiple clients. They get orders for conference management and manage events on behalf of their clients.
		* They have DB roles for each of their clients. Let's say they have two clients and associated roles, for 'RSA Conference team - USA', and 'Presidential debate team'.
		* They manage their conference attendees contact information list in a single table, with an RLS policy.
		* The 'RSA Conference team - USA' role would only be able to view the list of attendees for their conference and not any other conferences, when they query the table.
		* Event management company connects their DB to Mathesar, gives access to 'RSA Conference team - USA' and 'Presidential debate team' with their respective roles.
		* 'RSA Conference team' shares the attendees table with a public URL link. The 'Presendital debate team' should not be able to see the link *listed* in the Mathesar UI.
	* Are we all agreed that we need to support this?
	* How would this work on the backend?
	* How would the follow-up scenario work?
		* Now, there's a 'RSA Conference global team' that wants to conduct conferences across different countries. The Event Management company creates a DB role for them. They should be able to view the attendees of all the RSA conference sub-teams that manage single countries.
		* They should be able to view the list of links shared by the RSA sub teams for the attendees table.
	* Similar scenarnio applies for Mathesar objects like explorations. How would the solution work for them?

## External sharing to Mathesar users
* Should we allow sharing a table/exploration with the restriction that the human should be logged into a Mathesar account, but they don't necessarily need to have a DB role explicitly configured and shouldn't be able to view anything else in Mathesar?
	* Scenario:
		* Person conducts an internal survey within their company. They create and share a public URL.
		* They want whomever editing the table (or in the future, forms) to be a valid Mathesar user to prevent people from outside the organization to edit the data.
		* They don't want these users to browse the database via Mathesar. They simply want them to access one single table (or form) and only via the URL.
	* Are we all agreed that we need to support this?
		* **We're not going to support this**
	* How would this work on the backend?

## Implicit sharing between Mathesar users for co-ordination
* When a database is connected to Mathesar how should access control work for Mathesar users to access it?
* Do we need to move away from our existing setup where each connection is a single DB user? Why?
  - The main reason is for sharing Mathesar objects. Can we do this another way?
* Should an exploration/Mathesasr object ownership be tied to a human or the DB role?
* Should we provide access control options for structural level changes to explorations/Mathesar objects? Can we restrict this to owner-only?
* Do we need private explorations that only one Mathesar user owns?
* Do we need a team space where everyone co-owns items in the team space?
	* Do we need further access-control within a team space?
* Should we allow multiple projects/wrappers for the same DB?
	* Scenario: Multi-tenant setups.
