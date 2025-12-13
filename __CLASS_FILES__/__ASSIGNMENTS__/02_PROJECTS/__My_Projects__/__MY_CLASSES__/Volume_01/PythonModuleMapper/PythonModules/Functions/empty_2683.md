---
type: function
name: empty
module: queue
lineno: 115
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
  - public_method
---

# Function: empty()

## Overview

Return True if the queue is empty, False otherwise (not reliable!).

This method is likely to be removed at some point.  Use qsize() == 0
as a direct substitute, but be aware that either approach risks a race
condition where a queue can grow before the result of empty() or
qsize() can be used.

To create code that needs to wait for all queued tasks to be
completed, the preferred technique is to use the join() method.

```python
def empty(self)
```

**Module:** [[Modules/queue|queue]]
**Class:** [[Classes/Queue|Queue]]
**Type:** Method
**Line:** 115

## Categories

- [[Taxonomy/public_method|public_method]]
- [[Taxonomy/public_method|public_method]]
