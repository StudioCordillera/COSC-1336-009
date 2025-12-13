---
type: function
name: getuser
module: getpass
lineno: 154
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: getuser()

## Overview

Get the username from the environment or password database.

First try various environment variables, then the password
database.  This works on Windows as long as USERNAME is set.
Any failure to find a username raises OSError.

.. versionchanged:: 3.13
    Previously, various exceptions beyond just :exc:`OSError`
    were raised.

```python
def getuser()
```

**Module:** [[Modules/getpass|getpass]]
**Type:** Module-level function
**Line:** 154
