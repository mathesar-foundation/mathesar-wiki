# 2024-02-08 Product big-picture meeting

## Permissions

* How would a Mathesar user share a DB object via Mathesar?
	* To another Mathesar user
		* Is this required?
		* User flow for sharing
		* How would the DB object appear to the user to whom it was shared?
		* Underlying DB credential used by the user viewing the DB object
	* Publicly
		* Is this required?
		* User flow for sharing
		* How would the DB object appear to public users?
		* Underlying DB credential used by public users
* How would a Mathesar user share a Mathesar object?
	* To another Mathesar user
		* User flow for sharing
		* How would the object appear to the user to whom it was shared?
		* Underlying DB credential used by the user viewing the object
	* Publicly
		* User flow for sharing
		* How would the object appear to public users?
		* Underlying DB credential used by public users
* What degree of configurable access control do we want for Mathesar specific objects?

## User stories

### Database objects: Co-ordinating between Mathesar users

#### Library intern

**Library owner** has an **intern** working to update inventory. Intern should be able to insert/update/delete/select within `books` and `items`. Intern should be able to select within `checkouts` to see when certain items where checked out. Because owner cares about privacy of patrons, intern should _not_ be able to view `patrons`. When viewing `checkouts` table, intern should only be able to see the id of the patron associated with each checkout (no record summary).

### Notes

* We're all agreed that eventually we want to manage & grant permissions for db users to db objects via Mathesar UI
* For beta, we want feature parity with what we already have.

### Database objects: External anonymous sharing

#### Public books list

**Library owner** wants to publish the list of books available at their branch, as well as the number of copies currently available. **Anonymous user** should be able to view the data but not modify anything.

#### Potluck signup

**Potluck planner** invites **friends** to come over for dinner. Planner sends friends a URL to a publicly-shared table in Mathesar. Each friend is able to add a row to sign up for the potluck, indicating what food they will bring. Because this is a high-trust, low-stakes environment, friends are also permitted to update any cell value within the sheet. However the friends are not able able to manipulate the structure of the sheet (add/remove columns, or change column types).
