---
type: function
name: _eval_type
module: typing
lineno: 463
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: _eval_type()

## Overview

Evaluate all forward references in the given type t.

For use of globalns and localns see the docstring for get_type_hints().
recursive_guard is used to prevent infinite recursion with a recursive
ForwardRef.

```python
def _eval_type(t, globalns, localns, type_params)
```

**Module:** [[Modules/typing|typing]]
**Type:** Module-level function
**Line:** 463
