---
type: function
name: _extract_member
module: tarfile
lineno: 2516
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - protected_method
---

# Function: _extract_member()

## Overview

Extract the filtered TarInfo object tarinfo to a physical
file called targetpath.

filter_function is only used when extracting a *different*
member (e.g. as fallback to creating a symlink)

```python
def _extract_member(self, tarinfo, targetpath, set_attrs, numeric_owner)
```

**Module:** [[Modules/tarfile|tarfile]]
**Class:** [[Classes/TarFile|TarFile]]
**Type:** Method
**Line:** 2516

## Categories

- [[Taxonomy/protected_method|protected_method]]
