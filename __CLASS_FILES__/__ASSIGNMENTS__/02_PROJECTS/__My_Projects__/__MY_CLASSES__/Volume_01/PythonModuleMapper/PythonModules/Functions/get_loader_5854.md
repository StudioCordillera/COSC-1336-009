---
type: function
name: get_loader
module: pkgutil
lineno: 266
is_async: False
is_method: False
tags:
  - python
  - function
categories:
  - accessor
---

# Function: get_loader()

## Overview

Get a "loader" object for module_or_name

Returns None if the module cannot be found or imported.
If the named module is not already imported, its containing package
(if any) is imported, in order to establish the package __path__.

```python
def get_loader(module_or_name)
```

**Module:** [[Modules/pkgutil|pkgutil]]
**Type:** Module-level function
**Line:** 266

## Categories

- [[Taxonomy/accessor|accessor]]
