---
type: function
name: cast
module: typing
lineno: 2371
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: cast()

## Overview

Cast a value to a type.

This returns the value unchanged.  To the type checker this
signals that the return value has the designated type, but at
runtime we intentionally don't check anything (we want this
to be as fast as possible).

```python
def cast(typ, val)
```

**Module:** [[Modules/typing|typing]]
**Type:** Module-level function
**Line:** 2371
