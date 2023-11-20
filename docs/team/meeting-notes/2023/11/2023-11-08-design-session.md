# 2023-11-17 Design Session

## Bidirectional Navigation Design and the Shortcut Menu

### Design Question

- How might we integrate bidirectional navigation between explorations and a table without overcomplicating the design and ensuring it aligns with existing app functionalities?

### Brainstorming
We discussed bidirectional navigation between explorations and a table and options to solve the problem without complex design solutions.

- We agreed that this problem is worth solving, both Sean and Ghislaine found this issue annoying when using Mathesar in their workflow
- We discussed the concept of navigation via global search bar, but dismissed it as too high-concept and not related to this specific problem 
- We dismissed, the idea of using the shortcuts menu for links to explorations based on Sean's input. He pointed out that it is unlikely that users will think of using it for this purpose.
- Debated adding explorations inside the inspector panel but ended up rejecting this idea due to the inspector's designated function for table metadata only.
- We considered a separate panel to show explorations and links (i.e. a "related objects navigation" panel)
    - But the logic of showing / hiding a separate panel is difficult
    - We agreed that the inspector panel shouldn't be replaced by other panels and remain always visible and dynamically responsive to selection events (column, table, record etc.)
- Discussed, then rejected, the idea of a left side panel for explorations because it would have a broad impact on the UX for the app and we need to think through adding new top level navigation elements more holistically, and not just for this one small issue.
- We briefly considered renaming the "Inspector" to something else, but it seemed like overkill.

### Decision
- Decided to implement a drop-down menu next to filter, sort, and group options, labeled "Explorations". There should be a divider between "filter, sort, and group" and this new button.
- In the drop-down, users will find all explorations where the current table is the base, along with an option to add new explorations with the base table preselected.
- For both unsaved and saved explorations, we will have a link to the base table available on the top bar. 
- We decided on this option because:
    - It doesn't violate the concept of the table inspector
    - It doesn't require large changes to the application which should be considered more holistically
    - It doesn't add _too much_ clutter to the navigation.

## Future conversations
- Global search
- Tabs for navigation vs browser tabs
- Left navigation pane for related entities
