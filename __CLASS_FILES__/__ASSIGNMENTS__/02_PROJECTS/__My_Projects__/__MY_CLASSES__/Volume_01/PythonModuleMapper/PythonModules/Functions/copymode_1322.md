---
type: function
name: copymode
module: shutil
lineno: 294
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: copymode()

## Overview

Copy mode bits from src to dst.

If follow_symlinks is not set, symlinks aren't followed if and only
if both `src` and `dst` are symlinks.  If `lchmod` isn't available
(e.g. Linux) this method does nothing.

```python
def copymode(src, dst)
```

**Module:** [[Modules/shutil|shutil]]
**Type:** Module-level function
**Line:** 294
