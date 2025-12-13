---
type: function
name: formatargvalues
module: inspect
lineno: 1457
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: formatargvalues()

## Overview

Format an argument spec from the 4 values returned by getargvalues.

The first four arguments are (args, varargs, varkw, locals).  The
next four arguments are the corresponding optional formatting functions
that are called to turn names and values into strings.  The ninth
argument is an optional function to format the sequence of arguments.

```python
def formatargvalues(args, varargs, varkw, locals, formatarg, formatvarargs, formatvarkw, formatvalue)
```

**Module:** [[Modules/inspect|inspect]]
**Type:** Module-level function
**Line:** 1457
