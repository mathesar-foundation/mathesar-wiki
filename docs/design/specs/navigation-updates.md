# Navigation Updates

## Context

Mathesar users must be able to navigate between pages and know where they are at any point while using the system.

### Design Goals

- Users clearly understand which page they're on
- Users easily navigate to other pages
- Users may anticipate the result of navigation interactions

### Hierarchical Structure

The navigation design will be based on the following hierarchical structure:

- Database
  - Schema
    - Table
      - Record
    - Query

### Phasing Out Tab Navigation

Tabs will be phased out as part of the new navigation improvements.

## Navigational Elements

### URL

The URL should be used to display the navigation structure to users. It should be as simple as possible and built so that a user's path to the desired page may be easily determined.

### Top Navigation Bar

![image](/assets/design/specs/navigation-updates/180155893-8e997029-6397-4b56-b4d6-8515668b6f3e.png)

Every page has a top-level global navigation bar. Users may add new items or jump to existing ones from the top navigation bar.

#### Jump List and Search

<img width="600" alt="image" src="https://user-images.githubusercontent.com/845767/179805725-f1ff5ed4-155f-43d5-8874-9c988243e737.png">

<img width="300" alt="image" src="https://user-images.githubusercontent.com/845767/179806192-47b43b43-0ded-4053-a06a-7be49b805006.png">

1. Input Control

    When the input control (A) is activated, a list of recently used tables or queries is displayed. As soon as the user starts typing, the list narrows down to only include items whose names are similar to the search terms.

    Any of the results should be accessible using keyboard directional arrows, and pressing enter should take the user to the selected object's page.

1. Recent Items

    If we assume that users frequently access the same objects while doing their most routine tasks, then a list (B) of recently opened ones should help them work more quickly.

1. View All Link

    "View All" (C) is a link to the schema's homepage that allows users to access the full list of tables or queries.

1. Result Filters

    In some cases, the user just wants to look for a specific type object. When this is the case, users can use a filter to narrow down the results (D).

1. Matching Results

    Users will be presented with the results of their search and a highlighted section (E) of text that corresponds to their search term.

### Breadcrumb

The breadcrumbs are shown on all pages and indicate the current location in the context of the navigation path. For example, the user would see the current record, preceded by the table, schema, and database to which that record belongs while they're on a specific record page.

<img width="800" alt="image" src="https://user-images.githubusercontent.com/845767/179806555-51e89d56-e584-4632-b52a-28154fa5c242.png">

The breadcrumbs are shown on all pages and indicate the current location in the context of the navigation path. For example, the user would see the current record, preceded by the table, schema, and database to which that record belongs while they're on a specific record page.

### Table Row Links

![image](/assets/design/specs/navigation-updates/180157771-7e98353c-544d-4681-bb04-0f0a3efb10d3.png)

Users may use tables to go to a specific record page. Each row's primary key cell has a link to the record that the user may access by clicking on it.

### Record Page

1. Record Navigation

    ![image](/assets/design/specs/navigation-updates/180193437-ca7d0358-e3d9-4118-be8d-bbba95135b5c.png)

    When on a record page, you may use the record navigation controls to move between records. Included are options for going through the records sequentially or jumping to a specific record.

1. Linked Fields

    ![image](/assets/design/specs/navigation-updates/180197191-e7607eac-105b-4ee6-a0fe-68ee40bfff84.png)

    When fields with foreign keys are shown on the record page, the links to the tables they relate to be clickable by the user.

### Data Explorer

![image](/assets/design/specs/navigation-updates/180244256-3594fb03-21dd-4194-b812-e1f51975f796.png)

Users may access Data Explorer from various locations and as part of the following flows:

1. Creating a query from scratch

    From the schema homepage or top navigation, the user will have the option to create a new object. If they create a query, the system will open the 'Data Explorer.' Once the user is satisfied with the created query, they can choose to leave the 'Data Explorer' and should be redirected to the new query. They may then return to the 'Data Explorer' to edit the query, as described in more detail below.

1. Editing a query

    'Edit Mode' may be activated from any active query to inspect the settings that generate a query in the 'Data Explorer.'

1. Opening a table as a query

    'Data Explorer' can open any table in Mathesar. The 'Open in Data Explorer' menu option in the table settings will automatically build a query that contains all of the table columns.

    'Data Explorer' should treat any current filters or sorts in the table as steps.

1. Configuring an embedded query from the record page (Table Widget)

    'Data Explorer' will open if users customize an embedded query from the record page. The user can return to the record page after the query has been set up.
