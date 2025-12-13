---
type: function
name: walk_packages
module: pkgutil
lineno: 39
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: walk_packages()

## Overview

Yields ModuleInfo for all modules recursively
on path, or, if path is None, all accessible modules.

'path' should be either None or a list of paths to look for
modules in.

'prefix' is a string to output on the front of every module name
on output.

Note that this function must import all *packages* (NOT all
modules!) on the given path, in order to access the __path__
attribute to find submodules.

'onerror' is a function which gets called with one argument (the
name of the package which was being imported) if any exception
occurs while trying to import a package.  If no onerror function is
supplied, ImportErrors are caught and ignored, while all other
exceptions are propagated, terminating the search.

Examples:

# list all modules python can access
walk_packages()

# list all submodules of ctypes
walk_packages(ctypes.__path__, ctypes.__name__+'.')

```python
def walk_packages(path, prefix, onerror)
```

**Module:** [[Modules/pkgutil|pkgutil]]
**Type:** Module-level function
**Line:** 39
