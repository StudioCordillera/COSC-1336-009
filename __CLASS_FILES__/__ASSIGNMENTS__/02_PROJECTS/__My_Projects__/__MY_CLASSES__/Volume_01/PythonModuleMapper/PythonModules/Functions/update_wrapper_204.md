---
type: function
name: update_wrapper
module: functools
lineno: 36
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: update_wrapper()

## Overview

Update a wrapper function to look like the wrapped function

wrapper is the function to be updated
wrapped is the original function
assigned is a tuple naming the attributes assigned directly
from the wrapped function to the wrapper function (defaults to
functools.WRAPPER_ASSIGNMENTS)
updated is a tuple naming the attributes of the wrapper that
are updated with the corresponding attribute from the wrapped
function (defaults to functools.WRAPPER_UPDATES)

```python
def update_wrapper(wrapper, wrapped, assigned, updated)
```

**Module:** [[Modules/functools|functools]]
**Type:** Module-level function
**Line:** 36
