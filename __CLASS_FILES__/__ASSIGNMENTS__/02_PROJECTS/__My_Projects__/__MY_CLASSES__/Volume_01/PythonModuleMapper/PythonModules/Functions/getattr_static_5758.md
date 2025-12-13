---
type: function
name: getattr_static
module: inspect
lineno: 1818
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: getattr_static()

## Overview

Retrieve attributes without triggering dynamic lookup via the
descriptor protocol,  __getattr__ or __getattribute__.

Note: this function may not be able to retrieve all attributes
that getattr can fetch (like dynamically created attributes)
and may find attributes that getattr can't (like descriptors
that raise AttributeError). It can also return descriptor objects
instead of instance members in some cases. See the
documentation for details.

```python
def getattr_static(obj, attr, default)
```

**Module:** [[Modules/inspect|inspect]]
**Type:** Module-level function
**Line:** 1818
