---
type: function
name: findlinestarts
module: dis
lineno: 909
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: findlinestarts()

## Overview

Find the offsets in a byte code which are start of lines in the source.

Generate pairs (offset, lineno)
lineno will be an integer or None the offset does not have a source line.

```python
def findlinestarts(code)
```

**Module:** [[Modules/dis|dis]]
**Type:** Module-level function
**Line:** 909
