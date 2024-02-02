# Navigation Consistency Updates

## Overview

The proposed Navigation Consistency Updates aim to enhance the user experience by providing a coherent navigation system within the Mathesar application.

[GitHub Issue](https://github.com/mathesar-foundation/mathesar/issues/3287)

## User Experience

### Default State Logged In User

- **Mathesar Logo**: Always visible; acts as home button.

#### User has multiple databases (database connections list page)

![image](https://github.com/mathesar-foundation/mathesar-wiki/assets/845767/06c63089-57d3-4a61-a25b-ec4a3983e41c)

- **Database Connections Breadcrumb Button**:
  - On click, dropdown lists all database connections.
  - An option to "Manage Connections" is also available.

#### User has one database (database connection page)

![image](https://github.com/mathesar-foundation/mathesar-wiki/assets/845767/62a92b4c-510e-4c95-a6e0-e1914adc44eb)

- **Database Name with Icon**: Directs to database connection page.
- **Schemas Breadcrumb Button**: Opens a list of schemas in the database.

### From the Schema Page

![image](https://github.com/mathesar-foundation/mathesar-wiki/assets/845767/dc0cbde4-e3bc-4fb2-b1b5-7720a18d4aae)

- Retain elements from the database connection page.
- Add **Schema Name and Icon**.
- Introduce **Tables Breadcrumb Button**:
  - Lists tables and explorations in the schema when clicked.
  - Add Links to Import Table and Data Explorer pages.

### From the Table Page

![image](https://github.com/mathesar-foundation/mathesar-wiki/assets/845767/70bce2f9-172e-4111-81db-13aa02716829)

- Include **Table Name and Icon**.
- Add **Records List Button**: Opens a dropdown of table records.

### From the Record Page

![image](https://github.com/mathesar-foundation/mathesar-wiki/assets/845767/035b3ebe-7607-409d-9a13-457dc27fc94b)

- Append **Record Name and Icon** for context after the 'record list' button.

### From the Exploration Page

- Add **Exploration Name and Icon**.
- Exclude records list button since it is not relevant to exploration.

**For unsaved explorations:**

![image](https://github.com/mathesar-foundation/mathesar-wiki/assets/845767/274b1a54-0bfa-4be3-8fa7-9046b2c36634)

- The label should be **Data Explorer** with the exploration icon.

**For saved explorations:**

![image](https://github.com/mathesar-foundation/mathesar-wiki/assets/845767/68b58331-e529-4252-ab9e-cac905957404)

- The label should be **Exploration Name** with the exploration icon.

**For saved explorations in edit mode:**

![image](https://github.com/mathesar-foundation/mathesar-wiki/assets/845767/e41358ef-7d78-4d6a-83c4-36f7ad5838b6)

- The label should be **Exploration Name** with the edit icon.

### From the Import Page

![image](https://github.com/mathesar-foundation/mathesar-wiki/assets/845767/52bfe6a9-16a7-451c-9797-a011957f33ea)

- Display **Import Name and Icon** after the schema breadcrumb button.

### From the Administration Pages

![image](https://github.com/mathesar-foundation/mathesar-wiki/assets/845767/14d1c7c1-29c5-4c37-b470-f3cac989022f)

- No dropdown menus will be on the admin pages because they're at a higher level and don't need to help with data navigation. This keeps the menu behavior the same everywhere, which is less confusing for users.
- Icons in this section will adopt the primary color to distinguish it as a separate area.

## Additional UI Details

### Navigation Bar with Scrollable Lists

![image](https://github.com/mathesar-foundation/mathesar-wiki/assets/845767/02f5a05e-1bbb-45a3-a41d-0369629a91da)

The menu needs to be divided into sections:
- Main navigation links (Import and Data Explorer) that remain constant. This area will be fixed.
- Lists (Tables and Explorations) which can expand with numerous items. This part will have independent scrolling from the fixed area, ensuring that users don't lose sight of the main navigation links while scrolling through a long list.

## State Representation

### Active Breadcrumb Step

- The active breadcrumb step needs to be highlighted to indicate that it is the current page. The text will be bolder and the in white color.
