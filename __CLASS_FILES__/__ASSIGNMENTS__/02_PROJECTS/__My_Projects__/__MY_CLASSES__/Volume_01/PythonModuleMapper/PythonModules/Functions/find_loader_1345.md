---
type: function
name: find_loader
module: pkgutil
lineno: 294
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: find_loader()

## Overview

Find a "loader" object for fullname

This is a backwards compatibility wrapper around
importlib.util.find_spec that converts most failures to ImportError
and only returns the loader rather than the full spec

```python
def find_loader(fullname)
```

**Module:** [[Modules/pkgutil|pkgutil]]
**Type:** Module-level function
**Line:** 294
