How the documentation is organized
Mathesar has lots of components. A high-level overview of how it’s organized will help you know where to look for certain things:

#### DB Layer:
The `db` module consists of functions that aims to simplify database operations such as reflecting database object(columns, tables, views etc) properties, performing operation on database objects etc

[//]: # "Needs to filled out"




#### Service Layer:

1. Imports - Mathesar can read and import data from other formats like csv and add it to the database. This module consists of functions that helps with reading different formats, detecting encoding, saving the data into the database 
2. Database - Mathesar connects with the database using the sql alchemy client and provides few convienent abstractions over the database concepts. This module helps with connecting to a sqlalchemy client and also provides Mathesar data types used for grouping similar data types together.
3. Api - Api's are responsible for taking request from the frontend and connecting it to the relevant operation on the backend. Api module consists of views which is responsible calling out the necessary actions to be performed based on the request, serializers responsible for validating the sent data and converting the passed data into python objects 
4. Utils - Utility functions
5. Reflection - Mathesar tries to reflect off the required details to represent the database directly from the database as much as possible instead of having the user specify the details or hardcode it. This module is responsible for reflecting the details using `db` module functions and store it on the Mathesar owned database
6. Models - Most of the database information is directly reflected off the database in realtime, but this would make it really slow and hard to work with, so we use Django models to store necessary information of the database and any additional information required for features provided by Mathesar.
7. Tests - Test cases help in testing if Mathesar works as expected
