---
type: function
name: settrace
module: threading
lineno: 95
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: settrace()

## Overview

Set a trace function for all threads started from the threading module.

The func will be passed to sys.settrace() for each thread, before its run()
method is called.

```python
def settrace(func)
```

**Module:** [[Modules/threading|threading]]
**Type:** Module-level function
**Line:** 95
