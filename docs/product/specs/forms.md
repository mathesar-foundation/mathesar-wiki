# Forms

This spec describes the “Forms” feature. The following content is dated 2025-04-29, and describes the first iteration of the feature.

"Forms" lets non-technical users visually design and share data-entry forms publicly. Users select a base table, pick columns (including foreign-key, and reverse-foreign-key links), arrange and configure fields, and publish a public link. End users can then submit the form which store records in the database, with nested creation of related records.

## Terminology
- Reverse foreign key: Denotes foreign key columns in other tables that link to base table records.
- Mathesar user: Refers to users using Mathesar to create a form.
- End user: Refers to people filling the form.

## Requirements

### User stories

- **Form Builder (Mathesar admin)**
	- I want to share a form to end users via a public link to collect data required for my business needs.
	- I want to select a base table & related tables, and choose which columns appear on my form so I can tailor data-entry to business needs.
	- I want to ensure that all fields related to my business needs are part of the same form. This may involve multiple different tables related via FKs and reverse-FKs.
	- I want end users to be able to search through existing records with summaries, when they're filling in a foriegn key field.
	- I want to allow end users to be able to create new related records inline, if needed.
	- I want to configure labels, descriptions, placeholders, and validation rules for each field to guide end users.
	- I want to reorder fields via drag-and-drop and insert dividers or instructional text to structure my form visually.
	- I want the main record and any related/nested records to all be created in one shot, when the end user submits the form.

- **Form Submitter (End User)**  
	- I want a clear, labelled form that only shows fields relevant to my task.
	- I want descriptive messages to guide me fill the form.
	- I want clear indications when the form is successfully submitted.
	- I want useful help messages when form submission fails due to an error.
	- I want to know when I'm filling the form incorrectly while I'm filling it, not only while submitting.

### A simplified scenario
- Mathesar admin wants to create a form for end-users to fill in their favourite movies, including the director, producer, casting information, and genres.
- Mathesar admin has the following schema:
	![user-scenario-db-schema.png](/assets/product/specs/forms/user-scenario-db-schema.png)
- **Things to note**:
	- This is not a real-life example and is used only for representing the following cases:
		- Normal fields (Scalar columns in the `Movies` table).
		- Foriegn key fields referencing a table with multiple columns (`producer_id` -> `Producers`).
		- Foriegn key fields referencing a table with a single column (`director_id` -> `Directors`).
		- Reverse-foreign-key fields referencing a table with multiple columns (`Movie_Actor_mapping`).
		- Reverse-foreign-key fields referencing a table with a single column (excluding the fk to the base table) (`Movie_Genre_mapping`), i.e. a mapping table.
	- The wireframes below are representational, taking into consideration the implementation feasibility. They are not final.
- **Form displayed to the end user:**
	- ![new-form.png](/assets/product/specs/forms/new-form.png)
	- The `id` columns are not displayed i.e. any column that has a dynamic default is hidden.
		- The admin can still choose to display these columns in the form as readonly fields.
	- The foreign key field `movie.director_id` is displayed as a dropdown which selects records from `Directors`.
	- The foreign key field `movie.producer_id` is displayed as a dropdown which selects records from `Producers`.
	- End users can add entries in `Movie_Actor_mapping`, which is labelled as "Cast Members" in the form.
		- The admin can modify any label & add descriptions.
	- The "Genres" label has an input that adds entries to `Movie_Genre_mapping`.
		- Since that table is a mapping table with a single column, only the field for fk `Movie_Genre_mapping` -> `genre_id` is shown.
		- It opens a dropdown showing entries from `Genres`.
- **Filling in a foriegn key field:**
	- ![select-producer.png](/assets/product/specs/forms/select-producer.png)
	- ![select-director.png](/assets/product/specs/forms/select-director.png)
	- ![select-genre.png](/assets/product/specs/forms/select-genre.png)
	- Admin can configure whether or not they want to allow end users to add new records.
		- If they allow the '+ Add New' option is shown in the dropdowns.
		- Admins can configure the text shown.
	- This is a record selector shown in a dropdown. Only the summaries are shown in the list.
	- There will be a small Pagination section when the entires are more than 20.
	- The search area contains the columns that are part of the record summary.
	- These columns could be from any related joinable table, as configured by the record summary.
	- The admin cannot choose searchable columns if they are not part of the record summary configuration. The Record summary configuration is the only source here.
	- The admin can customize the labels for these columns.
- **Adding new records in related tables via fk fields:**
	- ![form-new-entry-fk-field.png](/assets/product/specs/forms/form-new-entry-fk-field.png)
	- End users can choose to add new records for Producers, Directors, and Genres.
	- Notice that the "Director" field shows the field "Person" for the column `person_id` which is an a FK for `People`.
	- The user could still add a nested entry for the `People` table using the "Person" dropdown.
		- ![form-new-nested-fk-entry.png](/assets/product/specs/forms/form-new-nested-fk-entry.png)
	- "Genres", however shows fields from the `Genre` table directly, since `Movie_Genre_mapping` is a mapping table with just a reverse-fk.
		- It adds entries to both `Genre` and `Movie_Genre_mapping`.

