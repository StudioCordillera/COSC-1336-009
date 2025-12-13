---
type: function
name: put_nowait
module: queue
lineno: 220
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
  - public_method
---

# Function: put_nowait()

## Overview

Put an item into the queue without blocking.

Only enqueue the item if a free slot is immediately available.
Otherwise raise the Full exception.

```python
def put_nowait(self, item)
```

**Module:** [[Modules/queue|queue]]
**Class:** [[Classes/Queue|Queue]]
**Type:** Method
**Line:** 220

## Categories

- [[Taxonomy/public_method|public_method]]
- [[Taxonomy/public_method|public_method]]
