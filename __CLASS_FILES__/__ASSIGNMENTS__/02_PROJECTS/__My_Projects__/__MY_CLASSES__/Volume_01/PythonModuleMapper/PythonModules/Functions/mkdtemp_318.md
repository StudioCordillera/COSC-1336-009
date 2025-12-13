---
type: function
name: mkdtemp
module: tempfile
lineno: 360
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: mkdtemp()

## Overview

User-callable function to create and return a unique temporary
directory.  The return value is the pathname of the directory.

Arguments are as for mkstemp, except that the 'text' argument is
not accepted.

The directory is readable, writable, and searchable only by the
creating user.

Caller is responsible for deleting the directory when done with it.

```python
def mkdtemp(suffix, prefix, dir)
```

**Module:** [[Modules/tempfile|tempfile]]
**Type:** Module-level function
**Line:** 360
