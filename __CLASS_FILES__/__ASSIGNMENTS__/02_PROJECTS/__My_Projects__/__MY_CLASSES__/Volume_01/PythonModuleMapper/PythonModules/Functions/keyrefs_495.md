---
type: function
name: keyrefs
module: weakref
lineno: 483
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: keyrefs()

## Overview

Return a list of weak references to the keys.

The references are not guaranteed to be 'live' at the time
they are used, so the result of calling the references needs
to be checked before being used.  This can be used to avoid
creating references that will cause the garbage collector to
keep the keys around longer than needed.

```python
def keyrefs(self)
```

**Module:** [[Modules/weakref|weakref]]
**Class:** [[Classes/WeakKeyDictionary|WeakKeyDictionary]]
**Type:** Method
**Line:** 483

## Categories

- [[Taxonomy/public_method|public_method]]
