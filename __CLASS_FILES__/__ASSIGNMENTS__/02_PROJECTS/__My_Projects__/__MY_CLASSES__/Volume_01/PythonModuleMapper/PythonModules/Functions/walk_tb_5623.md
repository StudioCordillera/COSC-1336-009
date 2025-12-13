---
type: function
name: walk_tb
module: traceback
lineno: 393
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: walk_tb()

## Overview

Walk a traceback yielding the frame and line number for each frame.

This will follow tb.tb_next (and thus is in the opposite order to
walk_stack). Usually used with StackSummary.extract.

```python
def walk_tb(tb)
```

**Module:** [[Modules/traceback|traceback]]
**Type:** Module-level function
**Line:** 393
