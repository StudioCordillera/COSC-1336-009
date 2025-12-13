---
type: function
name: _extract_one
module: tarfile
lineno: 2445
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - protected_method
---

# Function: _extract_one()

## Overview

Extract from filtered tarinfo to disk.

filter_function is only used when extracting a *different*
member (e.g. as fallback to creating a symlink)

```python
def _extract_one(self, tarinfo, path, set_attrs, numeric_owner, filter_function)
```

**Module:** [[Modules/tarfile|tarfile]]
**Class:** [[Classes/TarFile|TarFile]]
**Type:** Method
**Line:** 2445

## Categories

- [[Taxonomy/protected_method|protected_method]]
