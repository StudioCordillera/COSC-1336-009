---
type: function
name: heapreplace
module: heapq
lineno: 147
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: heapreplace()

## Overview

Pop and return the current smallest value, and add the new item.

This is more efficient than heappop() followed by heappush(), and can be
more appropriate when using a fixed-size heap.  Note that the value
returned may be larger than item!  That constrains reasonable uses of
this routine unless written as part of a conditional replacement:

    if item > heap[0]:
        item = heapreplace(heap, item)

```python
def heapreplace(heap, item)
```

**Module:** [[Modules/heapq|heapq]]
**Type:** Module-level function
**Line:** 147
