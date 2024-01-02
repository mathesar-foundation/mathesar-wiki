# Navigation Consistency Updates

## Overview

[GitHub Issue](https://github.com/mathesar-foundation/mathesar/issues/3287)

## User Experience

### Default State Logged In User

- **Mathesar Logo**: Always visible; acts as home button.

#### User has multiple databases (database connections list page)

![image](https://github.com/mathesar-foundation/mathesar-wiki/assets/845767/dd5dfe79-9fa4-4d62-9f66-7dfd53f78373)

- **Database Connections Breadcrumb Button**:
  - On click, dropdown lists all databases.

#### User has one database (database connection page)

![image](https://github.com/mathesar-foundation/mathesar-wiki/assets/845767/6f640137-2096-46e8-a7d3-32f43eb907fa)

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
- Records List Button should be disabled if the table is empty or in a non-readable state.

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

**For saved explorations in edit mode with unsaved changes:**

![image](https://github.com/mathesar-foundation/mathesar-wiki/assets/845767/ae2d04f7-52f4-468d-b287-f923ae4d74e2)

- The label should be **Exploration Name** with the edit icon and an asterisk.

### From the Import Page

![image](https://github.com/mathesar-foundation/mathesar-wiki/assets/845767/52bfe6a9-16a7-451c-9797-a011957f33ea)

- Display **Import Name and Icon** after the schema breadcrumb button.

## State Representation

### Active Page

- The active page in some cases is not the last element in the breadcrumb trail. It needs to be highlighted to indicate that it is the current page. The text will be bolder and the in white color.

### Inactive Pages

- Inactive pages will be in a lighter color and will not be bold.
- Inactive pages will be clickable and will direct the user to the page. For example, clicking on the database name will take the user to the database connection page.
