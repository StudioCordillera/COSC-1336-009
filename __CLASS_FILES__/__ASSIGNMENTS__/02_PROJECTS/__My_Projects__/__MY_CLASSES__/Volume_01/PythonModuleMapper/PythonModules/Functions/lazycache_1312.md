---
type: function
name: lazycache
module: linecache
lineno: 184
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: lazycache()

## Overview

Seed the cache for filename with module_globals.

The module loader will be asked for the source only when getlines is
called, not immediately.

If there is an entry in the cache already, it is not altered.

:return: True if a lazy load is registered in the cache,
    otherwise False. To register such a load a module loader with a
    get_source method must be found, the filename must be a cacheable
    filename, and the filename must not be already cached.

```python
def lazycache(filename, module_globals)
```

**Module:** [[Modules/linecache|linecache]]
**Type:** Module-level function
**Line:** 184
