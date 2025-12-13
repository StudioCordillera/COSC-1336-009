---
type: function
name: getmembers_static
module: inspect
lineno: 626
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: getmembers_static()

## Overview

Return all members of an object as (name, value) pairs sorted by name
without triggering dynamic lookup via the descriptor protocol,
__getattr__ or __getattribute__. Optionally, only return members that
satisfy a given predicate.

Note: this function may not be able to retrieve all members
   that getmembers can fetch (like dynamically created attributes)
   and may find members that getmembers can't (like descriptors
   that raise AttributeError). It can also return descriptor objects
   instead of instance members in some cases.

```python
def getmembers_static(object, predicate)
```

**Module:** [[Modules/inspect|inspect]]
**Type:** Module-level function
**Line:** 626
