---
type: function
name: whichdb
module: dbm
lineno: 98
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: whichdb()

## Overview

Guess which db package to use to open a db file.

Return values:

- None if the database file can't be read;
- empty string if the file can be read but can't be recognized
- the name of the dbm submodule (e.g. "ndbm" or "gnu") if recognized.

Importing the given module may still fail, and opening the
database using that module may still fail.

```python
def whichdb(filename)
```

**Module:** [[Modules/dbm|dbm]]
**Type:** Module-level function
**Line:** 98
