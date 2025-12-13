---
type: function
name: replace
module: dataclasses
lineno: 1580
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: replace()

## Overview

Return a new object replacing specified fields with new values.

This is especially useful for frozen classes.  Example usage::

  @dataclass(frozen=True)
  class C:
      x: int
      y: int

  c = C(1, 2)
  c1 = replace(c, x=3)
  assert c1.x == 3 and c1.y == 2

```python
def replace()
```

**Module:** [[Modules/dataclasses|dataclasses]]
**Type:** Module-level function
**Line:** 1580
