---
type: function
name: getframeinfo
module: inspect
lineno: 1661
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: getframeinfo()

## Overview

Get information about a frame or traceback object.

A tuple of five things is returned: the filename, the line number of
the current line, the function name, a list of lines of context from
the source code, and the index of the current line within that list.
The optional second argument specifies the number of lines of context
to return, which are centered around the current line.

```python
def getframeinfo(frame, context)
```

**Module:** [[Modules/inspect|inspect]]
**Type:** Module-level function
**Line:** 1661
