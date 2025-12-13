---
type: function
name: _get_codename
module: zipfile
lineno: 2204
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - accessor
---

# Function: _get_codename()

## Overview

Return (filename, archivename) for the path.

Given a module name path, return the correct file path and
archive name, compiling if necessary.  For example, given
/python/lib/string, return (/python/lib/string.pyc, string).

```python
def _get_codename(self, pathname, basename)
```

**Module:** [[Modules/zipfile|zipfile]]
**Class:** [[Classes/PyZipFile|PyZipFile]]
**Type:** Method
**Line:** 2204

## Categories

- [[Taxonomy/accessor|accessor]]
