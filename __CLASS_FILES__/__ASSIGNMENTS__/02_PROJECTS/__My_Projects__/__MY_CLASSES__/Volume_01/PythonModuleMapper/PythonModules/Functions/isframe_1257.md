---
type: function
name: isframe
module: inspect
lineno: 495
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: isframe()

## Overview

Return true if the object is a frame object.

Frame objects provide these attributes:
    f_back          next outer frame object (this frame's caller)
    f_builtins      built-in namespace seen by this frame
    f_code          code object being executed in this frame
    f_globals       global namespace seen by this frame
    f_lasti         index of last attempted instruction in bytecode
    f_lineno        current line number in Python source code
    f_locals        local namespace seen by this frame
    f_trace         tracing function for this frame, or None

```python
def isframe(object)
```

**Module:** [[Modules/inspect|inspect]]
**Type:** Module-level function
**Line:** 495
