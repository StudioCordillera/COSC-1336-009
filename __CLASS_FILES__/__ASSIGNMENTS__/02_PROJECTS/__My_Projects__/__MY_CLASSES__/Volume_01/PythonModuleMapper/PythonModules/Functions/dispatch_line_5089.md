---
type: function
name: dispatch_line
module: bdb
lineno: 120
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: dispatch_line()

## Overview

Invoke user function and return trace function for line event.

If the debugger stops on the current line, invoke
self.user_line(). Raise BdbQuit if self.quitting is set.
Return self.trace_dispatch to continue tracing in this scope.

```python
def dispatch_line(self, frame)
```

**Module:** [[Modules/bdb|bdb]]
**Class:** [[Classes/Bdb|Bdb]]
**Type:** Method
**Line:** 120

## Categories

- [[Taxonomy/public_method|public_method]]
