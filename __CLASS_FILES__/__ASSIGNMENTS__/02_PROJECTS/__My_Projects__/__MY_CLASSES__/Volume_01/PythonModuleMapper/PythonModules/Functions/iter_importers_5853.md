---
type: function
name: iter_importers
module: pkgutil
lineno: 237
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: iter_importers()

## Overview

Yield finders for the given module name

If fullname contains a '.', the finders will be for the package
containing fullname, otherwise they will be all registered top level
finders (i.e. those on both sys.meta_path and sys.path_hooks).

If the named module is in a package, that package is imported as a side
effect of invoking this function.

If no module name is specified, all top level finders are produced.

```python
def iter_importers(fullname)
```

**Module:** [[Modules/pkgutil|pkgutil]]
**Type:** Module-level function
**Line:** 237
