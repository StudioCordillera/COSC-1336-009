---
type: function
name: length_hint
module: operator
lineno: 185
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: length_hint()

## Overview

Return an estimate of the number of items in obj.
This is useful for presizing containers when building from an iterable.

If the object supports len(), the result will be exact. Otherwise, it may
over- or under-estimate by an arbitrary amount. The result will be an
integer >= 0.

```python
def length_hint(obj, default)
```

**Module:** [[Modules/operator|operator]]
**Type:** Module-level function
**Line:** 185
