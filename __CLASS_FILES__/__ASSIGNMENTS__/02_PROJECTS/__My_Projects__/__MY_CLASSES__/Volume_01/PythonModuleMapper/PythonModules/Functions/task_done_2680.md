---
type: function
name: task_done
module: queue
lineno: 72
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: task_done()

## Overview

Indicate that a formerly enqueued task is complete.

Used by Queue consumer threads.  For each get() used to fetch a task,
a subsequent call to task_done() tells the queue that the processing
on the task is complete.

If a join() is currently blocking, it will resume when all items
have been processed (meaning that a task_done() call was received
for every item that had been put() into the queue).

shutdown(immediate=True) calls task_done() for each remaining item in
the queue.

Raises a ValueError if called more times than there were items
placed in the queue.

```python
def task_done(self)
```

**Module:** [[Modules/queue|queue]]
**Class:** [[Classes/Queue|Queue]]
**Type:** Method
**Line:** 72

## Categories

- [[Taxonomy/public_method|public_method]]
