---
type: function
name: walk_stack
module: traceback
lineno: 380
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: walk_stack()

## Overview

Walk a stack yielding the frame and line number for each frame.

This will follow f.f_back from the given frame. If no frame is given, the
current stack is used. Usually used with StackSummary.extract.

```python
def walk_stack(f)
```

**Module:** [[Modules/traceback|traceback]]
**Type:** Module-level function
**Line:** 380
