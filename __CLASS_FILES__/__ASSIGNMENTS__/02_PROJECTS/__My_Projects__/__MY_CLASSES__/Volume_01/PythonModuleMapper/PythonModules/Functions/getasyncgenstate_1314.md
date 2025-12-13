---
type: function
name: getasyncgenstate
module: inspect
lineno: 1956
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: getasyncgenstate()

## Overview

Get current state of an asynchronous generator object.

Possible states are:
  AGEN_CREATED: Waiting to start execution.
  AGEN_RUNNING: Currently being executed by the interpreter.
  AGEN_SUSPENDED: Currently suspended at a yield expression.
  AGEN_CLOSED: Execution has completed.

```python
def getasyncgenstate(agen)
```

**Module:** [[Modules/inspect|inspect]]
**Type:** Module-level function
**Line:** 1956
