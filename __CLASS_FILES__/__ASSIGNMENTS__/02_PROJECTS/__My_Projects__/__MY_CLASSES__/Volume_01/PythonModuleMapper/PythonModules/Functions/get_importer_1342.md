---
type: function
name: get_importer
module: pkgutil
lineno: 212
is_async: False
is_method: False
tags:
  - python
  - function
categories:
  - accessor
---

# Function: get_importer()

## Overview

Retrieve a finder for the given path item

The returned finder is cached in sys.path_importer_cache
if it was newly created by a path hook.

The cache (or part of it) can be cleared manually if a
rescan of sys.path_hooks is necessary.

```python
def get_importer(path_item)
```

**Module:** [[Modules/pkgutil|pkgutil]]
**Type:** Module-level function
**Line:** 212

## Categories

- [[Taxonomy/accessor|accessor]]
