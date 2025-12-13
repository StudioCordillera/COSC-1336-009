---
type: function
name: get_nowait
module: queue
lineno: 364
is_async: False
is_method: True
tags:
  - python
  - function
---

# Function: get_nowait()

## Overview

Remove and return an item from the queue without blocking.

Only get an item if one is immediately available. Otherwise
raise the Empty exception.

```python
def get_nowait(self)
```

**Module:** [[Modules/queue|queue]]
**Class:** [[Classes/_PySimpleQueue|_PySimpleQueue]]
**Type:** Method
**Line:** 364
