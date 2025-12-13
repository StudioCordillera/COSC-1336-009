---
type: function
name: getgeneratorstate
module: inspect
lineno: 1875
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: getgeneratorstate()

## Overview

Get current state of a generator-iterator.

Possible states are:
  GEN_CREATED: Waiting to start execution.
  GEN_RUNNING: Currently being executed by the interpreter.
  GEN_SUSPENDED: Currently suspended at a yield expression.
  GEN_CLOSED: Execution has completed.

```python
def getgeneratorstate(generator)
```

**Module:** [[Modules/inspect|inspect]]
**Type:** Module-level function
**Line:** 1875
