---
type: function
name: put_nowait
module: queue
lineno: 356
is_async: False
is_method: True
tags:
  - python
  - function
---

# Function: put_nowait()

## Overview

Put an item into the queue without blocking.

This is exactly equivalent to `put(item, block=False)` and is only provided
for compatibility with the Queue class.

```python
def put_nowait(self, item)
```

**Module:** [[Modules/queue|queue]]
**Class:** [[Classes/_PySimpleQueue|_PySimpleQueue]]
**Type:** Method
**Line:** 356
