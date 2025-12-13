---
type: function
name: makelink_with_filter
module: tarfile
lineno: 2640
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: makelink_with_filter()

## Overview

Make a (symbolic) link called targetpath. If it cannot be created
(platform limitation), we try to make a copy of the referenced file
instead of a link.

filter_function is only used when extracting a *different*
member (e.g. as fallback to creating a link).

```python
def makelink_with_filter(self, tarinfo, targetpath, filter_function, extraction_root)
```

**Module:** [[Modules/tarfile|tarfile]]
**Class:** [[Classes/TarFile|TarFile]]
**Type:** Method
**Line:** 2640

## Categories

- [[Taxonomy/public_method|public_method]]
