---
type: function
name: cancel
module: sched
lineno: 87
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: cancel()

## Overview

Remove an event from the queue.

This must be presented the ID as returned by enter().
If the event is not in the queue, this raises ValueError.

```python
def cancel(self, event)
```

**Module:** [[Modules/sched|sched]]
**Class:** [[Classes/scheduler|scheduler]]
**Type:** Method
**Line:** 87

## Categories

- [[Taxonomy/public_method|public_method]]
