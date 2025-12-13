---
type: function
name: getmember
module: tarfile
lineno: 2050
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: getmember()

## Overview

Return a TarInfo object for member `name'. If `name' can not be
found in the archive, KeyError is raised. If a member occurs more
than once in the archive, its last occurrence is assumed to be the
most up-to-date version.

```python
def getmember(self, name)
```

**Module:** [[Modules/tarfile|tarfile]]
**Class:** [[Classes/TarFile|TarFile]]
**Type:** Method
**Line:** 2050

## Categories

- [[Taxonomy/public_method|public_method]]
