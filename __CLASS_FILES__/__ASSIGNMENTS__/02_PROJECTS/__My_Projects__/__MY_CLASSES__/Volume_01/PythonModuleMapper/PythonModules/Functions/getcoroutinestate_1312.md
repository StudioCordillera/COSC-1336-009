---
type: function
name: getcoroutinestate
module: inspect
lineno: 1917
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: getcoroutinestate()

## Overview

Get current state of a coroutine object.

Possible states are:
  CORO_CREATED: Waiting to start execution.
  CORO_RUNNING: Currently being executed by the interpreter.
  CORO_SUSPENDED: Currently suspended at an await expression.
  CORO_CLOSED: Execution has completed.

```python
def getcoroutinestate(coroutine)
```

**Module:** [[Modules/inspect|inspect]]
**Type:** Module-level function
**Line:** 1917
