---
type: function
name: dispatch_opcode
module: bdb
lineno: 208
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: dispatch_opcode()

## Overview

Invoke user function and return trace function for opcode event.
If the debugger stops on the current opcode, invoke
self.user_opcode(). Raise BdbQuit if self.quitting is set.
Return self.trace_dispatch to continue tracing in this scope.

```python
def dispatch_opcode(self, frame, arg)
```

**Module:** [[Modules/bdb|bdb]]
**Class:** [[Classes/Bdb|Bdb]]
**Type:** Method
**Line:** 208

## Categories

- [[Taxonomy/public_method|public_method]]
