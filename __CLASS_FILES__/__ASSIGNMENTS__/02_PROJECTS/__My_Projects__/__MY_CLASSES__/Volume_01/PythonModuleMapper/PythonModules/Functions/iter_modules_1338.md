---
type: function
name: iter_modules
module: pkgutil
lineno: 96
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: iter_modules()

## Overview

Yields ModuleInfo for all submodules on path,
or, if path is None, all top-level modules on sys.path.

'path' should be either None or a list of paths to look for
modules in.

'prefix' is a string to output on the front of every module name
on output.

```python
def iter_modules(path, prefix)
```

**Module:** [[Modules/pkgutil|pkgutil]]
**Type:** Module-level function
**Line:** 96
