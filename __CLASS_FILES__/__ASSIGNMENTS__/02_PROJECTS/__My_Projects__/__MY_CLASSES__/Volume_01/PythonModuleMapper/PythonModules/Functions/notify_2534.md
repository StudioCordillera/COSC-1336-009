---
type: function
name: notify
module: threading
lineno: 398
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: notify()

## Overview

Wake up one or more threads waiting on this condition, if any.

If the calling thread has not acquired the lock when this method is
called, a RuntimeError is raised.

This method wakes up at most n of the threads waiting for the condition
variable; it is a no-op if no threads are waiting.

```python
def notify(self, n)
```

**Module:** [[Modules/threading|threading]]
**Class:** [[Classes/Condition|Condition]]
**Type:** Method
**Line:** 398

## Categories

- [[Taxonomy/public_method|public_method]]
