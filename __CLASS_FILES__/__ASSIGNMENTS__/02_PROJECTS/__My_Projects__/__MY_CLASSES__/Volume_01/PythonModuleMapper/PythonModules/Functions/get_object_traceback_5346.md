---
type: function
name: get_object_traceback
module: tracemalloc
lineno: 257
is_async: False
is_method: False
tags:
  - python
  - function
categories:
  - accessor
---

# Function: get_object_traceback()

## Overview

Get the traceback where the Python object *obj* was allocated.
Return a Traceback instance.

Return None if the tracemalloc module is not tracing memory allocations or
did not trace the allocation of the object.

```python
def get_object_traceback(obj)
```

**Module:** [[Modules/tracemalloc|tracemalloc]]
**Type:** Module-level function
**Line:** 257

## Categories

- [[Taxonomy/accessor|accessor]]
