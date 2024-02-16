# 2023-12-14 Product big-picture meeting

## Concept: Projects (Workspaces)

### Problem
* We are currently managing permissions within Mathesar instead of utilizing the robust Postgres permission system.
	* This was meant to be temporary and we had always planned to utilize the Postgres permission system.
	* Several users have expressed interest towards using Postgres roles, some even mentioned it as a blocker to using Mathesar.
	* _(There are several architectural and UX reasons to support moving to the Postgres permission system. I'm not mentioning them here, since I don't expect disagreement. We can discuss more on that during the meeting, if needed.)_
* Our current way of collaborative sharing of objects (DBs, schemas) is primitive and as we extend to sharing more objects, the UX and architecture would become increasingly complex.

### Considerations
* The access-control behaviour in Mathesar should closely tie to how access-control works in Postgres. If we deviate from it, it'll end up making our architecture complex.
	* _(We'll first take some time during the meeting to discuss how permissions work in Postgres)_
* *Bonus*: The concept we come up with should suit our self-hosted, managed-hosted, and in the future SaaS variants of our product with minimal architectural and UX changes.
* The concept should be feasible to implement for our 'beta' release.

### Proposal
* We introduce a single top-level concept called a 'Project'.
* A Project:
	* connects to a single database.
	* stores multiple postgres roles that can connect to the said database.
	* allows Mathesar users connect to the database by utilizing one of the stored postgres roles *(each Mathesar user associated with a DB role)*.
	* has access-control implemented in Mathesar to manage it.
* I've tried to explain this concept in form of questions and answers. Please read through the following list: 

1. **How would the user flow look like, after installing Mathesar?**
	* The first thing the user would be expected to do after installation is to create a Project.
	* They will enter the database host, port, and atleast one postgres role with username and password, inorder to create the Project.
	* The user can then access the Project, or create more Projects.
	* The user who created the Project will be it's 'Manager'.
	* Discussion:
		- Kriti commented: I would call this Owner, Manager is a confusing name for this and generally implies lower permissions.
		- I agree. I originally called it Owner. I decided to call it Manager in this document for reading comprehension, since I use the word 'Owner' to represent DB object level owners, in following questions. The terminology needs to be discussed after the concept is approved.

1. **How will a Project home page look like to it's Manager?**
	* A Project home page will show the linked database information, and could list recently accessed schemas, tables, explorations etc., The finer UX details are not dicussed here.
	* Managers have access to add PG roles, invite users to the Project, modify Project settings, and delete the Project.
	* It will show the Database name, host, and port. The Manager can modify this.
	* It will contain a list of Postgres roles, that the Manager can add to, modify, or remove.
		* When adding Postgres roles, the Manager will have to type in the username and the password.
	* It will show all the Postgres roles, and the Mathesar users associated with each of them.

1. **How would the Manager share a Project with other users?**
	* The Manager can invite and add existing Mathesar users to a Project. _(Think of Basecamp)_.
	* When the Manager adds a Mathesar user to the Project, they will choose which Postgres role the user should be associated with.
	* The Manager can modify this at a later date.
	* Multiple Mathesar users can be configured to use a single Postgres role.
	* Think of Postgres roles as a 'group' of Mathesar users. To start with, a Mathesar user can belong to only one group, and not multiple groups.

1. **Do all users who are added to a Project have access to all objects in the database?**
	* The access-level (privileges) to underlying DB objects will depend on the role of the Mathesar user.
	* If the Postgres role associated with the user has access to a particular object, then the user will have access to it.
	* By default, all users will be able to view the names of all database objects and Mathesar-specific objects like Explorations. We will however differentiate the objects that they do not have access to.
		* Architecturally, we use pg_catalog which will list everything.

1. **Can multiple Mathesar users be Managers of a Project?**
	* No. There will be only one Manager per Project.
	* The Manager can shift their responsibility to another user by making them the Manager.
	* Hierarchially, a Project belongs to the Manager.

1. **How would individual object permissions work?**
	* In Postgres, if a 'PG user' creates a table, they are considered the owner of the table and only they have access to it. They can then grant priviliges to other 'PG users' (We refer to PG users as roles in this document for reading comprehension).
	* This affects permissions in Mathesar. Just because a user has access to a Project using a particular role does not guarantee that they will have access to other objects created with a different role.
		* This applies to the Manager as well.
		* The Manager however can bypass this by updating their own role.
	* Each object shown in Mathesar, will display its owner (The Postgres role and all Mathesar users associated with it).
	* Lets say, a Mathesar user named 'Laliari' creates a table 'Books'.
	* 'Laliari' is associated with the role 'DB_role_1'.
	* The table 'Books' will have the owner 'DB_role_1'.
	* All Mathesar users who use the role 'DB_role_1' will be owners of the table 'Books'.
	* All Mathesar users who use a different role will not be able to view the table.
	* Any of the Mathesar users who are owners can grant permission to any other role, via the Mathesar UI.
	* By default, **we will have a Project wide setting that will automatically grant privileges to all PG roles mentioned in the Project for all DB objects created from within Mathesar**.
		* This setting will be present in the Project page, and is customizable per Project.
	* Discussion:
		* Kriti: We also need to figure out how Postgres RLS would work, permissions can be at a row-level rather than at an object level. Even if we don't support RLS at first, we probably want to support it eventually.
	 	* Pavish: RLS that's already configured in the DB would work without additional configuration. I agree that it would help to figure out how to provide RLS controls and grant access to specific rows from within Mathesar, eventually.
	 	* Pavish: Similarly, we're currently not going to be focusing on granting column level privileges in Mathesar. Eventually, it'd be good to do this as well.

1. **How would users request access to individual objects in a Project?**
	* If a Mathesar user's Postgres role does not have access to a DB object within a Project, they can request any of the owners for access.
	* This would happen incase the above 'automatic grant setting' is set to false, or if the object is created outside Mathesar.
	* In the above example, say, I want to access the table 'Books'.
	* Mathesar will display all Mathesar users who have access to the table 'Books', and it displays 'Laliari'.
	* To start with, I will not be requesting access from within Mathesar. I would contact 'Laliari' via email or a different chat app asking for access.
	* Mathesar will contain an option to 'grant' access to other PG roles.
	* 'Laliari' will use the 'grant' option to provide me access to 'Books'.

1. **How would access-control for Mathesar-specific objects like Explorations work?**
	* Mathesar-specific objects like Explorations are often tied to underlying DB objects.
	* We will not be access-controlling these objects individually.
	* If the user has access to the underlying table(s), then they will have access to the explorations that makes use of those tables.
	* This will apply for table settings, and in the future, charts and forms.
	* Discussion:
		* Kriti: I'm not sure this is viable. I can imagine many scenarios where I'd want to give people access to a chart or a form, but not the underlying data.
		* Pavish: I agree. However, doesn't providing access to a chart or a form implicitly provide access to the underlying data?
			* The tricky part is deciding which role to use to provide access to the charts & forms. All users added to a Project must have a role and they will get access to all objects that the role has access to.
			* We can share objects for external access for other users & public access using the `public_share` role. This will allow sharing charts and forms individually, without them being able to access the Project.
			* If we want signed in users to be added to the Project and access only specific charts and forms without the tables/views, we may have to rethink the entire concept. I do not think we need this.
			* I also do not think we should try to do this for the beta.

1. **Would there be a Mathesar superuser? If so, can they access all Projects?**
	* There will be a Mathesar superuser.
	* The superuser can utilize Mathesar just like any other user.
	* They have an additional option to create and manage Mathesar users.
	* They can view the list of all Projects in the app.
	* By default, they **cannot** access a Project they are not added in.
	* They can request access to the Project's Manager.
	* They can 'hostile takeover' a Project, thereby becoming its Manager.

1. **Why only one Database per Project?**
	* DB roles, and Mathesar user association with each role, are both configured per Project.
	* If we allow multiple databases, it will require us to add another level of hierarchy inorder to configure the DB roles and add Mathesar users per role.
	* Keeping one Database per Project would keep the UX flat and simple for the user.

1. **How would public sharing work?**
	* Each Project will contain an option to set a role as the 'Public share' role.
	* When a user creates a Project, we will automatically create a new role in the databse called `public_share` or similar. _(The user must be utilizing a role with CREATE_ROLE attribute)_.
	* The user can alternatively choose a different existing role to use in it's place, say 'DB_role_1'.
	* Whenever a user shares a DB object, the shared link will utilize this role.
	* Each 'share' can override this, by specifying a different role.

1. **Can users create new databases when creating a Project?**
	* Yes. The users can create a new database when creating a Project.
	* The new DB can only be created within the internal DB server (i.e. the Django DB server).

1. **Can we provide out-of-the-box Postgres roles when creating a Project?**
	* Yes. When a Manager creates a Project and configures the DB, we can provide an option to automatically create some basic roles on the DB. Eg., (editor, viewer etc.,)
	* The Manager must use a role that has `CREATE_ROLE` attribute to enable this feature.
	* For Projects that create new DBs in the internal DB server, we will automatically create these roles without prompting the user.

1. **Can any user create a Project?**
	* Yes. All users can create Projects.
	* A user will be listed with the set of Projects they have access to when they login.

1. **Can a super-user take over a Project?**
	* A super-user can perform a hostile take over of a project, if needed.
	* When they take over a Project, they become the Manager of the project.

1. **Can users remove themselves from a Project?**
	* A Manager cannot remove themselves from their Project. They can reassign the Manager access to someone else and them remove themselves. They can choose to delete the Project as well.
	* Other users can remove themselves from a Project.

1. **What happens when a Project is deleted?**
	* If the underlying database was created in the internal database when the Project was created, the underlying DB will be deleted. If not, the DB will not be affected.
	* Every setting associated with the Project will be deleted.

1. **Can multiple Projects link to the same database?**
	* Yes, but each project will contain its own settings, PG roles, and Mathesar users.
	* Each project will contain its own Explorations and other Mathesar-specific objects.
	* Ideally, we'd not expect users to do this. However, if they wanted to, we shouldn't prevent them from doing it.

1. **Can Projects have any kind of relationships/shared-settings between them?**
	* No. Projects will not share any properties, relationships, or settings between them.
	* Each Project is isolated from others.

1. **Can Mathesar users modify their own Postgres roles within a Project?**
	* To start with, no. Only the Manager can choose the roles for a user.
	* In the future, we can consider users being able to enter the username and password and specify their own roles _(Only if they are already added in the Project by the Manager)_.

1. **How would this concept suit a SaaS variant setup?**
	* In a Mathesar SaaS variant, the superuser would be us (the people hosting Mathesar).
	* Normal users are those logging into the Mathesar site.
	* Each of those users can create their own Projects and share the Projects with other users who've signed up to the Mathesar site.
	* We will not allow connecting to external DBs for the SaaS variant (We could allow this based on user requests). To being with, users can only create new DBs with each new Project.
	* The UX would appear and work mostly similar to self-hosted variants.

1. **How will this simplify our architecture?**
	* We leave all permissions associated with DB objects to the DB. This will take a load off our shoulders.
	* All permissions for Mathesar specific objects related to DB objects will depend on the role having privileges over the DB object. We do not have to manage access control additionally.
	* The only access control we'd have to implement in Mathesar is to manage Projects.
	* We'd be closely tied to how privileges work in Postgres, so we'll have less friction moving foward.

## Outcome

We decided that it's essential to have more granular permissions handled by Mathesar for explorations and other Mathesar specifc objects. Pavish will take more time to think on it and come up with an updated concept.
