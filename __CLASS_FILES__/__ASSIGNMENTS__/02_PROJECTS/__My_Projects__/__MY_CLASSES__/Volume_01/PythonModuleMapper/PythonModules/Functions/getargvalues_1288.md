---
type: function
name: getargvalues
module: inspect
lineno: 1426
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: getargvalues()

## Overview

Get information about arguments passed into a particular frame.

A tuple of four things is returned: (args, varargs, varkw, locals).
'args' is a list of the argument names.
'varargs' and 'varkw' are the names of the * and ** arguments or None.
'locals' is the locals dictionary of the given frame.

```python
def getargvalues(frame)
```

**Module:** [[Modules/inspect|inspect]]
**Type:** Module-level function
**Line:** 1426
