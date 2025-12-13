---
type: function
name: symlink_or_copy
module: venv
lineno: 257
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: symlink_or_copy()

## Overview

Try symlinking a file, and if that fails, fall back to copying.
(Unused on Windows, because we can't just copy a failed symlink file: we
switch to a different set of files instead.)

```python
def symlink_or_copy(self, src, dst, relative_symlinks_ok)
```

**Module:** [[Modules/venv|venv]]
**Class:** [[Classes/EnvBuilder|EnvBuilder]]
**Type:** Method
**Line:** 257

## Categories

- [[Taxonomy/public_method|public_method]]
