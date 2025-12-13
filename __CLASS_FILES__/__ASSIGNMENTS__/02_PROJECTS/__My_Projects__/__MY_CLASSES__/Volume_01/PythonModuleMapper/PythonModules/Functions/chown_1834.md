---
type: function
name: chown
module: tarfile
lineno: 2690
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: chown()

## Overview

Set owner of targetpath according to tarinfo. If numeric_owner
is True, use .gid/.uid instead of .gname/.uname. If numeric_owner
is False, fall back to .gid/.uid when the search based on name
fails.

```python
def chown(self, tarinfo, targetpath, numeric_owner)
```

**Module:** [[Modules/tarfile|tarfile]]
**Class:** [[Classes/TarFile|TarFile]]
**Type:** Method
**Line:** 2690

## Categories

- [[Taxonomy/public_method|public_method]]
