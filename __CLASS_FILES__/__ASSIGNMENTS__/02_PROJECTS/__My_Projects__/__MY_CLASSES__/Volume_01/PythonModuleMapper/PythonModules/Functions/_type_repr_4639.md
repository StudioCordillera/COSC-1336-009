---
type: function
name: _type_repr
module: typing
lineno: 235
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: _type_repr()

## Overview

Return the repr() of an object, special-casing types (internal helper).

If obj is a type, we return a shorter version than the default
type.__repr__, based on the module and qualified name, which is
typically enough to uniquely identify a type.  For everything
else, we fall back on repr(obj).

```python
def _type_repr(obj)
```

**Module:** [[Modules/typing|typing]]
**Type:** Module-level function
**Line:** 235
