---
type: function
name: settrace_all_threads
module: threading
lineno: 104
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: settrace_all_threads()

## Overview

Set a trace function for all threads started from the threading module
and all Python threads that are currently executing.

The func will be passed to sys.settrace() for each thread, before its run()
method is called.

```python
def settrace_all_threads(func)
```

**Module:** [[Modules/threading|threading]]
**Type:** Module-level function
**Line:** 104
