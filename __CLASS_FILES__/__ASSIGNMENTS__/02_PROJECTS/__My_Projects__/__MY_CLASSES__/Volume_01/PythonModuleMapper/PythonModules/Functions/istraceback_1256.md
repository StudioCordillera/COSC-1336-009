---
type: function
name: istraceback
module: inspect
lineno: 485
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: istraceback()

## Overview

Return true if the object is a traceback.

Traceback objects provide these attributes:
    tb_frame        frame object at this level
    tb_lasti        index of last attempted instruction in bytecode
    tb_lineno       current line number in Python source code
    tb_next         next inner traceback object (called by this level)

```python
def istraceback(object)
```

**Module:** [[Modules/inspect|inspect]]
**Type:** Module-level function
**Line:** 485
