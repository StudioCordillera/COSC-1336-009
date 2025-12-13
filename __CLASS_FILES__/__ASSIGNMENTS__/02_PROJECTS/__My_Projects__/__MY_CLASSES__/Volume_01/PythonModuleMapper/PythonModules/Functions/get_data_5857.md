---
type: function
name: get_data
module: pkgutil
lineno: 413
is_async: False
is_method: False
tags:
  - python
  - function
categories:
  - accessor
---

# Function: get_data()

## Overview

Get a resource from a package.

This is a wrapper round the PEP 302 loader get_data API. The package
argument should be the name of a package, in standard module format
(foo.bar). The resource argument should be in the form of a relative
filename, using '/' as the path separator. The parent directory name '..'
is not allowed, and nor is a rooted name (starting with a '/').

The function returns a binary string, which is the contents of the
specified resource.

For packages located in the filesystem, which have already been imported,
this is the rough equivalent of

    d = os.path.dirname(sys.modules[package].__file__)
    data = open(os.path.join(d, resource), 'rb').read()

If the package cannot be located or loaded, or it uses a PEP 302 loader
which does not support get_data(), then None is returned.

```python
def get_data(package, resource)
```

**Module:** [[Modules/pkgutil|pkgutil]]
**Type:** Module-level function
**Line:** 413

## Categories

- [[Taxonomy/accessor|accessor]]
