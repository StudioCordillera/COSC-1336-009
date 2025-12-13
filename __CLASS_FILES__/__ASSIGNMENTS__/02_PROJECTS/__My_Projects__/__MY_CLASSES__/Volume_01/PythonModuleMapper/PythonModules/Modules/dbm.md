---
type: module
name: dbm
filepath: C:\Users\WORK_ADMIN\anaconda3\Lib\dbm\__init__.py
is_package: True
analyzed_at: 2025-12-10T03:46:16.007544
tags:
  - python
  - module
---

# Module: dbm

## Overview

Generic interface to all dbm clones.

Use

        import dbm
        d = dbm.open(file, 'w', 0o666)

The returned object is a dbm.sqlite3, dbm.gnu, dbm.ndbm or dbm.dumb database object, dependent on the
type of database being opened (determined by the whichdb function) in the case
of an existing dbm. If the dbm does not exist and the create or new flag ('c'
or 'n') was specified, the dbm type will be determined by the availability of
the modules (tested in the above order).

It has the following interface (key and data are strings):

        d[key] = data   # store data at key (may override data at
                        # existing key)
        data = d[key]   # retrieve data at key (raise KeyError if no
                        # such key)
        del d[key]      # delete data stored at key (raises KeyError
                        # if no such key)
        flag = key in d # true if the key exists
        list = d.keys() # return a list of all existing keys (slow!)

Future versions may change the order in which implementations are
tested for existence, and add interfaces to other dbm-like
implementations.

**Filepath:** `C:\Users\WORK_ADMIN\anaconda3\Lib\dbm\__init__.py`
**Type:** Package
**Analyzed:** 2025-12-10 03:46:16

## Dependencies

This module imports:
- [[Modules/dbm|dbm]]
- [[Modules/struct|struct]]

## Used By

This module is imported by:
- [[Modules/dbm|dbm]]

## Classes

- [[Classes/error|error]] (line 38)

## Functions

- [[Functions/open_1530|open()]] (line 53)
- [[Functions/whichdb_1531|whichdb()]] (line 98)
