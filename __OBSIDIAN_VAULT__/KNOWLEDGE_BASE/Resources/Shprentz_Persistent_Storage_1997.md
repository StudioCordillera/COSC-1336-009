# Persistent Storage of Python Objects in Relational Databases

**Joel Shprentz** (shprentz@bdm.com)  
*BDM*  
*1501 BDM Way*  
*McLean, Virginia 22102*

**Source:** 6th International Python Conference, 1997

## 1. Introduction

Existing Python database interfaces force programmers to write many SQL queries and translate retrieved rows into Python objects. These table- and row-oriented interfaces do not mesh well with Python's classes and objects.

Using the Persistent Storage module, Python objects can store themselves in relational database systems. The Persistent Storage module extends the capabilities of Python's early database interface modules, such as the Sybase Module, and the newer Python Database API. With the Persistent Storage module, many database applications need no hand coded SQL queries.

The Persistent Storage module abstracts and hides the underlying database interface. Persistent objects implement (through inheritance) data management methods such as save and delete. Persistent data managers provide behind-the-scenes support and offer public methods to retrieve objects from the database. The Persistent Storage module minimizes database activity by caching retrieved objects and by saving objects only after their attributes change.

An example of a persistent object is a Department. Each Department object has a name, an organization code, and other descriptive fields. In addition, a Department object stores a reference to a manager (a Person object) and to a list of employees (also Person objects). The Department object has methods to get its name, its manager object, its list of employee objects, and its other attributes. The database retrievals needed to implement these methods are hidden from objects outside the Department class.

Unlike Python's built-in `pickle` and `shelve` modules, the persistent storage module cannot support ad hoc requests to store arbitrary Python objects. Object persistence requires planning, database setup, and lots of boring Python code.

To relieve the tedium and reduce errors, a code generator takes a brief object description and writes a Python module for a persistent version of that object. The generated module includes a data manager that can create a relational database table, save objects into the table, and retrieve objects from the table. The module also includes the persistent object class, which has methods to get and update attribute values.

The Persistent Storage module has been used in several large applications. The Python code is available on the Internet.

## 2. Background

### 2.1 Relational Databases

Relational database systems, based on the relational data model introduced by Codd, dominate the commercial database world. In a relational database, data is organized in *tables* containing *rows* (records) and *columns* (fields or domains). For example, an employee table contains one row for each employee and columns for first and last name, Social Security number, birth date, salary, department code, etc.

The basic relational database operations are:
- **selection** - choosing some rows from a table
- **projection** - choosing some columns from a table
- **union** - combining rows from similar tables
- **join** - matching rows from different tables

Although some early relational database systems exposed the basic operations to programmers, most modern systems can be controlled with SQL (Structured Query Language). The database management system parses each SQL query and chooses the sequence of operations needed to retrieve the data.

### 2.2 Python's Database Access

The Python contributed software FTP archive contains modules to interface Python to about a dozen popular relational databases. Because these modules expose each database vendor's unique API, they vary in their approach, implementation, and interface.

Last year the Special Interest Group on Tabular Databases in Python agreed on a Python Database API. The API defines the Python interface to any relational database system by specifying the Python classes and methods needed to open and close database connections, submit queries, receive result descriptions, and receive query results.

The Python Database API, like many database-specific modules, returns retrieved data in a list of tuples, one tuple for each retrieved row. Although the Python Database API was successful at unifying the interface to various database management systems, its retrieved list of tuples provides little support for object-oriented programming.

There are two principal problems with the list of tuples approach:
1. The tuples and underlying SQL statement are application specific, so functions are not very reusable
2. The tuples support only tuple methods, not methods on actual objects (like employees)

### 2.3 Object Models for Persistent Storage

Coad provides a framework for understanding the relationships between a database management system and classes like Employee and Department. Coad's object modeling technique also encompasses user interfaces and interfaces to hardware and external systems.

When constructing an object model, Coad focuses on objects in the problem domain. He defers human interface, data management, and systems integration objects until later in the design process. Coad offers dozens of patterns and strategies for identifying objects, choosing their attributes, defining their relationships, and assigning their methods.

