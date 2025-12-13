---
type: function
name: setprofile_all_threads
module: threading
lineno: 81
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: setprofile_all_threads()

## Overview

Set a profile function for all threads started from the threading module
and all Python threads that are currently executing.

The func will be passed to sys.setprofile() for each thread, before its
run() method is called.

```python
def setprofile_all_threads(func)
```

**Module:** [[Modules/threading|threading]]
**Type:** Module-level function
**Line:** 81
