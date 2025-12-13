---
type: function
name: trace_vdelete
module: tkinter
lineno: 511
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: trace_vdelete()

## Overview

Delete the trace callback for a variable.

MODE is one of "r", "w", "u" for read, write, undefine.
CBNAME is the name of the callback returned from trace_variable or trace.

This deprecated method wraps a deprecated Tcl method that will
likely be removed in the future.  Use trace_remove() instead.

```python
def trace_vdelete(self, mode, cbname)
```

**Module:** [[Modules/tkinter|tkinter]]
**Class:** [[Classes/Variable|Variable]]
**Type:** Method
**Line:** 511

## Categories

- [[Taxonomy/public_method|public_method]]
