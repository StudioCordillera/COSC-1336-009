---
type: function
name: insort_left
module: bisect
lineno: 57
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: insort_left()

## Overview

Insert item x in list a, and keep it sorted assuming a is sorted.

If x is already in a, insert it to the left of the leftmost x.

Optional args lo (default 0) and hi (default len(a)) bound the
slice of a to be searched.

A custom key function can be supplied to customize the sort order.

```python
def insort_left(a, x, lo, hi)
```

**Module:** [[Modules/bisect|bisect]]
**Type:** Module-level function
**Line:** 57
