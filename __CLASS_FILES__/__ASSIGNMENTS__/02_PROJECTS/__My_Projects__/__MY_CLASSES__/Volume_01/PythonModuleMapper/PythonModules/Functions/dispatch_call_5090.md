---
type: function
name: dispatch_call
module: bdb
lineno: 132
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: dispatch_call()

## Overview

Invoke user function and return trace function for call event.

If the debugger stops on this function call, invoke
self.user_call(). Raise BdbQuit if self.quitting is set.
Return self.trace_dispatch to continue tracing in this scope.

```python
def dispatch_call(self, frame, arg)
```

**Module:** [[Modules/bdb|bdb]]
**Class:** [[Classes/Bdb|Bdb]]
**Type:** Method
**Line:** 132

## Categories

- [[Taxonomy/public_method|public_method]]
