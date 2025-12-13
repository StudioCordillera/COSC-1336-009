---
type: function
name: notify_all
module: threading
lineno: 428
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: notify_all()

## Overview

Wake up all threads waiting on this condition.

If the calling thread has not acquired the lock when this method
is called, a RuntimeError is raised.

```python
def notify_all(self)
```

**Module:** [[Modules/threading|threading]]
**Class:** [[Classes/Condition|Condition]]
**Type:** Method
**Line:** 428

## Categories

- [[Taxonomy/public_method|public_method]]
