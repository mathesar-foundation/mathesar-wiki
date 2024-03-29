# 2023-12-12 Design Session

## Topic

Discussion on GitHub Issue [#3242: Editing Link Records](https://github.com/mathesar-foundation/mathesar/issues/3242).

## Problem

### Overview

We want to improve the functionality for editing details of a linked record. Currently, there are two different ideas under consideration (see: [Github Issue Comments](https://github.com/mathesar-foundation/mathesar/issues/3242))

The proposed ideas are the following:

- **Idea 1:** Clicking on a linked record brings up the record selector for swapping the currently selected record, with the editing form accessible only through a contextual menu.
- **Idea 2:** Directly accessing the editing form upon clicking a link record.

The challenge in choosing between these ideas is that we don't have clarity on what the most frequent workflows are when interacting with link records. Based on what we know, from conversations we had with users, we'll try to identify some of these and use them to inform our decision.

### Considerations

- **Compatibility with Non-Editable Records**: In future versions, should Mathesar allow users to create read-only, shareable views, linked records would be accessible only for viewing details. The chosen interaction should not limit its usability.
- **Data Entry Focus:** Focusing on the editing form as the primary element of the UI is beneficial for data entry workflows. Our surveys showed users had interest in data entry via forms.
- **Record Page and Form Interactions:** Some inconsistencies might arise when users access these controls from the record page or the editing form. The solution needs to consider how the controls will work in different presentation modes for records.
- **Multiple Link Records:** If in the future we allow users to create multiple link records, then we'll need to consider how to handle the UI for editing multiple link records. 
- **Lack of Undo:** Given the current absence of an undo feature in Mathesar, it's important to minimize the likelihood of accidental edits, for example, a user thinking he's editing an instance of a record and not the record in another table.
- **Contextual Menu Discoverability:** The design should consider the potential issue of users not discovering or remembering the functionalities hidden within contextual menus.
- **Keyboard Navigation:** Ideally, users should be able to edit and replace records using keyboard-only navigation.

### Challenge

Finding a design solution that satisfies user needs for editing link records while prioritizing the most frequent workflows.

## Proposed Solutions

### Idea 1: Prioritize the Record Selector

**Use Cases:**

> "As a tutor, I need to update the foreign key in the 'leads' table when a student changes their course preference, or in the 'timesheets' table when a student is reassigned to a different tutor."

**Reassigning Frequently:** In cases where users need to reassign link records frequently, the record selector is a more efficient approach. It allows users to quickly swap the currently selected record without having to open the editing form.

**User Flow:**

* The user sets up a relationship between two tables.
* In a foreign key column, the user clicks on an empty cell.
* The record selector opens, allowing the user to select a record from the linked table.
* The user selects a record from the linked table. The record selector closes, and the selected record is displayed in the foreign key column as a tag-like element.
* If the user clicks on the tag-like element, the record selector opens again, allowing the user to select a different record from the linked table. The user can also click on the dropdown-arrow icon to directly open record selector.
* If the user right-clicks on the cell, a contextual menu opens with the option to edit the linked record.

### Idea 2: Prioritize the Editing Form

> "As a fundraising campaign manager, I need to frequently review and select potential donors from a large database. When I click on a donor's record, I want to see their contact and donation history. If I need to update their information, I'll click on the record to access the editing form."

**Editing Frequently:** In cases where users need to edit link records frequently, the direct editing approach is more efficient. It allows users to quickly access the editing form without having to open the record selector.
**User Expectations:** Users expect to be able to edit link records directly. This is the approach used by most other tools.

**User Flow:**

- User has set up a relationship between two tables.
- In a foreign key column, the user clicks on an empty cell.
- The record selector opens, allowing the user to select a record from the linked table.
- The user selects a record from the linked table. The record selector closes, and the selected record is displayed in the foreign key column as a tag-like element.
- If the user clicks on the tag-like element, the editing form opens, allowing the user to edit the linked record.
- If the user removes the tag-like element, by clicking on the `x` icon then they can click on the empty cell to open the record selector again.
- If the user right-clicks on the tag-like element, a contextual menu opens with the option to 'Replace record' which opens the record selector. The user can select a different record from the linked table.

### Idea 3: Balance Both

Given that Idea 1 and Idea 2 serve different user needs, a third idea would be to create a UI that allows users to clearly choose between editing a record and selecting a different record from the relationship. This would be best for mixed environments where users need to quickly and frequently perform both actions.

## Discussion Points

- What are the pros and cons of each idea?
- What are the use cases for editing link records? Which idea best addresses these use cases?
- What are the implications of each idea on the future product vision?

## Actions we need to support
- Add a new linked record
    - Editing current table 
    - Editing the other table
- De-link linked record
    - Editing only current table 
- Swap linked record for a different linked record
    - Editing only current table 
- Edit underlying record
    - Editing the other table
- Navigate to record page

We need to make it clear whether the user is editing the current record ONLY or a different table (because that can affect multiple records).