## Scope

### Initial release of "Forms":
1. Select form fields from base table.
1. Select form fields from related tables - both fk links and reverse-fk-links.
1. Publicly sharing a form for end-users to fill.
1. Customizable styling and success/failure messages.
1. Preview forms while creating/editing.
1. Basic Permissions.
	- Each form is owned by a role.
1. Redirection after submission.
	- Allow redirection to a custom endpoint after successful form submission. This would happen after showing the success message, with a timer.
1. Basic form-level validations.
	- Marking fields as "required" on the form to disallow empty fields, while the underlying columns allow NULL & empty strings.

### To consider in future releases:
1. Granular permissions management for forms.
1. Restrictions on filling forms.
	- Login required,
	- Password,
	- Captchas, etc.,
1. Email notifications after a form is submitted.
1. Creating an 'exploration' from a 'form' to view de-normalized data filled via forms.
1. Perform DDL operations while building form.
	- Being able to create a new table directly in the form view.
	- Being able to create new columns directly in the form view.
1. Advanced form-level validations.
1. Multi-language support for end-users filling the form.
1. Customizable Logos.

## Implementation notes

### Form structure
#### Type definitions:
```typescript
interface Form {
  id: number;
  base_table_oid: number;
	schema_oid: number; // Readonly - based on base_table_oid
  name: string;
  description: string;
  slug: string;
  published: boolean;
  owning_role_oid: number; // The owner of the form
  // owning_role_oid should be a member of submission_role_oid.
  // Default value of submission_role_oid is the same as owning_role_oid.
  submission_role_oid: number;
  submission_ui: {
    label: string;
    message: string;
    on_submit: SubmissionAction;
  };
  elements: FormElement[];
  created_at: string; // timestamp
  updated_at: string; // timestamp
}

// Discriminated union of form elements
type FormElement =
  | TextElement
  | DividerElement
  | ScalarColumnElement
  | ForeignKeyElementWithCreate
  | ForeignKeyElementWithoutCreate
  | ReverseForeignKeyElement;

interface BaseElement {
  id: string; // An uuid
  kind: string;
  styling?: { // Representational, will change during implementation
    size?: "header" | "subheader" | "normal" | string;
  }
}

interface TextElement extends BaseElement {
  kind: "text";
  text: string;
}

interface DividerElement extends BaseElement {
  kind: "divider";
}

interface ColumnElement extends BaseElement {
  label: string;
  description: string;
  placeholder: string;
  validation: ValidationRules;
  readonly: boolean;
}

interface ScalarColumnElement extends ColumnElement {
  kind: "scalar_column";
  column_oid: number;
}

interface ForeignKeyElement extends ColumnElement {
  kind: "foreign_key";
  column_oid: number;
  target_table_oid: number;
  record_summary_template: RecordSummaryTemplate;
}

// When allow_create === true, nested_elements is required
interface ForeignKeyElementWithCreate extends ForeignKeyElement {
  allow_create: true;
  nested_elements: FormElement[];
}

// When allow_create === false, nested_elements is not allowed
interface ForeignKeyElementWithoutCreate extends ForeignKeyElement {
  allow_create: false;
}

interface ReverseForeignKeyElement extends ColumnElement {
  kind: "reverse_foreign_key";
  linked_table_oid: number;
  nested_elements: FormElement[]; // Always required
}

interface ValidationRules {
  required: boolean;
}
```

#### Sample:
```json
{
  "id": 1, // Form id
  "base_table_oid": 42,
	"schema_oid": 1,
  "name": "Movie addition form", // Unique per schema
  "description": "string",
  "slug": "custom-link", // Used to compose /public/<slug>, unique, default: random uuid
  "published": true, // Toggles public link
  "owning_role_oid": 11020,
  "submission_role_oid": 11023,
  "submission_ui": {
    "label": "Send",
    "message": "thank you!", // Message to show after submission
    "on_submit": {
      "redirect": 'http://some-random-url',
      //... set of actions to do
    }
  },
  "elements": [
    {
      "id": "text_01",
      "kind": "text",
      "text": "Add a New Movie",
      "styling": { // Custom stlying options - used only by the frontend
        "size": "header"
      },
    },
    {
      "id": "div_01",
      "kind": "divider"
    },
    {
      "id": "fld_01",
      "kind": "scalar_column",
      "column_oid": 7,
      "label": "Name",
      "description": "",
      "placeholder": "some movie name", // Placeholder for input
      "validation": { // Additional validation on the form apart from DB validation
        "required": true
      },
      "readonly": false, // Can only be true for columns that have default values
      "styling": {},
    },
    {
      "id": "fld_02",
      "kind": "foreign_key",
      "column_oid": 9,
      "target_table_oid": 57,
      "record_summary_template": [], // User can configure custom record summary for each form
      // For foreign key rows
      "allow_create": true, // “+ Add new” button
      // Only one row can be created newly for foreign_key field kind
      "nested_elements": [ // Present if allow_create is true
        // ...
      ],
      "label": "Director",
      "description": "",
      "placeholder": "",
      "validation": { "required": true },
      "readonly": false,
      "styling": {},
    },
    {
      "id": "fld_03",
      "kind": "reverse_foreign_key",
      "linked_table_oid": 58,
      // Always allow creating records for reverse_foreign_key field types
      // Multiple rows can be created newly for reverse_foreign_key field
      "nested_elements": [
        {
          "id": "fld_03_01",
          "kind": "scalar_column",
          "column_oid": 3,
          "label": "Character"
        },
        // ...
      ],
      "label": "Cast Members",
      "description": "",
      "validation": {
        "required": false, // Form can be submitted with `0` rows.
      },
      "styling": {},
    }
  ],
  "created_at": "2015-10-03T00:00:00.0 AD",
  "updated_at": "2015-10-03T00:00:00.0 AD",
}
```

