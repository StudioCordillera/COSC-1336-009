---
type: function
name: abort
module: threading
lineno: 801
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: abort()

## Overview

Place the barrier into a 'broken' state.

Useful in case of error.  Any currently waiting threads and threads
attempting to 'wait()' will have BrokenBarrierError raised.

```python
def abort(self)
```

**Module:** [[Modules/threading|threading]]
**Class:** [[Classes/Barrier|Barrier]]
**Type:** Method
**Line:** 801

## Categories

- [[Taxonomy/public_method|public_method]]
