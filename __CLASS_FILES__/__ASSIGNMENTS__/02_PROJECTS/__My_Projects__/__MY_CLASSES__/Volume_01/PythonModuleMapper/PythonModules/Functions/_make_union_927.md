---
type: function
name: _make_union
module: typing
lineno: 797
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: _make_union()

## Overview

Used from the C implementation of TypeVar.

TypeVar.__or__ calls this instead of returning types.UnionType
because we want to allow unions between TypeVars and strings
(forward references).

```python
def _make_union(left, right)
```

**Module:** [[Modules/typing|typing]]
**Type:** Module-level function
**Line:** 797
