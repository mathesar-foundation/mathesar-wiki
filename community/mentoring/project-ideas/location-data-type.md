---
title: Location Data type
description: Gsoc project idea 
published: true
date: 2023-02-06T17:35:00.632Z
tags: 
editor: markdown
dateCreated: 2023-02-06T17:35:00.632Z
---


## Classification
- **Difficulty**: Hard
- **Skills needed**: SQLAlchemy, SQL, PostGIS
- **Skills that could be helpful**: Django, Svelte, TypeScript
- **Length**: Long (~350 hours)

## The Problem
- The Mathesar UI allows users to configure the column types for their data, choosing between types like "Number", "Date", "Text", and so on. 
We would like to provide a Spatial data type so that users can
  - Store Geometric values like a location coordinate, boundaries of an area etc
  - Process the spatial values like sorting based on nearest location coordinate, filtering for values within a certain boundary.
  - Visualize a spatial value 

## Feature Description
- Users should be able to install [PostGIS extension](https://postgis.net/)
- Users should be able to set the Postgis data types(Geometry, Geography data types) as a column type
- Users should be able to choose the spatial type(POINT, LINESTRING etc) for a Geometry/Geography column.
- Add the basic operations supported by Postgres and PostGIS to our [functions framework](https://github.com/centerofci/mathesar/blob/8cad33707fa646bfe17d87da9435ed8123a85097/db/functions/base.py#L70)
- Add the basic functions supported by PostGIS to our [functions framework](https://github.com/centerofci/mathesar/blob/8cad33707fa646bfe17d87da9435ed8123a85097/db/functions/base.py#L70)
- Add casting functions to change a column from a spatial data type to a different compatible spatial data type.
- **Bonus**: Provide a text based UI for the user to enter the coordinates.  Add Map based coordinate Picker UI, using something like [OpenStreetMap](https://www.openstreetmap.org/)

## Architectural Problems
We need to figure out
- the logic for identifying columns with spatial data value when the data is imported
- how to format the geometric data types when sending it to or receiving it from the frontend
- Figure out the logic for casting between various compatible spatial data types.

## Tasks
1. Add PostGIS data types to the list of available data types in Mathesar.
2. Integrate PostGIS data types with our data type inference logic when a dataset is imported.
3. Make sure we are able to infer spatial column type correctly when a column data is requested using the column API
4. Integrate all the PostGIS data type with our existing APIs.
5. Research and figure out a proper format to serialize and deserialize the PostGIS data types. You would need to confirm with the frontend team with the serialization format.
6. Add the functions and operators supported by PostGIS to our functions and filters APIs.
7. **Bonus:** Add frontend UI for the user to enter a spatial value into a Spatial column.

## Expected Outcome
- Users can set columns to the most of the commonly used data types along with the spatial type available in PostGIS.
- Users should be able to import data which contains Spatial values and expect Mathesar to infer the column type based on the imported Spatial value.
- Users should be able to get/set a column to a spatial data type.
- Users should be able to get/set a spatial value to a spatial column using the API.
- Users should be able to filter, sort the spatial data based on operators supported by PostGIS. The list of operators does not have to be exhaustive, only the infrastructure should be set in place, so that we can extend the list of supported operators in future.
- **Bonus:** Users should be able to set the spatial data using the UI.

## Application Tips
- Demonstrate proficiency with the required skills.
- Present some preliminary research into Spatial data types, Spatial data type serialization format.
- Demonstrate an understanding of how Mathesar does data type inference.

## Resources
- [The Ultimate List of GIS Formats and Geospatial File Extensions](https://gisgeography.com/gis-formats/)
- [PostGIS documentation](https://postgis.net/workshops/postgis-intro/)

## Mentors
**Primary Mentor**: Mukesh
**Secondary Mentor(s)**: Pavish 
