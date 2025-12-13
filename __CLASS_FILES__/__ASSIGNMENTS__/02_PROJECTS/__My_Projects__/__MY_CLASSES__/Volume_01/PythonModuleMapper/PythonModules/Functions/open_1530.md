---
type: function
name: open
module: dbm
lineno: 53
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: open()

## Overview

Open or create database at path given by *file*.

Optional argument *flag* can be 'r' (default) for read-only access, 'w'
for read-write access of an existing database, 'c' for read-write access
to a new or existing database, and 'n' for read-write access to a new
database.

Note: 'r' and 'w' fail if the database doesn't exist; 'c' creates it
only if it doesn't exist; and 'n' always creates a new database.

```python
def open(file, flag, mode)
```

**Module:** [[Modules/dbm|dbm]]
**Type:** Module-level function
**Line:** 53
