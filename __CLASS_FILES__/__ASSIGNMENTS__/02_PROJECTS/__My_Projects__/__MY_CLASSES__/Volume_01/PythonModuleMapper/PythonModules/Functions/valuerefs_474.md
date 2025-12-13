---
type: function
name: valuerefs
module: weakref
lineno: 301
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: valuerefs()

## Overview

Return a list of weak references to the values.

The references are not guaranteed to be 'live' at the time
they are used, so the result of calling the references needs
to be checked before being used.  This can be used to avoid
creating references that will cause the garbage collector to
keep the values around longer than needed.

```python
def valuerefs(self)
```

**Module:** [[Modules/weakref|weakref]]
**Class:** [[Classes/WeakValueDictionary|WeakValueDictionary]]
**Type:** Method
**Line:** 301

## Categories

- [[Taxonomy/public_method|public_method]]
