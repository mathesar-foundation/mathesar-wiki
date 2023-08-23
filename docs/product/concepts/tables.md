# Tables

## About

A **table** is where data in a [Database](/product/concepts/databases) is actually stored.

Tables consist of **columns** and **records** (rows).

- A **column** describes the data stored, including (but not limited to ) its [Data Type](/product/concepts/data-types).
- A **record** is a single unit of data that can be stored in a table. Each record stores data corresponding to each column defined on the table.

### Tables in Mathesar
Creating a table is the first step to managing your data within Mathesar.

### Example

| ID | Name | Country | Age | Birth |
|-|-|-|-|-|
| 1 | Jayanta Caoimhe | Papua New Guinea | 22 | March 26, 1999 (8:01 AM) |
| 2 | Tatenda Birgitta | Zimbabwe | 8 | October 31, 2013 (9:11 PM) |
| 3 | Barend Reinhild | Belgium | 45 | October 2, 1976 (9:36 AM) |

In this table, we have **5 columns** and **3 records** (rows).

- The columns are: `ID`, `Name`, `Country`, `Age`, and `Birth`.
- Each record fits the parameters defined by the column. So every record has a number as `ID` and date & time as `Birth`.

## Usage
In order to avoid duplicating data and make data entry easier, we encourage users to set up a single table for each category of data and then create links betweeen them as needed.

In the above example, it would be better to have a separate table for `Country` as follows.

##### People
| ID | Name | Country ID | Age | Birth |
|-|-|-|-|-|
| 1 | Jayanta Caoimhe | 21 | 22 | March 26, 1999 (8:01 AM) |
| 2 | Tatenda Birgitta | 23 | 8 | October 31, 2013 (9:11 PM) |
| 3 | Barend Reinhild | 25 | 45 | October 2, 1976 (9:36 AM) |

##### Countries
| ID | Country |
|-|-|
| 21 | Papua New Guinea |
| 23 | Zimbabwe |
| 25 | Belgium |

Now, if you need to add a new person from Papua New Guinea to the **People** table, you don't need to type `Papua New Guinea` again and risk making a typo. You don't need to remember that Papua New Guinea's ID is 21 either - Mathesar offers auto-complete functionality for linked tables and will find the correct record from **Countries** when you start typing the country name.

Although this is convenient for data entry, while looking at the data or analyzing it, you might want to see the full country name next to each person's name. For that functionality, you should set up a [View](/product/concepts/views). 