#### JSON while submitting the form:
```json
{
  "fld_01": "value_01",
  "fld_02": "value_02",
  "fld_03": "value_03",
  "fld_03_01": "value_03_01",
  //...
}
```

### Django DB schema
- A single table named: `Forms`.
	```
	id integer [primary key]
	base_table_oid oid
	name varchar
	description text
	owning_role_oid oid
	submission_role_oid oid
	elements jsonb
	published true
	slug string
	submission_ui jsonb
	created_at timestamp
	updated_at timestamp
	```
- `elements` are stored as a jsonb array.
	- Open to consideration: Using tables for `elements` instead of jsonb.
- `slug` is unique.
- `name` is unique per schema.
	- It is debatable whether we want schema_oid to be part of the table or validation to be at service layer.

### DB Permissions
- A form is associated with the role of the Mathesar user that created the form i.e. `owning_role_oid` is set to the oid of the role used by the user that creates the form.
- The user can change the role used when the form is submitted by setting the `submission_role_oid`.
- By default `submission_role_oid` is the same as `owning_role_oid`.
- The `owning_role_oid` SHOULD BE A MEMBER OF `submission_role_oid`. Other roles cannot be set as submission roles.
	- This restriction is consitent with how PostgreSQL functions.
- If `owning_role_oid` is a superuser, any role can be set for `submission_role_oid`.
- A owning role can change the ownership of the form to another role.
- **Important security consideration:**
	- We do not want users creating a form on tables they don't have INSERT privileges on, then sharing it publicly with an evelated role they don't have access to, inorder to fill the tables.
- Only the user with a role owning a form should be able to edit the form.
- All other users can view the form and use the public links.

### Public urls & RPC methods
- An unauthenticated route at `<mathesar_url>/forms/<form_slug>`.
- `forms.get`:
	- Required: `form_slug` or `form_id`.
	- Returns the form structure object associated with the slug.
	- Returns the table structure, column definitions, constraint defintions of all the tables mentioned in the form & it's elements (recursively):
		- `base_table_oid`.
		- `elements[].target_table_oid`.
		- `elements[].linked_table_oid`.
	- Returns the column definitions of columns part of the record_summary_template within form elements (recursively).
- `forms.submit`.
	- Required: `form_id`.
	- Required: values for the form as a json.
- `forms.list_record_summaries`:
	- Required: `form_id`.
	- Required: `element_id`.
		- `target_table_oid oid` is identified based on the element id.
	- Accepts filter defintion.
		- The filter columns should be a part of `record_summary_template` associated with `element_id`.
	- Returns list of record summaries of fk tables.
	- (This might change significantly based on the final UX)

### Searching through record summaries
- A record summary template looks like this: `[[4, 2], "-", [1]]`.
- Each array represents a path to a column, and this definition is used to make joins for the record summary. The text elements are static.
- Each path in a record summary would now have a new field 'alias', which is then used as both the label to display to the user and the key in filtering a list of summaries in the record summary dropdown. (Refer the sample ux above).
- Eg., `[{ path:[4, 2], alias: 'Name' }, "-", { path: [1], alias: 'Id' }]`.
- (This might change significantly based on the final UX).
- (Open to consideration: Use a table view with lookup column as we do right now in the table page).

### Creating the records
- When the form is submitted, all related records should be created in a single transaction.
- Order of precedence:
	- Insert records in tables referenced via foreign keys.
		- If nested elements are present, treat the related table as the base_table & insert records recursively.
	- Insert records in base table.
	- Insert records in tables with link to base table.
		- If nested elements are present, treat the linked table as the base_table & insert records recursively.
- Example sql:
  ```sql
  BEGIN;

  WITH producer_cte AS (
    INSERT INTO Producers (name, country)
    VALUES ('New Producer', 'India')
    RETURNING id
  ),

  base_cte AS (
    INSERT INTO Movies (name, year, producer_id)
    VALUES ('Some Movie', 2025, (SELECT id FROM producer_cte))
    RETURNING id
  )

  INSERT INTO Movie_Genre_mapping (movie_id, genre_id)
  SELECT id, genre_id FROM base_cte,
  (
    VALUES
      (1),
      (2)
  ) AS child_values(genre_id);

  COMMIT;
  ```
