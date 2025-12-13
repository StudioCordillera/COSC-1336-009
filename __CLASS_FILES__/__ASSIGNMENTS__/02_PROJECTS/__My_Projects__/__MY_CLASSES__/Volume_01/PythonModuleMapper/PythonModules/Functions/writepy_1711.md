---
type: function
name: writepy
module: zipfile
lineno: 2122
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: writepy()

## Overview

Add all files from "pathname" to the ZIP archive.

If pathname is a package directory, search the directory and
all package subdirectories recursively for all *.py and enter
the modules into the archive.  If pathname is a plain
directory, listdir *.py and enter all modules.  Else, pathname
must be a Python *.py file and the module will be put into the
archive.  Added modules are always module.pyc.
This method will compile the module.py into module.pyc if
necessary.
If filterfunc(pathname) is given, it is called with every argument.
When it is False, the file or directory is skipped.

```python
def writepy(self, pathname, basename, filterfunc)
```

**Module:** [[Modules/zipfile|zipfile]]
**Class:** [[Classes/PyZipFile|PyZipFile]]
**Type:** Method
**Line:** 2122

## Categories

- [[Taxonomy/public_method|public_method]]
