---
type: function
name: extend_path
module: pkgutil
lineno: 319
is_async: False
is_method: False
tags:
  - python
  - function
---

# Function: extend_path()

## Overview

Extend a package's path.

Intended use is to place the following code in a package's __init__.py:

    from pkgutil import extend_path
    __path__ = extend_path(__path__, __name__)

For each directory on sys.path that has a subdirectory that
matches the package name, add the subdirectory to the package's
__path__.  This is useful if one wants to distribute different
parts of a single logical package as multiple directories.

It also looks for *.pkg files beginning where * matches the name
argument.  This feature is similar to *.pth files (see site.py),
except that it doesn't special-case lines starting with 'import'.
A *.pkg file is trusted at face value: apart from checking for
duplicates, all entries found in a *.pkg file are added to the
path, regardless of whether they are exist the filesystem.  (This
is a feature.)

If the input path is not a list (as is the case for frozen
packages) it is returned unchanged.  The input path is not
modified; an extended copy is returned.  Items are only appended
to the copy at the end.

It is assumed that sys.path is a sequence.  Items of sys.path that
are not (unicode or 8-bit) strings referring to existing
directories are ignored.  Unicode items of sys.path that cause
errors when used as filenames may cause this function to raise an
exception (in line with os.path.isdir() behavior).

```python
def extend_path(path, name)
```

**Module:** [[Modules/pkgutil|pkgutil]]
**Type:** Module-level function
**Line:** 319
