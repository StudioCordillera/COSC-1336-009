---
type: function
name: getsourcelines
module: inspect
lineno: 1231
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: getsourcelines()

## Overview

Return a list of source lines and starting line number for an object.

The argument may be a module, class, method, function, traceback, frame,
or code object.  The source code is returned as a list of the lines
corresponding to the object and the line number indicates where in the
original source file the first line of code was found.  An OSError is
raised if the source code cannot be retrieved.

```python
def getsourcelines(object)
```

**Module:** [[Modules/inspect|inspect]]
**Type:** Module-level function
**Line:** 1231
