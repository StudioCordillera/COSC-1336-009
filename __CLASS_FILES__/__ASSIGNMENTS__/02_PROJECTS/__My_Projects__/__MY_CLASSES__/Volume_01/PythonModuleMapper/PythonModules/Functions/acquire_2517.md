---
type: function
name: acquire
module: threading
lineno: 176
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
  - public_method
---

# Function: acquire()

## Overview

Acquire a lock, blocking or non-blocking.

When invoked without arguments: if this thread already owns the lock,
increment the recursion level by one, and return immediately. Otherwise,
if another thread owns the lock, block until the lock is unlocked. Once
the lock is unlocked (not owned by any thread), then grab ownership, set
the recursion level to one, and return. If more than one thread is
blocked waiting until the lock is unlocked, only one at a time will be
able to grab ownership of the lock. There is no return value in this
case.

When invoked with the blocking argument set to true, do the same thing
as when called without arguments, and return true.

When invoked with the blocking argument set to false, do not block. If a
call without an argument would block, return false immediately;
otherwise, do the same thing as when called without arguments, and
return true.

When invoked with the floating-point timeout argument set to a positive
value, block for at most the number of seconds specified by timeout
and as long as the lock cannot be acquired.  Return true if the lock has
been acquired, false if the timeout has elapsed.

```python
def acquire(self, blocking, timeout)
```

**Module:** [[Modules/threading|threading]]
**Class:** [[Classes/_RLock|_RLock]]
**Type:** Method
**Line:** 176

## Categories

- [[Taxonomy/public_method|public_method]]
- [[Taxonomy/public_method|public_method]]
