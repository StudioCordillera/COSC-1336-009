---
type: function
name: release
module: threading
lineno: 519
is_async: False
is_method: True
tags:
  - python
  - function
---

# Function: release()

## Overview

Release a semaphore, incrementing the internal counter by one or more.

When the counter is zero on entry and another thread is waiting for it
to become larger than zero again, wake up that thread.

```python
def release(self, n)
```

**Module:** [[Modules/threading|threading]]
**Class:** [[Classes/Semaphore|Semaphore]]
**Type:** Method
**Line:** 519