Persistent problem domain objects have a few methods to support data management operations. For example, persistent objects can save themselves in a database. A Department object's `getRoster` method returns a list of Employee objects retrieved from the database. Similarly, its `getManager` method returns a single employee object.

Each persistent object class has a corresponding data manager class with a single instantiated object. The data managers share a database server object, which presents a standardized interface to an underlying database API object.

Data management objects mediate between problem domain objects and the database server object. All SQL queries are created by data management objects. A data manager knows how to create a table, insert a new record, delete a record, and update a record. A data manager also knows how to retrieve records that meet various criteria and how to convert the retrieved lists of tuples into objects.

## 3. Persistent Objects

Persistent objects are objects that can save their state between program runs. Persistent object classes inherit attributes and methods from the PersistentPD class. Persistent objects' classes include methods to perform problem domain functions.

### 3.1 Storage Representation

Persistent objects differ from non-persistent objects by storing an object ID number, storing some types of data in special ways, and storing two status flags: *in database* and *changed*.

Each persistent object has a permanent object ID number assigned by the database system. Within a Python program, persistent objects store numbers and text in ordinary Python object attributes. Persistent objects store dates and times as Python time tuples. Persistent objects store other persistent objects as a pair of values: the other object and its ID number.

When persistent objects are stored in a relational database, each class is assigned its own table with columns for object attributes. Each row in a table holds one object.

### 3.2 Object Creation

Applications can create new persistent objects and retrieve existing persistent objects.

Applications create new objects with a module's `new` function rather than via a class name. The `new` function creates a new persistent object with some initial attribute values, saves the new object in the database, and notes its new object ID.

When an application retrieves existing persistent objects, a data manager must convert retrieved row tuples into Python objects.

### 3.3 Access to Attributes

With persistent objects, attribute access must be tightly controlled. Objects maintain some attribute values in memory, but retrieve other attribute values from the database only when they are needed. To hide this complexity from applications, persistent object classes define methods to get attribute values.

For example, the Department class includes methods to get its attribute values: `getName`, `getManager`, `getEmployees`, and `getMissionStatement`.

Persistent objects are also concerned when attribute values change. Every new attribute value is compared with the old value to confirm that a change is needed. If the new value is different, the object saves the new attribute value and sets its *changed* flag. Later, when executing its `save` method, the object will examine its *changed* flag to decide whether the database copy needs to be updated.

### 3.4 Saving, Deleting, and Refreshing

Three methods inherited from PersistentPD control a persistent object's interaction with its data manager:
- `save` - saves an object in the database
- `delete` - deletes the object from the database
- `refresh` - retrieves fresh attribute values from the database

Persistent objects seldom save, delete, or refresh themselves because they do not understand their own context. Programmers must add these operations to applications where they are appropriate.

## 4. Data Managers

Data managers implement interactions between persistent objects and database systems. Data managers are responsible for retrieving and storing objects, for caching objects, and for performing miscellaneous database related tasks.

### 4.1 Locating Data Managers

Each persistent object class has a corresponding data manager class, which is instantiated with a single instance. Rather than require applications to know the names of all relevant data managers, the database server object supports a data manager registry.

### 4.2 Object Retrieval

Data managers offer various methods to retrieve objects from the database based on different criteria. The retrieval process involves executing SQL queries and converting the resulting tuples into Python objects.

### 4.3 Object Caching

To minimize database access, data managers maintain caches of recently retrieved objects. When an application requests an object, the data manager first checks its cache before querying the database.

### 4.4 Database Operations

Data managers handle all SQL generation for:
- Creating tables and indices
- Inserting new records
- Updating existing records
- Deleting records
- Complex queries with joins and conditions

## 5. Conclusion

The Persistent Storage module provides a framework for storing Python objects in relational databases while maintaining object-oriented programming principles. By hiding SQL complexity and managing database interactions through data managers, it allows developers to work with objects naturally while leveraging the power and reliability of relational databases.

The code generator significantly reduces the tedium of creating persistent object implementations, making it practical to use this approach in real applications. While it requires upfront planning and cannot handle arbitrary object persistence like `pickle`, it provides the structure and performance needed for production database applications.
