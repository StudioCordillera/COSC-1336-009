---
type: function
name: trace_variable
module: tkinter
lineno: 492
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: trace_variable()

## Overview

Define a trace callback for the variable.

MODE is one of "r", "w", "u" for read, write, undefine.
CALLBACK must be a function which is called when
the variable is read, written or undefined.

Return the name of the callback.

This deprecated method wraps a deprecated Tcl method that will
likely be removed in the future.  Use trace_add() instead.

```python
def trace_variable(self, mode, callback)
```

**Module:** [[Modules/tkinter|tkinter]]
**Class:** [[Classes/Variable|Variable]]
**Type:** Method
**Line:** 492

## Categories

- [[Taxonomy/public_method|public_method]]
