---
type: function
name: insort_right
module: bisect
lineno: 4
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: insort_right()

## Overview

Insert item x in list a, and keep it sorted assuming a is sorted.

If x is already in a, insert it to the right of the rightmost x.

Optional args lo (default 0) and hi (default len(a)) bound the
slice of a to be searched.

A custom key function can be supplied to customize the sort order.

```python
def insort_right(a, x, lo, hi)
```

**Module:** [[Modules/bisect|bisect]]
**Type:** Module-level function
**Line:** 4
