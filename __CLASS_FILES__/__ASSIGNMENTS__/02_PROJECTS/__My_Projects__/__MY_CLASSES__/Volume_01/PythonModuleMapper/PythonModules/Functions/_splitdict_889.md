---
type: function
name: _splitdict
module: tkinter
lineno: 128
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: _splitdict()

## Overview

Return a properly formatted dict built from Tcl list pairs.

If cut_minus is True, the supposed '-' prefix will be removed from
keys. If conv is specified, it is used to convert values.

Tcl list is expected to contain an even number of elements.

```python
def _splitdict(tk, v, cut_minus, conv)
```

**Module:** [[Modules/tkinter|tkinter]]
**Type:** Module-level function
**Line:** 128
