---
type: function
name: getclosurevars
module: inspect
lineno: 1579
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: getclosurevars()

## Overview

Get the mapping of free variables to their current values.

Returns a named tuple of dicts mapping the current nonlocal, global
and builtin references as seen by the body of the function. A final
set of unbound names that could not be resolved is also provided.

```python
def getclosurevars(func)
```

**Module:** [[Modules/inspect|inspect]]
**Type:** Module-level function
**Line:** 1579
