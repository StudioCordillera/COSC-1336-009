---
type: function
name: copy
module: shutil
lineno: 414
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: copy()

## Overview

Copy data and mode bits ("cp src dst"). Return the file's destination.

The destination may be a directory.

If follow_symlinks is false, symlinks won't be followed. This
resembles GNU's "cp -P src dst".

If source and destination are the same file, a SameFileError will be
raised.

```python
def copy(src, dst)
```

**Module:** [[Modules/shutil|shutil]]
**Type:** Module-level function
**Line:** 414
