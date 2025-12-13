---
type: function
name: enterabs
module: sched
lineno: 62
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: enterabs()

## Overview

Enter a new event in the queue at an absolute time.

Returns an ID for the event which can be used to remove it,
if necessary.

```python
def enterabs(self, time, priority, action, argument, kwargs)
```

**Module:** [[Modules/sched|sched]]
**Class:** [[Classes/scheduler|scheduler]]
**Type:** Method
**Line:** 62

## Categories

- [[Taxonomy/public_method|public_method]]
