---
type: function
name: RLock
module: threading
lineno: 122
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: RLock()

## Overview

Factory function that returns a new reentrant lock.

A reentrant lock must be released by the thread that acquired it. Once a
thread has acquired a reentrant lock, the same thread may acquire it again
without blocking; the thread must release it once for each time it has
acquired it.

```python
def RLock()
```

**Module:** [[Modules/threading|threading]]
**Type:** Module-level function
**Line:** 122
