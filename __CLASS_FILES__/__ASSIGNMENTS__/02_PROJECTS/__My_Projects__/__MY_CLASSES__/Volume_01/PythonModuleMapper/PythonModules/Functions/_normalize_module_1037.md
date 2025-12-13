---
type: function
name: _normalize_module
module: doctest
lineno: 213
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: _normalize_module()

## Overview

Return the module specified by `module`.  In particular:
  - If `module` is a module, then return module.
  - If `module` is a string, then import and return the
    module with that name.
  - If `module` is None, then return the calling module.
    The calling module is assumed to be the module of
    the stack frame at the given depth in the call stack.

```python
def _normalize_module(module, depth)
```

**Module:** [[Modules/doctest|doctest]]
**Type:** Module-level function
**Line:** 213
