---
type: function
name: bisect_right
module: bisect
lineno: 21
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: bisect_right()

## Overview

Return the index where to insert item x in list a, assuming a is sorted.

The return value i is such that all e in a[:i] have e <= x, and all e in
a[i:] have e > x.  So if x already appears in the list, a.insert(i, x) will
insert just after the rightmost x already there.

Optional args lo (default 0) and hi (default len(a)) bound the
slice of a to be searched.

A custom key function can be supplied to customize the sort order.

```python
def bisect_right(a, x, lo, hi)
```

**Module:** [[Modules/bisect|bisect]]
**Type:** Module-level function
**Line:** 21
