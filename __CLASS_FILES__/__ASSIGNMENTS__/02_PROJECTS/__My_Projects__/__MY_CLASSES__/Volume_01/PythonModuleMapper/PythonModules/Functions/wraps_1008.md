---
type: function
name: wraps
module: functools
lineno: 66
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: wraps()

## Overview

Decorator factory to apply update_wrapper() to a wrapper function

Returns a decorator that invokes update_wrapper() with the decorated
function as the wrapper argument and the arguments to wraps() as the
remaining arguments. Default arguments are as for update_wrapper().
This is a convenience function to simplify applying partial() to
update_wrapper().

```python
def wraps(wrapped, assigned, updated)
```

**Module:** [[Modules/functools|functools]]
**Type:** Module-level function
**Line:** 66
