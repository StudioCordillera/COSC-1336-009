---
type: function
name: _fastcopy_sendfile
module: shutil
lineno: 112
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: _fastcopy_sendfile()

## Overview

Copy data from one regular mmap-like fd to another by using
high-performance sendfile(2) syscall.
This should work on Linux >= 2.6.33 only.

```python
def _fastcopy_sendfile(fsrc, fdst)
```

**Module:** [[Modules/shutil|shutil]]
**Type:** Module-level function
**Line:** 112
