---
type: function
name: shutdown
module: queue
lineno: 236
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: shutdown()

## Overview

Shut-down the queue, making queue gets and puts raise ShutDown.

By default, gets will only raise once the queue is empty. Set
'immediate' to True to make gets raise immediately instead.

All blocked callers of put() and get() will be unblocked. If
'immediate', a task is marked as done for each item remaining in
the queue, which may unblock callers of join().

```python
def shutdown(self, immediate)
```

**Module:** [[Modules/queue|queue]]
**Class:** [[Classes/Queue|Queue]]
**Type:** Method
**Line:** 236

## Categories

- [[Taxonomy/public_method|public_method]]
