# User Invite Flow

## The Problem

Adding new users to Mathesar is currently a cumbersome process.

Administrators have to: 
- set up the user account
- find a secure way to send credentials to the user through an external channel

The user then has to:
- have the temporary password handy
- change the password upon first login
- then store that new password

### Is it feasible to solve?

Yes, there is a clear best practice here. Most applications send an email to the user when the user is added to the system, which eliminates most of the steps above.

Django supports a lot of this out of the box, so actual code needed should be minimal. We will need to add the ability for admins to configure sending out email.

## Use Cases

!!! example "Write use cases."
	Use cases and/or user stories.
	User persona-related synthesis (if any).

## Success Criteria

!!! example "Create success criteria."
	What are our externally measurable success criteria?
	How much time is it worth spending on solving this problem (T-shirt size)?

## Requirements

!!! example "Write requirements."
	A classic list of requirements, without delving too deep into implementation specifics.
