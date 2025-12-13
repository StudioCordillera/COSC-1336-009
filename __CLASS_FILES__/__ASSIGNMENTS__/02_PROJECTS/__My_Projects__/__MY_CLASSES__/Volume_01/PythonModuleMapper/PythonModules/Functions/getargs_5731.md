---
type: function
name: getargs
module: inspect
lineno: 1301
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: getargs()

## Overview

Get information about the arguments accepted by a code object.

Three things are returned: (args, varargs, varkw), where
'args' is the list of argument names. Keyword-only arguments are
appended. 'varargs' and 'varkw' are the names of the * and **
arguments or None.

```python
def getargs(co)
```

**Module:** [[Modules/inspect|inspect]]
**Type:** Module-level function
**Line:** 1301
