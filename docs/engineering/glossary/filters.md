# Filters in Mathesar

This page covers filters from an engineering/architecture perspective. Please see the ["Filters" product concepts page](/en/product/concepts/filters) for a user-facing looking at filters.

## Criteria for Filters in Mathesar
In Mathesar, filters are a subset of functions that take in a set of row or a relation as input and return only the rows that satisfy some condition.

To be considered a filter, a function has to only consider a single row at a time. It should have no knowledge of any other rows in the relation. This means that filters are **commutative**.

### Examples

Consider this table:

As an example, here's a table:

| ID | Title | Year | Favorite |
|-|-|-|-|
| 1 | Dante's Peak | 1997 | FALSE |
| 2 | Forrest Gump | 1994 | TRUE |
| 3 | The Karate Kid | 1984 | TRUE |
| 4 | Dante's Peak | 1997 | TRUE |
| 5 | The Karate Kid | 1984 | TRUE |

Here are some examples of correct and wrong filters. The emoji indicates whether they are correct.
- `"Year" > 1990`
- `"ID" = 5`
- `"Favorite" is TRUE`
- "Title" is a duplicate
- Latest "Year"

## Reasoning
You might be wondering why filter scope is limited to a single row. This is to allow filters to be applied in any order (to ensure filters are commutative). Otherwise, we will need to introduce users to the concept of a pipeline of operations and that seems more complicated to design. We plan to have a separate user-facing concept for operations that will have different results depending on the ordering.

This can be illustrated with treating "is a duplicate" as a filter below and observing how the results change based on ordering. This uses the table from the example above.

### Order 1
Imagine the user applies filters in this order: 
1. `"Year" > 1993`
2. `"Favorite" is TRUE`
3. `"Title" is a duplicate`

#### Filter 1: `"Year" > 1993`
After filtering:
| ID | Title | Year | Favorite |
|-|-|-|-|
| 1 | Dante's Peak | 1997 | FALSE |
| 2 | Forrest Gump | 1994 | TRUE |
| 4 | Dante's Peak | 1997 | TRUE |

####  Filter 2: `"Favorite" is TRUE`
After filtering:
| ID | Title | Year | Favorite |
|-|-|-|-|
| 2 | Forrest Gump | 1994 | TRUE |
| 4 | Dante's Peak | 1997 | TRUE |

#### Filter 3:`"Title" is a duplicate`
After filtering: *0 results.*

### Order 2
But instead if the user applies filter in this order
1. `"Year" > 1993`
2. `"Title" is a duplicate`
3. `"Favorite" is TRUE`

#### Filter 1: `"Year" > 1993`
After filtering:
| ID | Title | Year | Favorite |
|-|-|-|-|
| 1 | Dante's Peak | 1997 | FALSE |
| 2 | Forrest Gump | 1994 | TRUE |
| 4 | Dante's Peak | 1997 | TRUE |

#### Filter 2:`"Title" is a duplicate`
After filtering:
| ID | Title | Year | Favorite |
|-|-|-|-|
| 1 | Dante's Peak | 1997 | FALSE |
| 4 | Dante's Peak | 1997 | TRUE |

####  Filter 3: `"Favorite" is TRUE`
After filtering:
| ID | Title | Year | Favorite |
|-|-|-|-|
| 4 | Dante's Peak | 1997 | TRUE |