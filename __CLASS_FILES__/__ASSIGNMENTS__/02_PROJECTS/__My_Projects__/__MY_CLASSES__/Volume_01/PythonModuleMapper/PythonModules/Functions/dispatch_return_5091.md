---
type: function
name: dispatch_return
module: bdb
lineno: 154
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: dispatch_return()

## Overview

Invoke user function and return trace function for return event.

If the debugger stops on this function return, invoke
self.user_return(). Raise BdbQuit if self.quitting is set.
Return self.trace_dispatch to continue tracing in this scope.

```python
def dispatch_return(self, frame, arg)
```

**Module:** [[Modules/bdb|bdb]]
**Class:** [[Classes/Bdb|Bdb]]
**Type:** Method
**Line:** 154

## Categories

- [[Taxonomy/public_method|public_method]]
