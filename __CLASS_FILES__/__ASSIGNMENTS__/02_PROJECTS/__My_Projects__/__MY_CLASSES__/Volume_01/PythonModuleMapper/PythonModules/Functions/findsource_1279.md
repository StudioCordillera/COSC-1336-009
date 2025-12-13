---
type: function
name: findsource
module: inspect
lineno: 1052
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: findsource()

## Overview

Return the entire source file and starting line number for an object.

The argument may be a module, class, method, function, traceback, frame,
or code object.  The source code is returned as a list of all the lines
in the file and the line number indexes a line in that list.  An OSError
is raised if the source code cannot be retrieved.

```python
def findsource(object)
```

**Module:** [[Modules/inspect|inspect]]
**Type:** Module-level function
**Line:** 1052
