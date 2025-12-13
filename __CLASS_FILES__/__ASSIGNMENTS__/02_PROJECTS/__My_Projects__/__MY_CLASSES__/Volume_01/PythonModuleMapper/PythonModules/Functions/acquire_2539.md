---
type: function
name: acquire
module: threading
lineno: 472
is_async: False
is_method: True
tags:
  - python
  - function
---

# Function: acquire()

## Overview

Acquire a semaphore, decrementing the internal counter by one.

When invoked without arguments: if the internal counter is larger than
zero on entry, decrement it by one and return immediately. If it is zero
on entry, block, waiting until some other thread has called release() to
make it larger than zero. This is done with proper interlocking so that
if multiple acquire() calls are blocked, release() will wake exactly one
of them up. The implementation may pick one at random, so the order in
which blocked threads are awakened should not be relied on. There is no
return value in this case.

When invoked with blocking set to true, do the same thing as when called
without arguments, and return true.

When invoked with blocking set to false, do not block. If a call without
an argument would block, return false immediately; otherwise, do the
same thing as when called without arguments, and return true.

When invoked with a timeout other than None, it will block for at
most timeout seconds.  If acquire does not complete successfully in
that interval, return false.  Return true otherwise.

```python
def acquire(self, blocking, timeout)
```

**Module:** [[Modules/threading|threading]]
**Class:** [[Classes/Semaphore|Semaphore]]
**Type:** Method
**Line:** 472
