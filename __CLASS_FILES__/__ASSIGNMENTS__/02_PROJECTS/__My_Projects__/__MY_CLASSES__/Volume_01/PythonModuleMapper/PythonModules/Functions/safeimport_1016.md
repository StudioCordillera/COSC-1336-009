---
type: function
name: safeimport
module: pydoc
lineno: 485
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: safeimport()

## Overview

Import a module; handle errors; return None if the module isn't found.

If the module *is* found but an exception occurs, it's wrapped in an
ErrorDuringImport exception and reraised.  Unlike __import__, if a
package path is specified, the module at the end of the path is returned,
not the package at the beginning.  If the optional 'forceload' argument
is 1, we reload the module from disk (unless it's a dynamic extension).

```python
def safeimport(path, forceload, cache)
```

**Module:** [[Modules/pydoc|pydoc]]
**Type:** Module-level function
**Line:** 485
