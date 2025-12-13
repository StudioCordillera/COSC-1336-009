---
type: function
name: itervaluerefs
module: weakref
lineno: 228
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: itervaluerefs()

## Overview

Return an iterator that yields the weak references to the values.

The references are not guaranteed to be 'live' at the time
they are used, so the result of calling the references needs
to be checked before being used.  This can be used to avoid
creating references that will cause the garbage collector to
keep the values around longer than needed.

```python
def itervaluerefs(self)
```

**Module:** [[Modules/weakref|weakref]]
**Class:** [[Classes/WeakValueDictionary|WeakValueDictionary]]
**Type:** Method
**Line:** 228

## Categories

- [[Taxonomy/public_method|public_method]]
