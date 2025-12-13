---
type: module
name: sqlite3
filepath: C:\Users\WORK_ADMIN\anaconda3\Lib\sqlite3\__init__.py
is_package: True
analyzed_at: 2025-12-10T03:46:16.055970
tags:
  - python
  - module
---

# Module: sqlite3

## Overview

The sqlite3 extension module provides a DB-API 2.0 (PEP 249) compliant
interface to the SQLite library, and requires SQLite 3.15.2 or newer.

To use the module, start by creating a database Connection object:

    import sqlite3
    cx = sqlite3.connect("test.db")  # test.db will be created or opened

The special path name ":memory:" can be provided to connect to a transient
in-memory database:

    cx = sqlite3.connect(":memory:")  # connect to a database in RAM

Once a connection has been established, create a Cursor object and call
its execute() method to perform SQL queries:

    cu = cx.cursor()

    # create a table
    cu.execute("create table lang(name, first_appeared)")

    # insert values into a table
    cu.execute("insert into lang values (?, ?)", ("C", 1972))

    # execute a query and iterate over the result
    for row in cu.execute("select * from lang"):
        print(row)

    cx.close()

The sqlite3 module is written by Gerhard Häring <gh@ghaering.de>.

**Filepath:** `C:\Users\WORK_ADMIN\anaconda3\Lib\sqlite3\__init__.py`
**Type:** Package
**Analyzed:** 2025-12-10 03:46:16

## Functions

- [[Functions/DateFromTicks_1532|DateFromTicks()]] (line 42)
- [[Functions/TimeFromTicks_1533|TimeFromTicks()]] (line 45)
- [[Functions/TimestampFromTicks_1534|TimestampFromTicks()]] (line 48)
- [[Functions/register_adapters_and_converters_1535|register_adapters_and_converters()]] (line 57)
- [[Functions/__getattr___1536|__getattr__()]] (line 63)
