---
type: function
name: release
module: threading
lineno: 214
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
  - public_method
  - public_method
---

# Function: release()

## Overview

Release a lock, decrementing the recursion level.

If after the decrement it is zero, reset the lock to unlocked (not owned
by any thread), and if any other threads are blocked waiting for the
lock to become unlocked, allow exactly one of them to proceed. If after
the decrement the recursion level is still nonzero, the lock remains
locked and owned by the calling thread.

Only call this method when the calling thread owns the lock. A
RuntimeError is raised if this method is called when the lock is
unlocked.

There is no return value.

```python
def release(self)
```

**Module:** [[Modules/threading|threading]]
**Class:** [[Classes/_RLock|_RLock]]
**Type:** Method
**Line:** 214

## Categories

- [[Taxonomy/public_method|public_method]]
- [[Taxonomy/public_method|public_method]]
- [[Taxonomy/public_method|public_method]]
