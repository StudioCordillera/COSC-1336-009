---
type: function
name: setprofile
module: threading
lineno: 72
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: setprofile()

## Overview

Set a profile function for all threads started from the threading module.

The func will be passed to sys.setprofile() for each thread, before its
run() method is called.

```python
def setprofile(func)
```

**Module:** [[Modules/threading|threading]]
**Type:** Module-level function
**Line:** 72
