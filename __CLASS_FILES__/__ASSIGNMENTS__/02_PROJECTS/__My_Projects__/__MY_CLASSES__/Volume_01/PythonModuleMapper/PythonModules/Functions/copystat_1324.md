---
type: function
name: copystat
module: shutil
lineno: 348
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: copystat()

## Overview

Copy file metadata

Copy the permission bits, last access time, last modification time, and
flags from `src` to `dst`. On Linux, copystat() also copies the "extended
attributes" where possible. The file contents, owner, and group are
unaffected. `src` and `dst` are path-like objects or path names given as
strings.

If the optional flag `follow_symlinks` is not set, symlinks aren't
followed if and only if both `src` and `dst` are symlinks.

```python
def copystat(src, dst)
```

**Module:** [[Modules/shutil|shutil]]
**Type:** Module-level function
**Line:** 348
