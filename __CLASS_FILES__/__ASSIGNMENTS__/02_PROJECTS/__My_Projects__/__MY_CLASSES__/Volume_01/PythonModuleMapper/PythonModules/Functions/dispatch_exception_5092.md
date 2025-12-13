---
type: function
name: dispatch_exception
module: bdb
lineno: 181
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: dispatch_exception()

## Overview

Invoke user function and return trace function for exception event.

If the debugger stops on this exception, invoke
self.user_exception(). Raise BdbQuit if self.quitting is set.
Return self.trace_dispatch to continue tracing in this scope.

```python
def dispatch_exception(self, frame, arg)
```

**Module:** [[Modules/bdb|bdb]]
**Class:** [[Classes/Bdb|Bdb]]
**Type:** Method
**Line:** 181

## Categories

- [[Taxonomy/public_method|public_method]]
