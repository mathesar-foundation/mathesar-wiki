# List data type - Frontend specs

## Creating a column
From the table's view:
1. The user clicks on the "+" button.
2. The usual modal is displayed. Among the type options, the `list` type is displayed.

![data_types_dropdown.png](/assets/archive/product/projects/2023/07/list-datatype/data_types_dropdown.png)

3. The user has to set a name for the column. They also have to choose the `list` type. After clicking this option, the user has to choose the type of the items that the list will contain. A sub-list of the currently supported data types is displayed (excluding the list type).

![select_list_item_type.png](/assets/archive/product/projects/2023/07/list-datatype/select_list_item_type.png)

4. The "*Add*" button is enabled and the user has to click on it  in order to create the list column.

![add_button_enabled.png](/assets/archive/product/projects/2023/07/list-datatype/add_button_enabled.png)

### Notes
- Only one-dimensional (1-D) arrays are going to be supported, therefore, the user is not going to be prompted to provide a "dimensions" argument.
- Nested/multi-dimensional arrays are going to be displayed and treated as strings. 
Example of multi-dimensional arrays:
![nested_arrays_pills.png](/assets/archive/product/projects/2023/07/list-datatype/nested_arrays_pills.png)

- For already existing Postgresql databases from the user, which could contain multi-dimensional arrays, we can add an information note on the sidebar that warns about this constraint. The message could be something like: *"Only 1-D lists/arrays are supported. If there exist items with more dimensions, then the entire column will be considered as a list of strings type".*
![list_info_box.png](/assets/archive/product/projects/2023/07/list-datatype/list_info_box.png)
