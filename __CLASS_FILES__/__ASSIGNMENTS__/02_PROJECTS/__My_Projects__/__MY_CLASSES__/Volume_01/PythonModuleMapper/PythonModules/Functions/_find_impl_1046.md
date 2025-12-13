---
type: function
name: _find_impl
module: functools
lineno: 800
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: _find_impl()

## Overview

Returns the best matching implementation from *registry* for type *cls*.

Where there is no registered implementation for a specific type, its method
resolution order is used to find a more generic implementation.

Note: if *registry* does not contain an implementation for the base
*object* type, this function may return None.

```python
def _find_impl(cls, registry)
```

**Module:** [[Modules/functools|functools]]
**Type:** Module-level function
**Line:** 800
